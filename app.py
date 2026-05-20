from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    benefits = [
        {
            "title": "Clear Requirements",
            "description": "Teams agree on user needs, scope, and acceptance criteria before writing code.",
            "impact": "Cuts early ambiguity during planning.",
            "category": "clarity",
        },
        {
            "title": "Less Rework",
            "description": "Clarifications reduce assumptions and prevent avoidable redesign later.",
            "impact": "Avoids costly changes late in delivery.",
            "category": "delivery",
        },
        {
            "title": "Better Testing",
            "description": "Acceptance criteria become a practical foundation for automated tests.",
            "impact": "Improves release confidence before deployment.",
            "category": "quality",
        },
        {
            "title": "Traceable Delivery",
            "description": "Code, tests, and pipeline steps can be traced back to the original specification.",
            "impact": "Connects decisions to outcomes and ownership.",
            "category": "delivery",
        },
    ]

    iteration_cards = [
        {
            "name": "Iteration 1 - Foundations",
            "goal": "Clarify the purpose and user story for the page.",
            "deliverable": "Clean hero section that explains why SDD matters.",
        },
        {
            "name": "Iteration 2 - Visual Identity",
            "goal": "Introduce modern styling and stronger visual hierarchy.",
            "deliverable": "Design system with expressive typography and layered backgrounds.",
        },
        {
            "name": "Iteration 3 - Informative Content",
            "goal": "Add concise, practical value statements for teams.",
            "deliverable": "Benefit cards with measurable delivery impact.",
        },
        {
            "name": "Iteration 4 - Journey and Clarity",
            "goal": "Show the end-to-end SDD workflow users can follow.",
            "deliverable": "Lifecycle timeline and clarification-oriented FAQ.",
        },
        {
            "name": "Iteration 5 - Actionable Next Steps",
            "goal": "Help users turn understanding into execution.",
            "deliverable": "Readiness checklist and next sprint recommendations.",
        },
        {
            "name": "Iteration 6 - Interaction Polish",
            "goal": "Elevate usability with elegant, focused interactions.",
            "deliverable": "Section navigation, interactive filtering, accordion FAQ, and reading progress feedback.",
        },
    ]

    highlights = [
        {"label": "Requirement Drift", "value": "-42%"},
        {"label": "Rework", "value": "-31%"},
        {"label": "Release Confidence", "value": "+28%"},
    ]

    flow_steps = [
        {
            "title": "Constitution",
            "note": "Set project principles and quality gates.",
        },
        {
            "title": "Specification",
            "note": "Define user story, requirements, and acceptance criteria.",
        },
        {
            "title": "Clarification",
            "note": "Resolve ambiguity before implementation starts.",
        },
        {
            "title": "Plan",
            "note": "Choose architecture, risks, and delivery strategy.",
        },
        {
            "title": "Tasks",
            "note": "Break work into testable and traceable units.",
        },
        {
            "title": "Implementation",
            "note": "Build, validate, and ship with confidence.",
        },
    ]

    faq_items = [
        {
            "question": "Why use Spec-Driven Development for small projects?",
            "answer": "Even small projects benefit from clarity, fewer assumptions, and repeatable delivery habits.",
        },
        {
            "question": "When should we start writing tests?",
            "answer": "As soon as acceptance criteria are defined. Tests should validate the promises made in the specification.",
        },
        {
            "question": "How does this improve collaboration?",
            "answer": "Design, engineering, and QA share one source of truth and can review intent before code changes.",
        },
    ]

    sprint_actions = [
        "Review one user story with measurable acceptance criteria.",
        "Convert at least two acceptance criteria into tests.",
        "Capture one clarification decision in docs/spec-kit/03-clarifications.md.",
    ]

    return render_template(
        "index.html",
        benefits=benefits,
        iteration_cards=iteration_cards,
        highlights=highlights,
        flow_steps=flow_steps,
        faq_items=faq_items,
        sprint_actions=sprint_actions,
        current_year=datetime.now().year,
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)