# Feasibility and bounded comparisons

A constraint asks whether a condition holds. An objective orders feasible alternatives. Distinguish “a candidate meets the constraints,” “best among the tested candidates,” and “globally optimal in the stated domain.” Unknown or unobservable conditions remain unresolved.

For the constant-power rover:

- Duration = distance / speed.
- Used energy = power × duration.
- Remaining fraction = (capacity − used energy) / capacity.
- Reserve condition = remaining fraction ≥ required reserve.
- For positive capacity and reserve < 1, boundary capacity = used energy / (1 − reserve).

At 2000 m, 1 m/s and 100 W, duration is 2000 s and used energy is 200000 J. With reserve 0.2, the boundary capacity is 250000 J. Among 180000, 270000 and 360000 J, 270000 J is the smallest feasible option. This is exact arithmetic for the stated simplified equations; terrain, temperature, startup loads, battery ageing and uncertainty are omitted.

Record the units: W × s = J. Show independent calculations and check just below, exactly at, and above a threshold. If the numerical implementation uses floating point, state a justified comparison tolerance rather than silently changing the requirement.

Use [NASA decision analysis guidance](https://www.nasa.gov/reference/6-8-decision-analysis/) as practice context, qualified by the project's adopted method. This example does not claim NASA approval or physical validation of a rover design.
