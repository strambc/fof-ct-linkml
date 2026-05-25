---
search:
  boost: 5.0
---

# Slot: gene_id 


_Official gene identifier corresponding to rna_name. The type of identifier used (e.g. Ensembl gene ID, NCBI Gene ID) must be declared in the gene_id_type header field._



<div data-search-exclude markdown="1">



URI: [fof_ct:gene_id](https://w3id.org/fof-ct/gene_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [RNASpot](RNASpot.md) |
| Domain Of | [RNASpot](RNASpot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ENSG00000075624 |
| ENSG00000111640 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:gene_id |
| native | fof_ct:gene_id |




## LinkML Source

<details>
```yaml
name: gene_id
description: Official gene identifier corresponding to rna_name. The type of identifier
  used (e.g. Ensembl gene ID, NCBI Gene ID) must be declared in the gene_id_type header
  field.
examples:
- value: ENSG00000075624
- value: ENSG00000111640
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: RNASpot
domain_of:
- RNASpot
range: string

```
</details></div>