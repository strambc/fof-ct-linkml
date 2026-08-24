---
search:
  boost: 5.0
---

# Slot: roi_boundaries_format_type 


_Controlled-vocabulary identifier of the standard used to encode ROI boundaries in global coordinates (e.g. OME_Polygon for the OME ROI data model, or Mesh_OBJ for a 3D OBJ mesh). Written as ##ROI_Boundaries_Format_Type= in the file header. Default value is OME_Polygon._



<div data-search-exclude markdown="1">



URI: [fof_ct:roi_boundaries_format_type](https://w3id.org/fof-ct/roi_boundaries_format_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ROIBoundariesFormatTypeEnum](ROIBoundariesFormatTypeEnum.md) |
| Domain | [ROIMappingTable](ROIMappingTable.md) |
| Domain Of | [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| OME_Polygon |
| Mesh_OBJ |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:roi_boundaries_format_type |
| native | fof_ct:roi_boundaries_format_type |




## LinkML Source

<details>
```yaml
name: roi_boundaries_format_type
description: 'Controlled-vocabulary identifier of the standard used to encode ROI
  boundaries in global coordinates (e.g. OME_Polygon for the OME ROI data model, or
  Mesh_OBJ for a 3D OBJ mesh). Written as ##ROI_Boundaries_Format_Type= in the file
  header. Default value is OME_Polygon.'
examples:
- value: OME_Polygon
- value: Mesh_OBJ
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: ROIMappingTable
domain_of:
- ROIMappingTable
range: ROIBoundariesFormatTypeEnum

```
</details></div>