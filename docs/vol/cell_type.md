---
search:
  boost: 5.0
---

# Slot: cell_type 


_The type of cells present in this dataset, expressed using an ontology term from the Experimental Factor Ontology (EFO). Examples include "Cell in tissue" or "Cell in organoid". Written as #Cell_Type: in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:cell_type](https://w3id.org/fof-ct/cell_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CellTable](CellTable.md), [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Cell in tissue |
| Cell in organoid |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:cell_type |
| native | fof_ct:cell_type |




## LinkML Source

<details>
```yaml
name: cell_type
description: 'The type of cells present in this dataset, expressed using an ontology
  term from the Experimental Factor Ontology (EFO). Examples include "Cell in tissue"
  or "Cell in organoid". Written as #Cell_Type: in the file header.'
examples:
- value: Cell in tissue
- value: Cell in organoid
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- CellTable
- SubCellROITable
- ROIMappingTable
range: string

```
</details></div>