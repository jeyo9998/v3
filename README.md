# Motion Graphics AI Collaboration Framework

An open-source project to help compatible AI agents understand, plan, execute, and evaluate real Motion Graphics work across **Alight Motion** and **Adobe After Effects**.

The framework is designed for active AI collaborators—not just assistants that explain workflows. Agents should take useful initiative, work within the tools and permissions actually available, respect each application's own logic, and verify outcomes instead of claiming success without evidence.

> **Project status:** Early development. The repository currently contains the project specification and the first skill draft. Application procedures, execution integrations, and cross-agent compatibility must be tested before they are described as supported.

## Goals

- Build reusable, portable Agent Skills for Motion Graphics work.
- Support Alight Motion and Adobe After Effects as equal initial application targets.
- Share general Motion Graphics knowledge without forcing identical application workflows.
- Enable active collaboration through a hybrid execution approach: direct file manipulation, scripting/API access where supported, and application interaction where available.
- Evaluate skills with practical tasks and evidence from both target applications.
- Preserve user control, project integrity, and clear permission boundaries.

## Repository map

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

This is intentionally a small starting structure. `SKILL-ARCHITECTURE.md` defines the responsibility boundaries and handoffs for the planned Skills. Additional skills, application references, collaboration protocols, and benchmark cases will be added incrementally when their responsibilities and tests are clear.

## Skills

| Skill | Responsibility | Status |
|---|---|---|
| `project-understanding` | Understand the user's intent, project context, requirements, constraints, and acceptance criteria before work proceeds. | Initial draft |
| `motion-graphics-principles` | Shared creative and motion-design concepts independent of a specific application. | Planned |
| `application-adaptation` | Apply verified, application-specific knowledge for Alight Motion and After Effects. | Planned |
| `motion-graphics-execution` | Coordinate the actual creative task from plan through verified result. | Planned |
| `hybrid-execution` | Select and coordinate the available file, scripting/API, and application-interaction methods. | Planned |
| `visual-evaluation` | Evaluate visual and technical outcomes against the task's acceptance criteria. | Planned |
| `error-analysis` | Diagnose issues, separate evidence from hypotheses, and verify corrections. | Planned |

## Instructions for AI contributors

AI coding agents working in this repository should read [`AGENTS.md`](AGENTS.md) first. It explains the project boundaries, repository structure, evidence standards, incremental development workflow, and local validation commands. `AGENTS.md` guides work on the repository; individual files under `skills/` define task-specific Agent Skills.

## How to use a skill

Each skill is a self-contained directory with a required `SKILL.md` file. Use the skill with an AI-agent client that supports the Agent Skills format, following that client's current installation and discovery instructions. Support and loading behavior vary by agent implementation; the presence of a skill in this repository does not guarantee that every agent can use it identically.

Start with [`project-understanding`](skills/project-understanding/SKILL.md). It helps the agent form a reliable understanding of the task and prepare a concise handoff for the next relevant skill.

## Evaluate a skill

Scenario-based evaluation packs live in `evals/`. Start with [`evals/project-understanding/`](evals/project-understanding/README.md) to test the first skill against clear, ambiguous, cross-application, and camera-research tasks. These evaluations require an AI-agent client that can load the skill; the repository validator does not test semantic behavior.

## Validate the current skills

Python 3.10 or newer is recommended.

```bash
python -m pip install -r requirements-dev.txt
python tests/validate_skills.py
```

The validator checks basic Agent Skills frontmatter and repository naming conventions. It is a local project check, not a replacement for the official Agent Skills reference validator or platform-specific testing.

## Development principles

1. **Simple** — use the least complicated approach that meets the user's goal.
2. **Structured** — make responsibilities, inputs, outputs, and handoffs clear.
3. **Evaluated** — test outcomes against observable criteria and available evidence.
4. **Improved** — refine skills using verified findings and practical feedback.

We develop incrementally: design one skill, implement it, validate its structure, test it with realistic scenarios, review the evidence, then proceed to the next skill.

## Safety and project integrity

Agents must be honest about tool and application access. They must not claim to have inspected, changed, rendered, or verified files unless they actually did so. Preserve original user work where practical. Obtain appropriate authorization before destructive, overwriting, publishing, or otherwise consequential actions.

## Open-source status

The repository is being prepared for public release, but **no open-source license has been selected yet**. Until a license is chosen and added, do not assume that the files are licensed for reuse, modification, or redistribution. License selection is a release prerequisite.

## Contributing

Contribution guidance will be added before the first public contribution cycle. In the meantime, proposed changes should preserve the project goals, keep application-specific claims evidence-based, and include relevant validation or test notes.

## Agent Skills format

The skills are authored to follow the open Agent Skills format: a skill directory contains a `SKILL.md` with YAML frontmatter including `name` and `description`; optional resources can be added when needed. See the [Agent Skills specification](https://agentskills.io/specification) for the current format details.
