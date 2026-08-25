---
search:
  boost: 5.0
---

# Slot: vcf_version 


_Version of the VCF format used for the accompanying VCF file. Conditionally required (content-triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_Version= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:vcf_version](https://w3id.org/fof-ct/vcf_version)
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
| Domain Of | [SpotTable](SpotTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| v4.2 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:vcf_version |
| native | fof_ct:vcf_version |




## LinkML Source

<details>
```yaml
name: vcf_version
description: 'Version of the VCF format used for the accompanying VCF file. Conditionally
  required (content-triggered) when genome_assembly uses the ''custom-build:'' prefix.
  Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_Version=
  in the file header.'
examples:
- value: v4.2
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotTable
range: string

```
</details></div>