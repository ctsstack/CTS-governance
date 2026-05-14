---
created: 2026-05-13T17:05:00Z
edited: 2026-05-14T16:13:47Z
artifact: "self"
origin: "internal"
source: CTS
release: "R4_PUBLIC"
authority_level: "policy"
governance_tier: "core"
governance_class: "candidate"
wf_status: "draft"
tags: ["cts","ingest","ingestcore","lexicon","media_spine","artifact_candidate"]
index_phrase: "Canonical IngestCore lexicon defining pre-governance capture and artifact candidate creation"
---

## CTS IngestCore Lexicon

> This lexicon defines the vocabulary of IngestCore, a CTS subsystem that operates upstream of governance.

|**Term**|**Definition + Cross-Reference**|
|---|---|
|**Adapter**|**Definition:** A component that converts a captured Input Object into a Capture Event.<br><br>**Is:** A deterministic translator.<br>**Is not:** A classifier or semantic interpreter.<br><br>**Dependent Systems:** Capture systems; node agents.<br>**Used for:** Structured event generation.|
|**Artifact Candidate**|**Definition:** An Input Object and its associated Sidecar considered together as a structured candidate for downstream evaluation.<br><br>**Is:** Eligible for subsequent processing.<br>**Is not:** A governed Artifact.<br><br>**Dependent Systems:** Media_Spine; downstream processors.<br>**Used for:** Deferred adjudication and possible admission.|
|**Capture**|**Definition:** The act of acquiring an Input Object from an Input Surface.<br><br>**Is:** The first operational step in the ingest lifecycle.<br>**Is not:** Interpretation, validation, or classification.<br><br>**Dependent Systems:** Capture adapters; node agents.<br>**Used for:** Object acquisition.|
|**Capture Event**|**Definition:** The first structured representation of a captured Input Object and its immediate factual context.<br><br>**Is:** A structured record of capture facts.<br>**Is not:** Contract validation; governance assertion; Artifact creation.<br><br>**Dependent Systems:** Capture adapters; IngestCore.<br>**Used for:** Transition from raw capture to structured processing.|
|**Ingest**|**Definition:** The operational process that transforms captured objects into Artifact Candidates and places them in the Media_Spine.<br><br>**Is:** Capture-adjacent infrastructure; pre-governance processing.<br>**Is not:** A2E2; admission; artifact creation.<br><br>**Dependent Systems:** IngestCore; Media_Spine.<br>**Used for:** Candidate preparation and placement.|
|**Input Object**|**Definition:** A raw or semi-structured entity captured prior to CTS governance.<br><br>**Is:** Pre-governance content; a file, message, image, audio clip, or other captured payload.<br>**Is not:** An Artifact; an Artifact Candidate; a governed entity.<br><br>**Dependent Systems:** Capture adapters; IngestCore.<br>**Used for:** Initial capture and staging.|
|**Input Surface**|**Definition:** The interface through which an Input Object is captured.<br><br>**Is:** A source boundary such as mobile share, screenshot, clipboard, email export, or file drop.<br>**Is not:** A governance boundary.<br><br>**Dependent Systems:** Capture systems; node agents.<br>**Used for:** Source identification.|
|**Media Spine**|**Definition:** A canonical, durable storage substrate for external objects and Artifact Candidates awaiting or supporting downstream processing.<br><br>**Is:** Durable storage; governance-neutral; potentially implemented by one or more physical or logical storage locations.<br>**Is not:** A governance layer; a semantic authority layer; limited to a single filesystem path or device.<br><br>**Dependent Systems:** IngestCore; Capture systems; downstream processors.<br>**Used for:** Persistent storage of external objects and Artifact Candidates.|
|**Placement**|**Definition:** The act of storing an Artifact Candidate in its designated Media_Spine location.<br><br>**Is:** A storage operation.<br>**Is not:** Admission or acceptance.<br><br>**Dependent Systems:** IngestCore; mover components.<br>**Used for:** Durable candidate residency.|
|**Queue**|**Definition:** A mechanism that tracks items awaiting user enrichment or subsequent processing.<br><br>**Is:** Operational state management.<br>**Is not:** Governance adjudication.<br><br>**Dependent Systems:** IngestCore; modal prompts; automation agents.<br>**Used for:** Work coordination.|
|**Rejection**|**Definition:** Failure to create or place an Artifact Candidate due to operational issues.<br><br>**Is:** An ingest-level failure state.<br>**Is not:** Governance refusal.<br><br>**Dependent Systems:** Scanner; transport; mover components.<br>**Used for:** Error handling and recovery.|
|**Sidecar**|**Definition:** A structured metadata file stored alongside an object or Artifact Candidate.<br><br>**Is:** Companion metadata; mutable during capture and ingest.<br>**Is not:** A governed artifact; canonical frontmatter; proof of admission.<br><br>**Dependent Systems:** IngestCore; downstream processors.<br>**Used for:** Capture facts, user notes, placement metadata, and processing hints.|
|**Staging Buffer**|**Definition:** Temporary local storage used to isolate capture volatility from placement into the Media_Spine.<br><br>**Is:** Operational buffering.<br>**Is not:** Long-term authoritative storage.<br><br>**Dependent Systems:** Node agents; transport components.<br>**Used for:** Reliable local persistence prior to placement.|
|**Transport**|**Definition:** The movement of objects and sidecars between capture devices and the Media_Spine.<br><br>**Is:** A delivery mechanism.<br>**Is not:** Semantic processing.<br><br>**Dependent Systems:** Node agents; network services.<br>**Used for:** Reliable delivery.|

## Interpretive Notes

**System Position**  
IngestCore is a CTS subsystem that operates upstream of governance. Its output consists of Artifact Candidates, not Artifacts.

**Pre-Governance Scope**  
The IngestCore Lexicon describes activities that occur before CTS governance begins.

**Artifact Candidate**  
An Artifact Candidate is the highest-order construct produced by Ingest. It may be consumed by one or more downstream systems.

**Sidecar**  
The Sidecar is the principal metadata mechanism used during capture and ingest.

**Media_Spine**  
Media_Spine (or similar) stores candidates but does not define their meaning.

## Normative Constraints

- IngestCore MUST NOT create Artifacts.
- IngestCore MUST NOT perform validation, normalization, enrichment, or classification.
- Every Artifact Candidate MUST consist of an Input Object and a corresponding Sidecar.
- Artifact Candidates MUST be placed in the Media_Spine or other similarly authorized storage device.
- Placement in the Media_Spine MUST NOT be interpreted as admission.
- Sidecars MUST remain associated with their corresponding objects.
- Governance begins only after downstream acceptance converts an Artifact Candidate into an Artifact.

## End-to-End Mapping

Input Object → Capture → Capture Event → Sidecar → Ingest → Artifact Candidate → Placement → Media_Spine

## One-Line Anchor

**IngestCore transforms captured objects into Artifact Candidates and places them in the Media_Spine for possible downstream processing.**
