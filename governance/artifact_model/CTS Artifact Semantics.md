---
created: 2026-04-24T17:30:00Z
edited: 2026-04-28T02:17:19Z
artifact: "self"
origin: "internal"
source: reflexion
release: "R4_PUBLIC"
authority_level: "policy"
governance_tier: "core"
governance_class: "governed"
wf_status: "active"
tags: ["cts","governance","artifact","residency","policy"]
index_phrase: "Canonical definition of CTS artifact roles, residency rules, descriptor formats, and resolution mechanisms"
---

## Purpose

Defines the canonical semantics, residency rules, descriptor formats, and resolution mechanisms for CTS artifacts.

---

## Artifact Roles

artifact: "self" | "proxy" | "external"

### self
Artifact governs itself.

### proxy
Descriptor for non-metadata-capable object.

### external
Descriptor for external object (e.g., GitHub, Media Spine).

---

## Descriptor Requirements

- One structured reference section only  
- No metadata in target object  
- Descriptor is sole governed artifact  

---

## External Descriptor Format

## External Artifact Reference

target_type: file  
target_resolver: MEDIA_SPINE  
target_identifier: path/to/file  

---

## Proxy Descriptor Format

## Proxy Artifact Reference

target_type: file  
target_identifier: vault/relative/path  

---

## Configuration and Resolution Rules

### Resolver Definitions (Normative)

Allowed resolvers:

- MEDIA_SPINE  
- GITHUB  

### Resolver Behavior

MEDIA_SPINE:
- Resolves to CTS-configured storage  
- Non-semantic payloads  

GITHUB:
- Resolves to GitHub-hosted artifacts  
- target_identifier format:  
  org/repo/path  
- Resolution pattern:  
  https://github.com/{org}/{repo}/blob/main/{path}

---

### General Rules

- No absolute paths  
- Resolution via:
  - proxy → Vault lookup  
  - external → resolver  
- Paths supplied via configuration only  

---

## Optional Metadata

optional:
  hash: <sha256 | blank>  
  original_source: <text | blank>  

- Must not affect resolution  
- Not required for validity  

---

## Prohibited

- Absolute filesystem paths  
- Multiple targets  
- Embedded metadata in payload  

---

## Status

Normative, core-tier.
