---
search:
  boost: 5.0
---

# Slot: sm_localization_quality_records 


_The complete collection of SMLocalizationQualityRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:sm_localization_quality_records](https://w3id.org/fof-ct/sm_localization_quality_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SMLocalizationQualityTable](SMLocalizationQualityTable.md) | The SM Localization Quality table of a FOF-vol-CT dataset (namespace: FOF-CT_... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SMLocalizationQualityRecord](SMLocalizationQualityRecord.md) |
| Domain | [SMLocalizationQualityTable](SMLocalizationQualityTable.md) |
| Domain Of | [SMLocalizationQualityTable](SMLocalizationQualityTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:sm_localization_quality_records |
| native | fof_ct:sm_localization_quality_records |




## LinkML Source

<details>
```yaml
name: sm_localization_quality_records
description: The complete collection of SMLocalizationQualityRecord rows constituting
  this dataset. Each record corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: SMLocalizationQualityTable
domain_of:
- SMLocalizationQualityTable
range: SMLocalizationQualityRecord
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>