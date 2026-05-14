---
created: 2026-04-09T21:00:00Z
edited: 2026-05-14T19:08:12Z
artifact: "self"
origin: "internal"
source: CTS
release: "R4_PUBLIC"
authority_level: "policy"
governance_tier: "core"
governance_class: "governed"
wf_status: "active"
tags: ["CTS","lexicon","governance","canonical","semantics"]
index_phrase: "Canonical CTS lexicon defining governed entities, admission lifecycle, and semantic control boundaries"
---
## CTS Canonical Lexicon

> The CTS Canonical Lexicon defines the authoritative vocabulary of the CTS governed artifact domain.

|Term|Definition + Cross-Reference|
|---|---|
|**Admission**|**Definition:** Acceptance of content into Vault governance.<br><br>**Is:** Conditional on valid frontmatter.<br>**Is not:** Automatic.<br><br>**Dependent Systems:** CTS Canonical Frontmatter Standard; CTS Artifact Admission Rules.<br>**Used for:** Vault entry gating, lint enforcement.|
|**Admission State**|**Definition:** Lifecycle state of an entity transitioning into Vault governance.<br><br>**States include:** pre-admission, candidate, admitted, rejected.<br><br>**Is:** Explicit state model for ingestion and validation.<br>**Is not:** Implied or inferred condition.<br><br>**Dependent Systems:** A2E2; Admission Rules; validation tooling.|
|**Artifact**|**Definition:** The sole governed semantic control unit within CTS.<br><br>**Is:** The exclusive carrier of governance, authority, and provenance within CTS.<br>**Is not:** Binary payload; Media Spine object; generic file.<br><br>**Dependent Systems:** Frontmatter & Artifact Contract; Governance Vocabulary Specification; all enforcement mechanisms.|
|**Artifact Candidate**|**Definition:** A non-governed entity that has been structurally prepared for downstream evaluation and possible admission into CTS governance.<br><br>**Is:** An Input Object and associated Sidecar considered together as a candidate for admission.<br>**Is not:** An Artifact; a governed entity.<br><br>**Dependent Systems:** IngestCore; A2E2; downstream processors.<br>**Used for:** Pre-admission representation of prospective Artifacts.|
|**Authority**|**Definition:** Normative power an artifact asserts.<br><br>**Is:** Enforced by authority_level.<br>**Is not:** Structural placement.<br><br>**Dependent Systems:** Governance Vocabulary Specification.|
|**Authority Level**|**Definition:** Closed vocabulary describing normative power.<br><br>**Is:** Enumerated and enforced.<br>**Is not:** Free text.<br><br>**Defined in:** CTS Governance Vocabulary Specification.<br>**Used for:** Enforcement scope, supersession logic.|
|**Binary**|**Definition:** Non-text payload.<br><br>**Is:** Media Spine resident.<br>**Is not:** Metadata-capable.<br><br>**Dependent Systems:** Media Spine Boundary Policy.<br>**Used for:** Payload classification.|
|**Document**|**Definition:** A human-readable file that may become an artifact through admission.<br><br>**Is:** Pre-governance content.<br>**Is not:** Governed until admitted.<br><br>**Dependent Systems:** Canonical Frontmatter Standard.|
|**File**|**Definition:** Filesystem storage unit.<br><br>**Is:** Physical container only.<br>**Is not:** Semantic, governed, or authoritative.<br><br>**Dependent Systems:** Storage and bootstrap layers.|
|**Frontmatter**|**Definition:** Canonical metadata block governing admission and control.<br><br>**Is:** Admission contract.<br>**Is not:** Decoration or optional.<br><br>**Defined in:** CTS Canonical Frontmatter Standard.<br>**Used for:** Governance, provenance, validation.|
|**Governance**|**Definition:** Rules, constraints, and authority structures regulating CTS.<br><br>**Is:** Enforceable intent.<br>**Is not:** Merely documentation.<br><br>**Dependent Systems:** All governance-tier artifacts.|
|**Governance Tier**|**Definition:** Structural placement in the governance stack.<br><br>**Is:** Topological classification.<br>**Is not:** Authority.<br><br>**Defined in:** Governance Vocabulary Specification.<br>**Used for:** Hierarchy analysis, placement.|
|**Governed Entity**|**Definition:** Any entity subject to CTS governance.<br><br>**Is:** Instantiated as an artifact.<br>**Is not:** Storage construct or payload.<br><br>**Dependent Systems:** Governance model; enforcement logic.|
|**Media Spine**|**Definition:** The canonical, durable storage substrate for external objects and Artifact Candidates independent of CTS governance.<br><br>**Is:** Durable storage; governance-neutral.<br>**Is not:** A governance layer; a source of semantic authority.<br><br>**Dependent Systems:** IngestCore; Capture systems; downstream processors.<br>**Used for:** Persistent storage of objects and Artifact Candidates.|
|**Metadata Descriptor Artifact**|**Definition:** A Vault-resident artifact whose primary purpose is to define, constrain, or enumerate metadata fields, schemas, vocabularies, or admission rules used by CTS.<br><br>**Is:** Governing artifact over metadata semantics.<br>**Is not:** Payload-bearing artifact; Media Spine object.<br><br>**Dependent Systems:** CTS Canonical Frontmatter Standard; CTS Governance Vocabulary Specification; Admission and linting tools.|
|**Non-Governed Entity**|**Definition:** Any entity not currently subject to CTS governance.<br><br>**Is:** An external object, file, message, or data item that lacks Artifact status.<br>**Is not:** An Artifact.<br><br>**Dependent Systems:** Capture systems; IngestCore; Media_Spine; other ingest surfaces.<br>**Used for:** Boundary definition between governed and non-governed content.|
|**Object**|**Definition:** Non-governed storage abstraction used only in storage-layer discussions.<br><br>**Is:** Implementation-level term.<br>**Is not:** Governance-bearing or semantic.|
|**Payload**|**Definition:** Content governed by an artifact.<br><br>**Is:** Controlled data (text, image, audio, video, binary).<br>**Is not:** Authoritative.<br><br>**Dependent Systems:** Artifact Semantics; Media Spine Boundary Policy.|
|**Provenance**|**Definition:** Traceable origin and history.<br><br>**Is:** Authoritative when asserted by artifacts.<br>**Is not:** Inferred from storage.<br><br>**Dependent Systems:** Frontmatter Contract; Governance Vocabulary Spec.<br>**Used for:** Auditability, lineage.|
|**Reflexion**|**Definition:** Cognition surface for thinking, synthesis, narrative work.<br><br>**Is:** Human–AI reasoning space.<br>**Is not:** Storage substrate.<br><br>**Dependent Systems:** Bootstrap Declaration Specification.|
|**Residency**|**Definition:** Physical storage location.<br><br>**Is:** Orthogonal to governance.<br>**Is not:** Authority.<br><br>**Dependent Systems:** Bootstrap Declaration; Media Spine Boundary Policy.|
|**Sidecar**|**Definition:** A structured metadata file stored alongside a non-governed entity or Artifact Candidate.<br><br>**Is:** Companion metadata; mutable during capture and ingest.<br>**Is not:** Canonical frontmatter; a governed Artifact; proof of admission.<br><br>**Dependent Systems:** IngestCore; downstream processors.<br>**Used for:** Capture facts, user notes, placement metadata, and processing hints.|
|**Vault**|**Definition:** Governance and cognition plane where artifacts reside.<br><br>**Is:** Authority, indexing, control surface.<br>**Is not:** Raw binary storage.<br><br>**Dependent Systems:** Frontmatter Standard; Admission Rules.|

## Interpretive Notes

**System Position**  
The CTS Canonical Lexicon defines the authoritative vocabulary of the CTS governed artifact domain. Only governed Artifacts participate directly in this domain.

**Admission**  
Admission is a state transition, not a file operation. It is the moment governance becomes active.

**Artifact**  
Artifacts are the only entities capable of asserting truth within CTS. Everything else is subordinate.

**Media Spine**  
The Media Spine must remain semantically inert. Introducing meaning here breaks system boundaries.

**Metadata Descriptor Artifact**  
These artifacts define the rules of the system itself. They are governance amplifiers, not data carriers.

## Normative Constraints

 - If an entity is not an artifact, it MUST NOT participate in CTS governance.
 - All governance assertions MUST originate from an artifact
 - Admission MUST be explicit and validated; implicit admission is prohibited.
 - No semantics may be inferred from storage location.
 - Metadata Descriptor Artifacts MUST NOT carry payload.