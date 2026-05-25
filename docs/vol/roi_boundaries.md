---
search:
  boost: 5.0
---

# Slot: roi_boundaries 


_Boundary coordinates for this Cell or ROI, encoded in the format specified by roi_boundaries_format in the table header. For the OME ROI Polygon model, coordinates are provided as a space-separated list of "x,y" pairs (e.g. "12.5,40.2 13.1,41.0 ..."). For OBJ 3D mesh format, the field contains the vertex and face list for the boundary mesh._



<div data-search-exclude markdown="1">



URI: [fof_ct:roi_boundaries](https://w3id.org/fof-ct/roi_boundaries)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ROIMapping](ROIMapping.md) | A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a F... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ROIMapping](ROIMapping.md) |
| Domain Of | [ROIMapping](ROIMapping.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 12.5,40.2 13.1,41.0 14.0,40.5 13.5,39.8 |
| v 1.0 2.0 3.0
v 4.0 5.0 6.0
f 1 2 3 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:roi_boundaries |
| native | fof_ct:roi_boundaries |




## LinkML Source

<details>
```yaml
name: roi_boundaries
description: Boundary coordinates for this Cell or ROI, encoded in the format specified
  by roi_boundaries_format in the table header. For the OME ROI Polygon model, coordinates
  are provided as a space-separated list of "x,y" pairs (e.g. "12.5,40.2 13.1,41.0
  ..."). For OBJ 3D mesh format, the field contains the vertex and face list for the
  boundary mesh.
examples:
- value: 12.5,40.2 13.1,41.0 14.0,40.5 13.5,39.8
- value: 'v 1.0 2.0 3.0

    v 4.0 5.0 6.0

    f 1 2 3'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: ROIMapping
domain_of:
- ROIMapping
range: string

```
</details></div>