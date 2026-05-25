---
search:
  boost: 5.0
---

# Slot: extra_cell_rois 


_The complete collection of extracellular ROIs constituting this dataset. Each ExtraCellROI corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. ROI_Volume, Cell_Count) MUST be present in every submitted Extra-Cell ROI Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:extra_cell_rois](https://w3id.org/fof-ct/extra_cell_rois)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExtraCellROI](ExtraCellROI.md) |
| Domain | [ExtraCellROITable](ExtraCellROITable.md) |
| Domain Of | [ExtraCellROITable](ExtraCellROITable.md) |

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
| self | fof_ct:extra_cell_rois |
| native | fof_ct:extra_cell_rois |




## LinkML Source

<details>
```yaml
name: extra_cell_rois
description: The complete collection of extracellular ROIs constituting this dataset.
  Each ExtraCellROI corresponds to one data row in the TSV serialisation. At least
  one user-defined optional column (e.g. ROI_Volume, Cell_Count) MUST be present in
  every submitted Extra-Cell ROI Data table.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: ExtraCellROITable
domain_of:
- ExtraCellROITable
range: ExtraCellROI
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>