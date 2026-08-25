---
search:
  boost: 5.0
---

# Slot: x_precision 


_Metric quantifying the precision of the X-axis localization estimate. Typically the Cramer-Rao lower bound or Thompson method estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Must be accompanied by a description in the file header. Written as the reserved X_Loc_Precision column._



<div data-search-exclude markdown="1">



URI: [fof_ct:x_precision](https://w3id.org/fof-ct/x_precision)
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
| 0.01 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:x_precision |
| native | fof_ct:x_precision |




## LinkML Source

<details>
```yaml
name: x_precision
description: Metric quantifying the precision of the X-axis localization estimate.
  Typically the Cramer-Rao lower bound or Thompson method estimate. Highly recommended
  (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization
  Quality tables. Must be accompanied by a description in the file header. Written
  as the reserved X_Loc_Precision column.
examples:
- value: '0.01'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
- RNASpotQualityRecord
range: float

```
</details></div>