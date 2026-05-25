---
search:
  boost: 5.0
---

# Slot: genome_assembly 


_Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:genome_assembly](https://w3id.org/fof-ct/genome_assembly)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SpotTable](SpotTable.md), [RNASpotTable](RNASpotTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| GRCh38 |
| custom-build:GRCm38+pJT039(insertion) |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:genome_assembly |
| native | fof_ct:genome_assembly |




## LinkML Source

<details>
```yaml
name: genome_assembly
description: 'Genome build used for Chrom, Chrom_Start and Chrom_End coordinates.
  The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under
  study contains an INSERTION or DELETION the value must use the mandatory ''custom-build:''
  prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)).
  Written as ##Genome_Assembly= in the file header.'
examples:
- value: GRCh38
- value: custom-build:GRCm38+pJT039(insertion)
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotTable
- RNASpotTable
range: string

```
</details></div>