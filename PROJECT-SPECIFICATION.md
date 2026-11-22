# Motion Graphics AI Collaboration Framework

## Project Specification — Working Draft

**Status:** Working draft  
**Initial implementation:** Repository bootstrap  
**Last updated:** 2026-11-21

## 1. Project overview

The Motion Graphics AI Collaboration Framework is an open-source project intended to help multiple compatible AI-agent platforms understand, plan, execute, and evaluate Motion Graphics work.

The initial application targets are **Alight Motion** and **Adobe After Effects**. They are equal priorities. The framework aims for comparable ability to achieve the user's creative goals, not identical interfaces, features, file structures, or technical procedures.

The framework is intended to support active AI collaborators. An agent should take useful initiative—inspect accessible context, identify what is needed, propose a plan, perform supported work, and evaluate the result—while respecting user intent, tool limitations, and permission boundaries.

## 2. Vision

Make practical Motion Graphics knowledge and workflows reusable across AI agents and creative applications, so agents can participate in real work rather than only explain how the work could be done.

## 3. Goals

1. Provide modular Agent Skills that compatible AI clients can discover and use.
2. Support Alight Motion and Adobe After Effects as equal initial application targets.
3. Separate shared Motion Graphics concepts from application-specific implementation details.
4. Enable active, purposeful collaboration while preserving user control.
5. Support a hybrid execution approach: direct file manipulation, scripting/API access where supported, and application interaction where available.
6. Evaluate skills through practical tasks and observable evidence.
7. Record limitations, compatibility results, and verified solutions accurately.
8. Make the project understandable and maintainable by open-source contributors.

## 4. Non-goals

The framework does not aim to:

- Make Alight Motion and After Effects technically identical.
- Guarantee that every AI agent can load or execute every skill in the same way.
- Claim application integrations, file-format support, or automation capabilities that have not been tested.
- Replace the user's creative judgment or approval.
- Require extensive project documentation for simple tasks.
- Modify, overwrite, delete, export, or publish user work without appropriate authority.

## 5. Target users and environments

### 5.1 Users

- Motion Graphics creators and editors.
- Users who want an AI collaborator for creative projects.
- AI-agent developers and maintainers.
- Open-source contributors.

### 5.2 AI-agent environments

The repository targets multiple AI-agent platforms that support the Agent Skills format or can be adapted to consume its files. Compatibility must be tested per client and capability. A portable `SKILL.md` does not itself provide an application connection or execution tool.

### 5.3 Initial applications

- Alight Motion.
- Adobe After Effects.

Application-specific references must identify the application and, where known, the tested version. Unverified information must be labelled accordingly.

## 6. Core architecture

The framework has three conceptual layers.

### 6.1 Shared intelligence

Reusable knowledge and workflows that do not depend on one application's implementation:

- Understanding user intent and project context.
- Motion-design and animation principles.
- Planning and task decomposition.
- Visual and technical evaluation.
- Error reasoning and evidence handling.

### 6.2 Application adaptation

Application-specific knowledge for Alight Motion and After Effects:

- Terminology and interface concepts.
- Project and asset structures.
- Keyframes, effects, masks, composition, timeline, and export procedures.
- Available automation or scripting interfaces.
- Known limitations and version differences.

Shared concepts may be reused, but application-specific procedures must not be transferred between applications without evidence.

### 6.3 Active execution

The agent coordinates and performs supported work using available tools and permissions. It must distinguish between planning an action, attempting an action, and verifying the result.

## 7. Hybrid execution approach

The framework recognizes three execution methods:

### A. Direct file manipulation

Read or modify project files and assets when the format is sufficiently understood, the operation is appropriate, and safeguards are in place. Text-readable does not automatically mean safe or supported for editing.

### B. Scripting or API access

Use application APIs, scripting facilities, command-line tools, or other supported programmatic interfaces when they exist and are available to the agent. Record the application/version and dependencies tested. Do not assume both target applications expose equivalent interfaces.

### C. Application interaction

Interact with the application through an available UI-control or automation tool, or guide the user when direct control is not available. Verify visible outcomes when possible.

The agent should choose or combine methods based on the target application, file format, tool access, permissions, reversibility, and task requirements. It must disclose when a method is unavailable.

## 8. Active collaboration and permission boundaries

Agents should:

- Proactively inspect accessible information and identify missing dependencies.
- Propose useful next steps without waiting for unnecessary micro-instructions.
- Execute low-risk, reversible actions when the user has authorized the task and the environment permits them.
- Ask focused questions when uncertainty could materially change the outcome.
- Seek appropriate approval before destructive, irreversible, externally visible, or scope-changing actions.
- Preserve original project files where practical and explain backup or recovery choices.
- Never report an action or verification that did not occur.

Active initiative does not mean unrestricted autonomy.

## 9. Shared workflow principles

1. **Simple:** choose the simplest adequate approach and avoid unnecessary complexity.
2. **Structured:** define responsibilities, sequence, inputs, outputs, and handoffs.
3. **Evaluated:** check the result against observable acceptance criteria and evidence.
4. **Improved:** correct issues and retain reusable lessons only when supported by evidence.

## 10. Initial Agent Skills

The initial architecture contains seven skills:

| Skill | Primary responsibility |
|---|---|
| `project-understanding` | Understand intent, context, requirements, constraints, uncertainties, and success criteria. |
| `motion-graphics-principles` | Provide shared design, animation, and motion principles. |
| `application-adaptation` | Select and apply verified application-specific knowledge. |
| `motion-graphics-execution` | Coordinate the creative task from plan through completed, checked work. |
| `hybrid-execution` | Select and carry out the appropriate technical execution method. |
| `visual-evaluation` | Assess visual and technical results against acceptance criteria. |
| `error-analysis` | Diagnose problems, distinguish hypotheses from confirmed causes, and verify fixes. |

Skills must have non-overlapping primary responsibilities. They may hand off structured information to one another when needed. Not every task requires every skill.

## 11. Skill authoring requirements

Each skill must:

- Be stored in its own directory under `skills/`.
- Include a `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Use a `name` that matches the directory name and follows Agent Skills naming constraints.
- Describe what it does and when it should activate in the `description`.
- State its purpose, workflow, boundaries, and expected outputs.
- Avoid duplicating responsibilities assigned to another skill.
- Keep the main instructions focused; move detailed material into optional `references/`, `scripts/`, or `assets/` when justified.
- Avoid unverified application claims and unsupported compatibility promises.

The repository will follow the current Agent Skills specification and will recheck it during implementation and release.

## 12. Evaluation strategy

### 12.1 Skill-level evaluation

Each skill should have representative test cases, including normal, ambiguous, incomplete-context, and edge-case scenarios where relevant. Evaluate whether the agent follows instructions, produces the expected handoff or result, and respects boundaries.

### 12.2 Cross-application benchmark

Alight Motion and After Effects should be tested against comparable creative objectives, such as:

- Text animation.
- Position and scale animation.
- Timing and easing.
- Masking and compositing.
- Transitions.
- Project organization and export.

The benchmark compares whether the intended creative outcome is achieved, not whether the applications use identical controls or workflows.

### 12.3 Evidence and status

Record test date, application and version where known, AI client/model where relevant, tools used, task prompt, expected criteria, observed result, evidence, and limitations. Use clear statuses such as `pass`, `partial`, `fail`, or `not tested`.

A skill is not considered practically validated merely because its Markdown file is syntactically valid.

## 13. Error handling and data protection

Error reports should separate:

- Observed symptoms.
- Confirmed facts.
- Suspected causes.
- Diagnostic steps.
- Attempted changes.
- Verified resolution or unresolved status.

Treat user projects and assets as user-owned. Avoid including private project files, credentials, or confidential materials in public test fixtures. Prefer backups or copies before risky operations.

## 14. Incremental development roadmap

1. **Bootstrap:** create the repository foundation and first skill.
2. **Understand and validate:** test `project-understanding` with realistic prompts and refine it.
3. **Shared principles:** build the common Motion Graphics knowledge skill.
4. **Application adaptation:** document and test Alight Motion and After Effects independently.
5. **Execution:** develop task execution and hybrid method selection.
6. **Evaluation and recovery:** build visual evaluation and error analysis.
7. **Integration:** test handoffs, cross-agent compatibility, and balanced cross-application benchmarks.
8. **Release preparation:** select a license, add contribution guidance, validate, and publish.

The project uses an incremental method: complete and review a stage before moving to the next. Independent infrastructure work may be parallelized later when it does not destabilize the skill sequence.

## 15. Current decisions

- Project: open-source Motion Graphics AI collaboration framework.
- Target agents: multiple compatible AI-agent platforms.
- Initial application priorities: Alight Motion and Adobe After Effects equally.
- Agent mode: active collaborator, with bounded authority.
- Skill architecture: seven initial skills.
- Execution: hybrid—file manipulation, scripting/API where supported, and application interaction where available.
- Development method: incremental.
- Workflow values: Simple, Structured, Evaluated, Improved.

## 16. Open decisions

- Final repository name and GitHub owner.
- Open-source license.
- Initial target versions of Alight Motion and After Effects for testing.
- Which AI clients will be included in the first compatibility test matrix.
- Specific application integrations and execution tools.
- Contribution and release workflow.

## 17. Guiding statement

> Build AI agents that understand the creative goal, adapt to the application, take useful initiative, perform work when tools allow, verify what they produce, and improve through evidence.
