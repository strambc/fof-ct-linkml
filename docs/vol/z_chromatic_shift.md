---
search:
  boost: 5.0
---

# Slot: z_chromatic_shift 


_Chromatic aberration correction offset applied to the Z coordinate of this Spot. Same unit as Z._



<div data-search-exclude markdown="1">



URI: [fof_ct:z_chromatic_shift](https://w3id.org/fof-ct/z_chromatic_shift)
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


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:z_chromatic_shift |
| native | fof_ct:z_chromatic_shift |




## LinkML Source

<details>
```yaml
name: z_chromatic_shift
description: Chromatic aberration correction offset applied to the Z coordinate of
  this Spot. Same unit as Z.
examples:
- value: '0.02'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>