---
search:
  boost: 5.0
---

# Slot: rna_spot_id 


_Unique integer identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:rna_spot_id](https://w3id.org/fof-ct/rna_spot_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  yes  |
| [RNASpotQualityRecord](RNASpotQualityRecord.md) | A single row in the RNA Spot Quality table |  yes  |
| [RNASpotBiologicalRecord](RNASpotBiologicalRecord.md) | A single row in the RNA Spot Biological Data table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [RNASpot](RNASpot.md), [RNASpotQualityRecord](RNASpotQualityRecord.md), [RNASpotBiologicalRecord](RNASpotBiologicalRecord.md) |

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
| self | fof_ct:rna_spot_id |
| native | fof_ct:rna_spot_id |




## LinkML Source

<details>
```yaml
name: rna_spot_id
description: Unique integer identifier for an RNA bright Spot, unique across the entire
  dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in
  the RNA Quality and RNA Biological Data tables.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- RNASpot
- RNASpotQualityRecord
- RNASpotBiologicalRecord
range: integer

```
</details></div>