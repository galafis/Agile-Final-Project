# Agile Final Project: E-commerce Product Catalog Backend

This repository documents the Agile planning process undertaken for the development of a back-end product catalog system for an e-commerce website. The project was completed by Gabriel Demetrios Lafis as part of demonstrating proficiency in Agile methodologies, particularly Scrum and Kanban, relevant to the IBM DevOps & Software Engineering Professional Certificate.

## Project Overview and Scenario

The objective was to execute the initial Agile planning phases for a team tasked with building the core functionality of an e-commerce product catalog. This involved playing the roles of Product Owner, Scrum Master, and Developer to define requirements, build a backlog, plan a sprint, and execute the sprint using a Kanban board approach within GitHub Projects.

The core stakeholder requirements included the ability to perform CRUD operations (Create, Retrieve, Update, Delete) on products, list all products, query subsets of products, implement 'Like'/'Dislike' features, ensure cloud hosting, and establish automated deployment processes.

## Agile Process Implementation

A GitHub repository (`Agile-Final-Project`) was established to host the project artifacts. A GitHub Project board named "Final Project" was created and configured with the standard Kanban columns ('Icebox', 'Product Backlog', 'Sprint Backlog', 'In Progress', 'Review/QA', 'Done') to serve as the central board for managing the workflow.

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

### Backlog Refinement and Prioritization

A backlog refinement meeting was conducted:

*   **Icebox:** Issues #7 (List All Products) and #8 (Query Subset of Products) were moved to the 'Icebox' column, indicating they were lower priority and not ready for immediate development.
*   **Product Backlog:** The remaining issues (#1-6, #9, #10, #11 - note: issue #10 became #11 due to a re-creation step) formed the initial 'Product Backlog'. They were ranked in the 'Product Backlog' column according to the stakeholder requirement order, with the core CRUD operations prioritized.
*   **Acceptance Criteria:** The top 5 prioritized stories in the 'Product Backlog' (#1, #2, #3, #4, #5) were refined by adding specific Acceptance Criteria using the Gherkin syntax (`Given... When... Then...`) directly into the issue descriptions.
*   **Labels:** All issues were labeled appropriately. Core features (#1-8) were labeled `enhancement`, while infrastructure/process requirements (#9, #10, #11) were labeled `technical debt`.

### Sprint Planning

A Sprint Planning meeting was held:

*   **Sprint Milestone:** A two-week sprint milestone named 'Sprint' was created.
*   **Sprint Backlog:** The top 4 prioritized and refined stories from the Product Backlog (#1, #2, #3, #4) were selected for the first sprint and moved to the 'Sprint Backlog' column.
*   **Story Points:** Story points were assigned to the sprint backlog items (#1: 3 points, #2: 5 points, #3: 2 points, #4: 3 points).
*   **Assignment:** The four sprint backlog issues were assigned to the developer (Gabriel Demetrios Lafis).

### Sprint Execution

The execution of the sprint involved moving the assigned stories across the Kanban board columns:

1.  Issue #1 (Create Product) was assigned to Gabriel Demetrios Lafis and moved from 'Sprint Backlog' to 'In Progress'.
2.  Issue #1 was moved from 'In Progress' to 'Review/QA'.
3.  Issue #2 (Retrieve Product) was assigned to Gabriel Demetrios Lafis and moved from 'Sprint Backlog' to 'In Progress'.
4.  Issue #1 was moved from 'Review/QA' to 'Done'.
5.  Issue #2 was moved from 'In Progress' to 'Review/QA'.
6.  Issue #3 (Update Product) was assigned to Gabriel Demetrios Lafis and moved from 'Sprint Backlog' to 'In Progress'.
7.  Issue #2 was moved from 'Review/QA' to 'Done'.
8.  The sprint concluded with Issue #3 remaining 'In Progress', and Issue #4 (Delete Product) still in the 'Sprint Backlog', representing work carrying over to the next sprint.

### Burndown Chart

The burndown chart for the sprint correctly displayed the progress based on the completed story points (Issues #1 and #2) against the total estimated points for the sprint.

## Conclusion

This project successfully executed the core Agile planning activities for an e-commerce backend system using GitHub Issues and Projects. The process involved creating user stories, refining a backlog, defining acceptance criteria, labeling issues, planning a sprint with estimations, and executing the sprint by moving tasks across a configured Kanban board. This exercise demonstrates a practical application of Agile principles in a software development context by Gabriel Demetrios Lafis.

