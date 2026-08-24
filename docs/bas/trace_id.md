---
search:
  boost: 5.0
---

# Slot: trace_id 


_Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily) in the FOF-vol-CT SM Localization Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:trace_id](https://w3id.org/fof-ct/trace_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  yes  |
| [Trace](Trace.md) | A single chromatin Trace representing global properties associated with an en... |  yes  |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [Trace](Trace.md), [RNASpot](RNASpot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:trace_id |
| native | fof_ct:trace_id |




## LinkML Source

<details>
```yaml
name: trace_id
description: Unique identifier for a chromatin Trace. Used as a primary key in the
  Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily)
  in the FOF-vol-CT SM Localization Data table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Spot
- Trace
- RNASpot
range: integer

```
</details></div>