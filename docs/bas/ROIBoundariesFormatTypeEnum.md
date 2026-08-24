---
search:
  boost: 2.0
---


# Enum: ROIBoundariesFormatTypeEnum 




_Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI Mapping table (per the FOF-CT RTD "Allowable value lists" table). Default value is OME_Polygon._



<div data-search-exclude markdown="1">

URI: [fof_ct:ROIBoundariesFormatTypeEnum](https://w3id.org/fof-ct/ROIBoundariesFormatTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| OME_Polygon | None | OME ROI data model, polygon representation (default) |
| OME_Mask | None | OME ROI data model, mask representation |
| Mesh_OBJ | None | 3D mesh boundary described using the Wavefront OBJ format |
| Mesh_STL | None | 3D mesh boundary described using the STL format |
| Mesh_PLY | None | 3D mesh boundary described using the PLY format |
| GeoJSON | None | Boundary described using the GeoJSON format |
| WKT | None | Boundary described using Well-Known Text |
| Label_Mask_Image | None | Boundary described as a labeled mask image |
| Other | None | Any other boundary format |




## Slots

| Name | Description |
| ---  | --- |
| [roi_boundaries_format_type](roi_boundaries_format_type.md) | Controlled-vocabulary identifier of the standard used to encode ROI boundarie... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas






## LinkML Source

<details>
```yaml
name: ROIBoundariesFormatTypeEnum
description: 'Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI
  Mapping table (per the FOF-CT RTD "Allowable value lists" table). Default value
  is OME_Polygon.'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
permissible_values:
  OME_Polygon:
    text: OME_Polygon
    description: OME ROI data model, polygon representation (default).
  OME_Mask:
    text: OME_Mask
    description: OME ROI data model, mask representation.
  Mesh_OBJ:
    text: Mesh_OBJ
    description: 3D mesh boundary described using the Wavefront OBJ format.
  Mesh_STL:
    text: Mesh_STL
    description: 3D mesh boundary described using the STL format.
  Mesh_PLY:
    text: Mesh_PLY
    description: 3D mesh boundary described using the PLY format.
  GeoJSON:
    text: GeoJSON
    description: Boundary described using the GeoJSON format.
  WKT:
    text: WKT
    description: Boundary described using Well-Known Text.
  Label_Mask_Image:
    text: Label_Mask_Image
    description: Boundary described as a labeled mask image.
  Other:
    text: Other
    description: Any other boundary format. When used, ROI_Boundaries_Format_Description
      becomes mandatory.

```
</details>

</div>