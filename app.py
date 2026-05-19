from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    benefits = [
        {
            "title": "Clear Requirements",
            "description": "Teams agree on user needs, scope, and acceptance criteria before writing code.",
        },
        {
            "title": "Less Rework",
            "description": "Clarifications reduce assumptions and prevent avoidable redesign later.",
        },
        {
            "title": "Better Testing",
            "description": "Acceptance criteria become a practical foundation for automated tests.",
        },
        {
            "title": "Traceable Delivery",
            "description": "Code, tests, and pipeline steps can be traced back to the original specification.",
        },
    ]
    flow_steps = [
        "Constitution",
        "Specification",
        "Clarification",
        "Plan",
        "Tasks",
        "Implementation",
    ]
    return render_template(
        "index.html",
        benefits=benefits,
        flow_steps=flow_steps,
        current_year=datetime.now().year,
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)