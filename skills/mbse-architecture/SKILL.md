---
name: mbse-architecture
description: Develop or review logical and allocated system architectures, behavior, interfaces and design rationale without requiring SysML.
license: Apache-2.0
---

# MBSE Architecture

Separate required behavior from the selected realization so alternatives remain visible.

1. Establish scenarios, requirements, external actors and system boundary. Show external exchanges before decomposing the system.
2. Identify logical responsibilities and behavior, including failure or degraded scenarios relevant to the requested decision. Define exchanges by producer, consumer, information/energy/material, conditions and limits.
3. Propose candidate allocations to hardware, software, people and procedures. Trace each assigned responsibility and interface; record allocation criteria and assumptions. A named physical component alone is not a logical architecture.
4. Review coverage, conflicting ownership, interface compatibility, dependencies and resource budgets. Record unexplained gaps rather than drawing connections that imply resolved design.
5. Compare alternatives against explicit criteria and document the selected or proposed decision, consequences and change sensitivity.

Deliver context, logical responsibilities, candidate allocation and an interface/trace table in the project's chosen representation. Every critical exchange has endpoints and semantics; every selected allocation has rationale. For institutional context consult NASA [logical decomposition and design solution definition](https://www.nasa.gov/reference/4-0-system-design-processes/) §§4.3–4.4; this procedure is our tailored practice, not an assertion of NASA compliance.
