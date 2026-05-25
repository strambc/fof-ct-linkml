---
search:
  boost: 5.0
---

# Slot: vcf_file_name 


_Name of the Variant Call Format (VCF) file that must be submitted alongside the dataset to describe the genome insertion or deletion. Conditionally required when genome_assembly uses the 'custom-build:' prefix. Written as ##VCF_File_Name= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:vcf_file_name](https://w3id.org/fof-ct/vcf_file_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [SpotTable](SpotTable.md) |
| Domain Of | [SpotTable](SpotTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| pJT039:chr3.vcf |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:vcf_file_name |
| native | fof_ct:vcf_file_name |




## LinkML Source

<details>
```yaml
name: vcf_file_name
description: 'Name of the Variant Call Format (VCF) file that must be submitted alongside
  the dataset to describe the genome insertion or deletion. Conditionally required
  when genome_assembly uses the ''custom-build:'' prefix. Written as ##VCF_File_Name=
  in the file header.'
examples:
- value: pJT039:chr3.vcf
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: SpotTable
domain_of:
- SpotTable
range: string

```
</details></div>