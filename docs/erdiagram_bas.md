# ER Diagram — FOF-bas-CT

Entity-Relationship diagrams for the **FOF-bas-CT** (ball-and-stick) modality, generated using [LinkML's ER Diagram generator](https://linkml.io/linkml/generators/erdiagram.html).

FOF-bas-CT comprises **12 tables**. The **DNA-Spot/Trace Data core table** (table 1) is the only mandatory table. All other 11 tables are optional but recommended.

The Spot is the primary data unit. Localization events (from which Spots are extracted) may optionally be reported in the Demultiplexing table.

ID chain: `Loc_ID` (n→1) `Spot_ID` (n→1) `Trace_ID`

---

## FOF-bas-CT overview (all 12 tables, relationships only)

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
```

---

## FOF-bas-CT detail (all 12 tables, with attributes)

```mermaid
erDiagram
Spot {
    integer spot_id
    integer trace_id
    float x
    float y
    float z
    string chrom
    integer chrom_start
    integer chrom_end
    integer sub_cell_roi_id
    integer cell_id
    integer extra_cell_roi_id
}
SpotTable {
    string fof_ct_version
    string table_namespace
    string genome_assembly
    XYZUnitEnum xyz_unit
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    string modification
    string vcf_file_name
    string vcf_version
}
Localization {
    integer loc_id
    float x
    float y
    float z
    integer spot_id
    string fluor
}
DemultiplexingTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    XYZUnitEnum xyz_unit
    TimeUnitEnum time_unit
    string intensity_unit
    string intensity_measurement_method
}
Trace {
    integer trace_id
}
TraceTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
RNASpot {
    integer rna_spot_id
    float x
    float y
    float z
    string rna_name
    string gene_id
    integer trace_id
    string transcript_id
    integer sub_cell_roi_id
    integer cell_id
    integer extra_cell_roi_id
}
RNASpotTable {
    string fof_ct_version
    string table_namespace
    string genome_assembly
    string gene_id_type
    XYZUnitEnum xyz_unit
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    string transcript_id_type
}
SpotQualityRecord {
    integer spot_id
    string channel_name
    string fluorophore_name
    float x_precision
    float y_precision
    float z_precision
    integer photon_count
    float goodness_of_fit
    float centroid_intensity
    float peak_intensity
    float raw_x
    float raw_y
    float raw_z
    float x_drift
    float y_drift
    float z_drift
    float x_chromatic_shift
    float y_chromatic_shift
    float z_chromatic_shift
    float x_loc_error
    float y_loc_error
    float z_loc_error
}
SpotQualityTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    XYZUnitEnum xyz_unit
    TimeUnitEnum time_unit
    string intensity_unit
    string intensity_measurement_method
}
RNASpotQualityRecord {
    integer rna_spot_id
}
RNASpotQualityTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
SpotBiologicalRecord {
    integer spot_id
}
SpotBiologicalTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
RNASpotBiologicalRecord {
    integer rna_spot_id
}
RNASpotBiologicalTable {
    string fof_ct_version
    string table_namespace
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
Cell {
    integer cell_id
    integer extra_cell_roi_id
}
CellTable {
    string fof_ct_version
    string table_namespace
    string cell_type
    string extra_cell_roi_type
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    XYZUnitEnum xyz_unit
}
ExtraCellROI {
    integer extra_cell_roi_id
}
ExtraCellROITable {
    string fof_ct_version
    string table_namespace
    string extra_cell_roi_type
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
}
SubCellROI {
    integer sub_cell_roi_id
    integer cell_id
}
SubCellROITable {
    string fof_ct_version
    string table_namespace
    string sub_cell_roi_type
    string cell_type
    string lab_name
    string experimenter_name
    string experimenter_contact
    string description
    XYZUnitEnum xyz_unit
}
ROIMapping {
    integer sub_cell_roi_id
    integer cell_id
    integer extra_cell_roi_id
    string roi_boundaries
}
ROIMappingTable {
    string fof_ct_version
    string table_namespace
    string roi_boundaries_format
    XYZUnitEnum xyz_unit
    string cell_type
    string sub_cell_roi_type
    string extra_cell_roi_type
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

SpotTable ||--}| Spot : "spots"
SpotTable ||--}| Software : "softwares"
DemultiplexingTable ||--}| Localization : "localizations"
DemultiplexingTable ||--}| Software : "softwares"
TraceTable ||--}| Trace : "traces"
TraceTable ||--}o Software : "softwares"
RNASpotTable ||--}| RNASpot : "rna_spots"
RNASpotTable ||--}| Software : "softwares"
SpotQualityTable ||--}| SpotQualityRecord : "spot_quality_records"
SpotQualityTable ||--}o Software : "softwares"
RNASpotQualityTable ||--}| RNASpotQualityRecord : "rna_spot_quality_records"
RNASpotQualityTable ||--}o Software : "softwares"
SpotBiologicalTable ||--}| SpotBiologicalRecord : "spot_biological_records"
SpotBiologicalTable ||--}o Software : "softwares"
RNASpotBiologicalTable ||--}| RNASpotBiologicalRecord : "rna_spot_biological_records"
RNASpotBiologicalTable ||--}o Software : "softwares"
CellTable ||--}| Cell : "cells"
CellTable ||--}o Software : "softwares"
ExtraCellROITable ||--}| ExtraCellROI : "extra_cell_rois"
ExtraCellROITable ||--}o Software : "softwares"
SubCellROITable ||--}| SubCellROI : "sub_cell_rois"
SubCellROITable ||--}o Software : "softwares"
ROIMappingTable ||--}| ROIMapping : "roi_mappings"
ROIMappingTable ||--}o Software : "softwares"
```
