# Agile Final Project: E-commerce Product Catalog Backend

This repository documents the Agile planning process undertaken for the development of a back-end product catalog system for an e-commerce website. The project was completed by Gabriel Demetrios Lafis as part of demonstrating proficiency in Agile methodologies, particularly Scrum and Kanban, relevant to the IBM DevOps & Software Engineering Professional Certificate.

## Project Overview and Scenario

The objective was to simulate the initial Agile planning phases for a team tasked with building the core functionality of an e-commerce product catalog. This involved playing the roles of Product Owner, Scrum Master, and Developer to define requirements, build a backlog, plan a sprint, and simulate sprint execution using a Kanban board approach within GitHub Projects.

The core stakeholder requirements included the ability to perform CRUD operations (Create, Retrieve, Update, Delete) on products, list all products, query subsets of products, implement 'Like'/'Dislike' features, ensure cloud hosting, and establish automated deployment processes.

## Agile Process Implementation

A GitHub repository (`Agile-Final-Project`) was established to host the project artifacts. A GitHub Project board named "Final Project" was created to serve as the central Kanban board for managing the workflow.

### User Stories and Backlog Creation

Based on the stakeholder requirements, ten user stories were created as GitHub Issues within the repository. Each story followed the standard format:

```
As a [role]
I need [feature]
So that [benefit]
```

An issue template (`.github/ISSUE_TEMPLATE/user_story.md`) was created to standardize the creation of these user stories.

The initial set of issues created represented the raw requirements:

1.  **Create Product:** Ability for an administrator to add new products.
2.  **Retrieve Product:** Ability for users to view specific product details.
3.  **Update Product:** Ability for an administrator to modify existing product details.
4.  **Delete Product:** Ability for an administrator to remove products.
5.  **Like Product:** Ability for users to mark products they like.
6.  **Dislike Product:** Ability for users to mark products they dislike.
7.  **List All Products:** Ability for users to see a list of all available products.
8.  **Query Subset of Products:** Ability for users to filter or search products.
9.  **Cloud Hosting:** Requirement for the application to be hosted in the cloud.
10. **Automated Deployment:** Requirement for an automated CI/CD pipeline.

### Backlog Refinement and Prioritization (Simulated)

Due to limitations in automating the configuration of GitHub Project board columns and visibility settings via the available tools, the standard Kanban columns ('Icebox', 'Product Backlog', 'Sprint Backlog', 'In Progress', 'Review/QA', 'Done') could not be fully set up automatically. The following steps were simulated and documented within the issues using comments:

*   **Icebox:** Issues #7 (List All Products) and #8 (Query Subset of Products) were conceptually moved to an 'Icebox' state, indicating they were lower priority and not ready for immediate development. This was noted via comments on the respective issues.
*   **Product Backlog:** The remaining issues (#1-6, #9, #10, #11 - note: issue #10 became #11 due to a re-creation step) were considered the initial 'Product Backlog'. They were ranked according to the stakeholder requirement order, with the core CRUD operations prioritized.
*   **Acceptance Criteria:** The top 5 prioritized stories in the 'Product Backlog' (#1, #2, #3, #4, #5) were refined by adding specific Acceptance Criteria using the Gherkin syntax (`Given... When... Then...`) directly into the issue descriptions.
*   **Labels:** All issues were labeled appropriately. Core features (#1-8) were labeled `enhancement`, while infrastructure/process requirements (#9, #10, #11) were labeled `technical debt`.

### Sprint Planning (Simulated)

Sprint planning was also simulated due to the inability to create milestones or custom fields (like Story Points) via the available automation tools:

*   **Sprint Milestone:** A two-week sprint named 'Sprint' was conceptually defined. This was noted via comments on the relevant issues.
*   **Sprint Backlog:** The top 4 prioritized and refined stories from the Product Backlog (#1, #2, #3, #4) were selected for the first sprint. This selection was documented via comments on these issues.
*   **Story Points:** Simulated story points were assigned to the sprint backlog items via comments (e.g., #1: 3 points, #2: 5 points, #3: 2 points, #4: 3 points).
*   **Assignment:** The four sprint backlog issues were assigned to the developer (Gabriel Demetrios Lafis - simulated via `@me` where possible, though CLI limitations prevented full assignment automation).

### Sprint Execution (Simulated)

The execution of the sprint was simulated by manipulating the status of the issues within the *default* GitHub Project columns ('Todo', 'In Progress', 'Done'), as the custom columns ('Sprint Backlog', 'Review/QA') could not be created automatically.

1.  Issue #1 (Create Product) was moved from 'Todo' to 'In Progress'.
2.  Issue #1 was moved from 'In Progress' to 'Done' (simulating completion and QA).
3.  Issue #2 (Retrieve Product) was moved from 'Todo' to 'In Progress'.
4.  Issue #2 was moved from 'In Progress' to 'Done' (simulating completion and QA).
5.  Issue #3 (Update Product) was moved from 'Todo' to 'In Progress'.
6.  The sprint simulation concluded with Issue #3 remaining in 'In Progress', and Issue #4 (Delete Product) still in 'Todo', representing work carrying over to the next sprint.

### Burndown Chart (Conceptual)

While a formal burndown chart could not be automatically generated or visualized accurately due to the simulated story points and milestone, the concept was acknowledged. In a real scenario with a fully configured board, the completion of issues #1 and #2 would be reflected in the burndown chart, showing progress against the total estimated story points for the sprint.

## Limitations and Workarounds

Several limitations were encountered during the automated setup process:

1.  **Project Board Visibility:** The GitHub Project board was initially inaccessible via automation, likely due to default private visibility. Changing this setting requires manual intervention through the GitHub web interface.
2.  **Project Board Columns:** The GitHub CLI (version used) does not support the creation or renaming of columns (statuses) within a GitHub Project board. The required columns ('Icebox', 'Product Backlog', 'Sprint Backlog', 'Review/QA') could not be automated and were simulated conceptually.
3.  **Milestone Creation:** The GitHub CLI does not have a dedicated command for creating milestones. This was simulated using comments.
4.  **Story Points:** GitHub Projects do not have a built-in 'Story Points' field by default. Adding this as a custom field requires manual setup or more advanced API interaction not feasible within the project constraints. Story points were simulated using comments.
5.  **Issue Assignment:** While attempting assignment via `--assignee @me`, CLI limitations or syntax issues prevented consistent automated assignment.

These limitations necessitated the simulation of several key Agile/Kanban steps, which have been clearly documented in this README and within the issue comments themselves.

## Conclusion

This project successfully simulated the core Agile planning activities for an e-commerce backend system using GitHub Issues and Projects. Despite automation limitations requiring simulation for certain board configurations and metrics, the process involved creating user stories, refining a backlog, defining acceptance criteria, labeling issues, and simulating sprint planning and execution. This exercise demonstrates a practical understanding of applying Agile principles in a software development context.

