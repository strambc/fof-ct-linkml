---
search:
  boost: 5.0
---

# Slot: xyz_unit 


_Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table._



<div data-search-exclude markdown="1">



URI: [fof_ct:xyz_unit](https://w3id.org/fof-ct/xyz_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  no  |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |  no  |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  yes  |
| [SpotQualityTable](SpotQualityTable.md) | The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality... |  yes  |
| [RNASpotQualityTable](RNASpotQualityTable.md) | The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna... |  yes  |
| [SpotBiologicalTable](SpotBiologicalTable.md) | The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT... |  yes  |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [XYZUnitEnum](XYZUnitEnum.md) |
| Domain Of | [SpotTable](SpotTable.md), [DemultiplexingTable](DemultiplexingTable.md), [TraceTable](TraceTable.md), [RNASpotTable](RNASpotTable.md), [SpotQualityTable](SpotQualityTable.md), [RNASpotQualityTable](RNASpotQualityTable.md), [SpotBiologicalTable](SpotBiologicalTable.md), [RNASpotBiologicalTable](RNASpotBiologicalTable.md), [CellTable](CellTable.md), [ExtraCellROITable](ExtraCellROITable.md), [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| micron |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:xyz_unit |
| native | fof_ct:xyz_unit |




## LinkML Source

<details>
```yaml
name: xyz_unit
description: 'Unit used to represent X, Y, Z spatial coordinates or distances in this
  table. Use ''micron'' to avoid issues with Greek symbols. Values should be drawn
  from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in
  every FOF-CT table.'
examples:
- value: micron
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotTable
- DemultiplexingTable
- TraceTable
- RNASpotTable
- SpotQualityTable
- RNASpotQualityTable
- SpotBiologicalTable
- RNASpotBiologicalTable
- CellTable
- ExtraCellROITable
- SubCellROITable
- ROIMappingTable
range: XYZUnitEnum
required: true

```
</details></div>