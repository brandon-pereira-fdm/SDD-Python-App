document.addEventListener("DOMContentLoaded", () => {
    const revealItems = document.querySelectorAll(".reveal");
    const progressBar = document.querySelector("#progress-bar");
    const filterChips = document.querySelectorAll(".chip");
    const benefitCards = document.querySelectorAll(".benefit-card");
    const faqItems = document.querySelectorAll("[data-faq]");

    revealItems.forEach((item, index) => {
        if (!item.style.getPropertyValue("--index")) {
            item.style.setProperty("--index", String(index));
        }
    });

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("in-view");
                }
            });
        },
        { threshold: 0.18 }
    );

    revealItems.forEach((item) => observer.observe(item));

    const updateProgress = () => {
        if (!progressBar) {
            return;
        }

        const scrollTop = window.scrollY;
        const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
        const ratio = maxScroll > 0 ? (scrollTop / maxScroll) * 100 : 0;
        progressBar.style.width = `${Math.min(Math.max(ratio, 0), 100)}%`;
    };

    window.addEventListener("scroll", updateProgress, { passive: true });
    updateProgress();

    filterChips.forEach((chip) => {
        chip.addEventListener("click", () => {
            const filter = chip.dataset.filter;

            filterChips.forEach((button) => button.classList.remove("is-active"));
            chip.classList.add("is-active");

            benefitCards.forEach((card) => {
                const category = card.dataset.category;
                const showCard = filter === "all" || filter === category;
                card.classList.toggle("is-hidden", !showCard);
            });
        });
    });

    faqItems.forEach((item) => {
        const trigger = item.querySelector(".faq-trigger");
        const panel = item.querySelector(".faq-panel");
        const icon = item.querySelector(".faq-icon");

        if (!trigger || !panel || !icon) {
            return;
        }

        trigger.addEventListener("click", () => {
            const isOpen = trigger.getAttribute("aria-expanded") === "true";
            trigger.setAttribute("aria-expanded", String(!isOpen));
            panel.hidden = isOpen;
            icon.textContent = isOpen ? "+" : "-";
            item.classList.toggle("is-open", !isOpen);
        });
    });
});
