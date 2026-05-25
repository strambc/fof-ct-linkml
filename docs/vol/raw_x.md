---
search:
  boost: 5.0
---

# Slot: raw_x 


_X coordinate of this Spot before any post-processing corrections (drift correction, chromatic correction, etc.). Same unit as X._



<div data-search-exclude markdown="1">



URI: [fof_ct:raw_x](https://w3id.org/fof-ct/raw_x)
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
| 14.30 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:raw_x |
| native | fof_ct:raw_x |




## LinkML Source

<details>
```yaml
name: raw_x
description: X coordinate of this Spot before any post-processing corrections (drift
  correction, chromatic correction, etc.). Same unit as X.
examples:
- value: '14.30'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>