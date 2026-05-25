---
search:
  boost: 5.0
---

# Slot: transcript_id_type 


_Type of transcript identifier used in the transcript_id column (e.g. Ensembl_V38, RefSeq). Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. Written as ##Transcript_ID_Type= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:transcript_id_type](https://w3id.org/fof-ct/transcript_id_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  no  |






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
| RefSeq |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:transcript_id_type |
| native | fof_ct:transcript_id_type |




## LinkML Source

<details>
```yaml
name: transcript_id_type
description: 'Type of transcript identifier used in the transcript_id column (e.g.
  Ensembl_V38, RefSeq). Conditionally required when multiple transcripts share the
  same gene_id and the FISH probe can distinguish among them. Written as ##Transcript_ID_Type=
  in the file header.'
examples:
- value: Ensembl_V38
- value: RefSeq
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: RNASpotTable
domain_of:
- RNASpotTable
range: string

```
</details></div>