---
search:
  boost: 5.0
---

# Slot: sub_cell_roi_type 


_The type of sub-cellular structure ROI documented in this table or mapping file. It is recommended to use a GO 'cellular_component' child term. Examples include Nucleolus, Nuclear Lamina (NL), Nuclear Pore Complex (NPC), PML_body, Cajal_body, Chromosome_Domain. Written as #Sub_Cell_ROI_Type: in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:sub_cell_roi_type](https://w3id.org/fof-ct/sub_cell_roi_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Nucleolus |
| Nuclear Lamina (NL) |
| Nuclear Pore Complex (NPC) |
| Chromosome_Domain |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:sub_cell_roi_type |
| native | fof_ct:sub_cell_roi_type |




## LinkML Source

<details>
```yaml
name: sub_cell_roi_type
description: 'The type of sub-cellular structure ROI documented in this table or mapping
  file. It is recommended to use a GO ''cellular_component'' child term. Examples
  include Nucleolus, Nuclear Lamina (NL), Nuclear Pore Complex (NPC), PML_body, Cajal_body,
  Chromosome_Domain. Written as #Sub_Cell_ROI_Type: in the file header.'
examples:
- value: Nucleolus
- value: Nuclear Lamina (NL)
- value: Nuclear Pore Complex (NPC)
- value: Chromosome_Domain
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SubCellROITable
- ROIMappingTable
range: string

```
</details></div>