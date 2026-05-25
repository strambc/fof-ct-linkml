---
search:
  boost: 5.0
---

# Slot: roi_boundaries_format 


_Description of the coordinate format used to encode boundary data in the roi_boundaries column. Examples include the OME ROI Polygon model (coordinates as "x1,y1 x2,y2 ...") and the OBJ 3D mesh format (vertex and face lists). Must be sufficient for unambiguous parsing of all roi_boundaries values in this file. Written as #ROI_Boundaries_Format: in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:roi_boundaries_format](https://w3id.org/fof-ct/roi_boundaries_format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ROIMappingTable](ROIMappingTable.md) |
| Domain Of | [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| OME ROI Polygon model |
| OBJ 3D mesh |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:roi_boundaries_format |
| native | fof_ct:roi_boundaries_format |




## LinkML Source

<details>
```yaml
name: roi_boundaries_format
description: 'Description of the coordinate format used to encode boundary data in
  the roi_boundaries column. Examples include the OME ROI Polygon model (coordinates
  as "x1,y1 x2,y2 ...") and the OBJ 3D mesh format (vertex and face lists). Must be
  sufficient for unambiguous parsing of all roi_boundaries values in this file. Written
  as #ROI_Boundaries_Format: in the file header.'
examples:
- value: OME ROI Polygon model
- value: OBJ 3D mesh
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: ROIMappingTable
domain_of:
- ROIMappingTable
range: string

```
</details></div>