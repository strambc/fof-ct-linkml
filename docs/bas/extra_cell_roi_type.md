---
search:
  boost: 5.0
---

# Slot: extra_cell_roi_type 


_The type of extracellular structure ROI within which cells are embedded, expressed using an EFO 'organism part' child term (e.g. Tissue, Organoid). Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type: in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:extra_cell_roi_type](https://w3id.org/fof-ct/extra_cell_roi_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CellTable](CellTable.md), [ExtraCellROITable](ExtraCellROITable.md), [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Tissue |
| Organoid |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:extra_cell_roi_type |
| native | fof_ct:extra_cell_roi_type |




## LinkML Source

<details>
```yaml
name: extra_cell_roi_type
description: 'The type of extracellular structure ROI within which cells are embedded,
  expressed using an EFO ''organism part'' child term (e.g. Tissue, Organoid). Conditionally
  required when extracellular structure ROIs are identified and reported in a dedicated
  Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type: in the file header.'
examples:
- value: Tissue
- value: Organoid
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- CellTable
- ExtraCellROITable
- ROIMappingTable
range: string

```
</details></div>