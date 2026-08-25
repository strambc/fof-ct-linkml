---
search:
  boost: 5.0
---

# Slot: chrom 


_Chromosome name/identifier using BED (Browser Extensible Data) convention (e.g., chr3, chrY, chr2_random). Used by both the core (Spot) and vol_core (SMLocalization) tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:chrom](https://w3id.org/fof-ct/chrom)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  yes  |
| [SMLocalization](SMLocalization.md) | A single individual single-molecule (SM) localization event in a FOF-vol-CT d... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Spot](Spot.md), [SMLocalization](SMLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| chr3 |
| chrY |
| chr2_random |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:chrom |
| native | fof_ct:chrom |




## LinkML Source

<details>
```yaml
name: chrom
description: Chromosome name/identifier using BED (Browser Extensible Data) convention
  (e.g., chr3, chrY, chr2_random). Used by both the core (Spot) and vol_core (SMLocalization)
  tables.
examples:
- value: chr3
- value: chrY
- value: chr2_random
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- Spot
- SMLocalization
range: string

```
</details></div>