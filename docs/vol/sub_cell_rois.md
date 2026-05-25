---
search:
  boost: 5.0
---

# Slot: sub_cell_rois 


_The complete collection of sub-cellular ROIs constituting this dataset. Each SubCellROI corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. ROI_Volume, ROI_Area) MUST be present in every submitted Sub-Cell ROI Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:sub_cell_rois](https://w3id.org/fof-ct/sub_cell_rois)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SubCellROI](SubCellROI.md) |
| Domain | [SubCellROITable](SubCellROITable.md) |
| Domain Of | [SubCellROITable](SubCellROITable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:sub_cell_rois |
| native | fof_ct:sub_cell_rois |




## LinkML Source

<details>
```yaml
name: sub_cell_rois
description: The complete collection of sub-cellular ROIs constituting this dataset.
  Each SubCellROI corresponds to one data row in the TSV serialisation. At least one
  user-defined optional column (e.g. ROI_Volume, ROI_Area) MUST be present in every
  submitted Sub-Cell ROI Data table.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: SubCellROITable
domain_of:
- SubCellROITable
range: SubCellROI
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>