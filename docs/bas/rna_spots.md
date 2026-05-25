---
search:
  boost: 5.0
---

# Slot: rna_spots 


_The complete collection of RNA Spots constituting this dataset. Each RNASpot corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:rna_spots](https://w3id.org/fof-ct/rna_spots)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RNASpot](RNASpot.md) |
| Domain | [RNASpotTable](RNASpotTable.md) |
| Domain Of | [RNASpotTable](RNASpotTable.md) |

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
| self | fof_ct:rna_spots |
| native | fof_ct:rna_spots |




## LinkML Source

<details>
```yaml
name: rna_spots
description: The complete collection of RNA Spots constituting this dataset. Each
  RNASpot corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: RNASpotTable
domain_of:
- RNASpotTable
range: RNASpot
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>