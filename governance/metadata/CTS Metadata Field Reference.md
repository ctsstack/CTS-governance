---
created: 2026-01-24T10:55:00Z
edited: 2026-03-02T20:46:00Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R4_PUBLIC"
authority_level: "policy"
governance_tier: "core"
governance_class: "governed"
wf_status: "active"
tags: ["metadata","reference","governance","cts"]
index_phrase: "Canonical reference enumerating allowed values, mutability, and constraints for each CTS frontmatter metadata field."
---
## Purpose 

This document is the **authoritative lookup reference** for CTS frontmatter fields. It enumerates the **allowed values, mutability, and constraints** for each field without re‑stating semantic rationale or serialization rules.

This reference exists to:

- Eliminate ambiguity during authoring
    
- Support deterministic validation and tooling
    
- Prevent semantic drift across CTS artifacts
    

---

## Scope and Authority

- This document defines the canonical metadata fields, their allowed values, and associated constraints.

- Encoding and serialization are governed by the CTS Frontmatter Serialization Contract.

- Field-specific semantics are governed by the appropriate CTS policy documents (e.g., Timestamp Semantics and Authority Policy for temporal fields).

In the event of conflict:

1. CTS Frontmatter Serialization Contract governs syntax and encoding

2. Field-specific policy documents govern semantics

3. This document governs field definitions, allowed values, and constraints
---

## Metadata Field Reference

### Field: `created`

- Required: yes
    
- Type: timestamp (scalar)
    
- Allowed values: ISO 8601 UTC, Z-terminated (e.g. 2026-05-18T12:34:56Z)

- Mutable: no (except via Metadata Repair Policy)
    
- Governing documents:
    
    - Timestamp Semantics and Authority Policy
        
    - Metadata Repair and Historical Correction Policy
        

---

### Field: `edited`

- Required: yes (may be blank)
    
- Type: timestamp (scalar)
    
Allowed values: ISO 8601 UTC, Z-terminated (e.g. 2026-05-18T12:34:56Z) or empty
    
- Mutable: yes (tool‑managed)
    
- Governing documents:
     
    - Timestamp Semantics and Authority Policy
        

---

### Field: `artifact`

- Required: yes
    
- Type: enum (scalar)
    
- Allowed values:
    
    - `self`
        
    - `proxy`
        
    - `external`
        
- Mutable: no
    
- Governing documents:
    
    - Artifact Declaration and Proxy Semantics
        

---

### Field: `origin`

- Required: yes
    
- Type: enum (scalar)
    
- Allowed values:
    
    - `internal`
        
    - `external`
        
    - `imported`
        
- Mutable: no
    
- Governing documents:
    
    - Allowed values are defined in this document
        

---

### Field: `source`

- Required: yes
    
- Type: string (scalar)
    
- Allowed values:
    
    - reflexion  (Unquoted)
        
    - Other CTS‑defined provenance descriptors
        
- Mutable: no
    
- Governing documents:
    
    - Allowed values are defined in this document
        
 
---

### Field: `release`

- **Required:** yes
    
- **Type:** distribution posture identifier (scalar enum)
    
- **Allowed values:** closed vocabulary defined by CTS governance
 

|Value|Meaning|
|---|---|
|`R0_INTERNAL`|Core CTS governance only|
|`R1_RESTRICTED`|Internal operational circulation|
|`R2_CONFIDENTIAL`|Sensitive; explicit approval required|
|`R3_PARTNER`|Authorized external collaborators|
|`R4_PUBLIC`|Unrestricted public distribution|

- **Mutable:** yes (only when reliance posture changes)
    
- **Governing documents:**

> Promotion to public visibility is defined as a transition to:
> R4_PUBLIC  
> 
> All non-public release states (R0–R3) are outside the scope of this contract.

---

### Normative Clarification

The `release` field expresses the **reliance and exposure posture** of the artifact.

It indicates **who may rely upon or distribute the artifact**, not how many times the artifact has been revised.

The `release` field MUST NOT encode:

- Document version numbers
    
- Revision identifiers
    
- Semantic versioning patterns
    
- Edit sequences
    
- Change chronology
    

Mechanical version history is provided exclusively by version control systems (e.g., Git). Human-readable evolution is expressed within the document body where appropriate.

---

### Field: `authority_level`

- Required: yes
    
- Type: enum (scalar)
    
- Allowed values:
    
    - `none`
        
    - `guidance`
        
    - `policy`
        
- Mutable: no
    
- Governing documents:
    
    - Allowed values are defined in this document
        

---

### Field: `governance_tier`

- Required: yes
    
- Type: enum (scalar)
    
- Allowed values:
    
    - `supporting`
        
    - `core`
        
- Mutable: no
    
- Governing documents:
    
    - Allowed values are defined in this document
        

---
### Field: `governance_class`

- Required: conditional
- Type: enum (scalar)
- Allowed values:

	- `governed`
    
    - `candidate`
    
	- `superceded`

- Mutable: yes (until admission finalized)
- Governing documents:
    - CTS Admission Policy (governance_class enforcement rules)

---

### Constraint Rules
> This field is reserved for future admission policy enforcement actions and is **not** a part of the governance spine

- This field MUST NOT be present with an empty value
- If present, the value MUST be one of the allowed enumerations
- If required by CTS Admission Policy, the field MUST be present and valid
- If not applicable, the field SHOULD be absent (not empty)

---

### Applicability

- This field is conditionally required based on:
- 
    - `authority_level`
   
	- `governance_tier`

- Enforcement logic is defined in the CTS Admission Policy and is not restated here

---

### Usage Notes

- This field defines **epistemic admission status**, not authority or structure
- This field MUST NOT be inferred by tooling
- This field MUST NOT be replaced by tags or free-form metadata
- This field is used by retrieval and indexing systems to determine eligibility for inclusion

---

### Field: `wf_status`

- Required: yes
    
- Type: enum (scalar)
    
- Allowed values:
    
    - `draft`
        
    - `active`
        
    - `deprecated`
        
    - `archived`
        
- Mutable: yes
    
- Governing documents:
    
    - Allowed values are defined in this document
        
    - Artifact Versioning and Non‑Destructive Update Guidance
        

---

### Field: `tags`

- Required: yes
    
- Type: list of strings
    
- Allowed values:
    
    - Any quoted string
        
- Mutable: yes
    
- Governing documents:
    
    - Allowed values are defined in this document
        

---

### Field: `index_phrase`

- Required: yes
    
- Type: string (scalar)
    
- Allowed values:
    
    - One concise descriptive sentence
        
- Mutable: yes
    
- Governing documents:
    
    - Allowed values are defined in this document
        

---

## Usage Notes

- No CTS tooling may infer semantics beyond the constraints listed here
    
- Fields not listed in this document are **not permitted** unless introduced by policy
    
- This reference is intended for **consultation**, not narrative reading
    

---

## Status

This reference is active, core‑tier, and binding for all CTS‑governed artifacts.