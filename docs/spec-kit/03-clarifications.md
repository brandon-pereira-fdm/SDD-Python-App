# Clarifications

## Questions and decisions

Q1. Should the page remain static or include runtime data?
Decision: Keep it server-rendered and informational, but pass structured content from Flask for maintainability.

Q2. How should "5 iterations" be represented to users?
Decision: Add an explicit "Five Iterations" section with named cards describing goal and deliverable for each iteration.

Q3. What level of visual polish is expected?
Decision: Use a modern responsive design with dedicated CSS, expressive typography, atmosphere, and clear section hierarchy.

Q4. How informative should content be?
Decision: Include measurable highlights, benefit impact statements, lifecycle timeline details, FAQ clarifications, and sprint actions.

Q5. Should JavaScript be required for core content?
Decision: No. Core content remains fully visible without JavaScript; JS only enhances reveal animations.

Q6. What should be tested after iteration updates?
Decision: Verify route availability, SDD title/content, five-iteration presence, and key section labels.