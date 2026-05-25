---
search:
  boost: 5.0
---

# Slot: cell_id 


_Unique identifier for a Cell. Links to the Cell Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:cell_id](https://w3id.org/fof-ct/cell_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  no  |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  no  |
| [Cell](Cell.md) | A single Cell identified in a FOF-bas-CT experiment |  yes  |
| [SubCellROI](SubCellROI.md) | A single sub-cellular structure ROI (e |  yes  |
| [ROIMapping](ROIMapping.md) | A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a F... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [RNASpot](RNASpot.md), [Cell](Cell.md), [SubCellROI](SubCellROI.md), [ROIMapping](ROIMapping.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:cell_id |
| native | fof_ct:cell_id |




## LinkML Source

<details>
```yaml
name: cell_id
description: Unique identifier for a Cell. Links to the Cell Data table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Spot
- RNASpot
- Cell
- SubCellROI
- ROIMapping
range: integer

```
</details></div>