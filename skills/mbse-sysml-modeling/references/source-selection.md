# Selecting language sources

Start at [OMG SysML 2.0](https://www.omg.org/spec/SysML/2.0), [KerML 1.0](https://www.omg.org/spec/KerML/1.0), and [Systems Modeling API 1.0](https://www.omg.org/spec/SystemsModelingAPI/1.0). The API is a separate contract from language syntax and semantics.

The starter study inspected formal SysML 2.0 and KerML 1.0 PDFs from a local official-source corpus. Document identities are `formal/2026-03-02` (SysML) and `formal/2026-03-01` (KerML), both March 2026. Artifact SHA-256 values:

- SysML: `46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a`.
- KerML: `3bcc96f989bfa9d05cd28e026df3351b795fe8d494187b87bff3db7d96373697`.

Useful clause pointers verified against those PDFs:

| Question | Source location |
| --- | --- |
| Scope of language claims | SysML §2 Conformance |
| Namespaces/import context | SysML §7.5; KerML §7.2.5 |
| Feature foundations | KerML §7.3.4 |
| Attribute definitions/usages | SysML §7.7 |
| Calculations | SysML §7.19 |
| Constraint declarations/assertions | SysML §7.20 |
| Requirements/satisfaction | SysML §7.21 |
| Typed quantities and units | SysML §9.8 |

These are navigation aids. Read a clause before using it as the basis for an exact claim; the index does not supply all semantics, inherited dependencies or exceptions. Identify logical clause and physical PDF page separately. Native extraction is a retrieval aid, not an accepted interpretation.

Source record fields: title, language/version, artifact/document ID, authoritative URL, byte hash if retained, clause/page, authority (normative/informative/implementation/research), observed passage, original interpretation, uncertainty, and applicability to the requested property. Examples and tool behavior remain distinct from normative obligations.
