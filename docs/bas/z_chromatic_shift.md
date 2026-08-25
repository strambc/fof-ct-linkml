---
search:
  boost: 5.0
---

# Slot: z_chromatic_shift 


_Chromatic aberration correction offset applied to the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:z_chromatic_shift](https://w3id.org/fof-ct/z_chromatic_shift)
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
| 0.02 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:z_chromatic_shift |
| native | fof_ct:z_chromatic_shift |




## LinkML Source

<details>
```yaml
name: z_chromatic_shift
description: Chromatic aberration correction offset applied to the Z coordinate. Same
  unit as Z. Reserved, conditionally-required column name (Z_Chromatic_Shift) in the
  Spot Quality and RNA Spot Quality tables.
examples:
- value: '0.02'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
- RNASpotQualityRecord
range: float

```
</details></div>