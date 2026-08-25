---
search:
  boost: 5.0
---

# Slot: z_precision 


_Metric quantifying the precision of the Z-axis localization estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Written as the reserved Z_Loc_Precision column._



<div data-search-exclude markdown="1">



URI: [fof_ct:z_precision](https://w3id.org/fof-ct/z_precision)
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
| self | fof_ct:z_precision |
| native | fof_ct:z_precision |




## LinkML Source

<details>
```yaml
name: z_precision
description: Metric quantifying the precision of the Z-axis localization estimate.
  Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality,
  and SM Localization Quality tables. Written as the reserved Z_Loc_Precision column.
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