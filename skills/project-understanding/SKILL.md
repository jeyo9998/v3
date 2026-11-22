---
name: project-understanding
description: Understands a user's Motion Graphics goal, project context, requirements, constraints, references, and acceptance criteria before planning or execution. Use when starting or changing a task, reviewing supplied project materials, or resolving important ambiguity.
---

# Project Understanding

## Purpose

Build a reliable, task-focused understanding of what the user wants before another skill or agent plans or performs consequential Motion Graphics work.

This skill does more than restate the request. It identifies the intended outcome, relevant context, requirements, constraints, dependencies, uncertainties, and observable success criteria. It then passes a concise understanding to the next relevant skill.

## Use When

Activate this skill when:

- A user starts a new Motion Graphics task.
- A user asks to create, modify, improve, inspect, or troubleshoot a project.
- A user supplies project files, assets, screenshots, videos, or references.
- Requirements are ambiguous, incomplete, or conflicting.
- The target application or intended deliverable could materially change the workflow.
- A project changes scope or receives important new requirements.

For a simple, unambiguous request, use a lightweight understanding process. Do not create a lengthy brief unnecessarily.

## Don't Use When

Do not activate this skill as a separate step when:

- The user is asking a simple factual question unrelated to a project task.
- Another skill already has a sufficiently current understanding brief and the user has not changed the task.
- The task is a narrow execution step with all relevant context already established; continue through the responsible execution skill instead.

If the existing brief may be stale, revisit only the parts affected by the change.

## Workflow

### 1. Observe available context

Review the current request and relevant conversation context. Inspect accessible project materials only when the required tools and permissions are available.

Identify, where relevant:

- Target application: Alight Motion, Adobe After Effects, both, or not yet specified.
- Application version, if known.
- Existing project state and available assets.
- User-provided references and prior decisions.
- Desired deliverable and expected working format.

#### Inventory and classify available resources

When a task depends on supplied files or a workspace, inspect the relevant accessible sources before asking the user to upload or repeat information. Keep the inspection proportional to the task; do not scan unrelated locations.

Classify relevant resources instead of treating every file as the target project:

- **Target project:** Native/editable project files intended to be created, modified, or inspected.
- **Rendered preview:** Video, image sequence, or screenshot that can support visual review but may not expose editable project structure.
- **Reference material:** Examples, footage, images, audio, design references, or technical samples used to guide the work.
- **Project documentation:** README files, specifications, rules, workflow notes, and error records. These describe the project or framework; they are not themselves proof of the target edit's visual content.
- **Development/tooling files:** Skills, scripts, tests, and configuration used to build or validate the framework.

For a relevant source, distinguish whether it was **inspected**, merely **listed/identified**, **present but not inspected**, **not found in the checked source**, or **inaccessible**. Do not describe the entire workspace as empty when repository or documentation files are present but the target edit is absent.

If the target edit is missing, state the exact gap and request the smallest useful input: a rendered preview or screenshot is usually enough for an initial visual review; request the native project file when editable structure or direct modification is necessary.

Do not claim to have opened, inspected, or understood a file that you could not access.

### 2. Identify the intended outcome

Determine:

- What does the user want created, changed, inspected, or fixed?
- What should the result look like, communicate, or accomplish?
- Which creative characteristics matter (for example, style, composition, typography, timing, motion, or transitions)?
- Is the request about a new project, an existing project, or a cross-application workflow?

Distinguish the user's requested action from the outcome they want to achieve.

### 3. Extract requirements

Capture only relevant requirements in these groups:

**Creative requirements**
- Visual direction and reference intent.
- Composition, layout, and hierarchy.
- Typography, graphic elements, and color.
- Motion behavior, timing, easing, and transitions.

**Technical requirements**
- Target application and version, if known.
- Resolution, aspect ratio, frame rate, and duration, when specified or necessary.
- Required assets, file formats, and export requirements.
- Project editability or delivery constraints.

**Operational requirements**
- Available tools and access.
- Existing project structure and dependencies.
- File preservation and backup expectations.
- Required approvals and delivery expectations.

Do not invent missing specifications. Mark them unknown when they matter.

### 4. Identify constraints and dependencies

Look for missing assets, unavailable tools, application/version limitations, format uncertainty, conflicting requirements, resource limits, and actions that could overwrite or damage user work.

Separate verified limitations from suspected limitations. When a technical claim is not verified, say so and identify what would be needed to verify it.

### 5. Resolve material uncertainty

Classify important information as:

- **Confirmed:** explicitly supplied by the user or verified from accessible evidence.
- **Inferred:** a reasonable interpretation, not confirmed by the user.
- **Unknown:** not established.
- **Conflicting:** inconsistent instructions or evidence need resolution.

Ask a focused question when an unknown or conflict could materially change the result. Do not ask the user to repeat information already available.

For low-risk, reversible details, propose a reasonable default and label it as a proposal. The agent may make useful creative suggestions proactively, but must clearly distinguish suggestions from user requirements and must not silently replace the user's direction.

### 6. Define acceptance criteria

Translate the intended outcome into observable checks. Depending on the task, these may include:

- The visual result follows the agreed direction.
- Motion timing and easing match the intended feel.
- Required elements and assets are present.
- The result meets specified dimensions, frame rate, duration, or export settings.
- The project remains editable when requested.
- The final output has been checked using available evidence.

Use only criteria relevant to the task. Do not claim that a criterion has passed before evaluation.

### 7. Prepare a proportionate understanding brief

For complex tasks or handoffs, use the format below. For simple tasks, a concise summary is enough.

#### Project Understanding Brief

- **Objective:** What the user wants to accomplish.
- **Intended outcome:** What the finished result should achieve.
- **Target application:** Alight Motion, After Effects, both, or unknown; include version if known.
- **Confirmed requirements:** Explicit requirements and verified facts.
- **Constraints and dependencies:** Relevant technical, creative, and operational limitations.
- **References and assets:** Available material and its classification (target project, rendered preview, reference material, project documentation, or development/tooling); note what was inspected, merely identified, absent from checked sources, or inaccessible.
- **Uncertainties and assumptions:** Unknowns, inferences, and conflicts.
- **Acceptance criteria:** Observable conditions for success.
- **Approvals needed:** Permissions or decisions required before consequential actions.
- **Recommended next step:** The smallest useful next action and the relevant skill handoff.

### 8. Hand off selectively

Pass the brief to only the skills needed for the task:

- `motion-graphics-principles` for general design and animation concepts.
- `application-adaptation` for application-specific procedures and verified capabilities.
- `motion-graphics-execution` for coordinating the creative work.
- `hybrid-execution` for selecting and carrying out an available technical method.
- `visual-evaluation` for checking results against acceptance criteria.
- `error-analysis` for diagnosing an existing problem.

Do not activate every skill by default. If critical information is unresolved, make the blocker explicit before consequential execution.

## Rules

1. Understand the creative goal independently of the application's implementation.
2. Never force Alight Motion and After Effects to use identical workflows, terminology, or capabilities.
3. Use available conversation context and project material before asking questions.
4. Never present an inference, assumption, or unverified technical claim as confirmed fact.
5. Ask only questions whose answers could materially affect the work.
6. Be proactive: identify useful next steps and offer relevant creative suggestions without overriding the user's intent.
7. Do not claim to have inspected inaccessible files or performed actions that did not occur.
8. Respect user permissions. Seek approval before destructive, irreversible, externally visible, or scope-changing actions.
9. Preserve original project files where practical; identify backup or recovery needs before risky work.
10. Keep the brief proportionate to task complexity.

## Examples

### Example 1: Clear, small task

**User:** "Create a simple title animation in After Effects. The title should fade in and move upward over one second."

**Good understanding:** The goal, application, text animation, direction, and duration are clear. The agent can summarize the understanding briefly and hand off to the relevant principles, application, and execution skills. It should not ask for a project brief unless a missing detail blocks the work.

### Example 2: Ambiguous task

**User:** "Make this edit more professional."

**Good understanding:** Inspect the supplied edit if accessible. Identify observable issues and ask what matters most only if the desired direction cannot be inferred safely. Offer a few specific, clearly labelled improvement ideas rather than assuming a complete redesign is wanted.

### Example 3: Cross-application request

**User:** "Make the same text animation in Alight Motion and After Effects."

**Good understanding:** Treat the creative outcome as shared, but record that each application needs its own implementation. Ask for a reference or parameters only if needed to define the intended result. Hand off to application adaptation for separate procedures.

### Example 4: Missing reference

**User:** "Recreate the transition from the reference video," but no video is accessible.

**Good understanding:** State that the video could not be inspected. Ask the user to upload it or provide screenshots/a description. Do not invent the transition's appearance.

## Edge Cases

- **Conflicting instructions:** Identify the conflict and determine whether a later explicit user instruction supersedes an earlier one. Ask when priority is unclear.
- **Missing application:** Do not choose one if the choice affects implementation. Ask or prepare an application-neutral creative brief.
- **Unclear file format:** Do not assume a file is safely editable because it appears text-based. Request evidence or defer technical conclusions to the relevant skill.
- **Inaccessible assets:** Record what could not be inspected and avoid conclusions that depend on it.
- **Old project notes:** Check whether they still apply to the current task. Do not treat a previous project's preferences as universal.
- **Potentially destructive work:** Identify the risk and obtain the required approval before proceeding.
- **User requests a creative recommendation:** Provide helpful options, but separate recommendations from confirmed requirements.

## References

- [Agent Skills specification](https://agentskills.io/specification) — required `SKILL.md` structure and frontmatter conventions.
- [Project specification](../../PROJECT-SPECIFICATION.md) — framework goals, architecture, workflow, and boundaries.
