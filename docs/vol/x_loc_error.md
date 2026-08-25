---
search:
  boost: 5.0
---

# Slot: x_loc_error 


_Localization error estimate for the X coordinate (e.g. standard deviation of repeated measurements). Same unit as X. Reserved, conditionally-required column name (X_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:x_loc_error](https://w3id.org/fof-ct/x_loc_error)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |
| [RNASpotQualityRecord](RNASpotQualityRecord.md) | A single row in the RNA Spot Quality table |  yes  |
| [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) | A single row in the SM Localization Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md), [RNASpotQualityRecord](RNASpotQualityRecord.md), [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) |

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
| self | fof_ct:x_loc_error |
| native | fof_ct:x_loc_error |




## LinkML Source

<details>
```yaml
name: x_loc_error
description: Localization error estimate for the X coordinate (e.g. standard deviation
  of repeated measurements). Same unit as X. Reserved, conditionally-required column
  name (X_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality
  tables.
examples:
- value: '0.02'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
- RNASpotQualityRecord
- SMLocalizationQualityRecord
range: float

```
</details></div>