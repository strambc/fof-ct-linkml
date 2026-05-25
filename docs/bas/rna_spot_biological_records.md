---
search:
  boost: 5.0
---

# Slot: rna_spot_biological_records 


_The complete collection of RNASpotBiologicalRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined biological property column._



<div data-search-exclude markdown="1">



URI: [fof_ct:rna_spot_biological_records](https://w3id.org/fof-ct/rna_spot_biological_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RNASpotBiologicalRecord](RNASpotBiologicalRecord.md) |
| Domain | [RNASpotBiologicalTable](RNASpotBiologicalTable.md) |
| Domain Of | [RNASpotBiologicalTable](RNASpotBiologicalTable.md) |

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
| self | fof_ct:rna_spot_biological_records |
| native | fof_ct:rna_spot_biological_records |




## LinkML Source

<details>
```yaml
name: rna_spot_biological_records
description: The complete collection of RNASpotBiologicalRecord rows constituting
  this dataset. Each record corresponds to one data row in the TSV serialisation and
  must include at least one user-defined biological property column.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: RNASpotBiologicalTable
domain_of:
- RNASpotBiologicalTable
range: RNASpotBiologicalRecord
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>