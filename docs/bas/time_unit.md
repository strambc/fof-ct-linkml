---
search:
  boost: 5.0
---

# Slot: time_unit 


_Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column._



<div data-search-exclude markdown="1">



URI: [fof_ct:time_unit](https://w3id.org/fof-ct/time_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  no  |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |  no  |
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
| Range | [TimeUnitEnum](TimeUnitEnum.md) |
| Domain Of | [DemultiplexingTable](DemultiplexingTable.md), [TraceTable](TraceTable.md), [SpotQualityTable](SpotQualityTable.md), [RNASpotQualityTable](RNASpotQualityTable.md), [SpotBiologicalTable](SpotBiologicalTable.md), [RNASpotBiologicalTable](RNASpotBiologicalTable.md), [CellTable](CellTable.md), [ExtraCellROITable](ExtraCellROITable.md), [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| sec |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:time_unit |
| native | fof_ct:time_unit |




## LinkML Source

<details>
```yaml
name: time_unit
description: 'Unit used to represent time intervals in this table. Allowed values
  are SI time units plus ''min'' and ''hr''. Written as ##Time_Unit= in the file header.
  Conditionally required (metric- triggered) when any time metric is reported in an
  optional column.'
examples:
- value: sec
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- DemultiplexingTable
- TraceTable
- SpotQualityTable
- RNASpotQualityTable
- SpotBiologicalTable
- RNASpotBiologicalTable
- CellTable
- ExtraCellROITable
- SubCellROITable
- ROIMappingTable
range: TimeUnitEnum

```
</details></div>