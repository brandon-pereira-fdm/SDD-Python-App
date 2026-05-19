document.addEventListener("DOMContentLoaded", () => {
    const revealItems = document.querySelectorAll(".reveal");

    revealItems.forEach((item, index) => {
        if (!item.style.getPropertyValue("--index")) {
            item.style.setProperty("--index", String(index));
        }
    });
});
