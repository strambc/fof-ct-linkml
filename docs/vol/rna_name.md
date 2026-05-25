---
search:
  boost: 5.0
---

# Slot: rna_name 


_Official name of the gene from which the targeted RNA is transcribed (e.g. ACTB, GAPDH). Should follow HGNC (human) or MGI (mouse) gene nomenclature._



<div data-search-exclude markdown="1">



URI: [fof_ct:rna_name](https://w3id.org/fof-ct/rna_name)
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
| ACTB |
| GAPDH |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:rna_name |
| native | fof_ct:rna_name |




## LinkML Source

<details>
```yaml
name: rna_name
description: Official name of the gene from which the targeted RNA is transcribed
  (e.g. ACTB, GAPDH). Should follow HGNC (human) or MGI (mouse) gene nomenclature.
examples:
- value: ACTB
- value: GAPDH
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: RNASpot
domain_of:
- RNASpot
range: string

```
</details></div>