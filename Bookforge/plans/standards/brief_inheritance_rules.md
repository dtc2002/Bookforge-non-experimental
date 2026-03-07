# Brief Inheritance Rules

The Project Brief is the top-level intent document for a Bookforge project.

All downstream planning artifacts must inherit from the brief unless an explicit operator override is recorded.

## Must inherit

The following fields must remain aligned across planning stages:

- genre
- target_audience
- tone
- length_target
- content_boundaries
- required_elements
- forbidden_elements
- originality_constraints
- market_intent
- series_intent

## Preference resolution

If the brief uses a flexible value such as:
- no_preference
- empty field
- optional seed only

then the Story Skeleton may resolve that field into a concrete choice.

Resolved choices must still fit:
- the declared audience
- the declared length target
- the declared tone
- operator notes

## Drift is not allowed

Planning drift occurs when downstream artifacts materially depart from the brief without a justified operator override.

Examples of drift:
- adult horror brief becomes whimsical middle-grade adventure
- standalone brief quietly becomes sequel bait
- low-violence brief becomes graphic combat plot
- forbidden “chosen one prophecy” reappears as a renamed equivalent
- required haunted observatory disappears completely

Material drift is a blocking issue.

## Operator override

If the operator intentionally changes direction, the change should be reflected in:
- the active brief artifact, or
- a clearly recorded override note

Do not silently reinterpret the brief.