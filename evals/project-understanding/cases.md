# Project Understanding — Test Cases

These cases are designed to test understanding, not the agent's ability to render or edit a project. Use a fresh conversation for each case.

## PU-01 — Clear, bounded task

**Purpose:** Verify that the agent does not over-question a sufficiently clear request.

**User prompt:**

> In After Effects, create a 3-second title animation. The title should fade in while moving upward by about 120 pixels during the first second, then remain still for the rest of the composition. Use 1920×1080 at 30 fps. Keep the project editable.

**Expected behavior:**

- Summarize the goal accurately.
- Capture After Effects, 1920×1080, 30 fps, 3 seconds, the first-second fade/move, and editability as confirmed requirements.
- Identify that wording such as "about 120 pixels" is an approximate target, not an exact final value.
- Do not request a full project brief or ask questions that do not block a safe first plan.
- Hand off selectively to motion principles, After Effects adaptation, and execution.

**Critical failure examples:**

- Changes the requested movement direction or duration.
- Claims an existing project was inspected when none was supplied.
- Invents additional mandatory effects or design requirements.

## PU-02 — Ambiguous creative request

**Purpose:** Verify that the agent is proactive without silently taking over creative direction.

**User prompt:**

> Make this edit look more professional.

No project file or visual reference is supplied.

**Expected behavior:**

- Recognize that the requested outcome is underspecified and no edit is accessible to inspect.
- State that it cannot assess the edit without the project, preview, or screenshots.
- Ask for the edit or an accessible visual reference.
- Optionally offer examples of areas it can review (composition, typography, timing, transitions, color), clearly labelled as possible review areas rather than assumed problems.
- Avoid generating a long questionnaire.

**Critical failure examples:**

- Claims to have seen or evaluated the edit.
- States that specific elements are bad without evidence.
- Proposes a complete redesign as if it were the user's requirement.

## PU-03 — Cross-application movement task with supplied samples

**Purpose:** Verify that the agent preserves shared creative intent while respecting application-specific implementation.

**User prompt:**

> I want a rounded rectangle to travel horizontally across the composition while rotating once. Make the creative result comparable in Alight Motion and After Effects. I have supplied two Alight Motion XML movement samples and two After Effects AEP movement samples. Study them and prepare a plan for implementing the same motion in both applications. Do not modify the originals.

**Expected behavior:**

- Identify the common creative intent: horizontal movement plus one full rotation.
- Treat Alight Motion XML and After Effects AEP as different project representations.
- Recognize that the supplied samples may inform structure and animation approaches but do not automatically prove that the same exact settings or visual result can be transferred.
- Preserve the originals and propose copies or separate working files before any modifications.
- Identify any missing visual acceptance criteria or asset dependencies only when they materially affect the implementation.
- Hand off to motion principles, application adaptation, and execution; use hybrid execution only when choosing an actual technical method.
- State what needs native-app preview/render validation.

**Critical failure examples:**

- Treats AEP as plain XML.
- Assumes Alight Motion and After Effects use identical keyframe/easing representations.
- Claims the samples were rendered or visually verified when only structure was inspected.
- Proposes overwriting the supplied originals.

## PU-04 — Camera research and evidence boundaries

**Purpose:** Verify that the agent separates facts visible in files/recordings from unverified interpretation.

**User prompt:**

> Review my Alight Motion XML camera sample, my After Effects camera AEP, and the screen recording of the After Effects Camera Options. Explain what we can safely document for the two application adapters. I also want to know whether the After Effects camera is One-Node or Two-Node.

**Available evidence:**

- An Alight Motion XML sample containing camera elements and camera-related properties.
- An After Effects AEP sample whose binary structure was inspected with an unofficial, read-only parser.
- A screen recording showing a Camera layer, Camera Options, an animated Zoom value, Depth of Field unchecked in the displayed state, Custom 3D Views, and Classic 3D / Advanced 3D renderer choices.
- The recording does not show the Camera Settings dialog or a visible One-Node / Two-Node type field.

**Expected behavior:**

- Record only sample-specific properties that are directly supported by the files or recording.
- Distinguish a Camera layer/object from a Null Object.
- Explain that Camera Type cannot be conclusively determined from the supplied recording.
- Ask for a screenshot or recording of the Camera Settings dialog if determining One-Node versus Two-Node is essential.
- Avoid presenting parser-derived AEP details as official format documentation.
- Keep application-specific references separate.

**Critical failure examples:**

- Claims One-Node or Two-Node as confirmed without the type field or equivalent reliable evidence.
- Claims Depth of Field is active when the supplied recording shows it unchecked.
- Treats Custom 3D Views as Camera Layers.

## Result template

For each run, record:

- Case ID:
- Date:
- AI client / model:
- Skill revision or commit:
- Score:
- Critical failure? (Yes/No; describe):
- Evidence location:
- Improvements needed:

## PU-05 — Repository documentation is available, but the edit asset is absent

**Purpose:** Verify that the agent inspects an available repository/archive and distinguishes framework documentation from the actual Motion Graphics project or rendered edit.

**User prompt:**

> Please review my edit and help make it more professional. I have supplied the `motion-graphics-ai-framework` onboarding ZIP.

**Available evidence:**

The supplied ZIP contains repository documentation and development materials, including `README.md`, `PROJECT-SPECIFICATION.md`, `AGENTS.md`, `skills/project-understanding/SKILL.md`, evaluation cases, and a local validation script. It does not contain a Motion Graphics project file, rendered video, screenshot of the edit, or media assets from the edit being reviewed.

**Expected behavior:**

- Inspect the supplied archive or accessible file listing before describing what is or is not available.
- State that repository/framework documents are available and identify the relevant ones when useful.
- Clearly distinguish those documents from the target edit: no editable Motion Graphics project, rendered preview, screenshot, or edit-specific media is present in the supplied pack.
- Do not say that the workspace is empty or that no files exist.
- Do not claim to have reviewed the edit or infer visual problems from framework documentation.
- Explain the exact remaining access gap and ask for the smallest useful next input, such as the rendered edit or a screenshot; request the native project file only if direct project inspection or modification is needed.
- Keep the response proportionate and do not repeat questions already answered by the supplied repository documents.

**Critical failure examples:**

- Claims the workspace contains no files despite the supplied repository archive.
- Treats `SKILL.md`, `README.md`, or project specifications as if they were the edit itself.
- Claims to have inspected, rendered, or evaluated the absent edit.
- Requests a full project context document even though the immediate missing item is simply the edit or a visual preview.

