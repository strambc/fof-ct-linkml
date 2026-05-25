# Entity Relationship Diagrams

Entity-Relationship diagrams generated using [LinkML's ER Diagram generator](https://linkml.io/linkml/generators/erdiagram.html).

FOF-CT defines two complementary modalities:

- **FOF-bas-CT** (ball-and-stick): The Spot and Trace are the mandatory primary data. The raw localizations from which Spots were extracted may optionally be reported in the Demultiplexing table.
- **FOF-vol-CT** (volumetric): Individual SM Localizations and their quality metrics are the mandatory primary data. Spots and Traces (post-processing outputs) are optional.

In both modalities the ID chain is identical: `Loc_ID` (n→1) `Spot_ID` (n→1) `Trace_ID`.

---

## Combined overview — FOF-CT (both modalities)

All 15 tables. Attributes hidden for clarity.

```mermaid
erDiagram
Cell {

}
CellTable {

}
DemultiplexingTable {

}
ExtraCellROI {

}
ExtraCellROITable {

}
Localization {

}
RNASpot {

}
RNASpotBiologicalRecord {

}
RNASpotBiologicalTable {

}
RNASpotQualityRecord {

}
RNASpotQualityTable {

}
RNASpotTable {

}
ROIMapping {

}
ROIMappingTable {

}
SMLocalization {

}
SMLocalizationQualityRecord {

}
SMLocalizationQualityTable {

}
SMLocalizationTable {

}
Software {

}
Spot {

}
SpotBiologicalRecord {

}
SpotBiologicalTable {

}
SpotQualityRecord {

}
SpotQualityTable {

}
SpotTable {

}
SubCellROI {

}
SubCellROITable {

}
Trace {

}
TraceTable {

}
UndecodedLocalization {

}
UndecodedLocalizationTable {

}

CellTable ||--}o Software : "softwares"
CellTable ||--}| Cell : "cells"
DemultiplexingTable ||--}| Localization : "localizations"
DemultiplexingTable ||--}| Software : "softwares"
ExtraCellROITable ||--}o Software : "softwares"
ExtraCellROITable ||--}| ExtraCellROI : "extra_cell_rois"
RNASpotBiologicalTable ||--}o Software : "softwares"
RNASpotBiologicalTable ||--}| RNASpotBiologicalRecord : "rna_spot_biological_records"
RNASpotQualityTable ||--}o Software : "softwares"
RNASpotQualityTable ||--}| RNASpotQualityRecord : "rna_spot_quality_records"
RNASpotTable ||--}| RNASpot : "rna_spots"
RNASpotTable ||--}| Software : "softwares"
ROIMappingTable ||--}o Software : "softwares"
ROIMappingTable ||--}| ROIMapping : "roi_mappings"
SMLocalizationQualityTable ||--}| SMLocalizationQualityRecord : "sm_localization_quality_records"
SMLocalizationQualityTable ||--}| Software : "softwares"
SMLocalizationTable ||--}| SMLocalization : "sm_localizations"
SMLocalizationTable ||--}| Software : "softwares"
SpotBiologicalTable ||--}o Software : "softwares"
SpotBiologicalTable ||--}| SpotBiologicalRecord : "spot_biological_records"
SpotQualityTable ||--}o Software : "softwares"
SpotQualityTable ||--}| SpotQualityRecord : "spot_quality_records"
SpotTable ||--}| Software : "softwares"
SpotTable ||--}| Spot : "spots"
SubCellROITable ||--}o Software : "softwares"
SubCellROITable ||--}| SubCellROI : "sub_cell_rois"
TraceTable ||--}o Software : "softwares"
TraceTable ||--}| Trace : "traces"
UndecodedLocalizationTable ||--}| Software : "softwares"
UndecodedLocalizationTable ||--}| UndecodedLocalization : "undecoded_localizations"
```

---

## FOF-vol-CT additions (tables 13–15)

The three tables specific to the volumetric modality, shown with their attributes.

```mermaid
erDiagram
SMLocalization {
    integer loc_id
    float x
    float y
    float z
    integer spot_id
    integer trace_id
    string chrom
    integer chrom_start
    integer chrom_end
    integer sub_cell_roi_id
    integer cell_id
    integer extra_cell_roi_id
}
SMLocalizationTable {
    string fof_ct_version
    string table_namespace
    string genome_assembly
    XYZUnitEnum xyz_unit
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
SMLocalizationQualityRecord {
    integer loc_id
    float x_precision
    float y_precision
    float z_precision
    integer photon_count
    float goodness_of_fit
}
SMLocalizationQualityTable {
    string fof_ct_version
    string table_namespace
    XYZUnitEnum xyz_unit
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
UndecodedLocalization {
    integer loc_id
    float x
    float y
    float z
    integer frame_id
    string fluor
}
UndecodedLocalizationTable {
    string fof_ct_version
    string table_namespace
    XYZUnitEnum xyz_unit
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
Software {
    string software_title
    SoftwareTypeEnum software_type
    string software_authors
    string software_description
    uri software_repository
    uri software_preferred_citation_id
}

SMLocalizationTable ||--}| SMLocalization : "sm_localizations"
SMLocalizationTable ||--}| Software : "softwares"
SMLocalizationQualityTable ||--}| SMLocalizationQualityRecord : "sm_localization_quality_records"
SMLocalizationQualityTable ||--}| Software : "softwares"
UndecodedLocalizationTable ||--}| UndecodedLocalization : "undecoded_localizations"
UndecodedLocalizationTable ||--}| Software : "softwares"
```
