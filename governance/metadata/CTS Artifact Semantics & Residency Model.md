---
created: 2026-05-18T13:21:07Z
edited: 2026-02-09T08:29:00Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R0_INTERNAL"
authority_level: "policy"
governance_tier: "core"
governance_class: "candidate"
wf_status: "active"
tags: ["cts","governance","artifact","residency","policy"]
index_phrase: "Canonical definition of CTS artifact roles, residency rules, and metadata descriptor body formats"
---
## Purpose

This policy defines the **canonical semantics and residency rules** for CTS artifacts. It establishes how CTS-governed artifacts represent themselves, proxy other objects, or describe external objects, and it defines the authoritative **body formats** for Metadata Descriptor Artifacts.

---

## Artifact Role Overview

The `artifact` metadata field declares the **semantic role** of a CTS artifact. It does not describe file type, format, or storage medium.

The allowed values are intentionally minimal:

```
artifact: "self" | "proxy" | "external"
```

---

## Artifact Roles

### `artifact: "self"`

The artifact governs **itself**. The document’s frontmatter applies directly to its own content. This is the default and most common CTS artifact role.

No special body structure is required.

---

### `artifact: "proxy"`

The artifact is a **Metadata Descriptor Artifact** for a **Vault-resident, non-Markdown object** that cannot carry CTS frontmatter directly.

The descriptor document is the governed CTS artifact. The proxied object is governed **by reference only**.

---

### `artifact: "external"`

The artifact is a **Metadata Descriptor Artifact** for an object that reside **outside the Vault**. The object may reside in the Media Spine or another externally configured storage system.

The descriptor document is the governed CTS artifact. The external object is governed **by reference only**.

---

## Metadata Descriptor Artifact — General Rules

The following rules apply to all Metadata Descriptor Artifacts (`artifact: "proxy"` and `artifact: "external"`):

- The descriptor document is the **sole CTS-governed artifact**
    
- The target object MUST NOT be modified
    
- The target object MUST NOT contain CTS metadata
    
- Filenames MUST mirror the target object name, with `.md` appended where required
    
- The body MUST contain exactly one structured reference section
    

---

## External Artifact Descriptor — Body Format (Normative)

### Structural Requirement

The body MUST contain a single **External Artifact Reference** section. Ad-hoc prose formats are not permitted.

### Canonical Body Structure

```md
## External Artifact Reference

target_type: file
target_resolver: MEDIA_SPINE
target_identifier: image/file_name_001.jpg
```

### Field Semantics

- **`target_type`**
    
    - Identifies the class of external object
        
    - Initial allowed value: `file`
        
- **`target_resolver`**
    
    - Identifies the logical resolver used to locate the artifact
        
    - MUST correspond to a resolver defined in CTS / OTK configuration
        
    - MUST NOT encode environment-specific information
        
- **`target_identifier`**
    
    - Resolver-relative identifier for the target object
        
    - MUST NOT be an absolute path
        
    - MUST be stable across environments
        

---

## Proxy Artifact Descriptor — Body Format (Normative)

### Structural Requirement

The body MUST contain a single **Proxy Artifact Reference** section. Ad-hoc prose formats are not permitted.

### Canonical Body Structure

```md
## Proxy Artifact Reference

target_type: file
target_identifier: image/file_name_001.jpg
```r

### Field Semantics

- **`target_type`**
    
    - Identifies the class of proxied object
        
    - Initial allowed value: `file`
        
- **`target_identifier`**
    
    - Vault-relative path to the proxied object
        
    - MUST NOT be absolute
        
    - MUST resolve within the Vault namespace
        

---

## Configuration and Resolution Rules

- Concrete paths or storage locations MUST be supplied only via configuration
    
- No CTS artifact may embed absolute filesystem paths
    
- Resolution occurs at runtime via Vault-relative lookup (`proxy`) or configured resolver (`external`)
    

---

## Optional Metadata (Non-Normative)

The following optional structured content MAY be included beneath the reference block:

```md
optional:
  hash: <sha256 | blank>
  original_source: <free text | blank>
```

Optional fields:

- MUST NOT affect resolution
    
- MUST NOT be required for governance validity
    

---

## Prohibited Practices

The following are explicitly forbidden:

- Absolute filesystem paths (e.g., `K:\Media\...`)
    
- Multiple target references in a single descriptor
    
- Embedding metadata in target objects
    
- Environment-dependent identifiers
    

---

## Relationship to Other CTS Policies

This policy operates in conjunction with:

- CTS Metadata Policy
    
- CTS Frontmatter & Artifact Serialization Contract
    
- CTS Governance & Authority Model
    

In the event of conflict, this policy governs **artifact role semantics and descriptor body structure**.

---

## Status

This policy is **normative**, core-tier, and mandatory for all CTS Metadata Descriptor Artifacts.