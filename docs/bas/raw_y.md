---
search:
  boost: 5.0
---

# Slot: raw_y 


_Y coordinate of this Spot before any post-processing corrections. Same unit as Y._



<div data-search-exclude markdown="1">



URI: [fof_ct:raw_y](https://w3id.org/fof-ct/raw_y)
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
| 41.20 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:raw_y |
| native | fof_ct:raw_y |




## LinkML Source

<details>
```yaml
name: raw_y
description: Y coordinate of this Spot before any post-processing corrections. Same
  unit as Y.
examples:
- value: '41.20'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>