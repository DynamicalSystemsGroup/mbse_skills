# Modeling foundations

SysML uses KerML foundations; consult [SysML 2.0](https://www.omg.org/spec/SysML/2.0/PDF) and [KerML 1.0](https://www.omg.org/spec/KerML/1.0/PDF) in the selected revision. Useful paths: SysML §7.5 (namespaces), §7.7 (attributes), §7.20 (constraints), §7.21 (requirements), §9.8 (quantities); KerML §7.3.4 (features).

For a specific declaration, distinguish:

- Definition: the reusable classifier/structure being declared.
- Usage: its use in a context; identify typing, multiplicity and relationships.
- Typing: what kind of values a feature admits; units and physical quantity kinds matter.
- Specialization/redefinition: what meaning is inherited or narrowed; read the applicable rule before altering it.
- Namespace membership/import: where a name belongs and which names are visible.

A small original example, exercised with the starter engine profiles:

```sysml
package EnergyExample {
    private import ISQ::*;
    private import SI::*;
    attribute power : PowerValue = 100 [W];
    attribute duration : DurationValue = 2000 [s];
    attribute energy : EnergyValue = power * duration;
    constraint withinBudget { energy <= 216000 [J] }
}
```

The condition alone is not a complete requirement model. If the task needs explicit requirement subjects, satisfaction relationships, actions or verification cases, model those deliberately using the corresponding clauses and test their reachable engine operations. Engine acceptance of a snippet is a bounded observation, not a complete conformance determination.

Use standard imports and spellings for portable models. Record libraries and extensions. OpenSysML's packaged skills are useful tool guidance, but their engine-specific semantics and examples require verification against the pinned version; strict mode is still the engine's policy, not an independent certificate.
