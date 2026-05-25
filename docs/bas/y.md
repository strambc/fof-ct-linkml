---
search:
  boost: 5.0
---

# Slot: y 


_Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections._



<div data-search-exclude markdown="1">



URI: [fof_ct:y](https://w3id.org/fof-ct/y)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocalizationMixin](LocalizationMixin.md) | Mixin capturing the shared concept of a single localization event across FOF-... |  no  |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  yes  |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  yes  |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [LocalizationMixin](LocalizationMixin.md), [Spot](Spot.md), [RNASpot](RNASpot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 41.43 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:y |
| native | fof_ct:y |




## LinkML Source

<details>
```yaml
name: y
description: Sub-pixel Y coordinate of this detected event (Spot or localisation)
  in the unit specified by xyz_unit. The reported value is the final position after
  all post-processing corrections.
examples:
- value: '41.43'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- LocalizationMixin
- Spot
- RNASpot
range: float

```
</details></div>