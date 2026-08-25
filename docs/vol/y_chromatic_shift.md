---
search:
  boost: 5.0
---

# Slot: y_chromatic_shift 


_Chromatic aberration correction offset applied to the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:y_chromatic_shift](https://w3id.org/fof-ct/y_chromatic_shift)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |
| [RNASpotQualityRecord](RNASpotQualityRecord.md) | A single row in the RNA Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md), [RNASpotQualityRecord](RNASpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.04 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:y_chromatic_shift |
| native | fof_ct:y_chromatic_shift |




## LinkML Source

<details>
```yaml
name: y_chromatic_shift
description: Chromatic aberration correction offset applied to the Y coordinate. Same
  unit as Y. Reserved, conditionally-required column name (Y_Chromatic_Shift) in the
  Spot Quality and RNA Spot Quality tables.
examples:
- value: '0.04'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
- RNASpotQualityRecord
range: float

```
</details></div>