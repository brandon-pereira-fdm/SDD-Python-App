# Clarifications 
 
## Questions and decisions 
 
Q1. Should the app be dynamic or static? 
Decision: Static page only. No form submission or database. 
 
Q2. Which Python web framework should be used? 
Decision: Flask, because it is simple for learners and suitable for a small web app. 
 
Q3. Should the page use CSS? 
Decision: Use simple embedded CSS inside index.html to keep the project small. 
 
Q4. What should be tested? 
Decision: Test that the home page returns HTTP 200 and contains the expected SDD content. 
 
Q5. What should Jenkins do? 
Decision: Jenkins should install dependencies, run pytest, package the source into a ZIP file, and archive it. 
 
Q6. Is deployment required? 
Decision: No. CI pipeline demonstration is enough for this workshop. 