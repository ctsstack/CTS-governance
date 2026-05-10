# CTS GPA Workflow — Cowork Implementation Specification

---

## Purpose

This document specifies the architecture, schema, and workflow for the CTS Governance Projection Artifact (GPA) system. It is written for Cowork + Claude to reason about, implement tooling for, and extend as necessary. It is not a prescriptive step-by-step script — it is a specification from which Cowork should derive its own implementation decisions.

---

## Architectural Overview

The CTS governance system separates concerns across four surfaces:

| Surface                        | Role                                                     |
| ------------------------------ | -------------------------------------------------------- |
| GitHub `CTS-governance` repo   | Canonical governance authority                           |
| Local git clone (inside Vault) | Operational working copy                                 |
| Obsidian Vault                 | Cognitive editing, reference, and GPA staging            |
| GPAs                           | Derived Governance Projection and distribution Artifacts |

The git clone lives **inside** the Vault at:

```
K:\Reflexion\Governance\CTS-governance\
```

This means Obsidian can read and edit governance files directly. Git remains fully independent — the Obsidian Git plugin is intentionally not used. Governance publication is always a deliberate, manual git commit and push.

**Critical constraint:** Obsidian must not index `.git` internals. Confirm `userIgnoreFilters: [".git"]` is present in `.obsidian/app.json` before placing the clone inside the Vault.

---

## Reference Diagram

![CTS GPA Architecture](CTS_GPA_Architecture.drawio)

*Diagram shows: GitHub as canonical authority, git clone overlaid in Vault, GPA extraction from governance corpus, GPA injection/transformation into destination-typed outputs, and the publishing pipeline feeding Chat/Research, Code/Arch, Video, Website, Blog, Article, and SM Post.*

---

## What Is a GPA?

**A GPA is a derived projection of canonical governance for a specific execution or publication context.**

A GPA is not a summary, narrative, or documentation. It is a precision-formatted governance payload bound to a specific governance state.

GPAs serve two distinct purposes:

1. **Session injection** — delivering authoritative governance context into AI assistant sessions
2. **Content seeding** — delivering governance-sourced material into the publishing pipeline (blog, article, video script, SM post, etc.)

The destination determines the extraction lens. The governance corpus is always the source.

---

## GPA Types and Creation Modes

| GPA Type | Purpose | Primary Consumer | Creation Mode | Current Feasibility |
|---|---|---|---|---|
| `core` | Foundational CTS principles, authority semantics | LLM sessions, onboarding | Generated | Yes — bounded, known source |
| `domain` | Domain-specific governance (metadata schema, serialization contracts) | LLM sessions, tooling | Generated | Yes — bounded, known source |
| `session` | Behavioral directives scoped to a specific AI interaction context | LLM session injection | Generated | Yes — bounded, known source |
| `content` | Governance-sourced narrative for human-readable publishing output | Blog, article, video, SM post | Human-assisted | Always — editorial judgment required |

**Rationale:** `core`, `domain`, and `session` GPAs are deterministic derivations from structured governance source — mechanical extraction is more reliable than manual composition for these types. `content` GPAs require editorial judgment about audience, framing, and narrative angle; that judgment is inherently human.

**Important constraint:** The current corpus is structured enough to generate the first bounded set of GPAs mechanically. It is not yet structured enough for arbitrary, fully automated extraction across the entire corpus. Full corpus automation is a future milestone gated on corpus structure maturity — not a current obligation.

### Practical Naming Examples

**Generated:**
```
CTS_CORE_MIN_GPA.md
CTS_METADATA_GPA.md
CTS_SESSION_DEFAULT_GPA.md
```

**Human-curated:**
```
CTS_CONTENT_Substack_AI_Decay_GPA.md
CTS_CONTENT_Video_Cognitive_Load_GPA.md
```

---

## GPA Header Schema

Every GPA carries a YAML frontmatter header. The following fields are required and sufficient:

```yaml
---
gpa_id: "GPA-[TYPE]-[NNN]"
gpa_type: "core | domain | session | content"
source_commit: "[full git commit hash]"
generated_at: "[ISO 8601 timestamp]"
status: "draft | active | superseded"
---
```

### Field Semantics

| Field | Purpose | Notes |
|---|---|---|
| `gpa_id` | Unique stable identifier | Format: GPA-CORE-001, GPA-SESSION-003, etc. |
| `gpa_type` | Extraction lens and destination class | Determines payload structure and creation mode |
| `source_commit` | Pins the exact governance state at derivation time | Sine qua non — remove it and provenance collapses |
| `generated_at` | Records derivation timestamp | ISO 8601, UTC. Populate from `git rev-parse HEAD` at composition time |
| `status` | Lifecycle state | Only `active` GPAs should be injected or used |

### Dropped Fields (intentionally omitted)

`gpa_version`, `valid_for_release`, `injected_by`, `source_authority` — overhead without operational value at current scale. Candidates for reinstatement when corpus stabilizes and multi-participant workflows emerge.

---

## GPA Lifecycle

```
draft → active → superseded
```

| State | Meaning |
|---|---|
| `draft` | Under composition, not yet authoritative |
| `active` | Committed to Vault, bound to source commit, cleared for injection/use |
| `superseded` | Replaced by a newer GPA; retained for audit trail |

For generated GPAs, the generation script sets status to `active` on successful completion. For content GPAs, the author sets status to `active` after editorial review. The commit act is the review gate in both cases.

---

## GPA Payload Rule

Every statement in a GPA payload must be traceable to a specific source document in the governance corpus. If a statement cannot be pointed to a source document, it does not belong in the GPA.

This single rule does more error-prevention work than any schema enforcement mechanism. For generated GPAs, this rule must be enforced programmatically — each extracted statement should carry a source document reference.

---

## GPA Generation Workflow

```
GitHub CTS-governance (canonical)
        ↓  git pull
Local clone inside Vault
        ↓  [generated: script extracts from corpus]
        ↓  [content: author reviews corpus, composes payload]
GPA composed with header + payload
        ↓  payload rule verified
GPA stored in Vault/GPAs/[type]/
        ↓  status set to active
GPA injected into session or publishing pipeline
```

---

## Vault Storage Structure

```
Vault/
  Governance/
    CTS-governance/              ← git clone (constitutional authority)
      [governance source files]
  GPAs/
    core/
      GPA-CORE-001.md
      CTS_CORE_MIN_GPA.md
    domain/
      GPA-DOMAIN-metadata-001.md
      CTS_METADATA_GPA.md
    session/
      GPA-SESSION-default-001.md
      CTS_SESSION_DEFAULT_GPA.md
    content/
      CTS_CONTENT_Substack_AI_Decay_GPA.md
      CTS_CONTENT_Video_Cognitive_Load_GPA.md
```

GPAs in the Vault are derived artifacts, not governance authorities. They do not feed back into the git repository. The authority surface remains GitHub.

---

## Governance Publication Workflow

```
Obsidian (edit governance source file in CTS-governance/)
        ↓
git add [file]
git commit -m "[meaningful semantic commit message]"
        ↓
git push → GitHub (canonical publication)
```

Commit semantics matter. Commit messages should describe the governance intent of the change, not the mechanical action.

---

## Destination-Typed Output Pipeline

GPAs feed a multi-destination publishing pipeline. The `gpa_type` field determines the extraction lens:

| Destination | GPA Type | Output Format |
|---|---|---|
| LLM session (Chat, Code/Arch) | `session`, `core`, `domain` | Injected as system context |
| Blog / Article / Substack | `content` | `.md` seeded narrative |
| Video script | `content` | `.md` structured outline |
| Website content | `content` | `.md` or `.html` |
| SM Post | `content` | Short-form `.md` |
| Tooling / Automation | `domain` | YAML/structured payload |

A single governance concept may produce multiple GPAs with different types for different destinations. The corpus is always the source; the type determines the lens.

---

## Error Prevention Model

1. **Source commit binding** — every GPA is pinned to the exact governance state from which it was derived; drift is detectable
2. **Payload traceability rule** — every statement must point to a source document; unverifiable content is excluded
3. **Human-readable format** — GPA payloads are auditable before status is set to `active`
4. **Type constraints** — GPA type determines creation mode and limits what content belongs in the payload
5. **Supersession semantics** — stale GPAs are explicitly marked, preventing injection of outdated governance

---

## Governance Posture (Current)

CTS is in an early doctrinal state: single author, rapid evolution, architecture still stabilizing. The appropriate posture is **lightweight operational discipline**, not institutional governance machinery.

This means:
- Avoid casual, unreflective governance edits
- Treat canonical changes as intentional acts
- Use meaningful commit messages
- Maintain awareness of the distinction between working cognition (Vault notes) and constitutional canon (git-tracked governance documents)

Heavier governance process — promotion semantics, multi-participant review, formal modification pathways — is appropriate when doctrine hardens. Do not simulate that structure prematurely.

---

## Open Items (Deferred)

- Scripted GPA extraction tooling for `core`, `domain`, `session` types
- GPA schema validation tooling
- Automated drift detection (GPA `source_commit` vs. current HEAD)
- Multi-participant review process
- GPA deprecation and archival handling
- Formal `valid_for_release` binding
- Full corpus automation (gated on corpus structure maturity)

---

## Implementation Notes for Cowork

- The `.git` directory within the Vault clone must be excluded from Obsidian indexing. Verify `userIgnoreFilters: [".git"]` in `.obsidian/app.json` before any other operations.
- Git operations (add, commit, push, pull) are executed independently of Obsidian — via terminal, Cowork-invoked script, or direct git tooling.
- GPA files are plain markdown with YAML frontmatter. No special tooling is required to create or edit them.
- The `source_commit` field is populated from `git rev-parse HEAD` at the time of GPA composition.
- Generated GPA scripts must enforce the payload traceability rule programmatically — each extracted statement carries a source document reference.
- Priority implementation target: generation scripts for `CTS_CORE_MIN_GPA.md`, `CTS_METADATA_GPA.md`, and `CTS_SESSION_DEFAULT_GPA.md`.

---

*Document status: working specification. Subject to revision as governance doctrine matures.*
