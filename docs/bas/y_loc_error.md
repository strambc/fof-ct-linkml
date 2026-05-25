---
search:
  boost: 5.0
---

# Slot: y_loc_error 


_Localization error estimate for the Y coordinate of this Spot. Same unit as Y._



<div data-search-exclude markdown="1">



URI: [fof_ct:y_loc_error](https://w3id.org/fof-ct/y_loc_error)
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
| 0.02 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:y_loc_error |
| native | fof_ct:y_loc_error |




## LinkML Source

<details>
```yaml
name: y_loc_error
description: Localization error estimate for the Y coordinate of this Spot. Same unit
  as Y.
examples:
- value: '0.02'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>