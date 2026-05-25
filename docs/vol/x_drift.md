---
search:
  boost: 5.0
---

# Slot: x_drift 


_Drift correction offset applied to the X coordinate of this Spot. Same unit as X._



<div data-search-exclude markdown="1">



URI: [fof_ct:x_drift](https://w3id.org/fof-ct/x_drift)
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


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:x_drift |
| native | fof_ct:x_drift |




## LinkML Source

<details>
```yaml
name: x_drift
description: Drift correction offset applied to the X coordinate of this Spot. Same
  unit as X.
examples:
- value: '0.13'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>