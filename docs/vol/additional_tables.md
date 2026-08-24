---
search:
  boost: 5.0
---

# Slot: additional_tables 


_List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:additional_tables](https://w3id.org/fof-ct/additional_tables)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  no  |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |  yes  |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  yes  |
| [SpotQualityTable](SpotQualityTable.md) | The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality... |  yes  |
| [RNASpotQualityTable](RNASpotQualityTable.md) | The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna... |  yes  |
| [SpotBiologicalTable](SpotBiologicalTable.md) | The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT... |  yes  |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |
| [SMLocalizationTable](SMLocalizationTable.md) | The SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_vol... |  yes  |
| [SMLocalizationQualityTable](SMLocalizationQualityTable.md) | The SM Localization Quality table of a FOF-vol-CT dataset (namespace: FOF-CT_... |  yes  |
| [UndecodedLocalizationTable](UndecodedLocalizationTable.md) | The Undecoded SM Localization Data table of a FOF-vol-CT dataset (namespace: ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TableNamespaceEnum](TableNamespaceEnum.md) |
| Domain Of | [SpotTable](SpotTable.md), [DemultiplexingTable](DemultiplexingTable.md), [TraceTable](TraceTable.md), [RNASpotTable](RNASpotTable.md), [SpotQualityTable](SpotQualityTable.md), [RNASpotQualityTable](RNASpotQualityTable.md), [SpotBiologicalTable](SpotBiologicalTable.md), [RNASpotBiologicalTable](RNASpotBiologicalTable.md), [CellTable](CellTable.md), [ExtraCellROITable](ExtraCellROITable.md), [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md), [SMLocalizationTable](SMLocalizationTable.md), [SMLocalizationQualityTable](SMLocalizationQualityTable.md), [UndecodedLocalizationTable](UndecodedLocalizationTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:additional_tables |
| native | fof_ct:additional_tables |




## LinkML Source

<details>
```yaml
name: additional_tables
description: 'List of additional FOF-CT table namespaces being submitted alongside
  this table, separated by commas in the TSV header. Written as #Additional_Tables:
  in the file header.'
from_schema: https://w3id.org/fof-ct/vol
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
- SMLocalizationTable
- SMLocalizationQualityTable
- UndecodedLocalizationTable
range: TableNamespaceEnum
multivalued: true

```
</details></div>