---
search:
  boost: 5.0
---

# Slot: photon_count 


_Number of photons detected for this localization event or Spot. Reserved, conditionally-required column name (Photon_Count) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables; highly recommended in the latter._



<div data-search-exclude markdown="1">



URI: [fof_ct:photon_count](https://w3id.org/fof-ct/photon_count)
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
| Range | [Integer](Integer.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md), [RNASpotQualityRecord](RNASpotQualityRecord.md), [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1500 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:photon_count |
| native | fof_ct:photon_count |




## LinkML Source

<details>
```yaml
name: photon_count
description: Number of photons detected for this localization event or Spot. Reserved,
  conditionally-required column name (Photon_Count) in the Spot Quality, RNA Spot
  Quality, and SM Localization Quality tables; highly recommended in the latter.
examples:
- value: '1500'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
- RNASpotQualityRecord
- SMLocalizationQualityRecord
range: integer

```
</details></div>