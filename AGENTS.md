# Agent Guide — Motion Graphics AI Collaboration Framework

This document guides AI coding agents and other automated contributors **working inside this repository**. It explains how to orient yourself, how to make changes, and how to report what you have and have not verified.

It is a repository contribution guide. It is **not** a replacement for the runtime Agent Skills in `skills/`, and it does not itself give an agent access to Alight Motion, Adobe After Effects, a user's files, or application automation tools.

## 1. Project identity

The **Motion Graphics AI Collaboration Framework** is an early-stage open-source project intended to help compatible AI agents understand, plan, execute, and evaluate real Motion Graphics work.

The two initial application targets have equal priority:

- Alight Motion
- Adobe After Effects

The goal is comparable ability to achieve the user's creative intent, **not** identical application features, interfaces, project structures, file formats, or procedures.

The intended agent mode is an active collaborator: take useful initiative, inspect accessible context, identify dependencies, propose or carry out appropriate work, and evaluate outcomes. Initiative must remain within the user's intent, available tools, and permission boundaries.

## 2. First-read procedure

At the start of a repository task:

1. Read `README.md` for the repository map and current status.
2. Read `PROJECT-SPECIFICATION.md` for project goals, architecture, constraints, and decisions.
3. Read `SKILL-ARCHITECTURE.md` for Skill responsibilities, activation routing, handoffs, and current implementation status.
4. Read this `AGENTS.md` for repository-specific working rules.
5. Inspect the relevant directory and files before proposing or making changes.
6. Read the relevant `SKILL.md`, evaluation cases, references, or tests for the component being changed.
7. Check whether the requested capability is implemented, planned, experimentally observed, or not tested.

Do not assume that a file exists because it is mentioned in a roadmap or earlier discussion. Confirm its presence in the current checkout.

## 3. Repository map and current implementation state

```text
motion-graphics-ai-framework/
├── AGENTS.md
├── README.md
├── PROJECT-SPECIFICATION.md
├── SKILL-ARCHITECTURE.md
├── requirements-dev.txt
├── skills/
│   └── project-understanding/
│       └── SKILL.md
├── evals/
│   └── project-understanding/
│       ├── README.md
│       ├── cases.md
│       └── scorecard.md
└── tests/
    ├── README.md
    └── validate_skills.py
```

Current status in this repository:

- `project-understanding` has an initial Skill draft and a scenario-based evaluation pack.
- The other six planned Skills are not yet implemented in this checkout.
- The current validator checks basic Skill directory and frontmatter conventions. It does not prove that an agent discovers, activates, or follows a Skill correctly.
- No application integration or execution adapter is established merely by the presence of documentation.
- Alight Motion and After Effects execution, round-trip file modification, rendering, and cross-agent compatibility require separate practical tests.
- A public-release license has not yet been selected. Do not claim that the repository is already licensed for reuse or redistribution.

Update this section when the repository structure or implementation status changes.

## 4. Source-of-truth and evidence rules

Use the following guidance when sources differ:

1. Follow the user's latest explicit task instructions, unless they conflict with applicable safety, authorization, or repository constraints.
2. Treat `PROJECT-SPECIFICATION.md` as the project's architectural and scope reference. Propose a specification update when an implementation change requires a new project decision; do not silently redefine the project.
3. Treat this `AGENTS.md` as the working procedure for contributions to this repository.
4. Treat each `skills/<skill-name>/SKILL.md` as the operational instructions for that specific Skill.
5. Treat evaluation cases and test results as evidence about the tested revision and conditions, not universal proof of capability.
6. Treat application documentation, observed application behavior, sample files, parser output, and hypotheses as different evidence types. Identify which type supports each technical claim.

When evidence conflicts, preserve the conflict and investigate it. Do not silently reconcile it by guessing.

Use these labels where useful:

- **Confirmed:** directly stated by the user or verified from accessible, reliable evidence.
- **Observed in sample:** present in a supplied file or recording; do not generalize it to every version or project.
- **Inferred:** a reasoned interpretation that has not been confirmed.
- **Unverified:** not yet checked against sufficient evidence.
- **Not tested:** no relevant test has been run.

Do not claim to have opened, inspected, modified, rendered, executed, or tested something unless that action actually occurred.

## 5. Architecture rules

Keep the seven planned Skills' primary responsibilities distinct:

| Skill | Primary responsibility |
|---|---|
| `project-understanding` | Understand user intent, project context, requirements, constraints, uncertainties, and acceptance criteria. |
| `motion-graphics-principles` | Explain reusable creative and motion-design concepts independent of a specific application. |
| `application-adaptation` | Apply verified, application-specific knowledge for Alight Motion and After Effects. |
| `motion-graphics-execution` | Coordinate the creative task from plan through completed, checked work. |
| `hybrid-execution` | Select and carry out an available technical method: file manipulation, scripting/API, or application interaction. |
| `visual-evaluation` | Evaluate visual and technical outcomes against acceptance criteria. |
| `error-analysis` | Diagnose issues, distinguish hypotheses from confirmed causes, and verify corrections. |

Do not create an additional top-level Skill when a reference, script, test, protocol, or a clearly scoped section of an existing Skill is sufficient. If responsibilities overlap, resolve the boundary before adding more instructions.

Preserve the three conceptual layers in the project specification:

- Shared intelligence and creative principles.
- Application-specific adaptation.
- Active execution and evaluation.

## 6. Cross-application rules

- Treat Alight Motion and Adobe After Effects as equal initial targets.
- Preserve shared creative intent while documenting application-specific implementation separately.
- Never assume that matching names imply matching behavior or parameters.
- Do not transfer keyframe, easing, effect, camera, layer, parenting, 3D, export, or project-file procedures from one application to the other without evidence.
- Record the application and version when known.
- Distinguish a feature's presence in a sample from proof that the feature works in all versions or is active in the sample.
- Compare applications by whether they achieve the agreed creative outcome, not by whether their internal controls are identical.

For file formats:

- Do not treat an Alight Motion XML project as generic interchange XML without understanding its application-specific structure and dependencies.
- Do not treat an After Effects `.aep` file as plain XML or text. If an unofficial parser or reverse-engineered format description is used, label its output accordingly and do not present it as official Adobe format documentation.
- Do not modify original user project files during research. Use copies and reversible workflows for experiments.

## 7. Skill authoring rules

When creating or editing a Skill:

1. Keep it in its own directory under `skills/`.
2. Include a `SKILL.md` with valid YAML frontmatter containing non-empty `name` and `description` fields.
3. Make `name` match the Skill directory name and follow the Agent Skills naming rules.
4. Make `description` specific about what the Skill does and when it should be used.
5. State purpose, activation conditions, inputs, workflow, outputs, boundaries, and relevant evaluation criteria.
6. Give the Skill one clear primary responsibility and define handoffs to other Skills.
7. Keep the main instructions focused. Move detailed material into `references/`, `scripts/`, or `assets/` when that improves clarity and context efficiency.
8. Reference supporting files with correct relative paths and ensure those files exist.
9. Do not add speculative application procedures as confirmed instructions.
10. Check the current Agent Skills specification when changing format assumptions; do not rely on memory for version-sensitive schema details.

Follow progressive disclosure: the main `SKILL.md` should orient the agent and point to relevant supporting material; load detailed references only when the task needs them.

## 8. Active collaboration and permission boundaries

Agents should take useful initiative by inspecting available context, identifying missing dependencies, suggesting an appropriate plan, and performing authorized, supported work.

Active initiative does not mean unrestricted autonomy.

- Do not invent user intent, missing assets, application capabilities, or test results.
- Do not ask the user to repeat information already present in the current task or accessible project context.
- Ask focused questions when an unknown or conflict could materially change the work.
- Do not require optional project-context documents when the available context is sufficient.
- Preserve original project materials where practical.
- Obtain appropriate approval before destructive, irreversible, externally visible, publishing, or scope-changing actions.
- State when tools or application access are unavailable and offer a practical next step.

## 9. Incremental development workflow

The project uses an incremental method. For each Skill or infrastructure component:

1. **Design:** state the purpose, scope, inputs, outputs, dependencies, and boundaries.
2. **Implement:** make the smallest coherent change that meets the agreed scope.
3. **Validate:** run structural checks and check links, paths, and references.
4. **Evaluate:** test representative scenarios, including edge cases where relevant.
5. **Review:** report results, failures, uncertainties, and evidence.
6. **Improve:** fix demonstrated problems and rerun affected checks.

Do not mark a component complete solely because a file was created or a syntax validator passed. Distinguish structural validation from behavioral evaluation and real application execution.

Do not begin the next dependent Skill until the current one has been reviewed. Independent documentation or tooling may be prepared in parallel only when it does not obscure dependencies or bypass the user's incremental decision process.

## 10. Local validation

From the repository root, install development dependencies and run the current validator.

Windows Command Prompt or PowerShell:

```powershell
py -m pip install -r requirements-dev.txt
py tests/validate_skills.py
```

macOS or Linux:

```bash
python3 -m pip install -r requirements-dev.txt
python3 tests/validate_skills.py
```

The validator currently checks basic Skill directory and YAML frontmatter conventions. Read `tests/README.md` before interpreting its result. A `PASS` does not establish semantic quality, cross-agent compatibility, application integration, or successful Motion Graphics execution.

When editing the validator, include tests or clear reproduction steps for new checks. Keep dependencies minimal and document any additions in `requirements-dev.txt`.

## 11. Documentation, samples, and privacy

- Keep `README.md` aligned with the actual repository contents and current status.
- Keep `PROJECT-SPECIFICATION.md` aligned with agreed project decisions.
- Document application-specific findings with provenance, application/version where known, and verification status.
- Keep sample-derived observations separate from general application behavior.
- Do not commit private user projects, proprietary media, credentials, tokens, or confidential recordings without explicit permission and a clear licensing basis.
- The repository has no selected public license yet. Do not add a license file or claim open-source reuse rights without an explicit project decision.
- Do not copy third-party reference repository content wholesale. Learn from its structure and practices, and write original project documentation.

## 12. Change reporting

When completing a task, report:

- Files created, changed, or removed.
- Why each meaningful change was made.
- Commands or tests actually run and their results.
- What remains untested or uncertain.
- Any decision or approval needed next.

Never report a test as passing if it was not run. Never describe a planned feature as implemented.

## 13. Working principles

All contributions should support the project's four principles:

1. **Simple** — choose the simplest adequate solution.
2. **Structured** — keep responsibilities, files, and handoffs clear.
3. **Evaluated** — verify outcomes against observable criteria.
4. **Improved** — refine through evidence and practical feedback.
