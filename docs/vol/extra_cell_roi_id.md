---
search:
  boost: 5.0
---

# Slot: extra_cell_roi_id 


_Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:extra_cell_roi_id](https://w3id.org/fof-ct/extra_cell_roi_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  no  |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  no  |
| [Cell](Cell.md) | A single Cell identified in a FOF-bas-CT experiment |  yes  |
| [ExtraCellROI](ExtraCellROI.md) | A single extracellular structure ROI (e |  yes  |
| [ROIMapping](ROIMapping.md) | A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a F... |  yes  |
| [SMLocalization](SMLocalization.md) | A single individual single-molecule (SM) localization event in a FOF-vol-CT d... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [RNASpot](RNASpot.md), [Cell](Cell.md), [ExtraCellROI](ExtraCellROI.md), [ROIMapping](ROIMapping.md), [SMLocalization](SMLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:extra_cell_roi_id |
| native | fof_ct:extra_cell_roi_id |




## LinkML Source

<details>
```yaml
name: extra_cell_roi_id
description: Unique identifier for an extracellular structure ROI (e.g., tissue, organoid).
  Links to the Extra-Cell ROI Data table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- Spot
- RNASpot
- Cell
- ExtraCellROI
- ROIMapping
- SMLocalization
range: integer

```
</details></div>