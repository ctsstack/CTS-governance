---
created: 2026-04-24T16:10:00Z
edited: 2026-04-28T02:30:11Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R0_INTERNAL"
authority_level: "policy"
governance_tier: "core"
governance_class: “candidate”
wf_status: "active"
tags: ["cts","execution","compliance","llm","contract","governance"]
index_phrase: "Defines the mandatory execution and compliance behavior required for any system or agent producing CTS-governed artifacts"
---

## Purpose

Define the mandatory execution and compliance behavior for any system (human or machine) generating CTS-governed artifacts.

---

## Core Principle

No artifact is valid unless it is compliant at time of creation.

---

## Mandatory Output Requirements

All generated artifacts MUST include:

- Valid CTS frontmatter block
- All required fields populated
- Proper serialization
- Body consistent with artifact role

> Descriptor artifacts MUST conform to Artifact Semantic body structure

---

## Execution Rules

1. Frontmatter MUST be first  
2. No missing fields  
3. Canonical field names only  
4. Body must match artifact role
5. - Conditional Fields
	 - governance_class _may_ be present
	 - If present, it MUST be valid per the Metadata Field Reference
	 - If required by policy, it MUST be present

---

## Validation Behavior

- Missing data → request or default  
- Invalid values → correct or fail  
- Output must be internally consistent  

---

## Non-Compliance Handling

If compliance cannot be achieved:

- Do NOT emit artifact  
- Report violations  

---

## Prohibited Behaviors

- No frontmatter  
- Invalid fields  
- Partial compliance  
- Optional governance  

---

## Modes

Strict Mode (default): enforce and reject  
Assisted Mode: suggest and iterate  

---

## Summary

This contract enforces CTS at runtime.
