---
search:
  boost: 5.0
---

# Slot: raw_z 


_Z coordinate of this Spot before any post-processing corrections. Same unit as Z._



<div data-search-exclude markdown="1">



URI: [fof_ct:raw_z](https://w3id.org/fof-ct/raw_z)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1.10 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:raw_z |
| native | fof_ct:raw_z |




## LinkML Source

<details>
```yaml
name: raw_z
description: Z coordinate of this Spot before any post-processing corrections. Same
  unit as Z.
examples:
- value: '1.10'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>