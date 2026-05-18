---
created: 2026-01-27T20:50:00Z
edited: 2026-03-02T20:27:00Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R0_INTERNAL"
authority_level: "policy"
governance_tier: "core"
governance_class: “governed”
wf_status: "active"
tags: ["frontmatter","serialization","metadata","governance","cts","policy"]
index_phrase: "Defines the authoritative serialization, quoting, and normalization rules for CTS frontmatter fields."
---
## Purpose

This contract defines the **canonical serialization rules** for CTS frontmatter. It governs how metadata fields are **encoded, quoted, and normalized**, independent of their semantic meaning.

This document is authoritative for all CTS tooling, validators, loaders, and enforcement scripts.

---

## Scope and Non‑Scope

This contract:

- Defines how metadata is written

- Defines canonical quoting and list forms

- Defines normalization and rejection rules


This contract does **not**:

- Define the semantic meaning of fields

- Define governance authority or workflow

- Define field existence or allowed values


Those concerns are handled by the Metadata Field Reference and related policy documents.

---

## General Serialization Rules

- Frontmatter MUST be valid YAML

- Field order is **not semantically significant**

- Fields MUST be identified by name, not position

- Tooling MUST be resilient to ordering differences


---

## Scalar Classification

CTS frontmatter fields fall into two scalar classes for serialization purposes.

---

## Quoted Enumerated Scalars

The following fields are **enumerated identifiers** and MUST be serialized as **quoted scalars** to avoid YAML ambiguity and to preserve forward compatibility:

- artifact

- origin

- authority_level

- governance_tier

- wf_status


---

## Unquoted Free Scalars

The following fields MUST be serialized as **unquoted scalars**. These fields are timestamps or simple provenance markers and do not carry enumerated or structured semantics:

- created

- edited

- source


---

## Quoted Structured Scalars

The following fields MUST be serialized as **quoted scalars** due to structure, pattern constraints, or human‑readable free text:

- release

- index_phrase


---

## Release Field Serialization Rule

`release` MUST be a quoted scalar matching the closed distribution vocabulary defined by CTS governance.

`release` SHALL represent distribution posture only and MUST NOT encode revision, versioning, or change chronology semantics.

---

## List Fields

### Tags Serialization and Normalization Rule

The `tags` field MUST be serialized as an **inline YAML list of quoted strings**, with no spaces following delimiters. The canonical and enforced form is:

```
tags: ["governance","cts","policy"]
```

The following encodings are non‑conformant and MUST be rejected or normalized:

- Block‑style lists

- Unquoted tag values

- Inline lists containing spaces after commas

- Multi‑line tag representations


---

## Empty and Optional Fields

- Optional fields MAY be present with empty values

- Empty fields MUST retain valid YAML syntax

- Tooling MUST distinguish between empty and absent fields


---

## Normalization vs Rejection

CTS tooling MAY normalize non‑conformant serialization into canonical form when safe to do so.

If normalization would risk semantic ambiguity, the artifact MUST be rejected and flagged for remediation.

---

## Enforcement

Any CTS‑governed artifact that violates this contract:

- MUST be flagged during validation

- MUST NOT be promoted to authoritative status

- MAY be blocked at ingress or publication


---

## Status

This contract is active, core‑tier, and mandatory for all CTS‑governed artifacts.