# Constitution: SDD Python Web App 
 
## Project principles 
1. Keep the application simple and understandable for workshop learners. 
2. Every visible page must clearly communicate the benefits of Spec-Driven Development. 
3. The implementation must match the specification and acceptance criteria. 
4. The app must include at least one automated test for page availability and expected content. 
5. The Jenkins pipeline must run tests before packaging or archiving the application. 
6. Do not add unnecessary frameworks or external services. 
7. Source code, tests, and pipeline files must be readable and easy to explain. 
 
## Quality gates 
- The home page returns HTTP 200. 
- The page contains the phrase "Spec-Driven Development". 
- The page lists at least four benefits of SDD. 
- Tests pass locally before the Jenkins pipeline is used. 
- Jenkinsfile contains checkout, install, test, package, and archive stages.