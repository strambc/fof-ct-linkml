---
search:
  boost: 5.0
---

# Slot: loc_id 


_A unique integer identifier for an individual localization event. Loc_ID values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing, SM Localization Data, SM Localization Quality, and Undecoded SM Localization tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:loc_id](https://w3id.org/fof-ct/loc_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocalizationMixin](LocalizationMixin.md) | Mixin capturing the shared concept of a single localization event across FOF-... |  no  |
| [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) | A single row in the SM Localization Quality table |  yes  |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |
| [SMLocalization](SMLocalization.md) | A single individual single-molecule (SM) localization event in a FOF-vol-CT d... |  yes  |
| [UndecodedLocalization](UndecodedLocalization.md) | A single raw, undecoded SM localization event in a FOF-vol-CT dataset |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [LocalizationMixin](LocalizationMixin.md), [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:loc_id |
| native | fof_ct:loc_id |




## LinkML Source

<details>
```yaml
name: loc_id
description: A unique integer identifier for an individual localization event. Loc_ID
  values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing,
  SM Localization Data, SM Localization Quality, and Undecoded SM Localization tables.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- LocalizationMixin
- SMLocalizationQualityRecord
range: integer

```
</details></div>