---
search:
  boost: 5.0
---

# Slot: chrom_start 


_0-based start coordinate on the chromosome for the genomic target sequence associated with this Spot, following BED convention._



<div data-search-exclude markdown="1">



URI: [fof_ct:chrom_start](https://w3id.org/fof-ct/chrom_start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [Spot](Spot.md) |
| Domain Of | [Spot](Spot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |











## Examples

| Value |
| --- |
| 0 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:chrom_start |
| native | fof_ct:chrom_start |




## LinkML Source

<details>
```yaml
name: chrom_start
description: 0-based start coordinate on the chromosome for the genomic target sequence
  associated with this Spot, following BED convention.
examples:
- value: '0'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: Spot
domain_of:
- Spot
range: integer
minimum_value: 0

```
</details></div>