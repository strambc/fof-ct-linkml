# ER Diagram — FOF-vol-CT

Entity-Relationship diagrams for the **FOF-vol-CT** (volumetric) modality, generated using [LinkML's ER Diagram generator](https://linkml.io/linkml/generators/erdiagram.html).

FOF-vol-CT comprises **15 tables**: all 12 FOF-bas-CT tables plus 3 volumetric-specific tables. The **SM Localization Data table** (table 13) is the only mandatory FOF-vol-CT-exclusive table. The SM Localization Quality table (table 14) and the Undecoded SM Localization table (table 15) are both optional but recommended.

The SM Localization event is the primary data unit. Spots and Traces are optional post-processing outputs.

ID chain: `Loc_ID` (n→1) `Spot_ID` (n→1) `Trace_ID`

---

## Overview (all 15 tables, relationships only)

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

## FOF-vol-CT additions (tables 13–15, with attributes)

```mermaid
erDiagram
SMLocalization {
    integer cell_id
    string chrom
    integer chrom_end
    integer chrom_start
    integer extra_cell_roi_id
    integer loc_id
    integer spot_id
    integer sub_cell_roi_id
    integer trace_id
    float x
    float y
    float z
}
SMLocalizationQualityRecord {
    float centroid_intensity
    string channel_name
    string fluorophore_name
    float goodness_of_fit
    integer loc_id
    float peak_intensity
    integer photon_count
    float raw_x
    float raw_y
    float raw_z
    float x_loc_error
    float x_precision
    float y_loc_error
    float y_precision
    float z_loc_error
    float z_precision
}
SMLocalizationQualityTable {
    string description
    TableNamespaceEnumList additional_tables
    string experimenter_contact
    string experimenter_name
    string fof_ct_version
    string intensity_measurement_method
    string intensity_unit
    string lab_name
    string table_namespace
    TimeUnitEnum time_unit
    XYZUnitEnum xyz_unit
}
SMLocalizationTable {
    string description
    TableNamespaceEnumList additional_tables
    string experimenter_contact
    string experimenter_name
    string fof_ct_version
    string genome_assembly
    string intensity_measurement_method
    string intensity_unit
    string lab_name
    string modification
    string table_namespace
    TimeUnitEnum time_unit
    string vcf_file_name
    string vcf_version
    XYZUnitEnum xyz_unit
}
Software {
    string software_authors
    string software_description
    string software_parameters
    uri software_preferred_citation_id
    uri software_repository
    string software_title
    SoftwareTypeEnum software_type
}
UndecodedLocalization {
    string channel_name
    string fluorophore_name
    integer hyb_id
    integer image_frame_id
    integer loc_id
    integer the_z
    float x
    float y
    float z
}
UndecodedLocalizationTable {
    string description
    TableNamespaceEnumList additional_tables
    string experimenter_contact
    string experimenter_name
    string fof_ct_version
    string intensity_measurement_method
    string intensity_unit
    string lab_name
    string table_namespace
    TimeUnitEnum time_unit
    XYZUnitEnum xyz_unit
}

SMLocalizationQualityTable ||--}| SMLocalizationQualityRecord : "sm_localization_quality_records"
SMLocalizationQualityTable ||--}| Software : "softwares"
SMLocalizationTable ||--}| SMLocalization : "sm_localizations"
SMLocalizationTable ||--}| Software : "softwares"
UndecodedLocalizationTable ||--}| Software : "softwares"
UndecodedLocalizationTable ||--}| UndecodedLocalization : "undecoded_localizations"
```
