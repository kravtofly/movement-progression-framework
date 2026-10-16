# Expert Review Triage: Specification v1.1

Working document for turning the first round of expert review into a v1.2 change set.

**Source:** review responses captured by the `mpf-review-v2` HTML review surface (final answer per field).
**Reviewers:**

| Code | Scope reviewed | Date |
| --- | --- | --- |
| ZV | Flyer Tier (Solo, Group) + core questions | 2026-07-23/24 |
| TS | Full specification | 2026-09-03 |

Both reviews post-date v1.1 (2026-07-22). Nothing below has been applied.

Reviewer comments are paraphrased. Verbatim responses stay in the review database, not in this public repo.

## How to use this

Each row has a **Proposed** outcome. Fill in **Decision** (Accept / Modify / Decline / Discuss). Accepted rows then follow the Specification Change Process: Design Decision where needed, spec edit, change-log row, derivative updates (PWA dataset regeneration).

Outcome key:

- **Accept**: apply essentially as suggested.
- **Modify**: the concern is valid; the fix differs from the suggestion.
- **Decline**: no change; reason given.
- **Discuss**: a program-owner call (usually safety or structural) that needs a decision before any wording.
- **Answer**: a question, not a change request. Reply to the reviewer; may point to a spec gap.

Safeguards that apply (Part V): privilege changes require Privilege Change Review; restriction removals require Restriction Removal Review; skill IDs are frozen (retire, never renumber).

---

## Theme A: Solo entry and solo privileges (safety, highest priority)

> **Decided 2026-10-16 (v1.2, DD-029).** Solo is retired as the entry level and replaced by **Follow**: a flyer's first movement jumps are made with one leader holding Lead 1 or higher, and solo movement jumps become a **Lead 1 privilege**. The Solo skill IDs are retired in favour of `FOLLOW-*` IDs. Themes A and C are applied in v1.2; Themes B, D, E, F and G remain open.

Both reviewers independently pushed to make Solo stricter. This is the single most consequential decision in the set.

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | TS | Solo › Prerequisites (A license, 25 jumps) | 25 jumps is too early to focus on tracking/angle; belly fundamentals are still being learned. Suggests ~50 jumps. | **Discuss** | Competency-based progression (FP-001) argues against leaning on jump numbers, but the 25 floor is itself a number. Options: raise to 50; keep 25 but gate the solo privilege (A2); or tie it to a demonstrated belly-skill baseline. | Accepted, modified: USPA B License or equivalent (about 50 jumps, includes canopy proficiency); separate jump count dropped. See DD-029. |
| A2 | TS | Solo › Privileges ("Conduct solo belly-tracking jumps") | Solo tracking at low experience is dangerous and unverifiable: the evaluator can see the exit, not the flight path, and the jumper can't judge distance covered. First tracking jumps should be with an experienced jumper. | **Discuss** (lean Modify) | Strongest single comment. Possible shape: Solo certification is earned on coached jumps with an experienced flyer; unaccompanied solo tracking becomes a later privilege or needs N coached jumps first. Requires Privilege Change Review. | Accepted, restructured: Follow replaces Solo; solo jumps become a Lead 1 privilege (DD-029). |
| A3 | TS | Solo › Evaluation (flyer-q4) | Hard to verify a solo flyer kept a good flight path. | **Modify** | Folds into A2. If evaluation stays solo, require video showing the full flight path (wingsuit-style GPS or a camera flyer), not just the exit. | Resolved by DD-029: the leader is in the air for the full flight path; leader video is the preferred evidence. |
| A4 | ZV | Solo › Prerequisites | Add the B-license canopy control course, given the added risk of landing away from the designated LZ. | **Discuss** | Ties a USPA course to the spec, so it's US-specific. Could be written as "a canopy course covering off-field landings (e.g. USPA B-license canopy course)". | Accepted via A1: the B License prerequisite includes canopy proficiency training. |
| A5 | ZV | Solo › Prerequisites or Knowledge | Require an audible altimeter and a freefly-friendly rig. | **Modify** | Accept as an **equipment requirement**. The spec has no equipment section today; add one at Solo (carried by every later level). Define "freefly-friendly" in Knowledge (closed-pin rig, secured handles/BOC, no loose flaps). | Accepted: Required Equipment at Follow, applies at every later level; defined in Knowledge. |

## Theme B: Group (Flyer Tier) skills

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | ZV | GROUP-SLT-006 (avoid passing the leader) | Eliminate. Staying strictly behind the leader is not modern technique and builds bad positions (burble). A bit in front gives margin and makes following easier. Agrees with not being *too* far ahead. | **Modify** | Reword rather than retire: "Do not overtake the leader's line of flight or pass significantly ahead." Also edit the related Knowledge bullet ("Why passing the leader creates unnecessary risk") and the matching bullet in GROUP-SLT-001 guidance. If you prefer to retire SLT-006, that's a documented consolidation into SLT-001; the ID is never reused. | |
| B2 | ZV | GROUP-SLT-001 (establish the assigned slot) | "Establish the assigned slot" is too high a bar for entry. Flyers who can hold a quadrant under control can safely fly groups while still learning to slot. Asks whether "slot" can mean a zone. | **Accept** | Reword to "approach and hold the assigned slot or quadrant under control." Guidance: an assigned zone is acceptable at Group; precise slotting develops through Lead tiers. | |
| B3 | ZV | GROUP-FLT-001 (breakoff) | Breakoff is triggered by assigned **altitude**, not time. If you reach breakoff altitude first, you start breakoff. Don't slow down significantly before deployment; a hard slowdown is as dangerous as reversing. | **Accept** | Replace "at the assigned time" with "at the assigned altitude, or earlier if the flyer reaches it first." Add guidance: maintains speed through separation; no significant slowdown before deployment. Consider Safety Critical. | |
| B4 | TS | GROUP-FLT-001 (breakoff) | Flatten out (slow down) only after separating from the group, not mid-formation at the altimeter alarm. | **Accept** | Merges with B3 into one guidance line. | |
| B5 | TS | Group › Restrictions (no back flying) | Introduce back flying at Group in a small (2–3) controlled setting, with the privilege removable if the flyer crosses the centerline or moves too much. | **Discuss** (lean Decline for v1.2) | Conflicts with ZV's emphasis on proving follower skills first. Restriction Removal Review would need to show the developmental objective is kept. A middle path: allow back flying at Group only on a **coached** jump with an Evaluator. | |
| B6 | TS | Flyer Tier › Knowledge (flyer-q1) | Add: exit order for movement jumps (a jump with several pass-throughs exits as a freefly group), and using winds to inform heading choice. | **Accept** | Exit order → Group Knowledge. Winds → Solo Knowledge under Heading selection. | |
| B7 | ZV | Flyer Tier (flyer-q1) | Same as A4/A5 (altimeter, rig, canopy course). | n/a | Covered by A4/A5. | |

## Theme C: Solo skill wording (small edits)

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | ZV | SOLO-FLT-001 (stable exit) | Can be any style of exit (belly, track, freestyle)? | **Accept** | Guidance: "Any exit style is acceptable if it is controlled and transitions promptly to the planned flight." | Accepted (FOLLOW-FLT-001). |
| C2 | ZV | SOLO-FLT-002 (stable belly tracking) | Add glide-path control. | **Accept** | Add to guidance: controls glide path, not only body position. | Accepted (FOLLOW-FLT-002). |
| C3 | ZV | SOLO-FLT-004 (deploy in intended area) | Add "at the intended altitude." | **Accept** | Requirement wording becomes "Deploy in the intended area at the intended altitude." | Accepted (FOLLOW-FLT-005). |
| C4 | ZV | SOLO-HDG-001 (determine heading) | Heading is relative to the drift zone as well as jump run. | **Accept** | Student explanation: "relative to jump run and the drift zone." | Accepted (FOLLOW-HDG-001). |
| C5 | ZV | SOLO-HDG-003 (maintain heading) | A **lack** of significant movement should also be investigated. | **Accept** | Add: "Absence of meaningful forward movement should also be investigated." | Accepted (FOLLOW-HDG-003). |

## Theme D: Readiness before Lead

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | ZV | Lead 1 › Prerequisites (core-q2, open-final) | Demonstrated flight skills as a follower in groups before Lead is extremely important; reviewer didn't see it. | **Modify** | It exists: Group certification requires consistent slot discipline and predictable participation. It just isn't visible on the ladder. Two fixes: (1) say it explicitly in the Lead 1 intent/prerequisites ("Group certification, which requires demonstrated follower flight skills"); (2) Discuss whether Lead 1 also needs a minimum number of logged group jumps as a follower *after* Group. | |

## Theme E: Leader Tier

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | TS | LEAD3-MGT-001 (leader-q4) | Changing the plan mid-jump is a bad idea; a Lead 3 isn't experienced enough to recognize overwhelm while also navigating and flying. Simplification belongs on the ground before the jump. | **Modify** | Fair challenge to assessability. Reframe: primary evidence is **pre-jump** calibration (plan matched to participants) plus **in-air** simplification limited to pre-briefed fallbacks (e.g. "if we lose anyone, we stop turning and fly straight"). That keeps the competency while removing improvised replanning. | |
| E2 | TS | Lead 2 › Privileges (note-priv-Lead2) | Emphasize simplicity: a 2-way to 3-way is a big jump; one turn, maybe two. | **Accept** | Strengthen guidance under the Lead 1 Simplicity Principle as applied to Lead 2. Optional: cap planned heading changes at Lead 2. | |
| E3 | TS | Lead 3 › Privileges (note-priv-Lead3) | More than 3 followers is fine at Lead 3; maybe 4. | **Decline** (for now) | The Lead N naming and the tier structure assume group size grows one per level; 4 followers is Lead 4. Revisit only if other reviewers agree. | |
| E4 | TS | Lead 2 › Restrictions (leader-q2) | Disagrees with the Lead 2 back-flying restriction (answer: "Not for backfly"). | **Discuss** | Same question as B5. Decide once for Group, Lead 1 and Lead 2 together. | |
| E5 | TS | Lead 4 (leader-q5) | Lead 4 removing guardrails is the right call. | **Decline** (no change) | Endorsement. | |
| E6 | TS | Lead 4 › This Level Is Not About | Lead 4 flyers must not act like they know everything; learning continues and they should take everyone's ideas on board. | **Accept** | Mostly present ("Believing there is nothing left to learn"). Add: "Dismissing input from participants." | |
| E7 | TS | Leader Tier (leader-q6) | What leaders do every jump: a thorough briefing, walking every part from exit to breakoff. | **Accept** (verify) | Check LEAD1-BRF-001/002 covers exit-through-breakoff explicitly; add the phrase if not. | |

## Theme F: EE Tier

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | TS | Evaluator competencies (ee-q1) | Add consistency. | **Modify** | Already part of Standards Discipline and Examiner calibration duties. Make it explicit in the Standards Discipline definition rather than adding a seventh competency. | |
| F2 | TS | Evaluator › Evidence bar (ee-q3) | When uncertain, consistency is what matters. | **Decline** (no change) | Matches "probably ready is Not Yet." | |
| F3 | TS | Evaluator › Restrictions ("without sufficient evidence") | What counts as "sufficient"? People will argue. | **Accept** | Real gap. Define in Evidence Architecture: minimum evidence per level (e.g. video showing exit through deployment for flyer levels), plus a pointer to EVAL-STD guidance. | |
| F4 | TS | Evaluator › Selection (note-priv-Evaluator) | How will evaluators be chosen? | **Answer** | Selection section + DD-017/DD-028 cover it. Reply to the reviewer; consider a plain-language summary in the Student Guide. | |
| F5 | TS | Examiner (note-priv-Examiner) | Can examiners be from anywhere in the world? | **Answer** | The spec is silent on geography. Reply yes (if so), and decide whether to state it. | |

## Theme G: Overall framework (UX, not spec wording)

| # | Rev | Spec target | Comment (paraphrased) | Proposed | Notes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | TS | Whole program (core-q4, core-q5) | Too much information and too many words; would participate personally but complexity could deter newer flyers. Wants simplicity. | **Modify** | Not a spec change: the spec is meant to be exhaustive (DD-019). Fix in the **derived outputs**: a short Student Guide, and progressive disclosure in the PWA (headline requirement first, student explanation and guidance on tap). Feed into the PWA UI/UX pass. | |
| G2 | ZV | Program structure (core-q5) | Progression is a web, not a ladder, but the ladder helps comprehension. | **Decline** (no change) | The reviewer accepts the ladder. Possibly acknowledge it in Foundational Philosophy. | |
| G3 | TS | Core (core-q1) | Both competency and experience matter: natural flyers new to the sport haven't seen much; experienced jumpers may lack practice. | **Decline** (no change) | Supports FP-001 as written; related to A1. | |
| G4 | ZV | Ready / Not Yet (core-q3) | Whether it works "depends on the incentives." | **Discuss** | Worth a follow-up conversation; links to the evaluator-incentive design (paid reviews, DZ relationships). | |
| G5 | TS | Open | Offers to keep helping. | n/a | Close the loop with the v1.2 changes; candidate for direct appointment conversation (DD-028)? | |

---

## Proposed v1.2 scope

1. **Decide first:** A1, A2, A4 (Solo gate and privilege), B5 + E4 (back flying, decided once), D1 (follower-jump minimum).
2. **Ready to apply once decisions are in:** A5, B1–B4, B6, C1–C5, E1, E2, E6, E7, F1, F3.
3. **No spec change:** E3, E5, F2, G2, G3; reply to the reviewer on F4, F5.
4. **Out of spec scope:** G1 goes to the PWA UI/UX pass and the Student Guide.

New Design Decisions likely needed: Solo privilege/gate change (DD-029), equipment requirements (DD-030), sufficient-evidence definition (DD-031).

## Downstream (krav-pwa / krav-platform)

- Regenerate the level and skill dataset from the updated spec; ship as a migration.
- Prerequisite changes (A1/A4/A5/D1) touch the PWA's sticker prerequisites and the submit-flow gate. Check how jump count and license are enforced today.
- Breakoff reclassified as Safety Critical (B3) changes evaluation outcomes for in-flight reviews.
- Existing Solo/Group holders: decide whether a stricter gate is grandfathered (recommended: yes, no retroactive revocation).
