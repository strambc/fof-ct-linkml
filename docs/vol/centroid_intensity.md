---
search:
  boost: 5.0
---

# Slot: centroid_intensity 


_Signal intensity of the centroid pixel of the Spot. Conditionally required in the Spot Quality table when intensity metrics are reported._



<div data-search-exclude markdown="1">



URI: [fof_ct:centroid_intensity](https://w3id.org/fof-ct/centroid_intensity)
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
| 2500.0 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:centroid_intensity |
| native | fof_ct:centroid_intensity |




## LinkML Source

<details>
```yaml
name: centroid_intensity
description: Signal intensity of the centroid pixel of the Spot. Conditionally required
  in the Spot Quality table when intensity metrics are reported.
examples:
- value: '2500.0'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>