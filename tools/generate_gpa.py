#!/usr/bin/env python3
"""
CTS GPA Generation Script

Generates GPA-CORE-001, GPA-DOMAIN-metadata-001, and GPA-SESSION-default-001
from the CTS governance corpus.

Usage:
    python generate_gpa.py                   # generate all three
    python generate_gpa.py --type core
    python generate_gpa.py --type metadata
    python generate_gpa.py --type session
    python generate_gpa.py --vault-root /custom/path

Paths resolve relative to this script's location:
    Script:     CTS-governance/tools/generate_gpa.py
    Repo root:  CTS-governance/
    Vault root: two levels up (K:/Reflexion/)
    GPA output: Vault root/GPAs/[type]/[filename]
"""

import subprocess
import datetime
import os
import sys
import argparse

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
VAULT_ROOT  = os.path.normpath(os.path.join(REPO_ROOT, "..", ".."))

GOVERNANCE_DIR    = os.path.join(REPO_ROOT, "governance")
FOUNDATIONAL_DIR  = os.path.join(GOVERNANCE_DIR, "foundational")
METADATA_DIR      = os.path.join(GOVERNANCE_DIR, "metadata")
ARTIFACT_DIR      = os.path.join(GOVERNANCE_DIR, "artifact_model")

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def get_source_commit():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Could not retrieve git HEAD: {e}", file=sys.stderr)
        sys.exit(1)


def get_generated_at():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def verify_source(path, label):
    if not os.path.isfile(path):
        print(f"ERROR: Source document not found — {label}: {path}", file=sys.stderr)
        sys.exit(1)


def write_gpa(path, content, label):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  + {label}")
    print(f"    {path}")


def gpa_header(gpa_id, gpa_type, source_commit, generated_at):
    return (
        f"---\n"
        f'gpa_id: "{gpa_id}"\n'
        f'gpa_type: "{gpa_type}"\n'
        f'source_commit: "{source_commit}"\n'
        f'generated_at: "{generated_at}"\n'
        f'status: "active"\n'
        f"---\n"
    )


# ---------------------------------------------------------------------------
# GPA-CORE-001
# Sources: CTS Core Philosophy.md, CTS Execution Compliance Contract.md
# ---------------------------------------------------------------------------

def build_core_gpa(source_commit, generated_at):
    verify_source(
        os.path.join(FOUNDATIONAL_DIR, "CTS Core Philosophy.md"),
        "CTS Core Philosophy.md"
    )
    verify_source(
        os.path.join(FOUNDATIONAL_DIR, "CTS Execution Compliance Contract.md"),
        "CTS Execution Compliance Contract.md"
    )

    header = gpa_header("GPA-CORE-001", "core", source_commit, generated_at)

    payload = """\
# CTS Core GPA — Minimal Injection Payload

Foundational CTS principles and authority semantics for LLM session injection and onboarding.
Every statement is traceable to a source document in the governance corpus.

---

## System Composition

> Source: CTS Core Philosophy.md

CTS is a constructed system composed of three co-equal domains:

**1. Cognition Topology Stack (Topology)**
Defines the structural model of cognition: knowledge boundaries, artifact relationships,
layer separation and interface constraints.
Function: how cognition is organized.

**2. Cognition Tool Set (Tools)**
Implements operational capability within the topology. Tools operate *within* the topology;
they do not define it.
Function: how cognition is executed.

**3. Governance (Artifacts)**
Defines authority, meaning, and system coherence: metadata schema, authority levels,
provenance, and lifecycle control. Meaning attaches to artifacts — not to tools.
Function: how the system remains coherent over time.

---

## Emergent Layer: COE

> Source: CTS Core Philosophy.md

The Cognitive Operating Environment (COE) is not a component, module, or repository.
It is the emergent result of Topology, Tools, and Governance operating together within
defined constraints. COE cannot be constructed directly — it can only emerge from a
correctly governed system.

> CTS constructs the system. COE is the result.

---

## Non-Inversion Constraint (Normative)

> Source: CTS Core Philosophy.md

The following interpretations are strictly prohibited:

- COE contains CTS
- Tools define topology
- Governance is optional or descriptive
- Meaning is derived from tools instead of artifacts

Any such inversion constitutes structural violation of CTS doctrine.

---

## Practical Implications

> Source: CTS Core Philosophy.md

- Governance artifacts MUST remain independent and authoritative
- Tools MUST defer to governance
- Publication surfaces (e.g., website) are projections, not sources of truth
- Artifact authority MUST be preserved across all transformations

---

## Execution Compliance — Core Principle

> Source: CTS Execution Compliance Contract.md

No artifact is valid unless it is compliant at time of creation.

All generated artifacts MUST include:
- Valid CTS frontmatter block
- All required fields populated
- Proper serialization
- Body consistent with artifact role

---

## Execution Rules

> Source: CTS Execution Compliance Contract.md

1. Frontmatter MUST be first
2. No missing fields
3. Canonical field names only
4. Body must match artifact role
5. `governance_class` — if present, MUST be a valid enumerated value; if required by
   policy, MUST be present; if not applicable, SHOULD be absent (not empty)

---

## Non-Compliance Handling

> Source: CTS Execution Compliance Contract.md

If compliance cannot be achieved:
- Do NOT emit the artifact
- Report all violations

Prohibited at all times: no frontmatter, invalid fields, partial compliance,
optional governance treatment.

---

## Governance Posture (Current)

> Source: CTS GPA Cowork Spec

CTS is in early doctrinal state: single author, rapid evolution, architecture stabilizing.
Appropriate posture is lightweight operational discipline — not institutional governance
machinery. Heavier process (multi-participant review, formal modification pathways) is
deferred until doctrine hardens.
"""

    return header + "\n" + payload


# ---------------------------------------------------------------------------
# GPA-DOMAIN-metadata-001
# Sources: CTS Metadata Field Reference.md, CTS Frontmatter Serialization Contract.md,
#          CTS Timestamp Semantics and Authority Policy.md
# ---------------------------------------------------------------------------

def build_metadata_gpa(source_commit, generated_at):
    verify_source(
        os.path.join(METADATA_DIR, "CTS Metadata Field Reference.md"),
        "CTS Metadata Field Reference.md"
    )
    verify_source(
        os.path.join(METADATA_DIR, "CTS Frontmatter Serialization Contract.md"),
        "CTS Frontmatter Serialization Contract.md"
    )
    verify_source(
        os.path.join(METADATA_DIR, "CTS Timestamp Semantics and Authority Policy.md"),
        "CTS Timestamp Semantics and Authority Policy.md"
    )

    header = gpa_header("GPA-DOMAIN-metadata-001", "domain", source_commit, generated_at)

    payload = """\
# CTS Metadata GPA — Domain Governance Payload

Complete CTS metadata schema and serialization rules for producing CTS-compliant frontmatter.
Every statement is traceable to a source document in the governance corpus.

---

## Field Reference

> Source: CTS Metadata Field Reference.md

| Field            | Required    | Type            | Mutable                      |
|------------------|-------------|-----------------|------------------------------|
| `created`        | yes         | timestamp       | no (repair policy only)      |
| `edited`         | yes         | timestamp       | yes (tool-managed)           |
| `artifact`       | yes         | enum            | no                           |
| `origin`         | yes         | enum            | no                           |
| `source`         | yes         | string          | no                           |
| `release`        | yes         | enum            | yes (posture changes only)   |
| `authority_level`| yes         | enum            | no                           |
| `governance_tier`| yes         | enum            | no                           |
| `governance_class`| conditional| enum            | yes (until admission final)  |
| `wf_status`      | yes         | enum            | yes                          |
| `tags`           | yes         | list of strings | yes                          |
| `index_phrase`   | yes         | string          | yes                          |

Fields not listed here are not permitted unless introduced by policy.

---

## Allowed Values

> Source: CTS Metadata Field Reference.md

**artifact:** `self` | `proxy` | `external`

**origin:** `internal` | `external` | `imported`

**source:** `reflexion` (unquoted) or other CTS-defined provenance descriptor

**authority_level:** `none` | `guidance` | `policy`

**governance_tier:** `supporting` | `core`

**governance_class:** `governed` | `candidate`
(conditional; SHOULD be absent if not applicable — MUST NOT be empty)

**wf_status:** `draft` | `active` | `deprecated` | `archived`

**release vocabulary:**

| Value            | Meaning                                  |
|------------------|------------------------------------------|
| `R0_INTERNAL`    | Core CTS governance only                 |
| `R1_RESTRICTED`  | Internal operational circulation         |
| `R2_CONFIDENTIAL`| Sensitive; explicit approval required    |
| `R3_PARTNER`     | Authorized external collaborators        |
| `R4_PUBLIC`      | Unrestricted public distribution         |

`release` expresses reliance and exposure posture — not revision history, version numbers,
or edit sequences. Mechanical version history is Git's domain exclusively.

---

## Serialization Rules

> Source: CTS Frontmatter Serialization Contract.md

Frontmatter MUST be valid YAML. Field order is not semantically significant.

**Quoted enumerated scalars** (MUST be quoted):
`artifact`, `origin`, `authority_level`, `governance_tier`, `wf_status`

**Unquoted free scalars** (MUST NOT be quoted):
`created`, `edited`, `source`

**Quoted structured scalars** (MUST be quoted):
`release`, `index_phrase`

**Tags** — MUST be inline YAML list of quoted strings, no spaces after delimiters:

```yaml
tags: ["governance","cts","policy"]
```

Non-conformant forms — block-style lists, unquoted values, spaces after commas,
multi-line representations — MUST be rejected or normalized.

---

## Timestamp Semantics

> Source: CTS Timestamp Semantics and Authority Policy.md

Format: ISO 8601 UTC (Z-terminated) — `YYYY-MM-DDTHH:MM:SSZ`

**`created`**: First admission into CTS governance. Immutable. Repair policy only.

**`edited`**: Most recent modification. Mutable. Must reflect latest edit.
May be empty at initial creation.

Constraints:
- `edited` MUST NOT precede `created`
- Local time zones prohibited
- Non-ISO formats prohibited
- Partial timestamps prohibited
- Inferred timestamps prohibited

---

## Conflict Resolution Order

> Source: CTS Metadata Field Reference.md

1. CTS Frontmatter Serialization Contract — governs syntax and encoding
2. Field-specific policy documents — govern semantics
3. CTS Metadata Field Reference — governs field definitions, allowed values, constraints
"""

    return header + "\n" + payload


# ---------------------------------------------------------------------------
# GPA-SESSION-default-001
# Sources: CTS Execution Compliance Contract.md, CTS Core Philosophy.md,
#          CTS Artifact Semantics.md
# ---------------------------------------------------------------------------

def build_session_gpa(source_commit, generated_at):
    verify_source(
        os.path.join(FOUNDATIONAL_DIR, "CTS Execution Compliance Contract.md"),
        "CTS Execution Compliance Contract.md"
    )
    verify_source(
        os.path.join(FOUNDATIONAL_DIR, "CTS Core Philosophy.md"),
        "CTS Core Philosophy.md"
    )
    verify_source(
        os.path.join(ARTIFACT_DIR, "CTS Artifact Semantics.md"),
        "CTS Artifact Semantics.md"
    )

    header = gpa_header("GPA-SESSION-default-001", "session", source_commit, generated_at)

    payload = """\
# CTS Session GPA — Default AI Session Injection Payload

Behavioral directives for AI agents operating within a CTS-governed session. Inject as
system context before any CTS artifact generation task. Complements — does not replace —
core and domain GPAs. Every directive is traceable to a source document in the governance
corpus.

---

## Mandatory Output Behavior

> Source: CTS Execution Compliance Contract.md

Every artifact produced in this session MUST include:
- Valid CTS frontmatter as the first block in the file
- All required fields populated with valid enumerated values
- Serialization conformant with the CTS Frontmatter Serialization Contract
- Body content consistent with the declared artifact role

Descriptor artifacts (proxy, external) MUST conform to Artifact Semantic body structure.

---

## Execution Rules

> Source: CTS Execution Compliance Contract.md

1. Frontmatter MUST be first — no content before the YAML block
2. No missing required fields — populate or request clarification; never omit
3. Canonical field names only — no aliases, abbreviations, or invented fields
4. Body must match artifact role
5. `governance_class` — if present, MUST be `governed` or `candidate`; MUST NOT be
   inferred by tooling; SHOULD be absent if not applicable

---

## Validation Behavior

> Source: CTS Execution Compliance Contract.md

- Missing data → request clarification or apply documented default
- Invalid values → correct or fail explicitly; do not silently coerce
- Output must be internally consistent

**Strict mode** (default): enforce and reject non-compliant output.
**Assisted mode**: suggest corrections and iterate with the author.

---

## Non-Compliance Handling

> Source: CTS Execution Compliance Contract.md

If full compliance cannot be achieved:
- Do NOT emit the artifact
- Report all violations explicitly before attempting correction

---

## Prohibited Behaviors

> Source: CTS Execution Compliance Contract.md

- Emitting artifacts without frontmatter
- Using invalid or non-canonical field values
- Partial compliance (some fields valid, others absent or malformed)
- Treating governance as optional or advisory

---

## Structural Authority Rules

> Source: CTS Core Philosophy.md

- Governance artifacts are authoritative; tools defer to them
- Meaning attaches to artifacts — not to tools
- Publication surfaces are projections, not sources of truth
- Artifact authority must be preserved across all transformations

Do not invert these relationships. COE emerges from correctly governed artifacts —
it cannot be constructed by tooling alone.

---

## Artifact Role Semantics

> Source: CTS Artifact Semantics.md

| Role       | Meaning                                                        |
|------------|----------------------------------------------------------------|
| `self`     | Artifact governs itself; frontmatter and body are co-resident  |
| `proxy`    | Descriptor for a non-metadata-capable object in the Vault      |
| `external` | Descriptor for an object outside the Vault (GitHub, MEDIA_SPINE)|

Constraints for proxy and external descriptors:
- One structured reference section only
- No absolute filesystem paths
- No multiple targets in a single descriptor

---

## Session Compliance Summary

> Source: CTS Execution Compliance Contract.md, CTS Core Philosophy.md

An AI system in a CTS session MUST:

1. Produce fully compliant frontmatter before any artifact body
2. Use only canonical field names and enumerated values
3. Refuse to emit non-compliant artifacts and report all violations
4. Preserve artifact authority across all operations
5. Treat governance as structural — not advisory
"""

    return header + "\n" + payload


# ---------------------------------------------------------------------------
# Dispatch table
# ---------------------------------------------------------------------------

GPA_REGISTRY = {
    "core": {
        "builder":    build_core_gpa,
        "output_dir": "core",
        "filename":   "CTS_CORE_MIN_GPA.md",
        "label":      "GPA-CORE-001  →  GPAs/core/CTS_CORE_MIN_GPA.md",
    },
    "metadata": {
        "builder":    build_metadata_gpa,
        "output_dir": "domain",
        "filename":   "CTS_METADATA_GPA.md",
        "label":      "GPA-DOMAIN-metadata-001  →  GPAs/domain/CTS_METADATA_GPA.md",
    },
    "session": {
        "builder":    build_session_gpa,
        "output_dir": "session",
        "filename":   "CTS_SESSION_DEFAULT_GPA.md",
        "label":      "GPA-SESSION-default-001  →  GPAs/session/CTS_SESSION_DEFAULT_GPA.md",
    },
}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate CTS Governance Projection Artifacts from the governance corpus."
    )
    parser.add_argument(
        "--type",
        choices=list(GPA_REGISTRY.keys()),
        default=None,
        help="GPA type to generate. Omit to generate all three.",
    )
    parser.add_argument(
        "--vault-root",
        default=None,
        help=f"Override Vault root path. Default: {VAULT_ROOT}",
    )
    args = parser.parse_args()

    vault_root = os.path.normpath(args.vault_root) if args.vault_root else VAULT_ROOT
    gpa_root   = os.path.join(vault_root, "GPAs")

    source_commit = get_source_commit()
    generated_at  = get_generated_at()
    targets       = [args.type] if args.type else list(GPA_REGISTRY.keys())

    print()
    print("CTS GPA Generation")
    print(f"  source_commit : {source_commit}")
    print(f"  generated_at  : {generated_at}")
    print(f"  vault_root    : {vault_root}")
    print(f"  targets       : {', '.join(targets)}")
    print()

    for target in targets:
        spec    = GPA_REGISTRY[target]
        content = spec["builder"](source_commit, generated_at)
        out     = os.path.join(gpa_root, spec["output_dir"], spec["filename"])
        write_gpa(out, content, spec["label"])

    print()
    print(f"{len(targets)} GPA(s) generated — status: active")
    print()


if __name__ == "__main__":
    main()
