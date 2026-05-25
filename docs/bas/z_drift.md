---
search:
  boost: 5.0
---

# Slot: z_drift 


_Drift correction offset applied to the Z coordinate of this Spot. Same unit as Z._



<div data-search-exclude markdown="1">



URI: [fof_ct:z_drift](https://w3id.org/fof-ct/z_drift)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.13 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:z_drift |
| native | fof_ct:z_drift |




## LinkML Source

<details>
```yaml
name: z_drift
description: Drift correction offset applied to the Z coordinate of this Spot. Same
  unit as Z.
examples:
- value: '0.13'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>