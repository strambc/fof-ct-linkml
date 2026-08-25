---
search:
  boost: 5.0
---

# Slot: roi_boundaries_format_description 


_Free-text description of how ROI boundaries are encoded, sufficient for unambiguous parsing of all roi_boundaries values in this file (e.g. coordinate order, dimensionality, or an external file reference). Written as ##ROI_Boundaries_Format_Description= in the file header. Conditionally required (content-triggered): MANDATORY whenever roi_boundaries_format_type is 'Other'; otherwise recommended._



<div data-search-exclude markdown="1">



URI: [fof_ct:roi_boundaries_format_description](https://w3id.org/fof-ct/roi_boundaries_format_description)
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
| Cell boundaries are reported in global coordinates as lists of comma separated x,y coordinates separated by spaces like "x1,y1 x2,y2 x3,y3" (e.g. "0,0 1,2 3,5"). |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:roi_boundaries_format_description |
| native | fof_ct:roi_boundaries_format_description |




## LinkML Source

<details>
```yaml
name: roi_boundaries_format_description
description: 'Free-text description of how ROI boundaries are encoded, sufficient
  for unambiguous parsing of all roi_boundaries values in this file (e.g. coordinate
  order, dimensionality, or an external file reference). Written as ##ROI_Boundaries_Format_Description=
  in the file header. Conditionally required (content-triggered): MANDATORY whenever
  roi_boundaries_format_type is ''Other''; otherwise recommended.'
examples:
- value: Cell boundaries are reported in global coordinates as lists of comma separated
    x,y coordinates separated by spaces like "x1,y1 x2,y2 x3,y3" (e.g. "0,0 1,2 3,5").
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: ROIMappingTable
domain_of:
- ROIMappingTable
range: string

```
</details></div>