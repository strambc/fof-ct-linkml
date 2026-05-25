---
search:
  boost: 5.0
---

# Slot: rna_spot_quality_records 


_The complete collection of RNASpotQualityRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined quality metric column._



<div data-search-exclude markdown="1">



URI: [fof_ct:rna_spot_quality_records](https://w3id.org/fof-ct/rna_spot_quality_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpotQualityTable](RNASpotQualityTable.md) | The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RNASpotQualityRecord](RNASpotQualityRecord.md) |
| Domain | [RNASpotQualityTable](RNASpotQualityTable.md) |
| Domain Of | [RNASpotQualityTable](RNASpotQualityTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:rna_spot_quality_records |
| native | fof_ct:rna_spot_quality_records |




## LinkML Source

<details>
```yaml
name: rna_spot_quality_records
description: The complete collection of RNASpotQualityRecord rows constituting this
  dataset. Each record corresponds to one data row in the TSV serialisation and must
  include at least one user-defined quality metric column.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: RNASpotQualityTable
domain_of:
- RNASpotQualityTable
range: RNASpotQualityRecord
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>