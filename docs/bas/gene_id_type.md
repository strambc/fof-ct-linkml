---
search:
  boost: 5.0
---

# Slot: gene_id_type 


_Type of gene identifier used in the gene_id column (e.g. Ensembl_V38, NCBI_Gene). Written as ##Gene_ID_Type= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:gene_id_type](https://w3id.org/fof-ct/gene_id_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [RNASpotTable](RNASpotTable.md) |
| Domain Of | [RNASpotTable](RNASpotTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Ensembl_V38 |
| NCBI_Gene |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:gene_id_type |
| native | fof_ct:gene_id_type |




## LinkML Source

<details>
```yaml
name: gene_id_type
description: 'Type of gene identifier used in the gene_id column (e.g. Ensembl_V38,
  NCBI_Gene). Written as ##Gene_ID_Type= in the file header.'
examples:
- value: Ensembl_V38
- value: NCBI_Gene
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: RNASpotTable
domain_of:
- RNASpotTable
range: string

```
</details></div>