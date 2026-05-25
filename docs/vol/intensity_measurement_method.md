---
search:
  boost: 5.0
---

# Slot: intensity_measurement_method 


_Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported._



<div data-search-exclude markdown="1">



URI: [fof_ct:intensity_measurement_method](https://w3id.org/fof-ct/intensity_measurement_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  no  |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |  no  |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |  no  |
| [SpotQualityTable](SpotQualityTable.md) | The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality... |  yes  |
| [RNASpotQualityTable](RNASpotQualityTable.md) | The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna... |  yes  |
| [SpotBiologicalTable](SpotBiologicalTable.md) | The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT... |  yes  |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |  yes  |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |  yes  |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |
| [SMLocalizationTable](SMLocalizationTable.md) | The SM Localization Data table of a FOF-vol-CT dataset (namespace: 4dn_FOF-CT... |  no  |
| [SMLocalizationQualityTable](SMLocalizationQualityTable.md) | The SM Localization Quality table of a FOF-vol-CT dataset (namespace: 4dn_FOF... |  no  |
| [UndecodedLocalizationTable](UndecodedLocalizationTable.md) | The Undecoded SM Localization Data table of a FOF-vol-CT dataset (namespace: ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DemultiplexingTable](DemultiplexingTable.md), [TraceTable](TraceTable.md), [RNASpotTable](RNASpotTable.md), [SpotQualityTable](SpotQualityTable.md), [RNASpotQualityTable](RNASpotQualityTable.md), [SpotBiologicalTable](SpotBiologicalTable.md), [RNASpotBiologicalTable](RNASpotBiologicalTable.md), [CellTable](CellTable.md), [ExtraCellROITable](ExtraCellROITable.md), [SubCellROITable](SubCellROITable.md), [ROIMappingTable](ROIMappingTable.md), [SMLocalizationTable](SMLocalizationTable.md), [SMLocalizationQualityTable](SMLocalizationQualityTable.md), [UndecodedLocalizationTable](UndecodedLocalizationTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Localization centroid intensity |
| Mean Fluorescence Intensity |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:intensity_measurement_method |
| native | fof_ct:intensity_measurement_method |




## LinkML Source

<details>
```yaml
name: intensity_measurement_method
description: 'Method used to perform intensity measurements, including how digital
  signals were converted to photon counts. Written as #Intensity_Measurement_Method:
  in the file header. Conditionally required when any intensity metric is reported.'
examples:
- value: Localization centroid intensity
- value: Mean Fluorescence Intensity
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
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
range: string

```
</details></div>