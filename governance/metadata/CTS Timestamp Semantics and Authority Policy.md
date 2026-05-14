---
created: 2026-04-24T17:05:00Z
edited: 2026-05-14T19:13:12Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R4_PUBLIC"
authority_level: "policy"
governance_tier: "core"
governance_class: “governed”
wf_status: "active"
tags: ["cts","timestamp","policy","governance","metadata"]
index_phrase: "Defines the authoritative semantics, constraints, and usage rules for timestamps within CTS governed artifacts"
---

## Purpose

Define the authoritative semantics, constraints, and enforcement rules for timestamp fields within CTS-governed artifacts. 

---

## Scope

Applies to:
- created
- edited

---

## Core Principle

Timestamps are authoritative system metadata used for ordering, provenance, and auditability.

---

## Timestamp Format (Normative)

ISO 8601 UTC (Z-terminated)

Example:
2026-04-24T17:05:00Z

---

## Field Semantics

### created
Represents first admission into CTS governance.

- Required
- Immutable
- Only changeable via repair policy

### edited
Represents most recent modification.

- Required (may be empty initially)
- Mutable
- Must reflect latest edit

---

## Authority Model

created → high / immutable  
edited → medium / mutable  

---

## Generation Rules

- Prefer system-generated timestamps  
- Manual entry must conform exactly  

---

## Consistency Rules

- edited must not precede created  
- Empty edited valid only at creation  

---

## Validation

Non-compliant if:
- Invalid format
- created modified
- edited < created
- missing fields

---

## Prohibited

- Local time zones  
- Non-ISO formats  
- Partial timestamps  
- Inferred timestamps  

---

## Relationships

- Metadata Field Reference → field constraints  
- Serialization Contract → encoding  
- Execution Contract → enforcement  

---

## Status

Normative, core-tier, mandatory.
