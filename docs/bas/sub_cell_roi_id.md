---
search:
  boost: 5.0
---

# Slot: sub_cell_roi_id 


_Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:sub_cell_roi_id](https://w3id.org/fof-ct/sub_cell_roi_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  no  |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  no  |
| [SubCellROI](SubCellROI.md) | A single sub-cellular structure ROI (e |  yes  |
| [ROIMapping](ROIMapping.md) | A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a F... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [RNASpot](RNASpot.md), [SubCellROI](SubCellROI.md), [ROIMapping](ROIMapping.md) |

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
| self | fof_ct:sub_cell_roi_id |
| native | fof_ct:sub_cell_roi_id |




## LinkML Source

<details>
```yaml
name: sub_cell_roi_id
description: Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus).
  Links to the Sub-Cell ROI Data table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Spot
- RNASpot
- SubCellROI
- ROIMapping
range: integer

```
</details></div>