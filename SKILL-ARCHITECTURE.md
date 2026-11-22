# Skill Architecture Map

**Project:** Motion Graphics AI Collaboration Framework  
**Document status:** Architecture draft  
**Version:** 0.3.0  
**Based on:** Current repository bootstrap and `PROJECT-SPECIFICATION.md`  
**Purpose:** Define responsibilities, activation conditions, handoffs, and evaluation boundaries for the initial Agent Skills.

---

## 1. Purpose and scope

This document turns the project's high-level architecture into an operational map for the initial seven Skills. It defines what each Skill owns, what it receives, what it produces, and when it hands work to another Skill.

It is an architecture guide, not an application integration and not an additional runtime Skill. It does not itself provide access to Alight Motion, Adobe After Effects, project files, scripts, APIs, UI automation, or other agents.

The map follows the current project decisions:

- **Target agents:** Multiple compatible AI-agent platforms.
- **Initial application targets:** Alight Motion and Adobe After Effects, with equal priority.
- **Agent mode:** Active collaborator, with bounded authority.
- **Execution:** Hybrid; use direct file manipulation, scripting/API access, and application interaction where actually supported.
- **Application behavior:** Preserve each application's own logic and procedures.
- **User context documentation:** Optional; request it only when it materially helps.
- **Working principles:** Simple, Structured, Evaluated, Improved.

## 2. Architecture principles

### 2.1 Shared creative intent, application-specific implementation

The framework should represent the user's creative goal once, in application-neutral terms. Each application adapter then translates that goal into procedures supported by the target application.

Do not create false parity by forcing identical controls, terminology, file structures, or editing logic. Compare Alight Motion and After Effects by whether they can achieve the agreed creative outcome and satisfy the same acceptance criteria.

### 2.2 Skills describe capabilities; tools provide access

An Agent Skill contains instructions and supporting resources. It does not automatically grant an agent permission or technical access to an application, file system, scripting interface, API, emulator, or desktop UI.

Execution is possible only when the host agent has the relevant tool, integration, application access, and user authorization. A Skill must describe what to do when a needed capability is absent.

### 2.3 Active initiative, bounded authority

Agents should proactively inspect accessible context, identify dependencies, propose useful next steps, and perform low-risk, reversible work that is within the user's request and granted permissions.

They must seek appropriate approval before destructive, irreversible, externally visible, publishing, overwriting, or scope-changing actions. Never claim that an action or verification happened unless it actually happened.

### 2.4 Progressive disclosure

Keep each `SKILL.md` focused on its own responsibility. Put detailed application notes, schemas, examples, scripts, and templates in skill-local supporting files when useful. Load references only when the current task needs them.

## 3. Three conceptual layers

```text
USER REQUEST + ACCESSIBLE PROJECT CONTEXT
                  |
                  v
+---------------------------------------------+
| 1. SHARED INTELLIGENCE                      |
| project-understanding                       |
| motion-graphics-principles                  |
+---------------------------------------------+
                  |
                  v
+---------------------------------------------+
| 2. APPLICATION ADAPTATION                   |
| application-adaptation                      |
|   + Alight Motion references                |
|   + After Effects references                |
+---------------------------------------------+
                  |
                  v
+---------------------------------------------+
| 3. ACTIVE EXECUTION AND EVALUATION          |
| motion-graphics-execution                   |
| hybrid-execution                            |
| visual-evaluation                           |
| error-analysis (when needed)                |
+---------------------------------------------+
                  |
                  v
       VERIFIED RESULT + HANDOFF / REPORT
```

These layers are conceptual, not a requirement that every request activate every Skill. Route only to the Skills needed for the task.

## 4. Skill responsibility map

| Skill | Primary responsibility | Activate when | Main output |
|---|---|---|---|
| `project-understanding` | Establish what the user wants, what project context is available, and what success means. | A project task starts, changes scope, or has material ambiguity. | A proportionate Project Understanding Brief. |
| `motion-graphics-principles` | Explain or specify reusable creative and animation principles independently of a particular application. | A task requires design, motion, timing, composition, or animation reasoning. | An application-neutral creative/motion specification. |
| `application-adaptation` | Translate shared creative intent into verified procedures for the selected application. | An application is known and implementation details are needed. | An application-specific implementation plan with evidence status. |
| `motion-graphics-execution` | Coordinate the creative task from approved brief through completed work and checked status. | The user asks to create, modify, improve, or troubleshoot actual project work. | An execution plan, task sequence, and consolidated work status. |
| `hybrid-execution` | Choose and carry out an available technical route for a defined operation. | A concrete operation must be performed on files, through scripting/API, or via the application UI. | Method choice, action/change log, outputs, and execution evidence. |
| `visual-evaluation` | Judge the resulting work against user-approved acceptance criteria. | A preview, render, project state, or other relevant result is available to inspect. | Pass / partial / fail assessment with evidence and gaps. |
| `error-analysis` | Investigate a known discrepancy or failure, separate hypotheses from confirmed causes, and verify a correction. | Evaluation or execution identifies an error, unexpected result, or unresolved failure. | Diagnostic report, confirmed/suspected cause, and verified or unresolved status. |

### 4.1 Explicit responsibility boundaries

**Project understanding vs. motion principles**

- `project-understanding` records what the user wants and what constraints apply.
- `motion-graphics-principles` recommends or specifies creative approaches to achieve that intent.
- The principles Skill must not rewrite user requirements as though its recommendations were user instructions.

**Motion execution vs. hybrid execution**

- `motion-graphics-execution` owns the creative task plan: what needs to happen, in what sequence, and how completion will be judged.
- `hybrid-execution` owns the technical method for carrying out a defined operation: how to perform it using available file, script/API, or UI capabilities.
- Hybrid execution must not independently change the creative brief or broaden the task.

**Application adaptation vs. hybrid execution**

- `application-adaptation` supplies verified application-specific knowledge and procedures.
- `hybrid-execution` chooses among available technical routes and executes the operation using those procedures.
- Application adaptation does not claim that an integration or control tool is installed merely because a procedure is documented.

**Visual evaluation vs. error analysis**

- `visual-evaluation` determines whether observed results meet the acceptance criteria and identifies mismatches.
- `error-analysis` investigates why a mismatch or failure occurred and whether a correction worked.
- A failed evaluation does not automatically prove a particular root cause.

## 5. Workspace and resource discovery

Workspace discovery is a required behavior within `project-understanding`, not a separate top-level Skill in the initial architecture. This avoids a duplicate Skill whose responsibilities would substantially overlap with project understanding.

When relevant tools and permissions are available, the agent should:

1. Check the current conversation and supplied attachments for project files, screenshots, previews, references, and prior decisions.
2. Inspect the accessible project/workspace location or repository relevant to the task; confirm actual paths and filenames before relying on them.
3. Identify which materials are accessible, which were actually inspected, and which remain unavailable or uninspected.
4. Read only the relevant documents or inspect the relevant assets needed to understand the task.
5. Check for project context instructions, such as introduction, rules, references, expected results, and error records, when present.
6. Avoid asking the user to upload or repeat something that is already accessible.
7. If required material is unavailable, explain the precise access gap and ask for the smallest useful missing input.

The Skill must not imply that all AI clients share a filesystem or can inspect the user's local computer. Workspace discovery is limited to the current agent's actual tools and accessible locations.

## 6. Task lifecycle and activation routing

```text
NEW OR CHANGED USER TASK
          |
          v
project-understanding
  - inspect accessible context
  - clarify material unknowns
  - define acceptance criteria
          |
          +------------------------------+
          |                              |
          v                              v
motion-graphics-principles       application-adaptation
(when creative reasoning          (when target-app procedures
 is required)                      are needed)
          |                              |
          +---------------+--------------+
                          |
                          v
              motion-graphics-execution
              - sequence the work
              - track task status
                          |
                          v
                  hybrid-execution
                  - choose A / B / C
                  - perform authorized action
                          |
                          v
                  visual-evaluation
                    /          \
                 PASS        PARTIAL / FAIL
                   |               |
                   v               v
             Final report     error-analysis
                                  |
                                  v
                         approved correction plan
                                  |
                                  +----> execution / hybrid execution
                                  |
                                  v
                           visual re-evaluation
```

This is a logical workflow. A host agent may implement it with native Skill activation, internal routing, explicit agent handoffs, or manual invocation. The Agent Skills file format alone does not guarantee automatic orchestration.

### 6.1 Activation rules

- A simple factual question about animation theory may use `motion-graphics-principles` without a full project brief.
- A new project task should normally begin with `project-understanding`, but the brief should remain concise for simple, clear tasks.
- A task that names both applications should preserve one shared creative intent and create separate implementation paths for each app.
- Use `application-adaptation` only when a target application or its technical behavior matters.
- Use `motion-graphics-execution` for actual create/modify/improve work, not merely for a general explanation.
- Use `hybrid-execution` when a concrete operation and technical method need to be selected or performed.
- Use `visual-evaluation` when there is an output or state that can be compared with acceptance criteria.
- Use `error-analysis` conditionally when a problem, mismatch, or failed attempt exists.

## 7. Cross-Skill handoff contract

Use a concise Markdown handoff by default. Do not force a platform-specific JSON schema until a real integration requires it.

```markdown
## Task Handoff
- Objective:
- Intended outcome:
- Target application(s) and version(s):
- Project/assets available:
- Evidence inspected:
- Creative requirements:
- Technical constraints:
- Confirmed facts:
- Assumptions / unknowns / conflicts:
- Acceptance criteria:
- Permissions and approval boundaries:
- Backup / recovery status:
- Work already performed and verified:
- Requested next action:
- Receiving skill:
```

Handoff rules:

1. Preserve the user's exact intent and distinguish it from recommendations.
2. Do not drop important constraints or uncertainty when passing work onward.
3. Reference actual files and evidence, not guessed paths.
4. Record the target application and version where known.
5. Include the user's authorization boundaries and whether a recoverable copy exists.
6. Keep the handoff proportionate; omit irrelevant fields rather than inventing values.
7. Record which actions were planned, attempted, completed, and verified as separate states.

## 8. Execution method selection

`hybrid-execution` recognizes the three methods in the Project Specification:

| Method | Description | Select when | Important limitation |
|---|---|---|---|
| **A — Direct file manipulation** | Inspect or modify a supported project or asset file directly. | The format and operation are sufficiently understood and a safe, recoverable workflow exists. | Readable files are not automatically safe to edit. Preserve originals and validate in the native application where possible. |
| **B — Scripting / API** | Use an application-supported script, API, plugin, extension, or command-line interface. | The target app exposes a documented and available programmatic route. | Verify app/version, permissions, dependencies, and side effects. Do not assume equivalent interfaces across apps. |
| **C — Application interaction** | Use authorized UI-control or application interaction tools. | The needed operation is accessible through the app UI and the agent has appropriate control. | Depends on platform, device, permissions, and UI/tool availability; mobile interaction may require a device or emulator. |

The method decision should record:

- Target application and version.
- Intended operation.
- Available tools and permissions.
- Evidence that the method is supported.
- Data-preservation / recovery approach.
- Expected output and validation step.
- Reason for selecting or rejecting each method.

A method can be `available`, `unavailable`, `unverified`, or `not applicable`. Do not present a proposed route as an implemented integration.

## 9. Active collaboration and permission model

### The agent may take initiative to

- Inspect accessible, relevant context.
- Identify missing dependencies and likely blockers.
- Prepare a plan and recommend improvements.
- Perform low-risk, reversible work within the user's request and permissions.
- Verify its own changes using available evidence.
- Prepare a concise report of completed, partial, and blocked work.

### The agent must seek appropriate approval before

- Deleting or overwriting original project files.
- Performing irreversible or destructive changes.
- Publishing, uploading, sharing, or externally distributing user work.
- Changing project scope or making a major creative direction change not implied by the request.
- Changing security-sensitive application settings or executing scripts with material side effects when the user has not authorized them.

### Required execution status language

Use precise statuses such as:

- `planned` — described but not attempted.
- `attempted` — action started, completion not established.
- `completed` — operation finished, but result may not yet be validated.
- `verified` — output was checked against a stated criterion using evidence.
- `blocked` — cannot proceed due to a specific missing tool, permission, input, or dependency.

## 10. Evaluation and error-recovery loop

Evaluation should compare the result with acceptance criteria, not with assumptions about how an application should work.

For each meaningful test or delivery, record:

- Task/case ID and test date.
- AI client/model where relevant.
- Target application and version.
- Execution method(s) used.
- Prompt/brief and acceptance criteria.
- Observed result and status (`pass`, `partial`, `fail`, `not tested`).
- Evidence location and what the evidence demonstrates.
- Known limitations and unresolved questions.

When a result is partial or fails:

1. `visual-evaluation` records the mismatch without guessing its cause.
2. `error-analysis` investigates observed evidence and labels possible causes as confirmed, suspected, or unknown.
3. A correction is passed back to `motion-graphics-execution` for planning and `hybrid-execution` for implementation as appropriate.
4. `visual-evaluation` checks the corrected output against the same acceptance criteria.
5. Record the verified resolution or leave the issue explicitly unresolved.

## 11. Alight Motion / After Effects parity model

The two application targets are equal priorities, but parity is measured at the level of creative outcomes and tested capabilities.

Each benchmark task should have:

1. One application-neutral creative brief.
2. A shared set of visual/technical acceptance criteria.
3. A separately documented Alight Motion implementation.
4. A separately documented After Effects implementation.
5. Application/version and execution method for each run.
6. Evidence from each application's actual output or state.
7. A comparison of outcome quality, editability, workflow constraints, and limitations.

Do not penalize an application for using different internal controls if it meets the shared criteria. Do not mark parity as achieved merely because both procedures are documented. Parity requires practical evidence for both targets.

Suggested first benchmark tasks:

- Title fade and position animation.
- Position and scale animation with specified timing.
- A movement with a defined easing feel.
- Masking/reveal transition.
- Simple layer/composition organization and export.

Start with small, reproducible tasks. Increase complexity only after both application paths can be tested reliably.

## 12. Multi-agent collaboration boundary

The repository targets multiple AI-agent platforms, but Skills are not an inter-agent messaging protocol. A `SKILL.md` does not, by itself, make one agent invoke another agent or share its runtime tools and files.

For the initial release:

- Keep the Skill content portable.
- Use the Task Handoff contract in Section 7 to pass context between agents or between Skill stages.
- Require each receiving agent to verify which files, tools, and permissions it actually has.
- Preserve evidence and provenance when work moves between agents.
- Do not assume a second agent can access the first agent's local workspace or application session.

A platform-specific orchestration adapter or MCP/tool integration may be designed later, after target agent platforms and real collaboration use cases are selected. It should sit outside the portable Skill instructions and must not be treated as an existing capability until implemented and tested.

## 13. Implementation and evaluation sequence

The repository already contains an initial `project-understanding` Skill and a scenario-based evaluation pack. The recommended next steps are therefore:

### Step 1 — Review and baseline `project-understanding`

- Check the Skill against this architecture map.
- Use `evals/project-understanding/cases.md` and `scorecard.md`, including PU-05 for workspace discovery.
- Run the cases on at least one compatible AI-agent client.
- Record the client/model, date, Skill revision, scores, critical failures, and evidence.
- Refine the Skill only where the tests demonstrate a gap.

### Step 2 — Complete `motion-graphics-principles`

- Define shared creative concepts and application-neutral outputs.
- Create test cases for concept explanation and motion-spec generation.
- Keep app-specific controls and instructions out of this Skill.

### Step 3 — Develop `application-adaptation`

- Create separate references for Alight Motion and After Effects.
- Track sources, tested app versions, confidence, and unknowns.
- Use the same creative briefs to test each adapter independently.

### Step 4 — Develop `motion-graphics-execution` and `hybrid-execution`

- Keep task coordination separate from low-level method selection and technical actions.
- Add method-specific tests only where tools and integrations exist.
- Do not claim actual application execution until an end-to-end test succeeds.

### Step 5 — Develop `visual-evaluation` and `error-analysis`

- Define observable acceptance criteria and evidence formats.
- Test the distinction between detecting a mismatch and diagnosing its cause.
- Verify that corrections are re-evaluated.

### Step 6 — Integrate and benchmark

- Test the full handoff sequence.
- Compare Alight Motion and After Effects using shared benchmark briefs.
- Test multiple AI clients and record client-specific compatibility.
- Add platform-specific orchestration only when justified by tested collaboration needs.

Do not mark a Skill complete because its file exists or its YAML is valid. Structural validation, behavioral evaluation, application execution, and cross-agent compatibility are separate evidence levels.

## 14. Current implementation status

Based on the supplied repository archive:

| Component | Present? | Current evidence/status |
|---|---:|---|
| Project specification | Yes | Working draft; see `PROJECT-SPECIFICATION.md`. |
| Repository contribution guide | Yes | `AGENTS.md` contains source-of-truth, workflow, safety, and reporting rules. |
| `project-understanding` | Yes | Initial Skill draft exists. |
| `project-understanding` evaluation pack | Yes | Four scenarios and scorecard exist; README says not yet run against an external AI-agent client. |
| Local Skill validator | Yes | Basic frontmatter/directory validation; not behavioral testing. |
| Remaining six Skills | No | Planned, not implemented in this archive. |
| Application adapters/integrations | No | No runnable Alight Motion or After Effects integration is established by this archive. |
| Cross-agent orchestration | No | Handoff is specified conceptually; runtime orchestration is not implemented. |
| Public open-source license | No | Not selected; keep repository pre-release until decided. |

## 15. Open architecture decisions

These decisions should remain open until there is enough evidence to choose:

- Which AI-agent clients will be used for the first behavioral and compatibility tests?
- How will a receiving agent access the handoff, project files, and evidence from another agent?
- Which Alight Motion and After Effects versions/devices will form the first benchmark environment?
- Which application capabilities can be exercised by Method A, B, or C in the actual test environment?
- Which open-source license is appropriate for the original code and documentation, and what third-party asset rules are needed?

Do not resolve these through assumptions. Record a decision when the user or project maintainers confirm it, or when a documented test provides sufficient evidence.

---

**End of Skill Architecture Map — Draft 0.3.0**
