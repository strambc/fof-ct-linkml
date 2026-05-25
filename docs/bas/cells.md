---
search:
  boost: 5.0
---

# Slot: cells 


_The complete collection of Cells constituting this dataset. Each Cell corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. Cell_Size, Cell_Volume) MUST be present in every submitted Cell Data table._



<div data-search-exclude markdown="1">



URI: [fof_ct:cells](https://w3id.org/fof-ct/cells)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Cell](Cell.md) |
| Domain | [CellTable](CellTable.md) |
| Domain Of | [CellTable](CellTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:cells |
| native | fof_ct:cells |




## LinkML Source

<details>
```yaml
name: cells
description: The complete collection of Cells constituting this dataset. Each Cell
  corresponds to one data row in the TSV serialisation. At least one user-defined
  optional column (e.g. Cell_Size, Cell_Volume) MUST be present in every submitted
  Cell Data table.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: CellTable
domain_of:
- CellTable
range: Cell
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>