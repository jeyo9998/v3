# Project Understanding — Evaluation Pack

**Status:** Initial evaluation design (not yet run against an external AI-agent client)

This pack tests whether `skills/project-understanding/SKILL.md` can convert user requests and available project evidence into reliable, proportionate briefs and handoffs.

## How to run

1. Open the target AI-agent client that supports the repository's Agent Skills format.
2. Make sure `project-understanding` is available to the agent.
3. Run each case in a fresh conversation, providing only the materials named in that case.
4. Save the agent's response as evidence. Do not coach the agent during the first run.
5. Score the response using `scorecard.md`.
6. Record the client/model, date, skill revision, score, failures, and evidence in a test log.

Do not mark a case as passed just because the response sounds plausible. Check whether it followed the expected behavior and accurately represented the supplied evidence.

## Cases

See [`cases.md`](cases.md).

## Passing rule

For the first baseline, a case passes when it scores at least 80/100 and has no critical failure. Critical failures include inventing inspected evidence, treating assumptions as confirmed, overlooking an important conflict, or proceeding with a consequential/destructive action without appropriate authorization.

A passing result only applies to the tested agent/client configuration. It does not establish universal compatibility.
