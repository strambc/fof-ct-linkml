# FISH Omics Format for Chromatin Tracing - Ball-and-Stick modality (FOF-bas-CT)

Root schema for the FISH Omics Format for Chromatin Tracing - Ball-and-Stick modality (FOF-bas-CT). Imports all twelve table schemas that together constitute the complete FOF-bas-CT data model. The DNA-Spot/Trace Data core table is the only mandatory table; all other 11 tables are optional but recommended. Each table schema imports fof_bas_ct_common for shared slots, the Software class, and enumerations.

URI: https://w3id.org/fof-ct/bas

Name: fof_bas_ct



## Classes

| Class | Description |
| --- | --- |
| [Cell](Cell.md) | A single Cell identified in a FOF-bas-CT experiment |
| [CellTable](CellTable.md) | The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell) |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |
| [ExtraCellROI](ExtraCellROI.md) | A single extracellular structure ROI (e |
| [ExtraCellROITable](ExtraCellROITable.md) | The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |
| [LocalizationMixin](LocalizationMixin.md) | Mixin capturing the shared concept of a single localization event across FOF-... |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |
| [RNASpotBiologicalRecord](RNASpotBiologicalRecord.md) | A single row in the RNA Spot Biological Data table |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FO... |
| [RNASpotQualityRecord](RNASpotQualityRecord.md) | A single row in the RNA Spot Quality table |
| [RNASpotQualityTable](RNASpotQualityTable.md) | The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna... |
| [RNASpotTable](RNASpotTable.md) | The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna) |
| [ROIMapping](ROIMapping.md) | A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a F... |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |
| [Software](Software.md) | Provenance metadata for a single software tool used to produce or process dat... |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |
| [SpotBiologicalRecord](SpotBiologicalRecord.md) | A single row in the Spot Biological Data table |
| [SpotBiologicalTable](SpotBiologicalTable.md) | The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT... |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |
| [SpotQualityTable](SpotQualityTable.md) | The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality... |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |
| [SubCellROI](SubCellROI.md) | A single sub-cellular structure ROI (e |
| [SubCellROITable](SubCellROITable.md) | The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_su... |
| [Trace](Trace.md) | A single chromatin Trace representing global properties associated with an en... |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |



## Slots

| Slot | Description |
| --- | --- |
| [additional_tables](additional_tables.md) | List of additional FOF-CT table namespaces being submitted alongside this tab... |
| [cell_id](cell_id.md) | Unique identifier for a Cell |
| [cell_type](cell_type.md) | The type of cells present in this dataset, expressed using an ontology term f... |
| [cells](cells.md) | The complete collection of Cells constituting this dataset |
| [centroid_intensity](centroid_intensity.md) | Signal intensity of the centroid pixel of the Spot / localization |
| [channel_name](channel_name.md) | The wavelength characteristics of the emission channel used to image this Spo... |
| [chrom](chrom.md) | Chromosome name/identifier using BED (Browser Extensible Data) convention (e |
| [chrom_end](chrom_end.md) | Non-inclusive end coordinate on the chromosome for the genomic target sequenc... |
| [chrom_start](chrom_start.md) | 0-based start coordinate on the chromosome for the genomic target sequence, f... |
| [description](description.md) | Free-text description of the experiment and of the data recorded in this tabl... |
| [experimenter_contact](experimenter_contact.md) | Email address of the person who performed the experiment |
| [experimenter_name](experimenter_name.md) | Full name of the person who performed the experiment |
| [extra_cell_roi_id](extra_cell_roi_id.md) | Unique identifier for an extracellular structure ROI (e |
| [extra_cell_roi_type](extra_cell_roi_type.md) | The type of extracellular structure ROI within which cells are embedded, expr... |
| [extra_cell_rois](extra_cell_rois.md) | The complete collection of extracellular ROIs constituting this dataset |
| [fluorophore_name](fluorophore_name.md) | The name of the fluorophore whose emission was used to detect this Spot / RNA... |
| [fof_ct_version](fof_ct_version.md) | Version of the FOF-CT format used in this file |
| [gene_id](gene_id.md) | Official gene identifier corresponding to rna_name |
| [gene_id_type](gene_id_type.md) | Type of gene identifier used in the gene_id column (e |
| [genome_assembly](genome_assembly.md) | Genome build used for Chrom, Chrom_Start and Chrom_End coordinates |
| [goodness_of_fit](goodness_of_fit.md) | Metric quantifying how well the fitted model matches the observed signal (e |
| [hyb_id](hyb_id.md) | Unique identifier for the hybridization round in which this localization even... |
| [image_frame_id](image_frame_id.md) | Unique integer identifier for the imaging frame in which this undecoded local... |
| [intensity_measurement_method](intensity_measurement_method.md) | Method used to perform intensity measurements, including how digital signals ... |
| [intensity_unit](intensity_unit.md) | Unit used to represent intensity measurements in this table |
| [lab_name](lab_name.md) | Name of the laboratory where the experiment was performed |
| [loc_id](loc_id.md) | A unique integer identifier for an individual localization event |
| [localizations](localizations.md) | The complete collection of Localization events constituting this dataset |
| [modification](modification.md) | Description of the nature and genomic position of a DNA insertion or deletion... |
| [peak_intensity](peak_intensity.md) | Signal intensity of the brightest pixel within the Spot / localization bounda... |
| [photon_count](photon_count.md) | Number of photons detected for this localization event or Spot |
| [raw_x](raw_x.md) | X coordinate before any post-processing corrections (drift correction, chroma... |
| [raw_y](raw_y.md) | Y coordinate before any post-processing corrections |
| [raw_z](raw_z.md) | Z coordinate before any post-processing corrections |
| [rna_name](rna_name.md) | Official name of the gene from which the targeted RNA is transcribed (e |
| [rna_spot_biological_records](rna_spot_biological_records.md) | The complete collection of RNASpotBiologicalRecord rows constituting this dat... |
| [rna_spot_id](rna_spot_id.md) | Unique integer identifier for an RNA bright Spot, unique across the entire da... |
| [rna_spot_quality_records](rna_spot_quality_records.md) | The complete collection of RNASpotQualityRecord rows constituting this datase... |
| [rna_spots](rna_spots.md) | The complete collection of RNA Spots constituting this dataset |
| [roi_boundaries](roi_boundaries.md) | Boundary coordinates for this Cell or ROI, encoded in the format specified by... |
| [roi_boundaries_format_description](roi_boundaries_format_description.md) | Free-text description of how ROI boundaries are encoded, sufficient for unamb... |
| [roi_boundaries_format_type](roi_boundaries_format_type.md) | Controlled-vocabulary identifier of the standard used to encode ROI boundarie... |
| [roi_mappings](roi_mappings.md) | The complete collection of ROI boundary records constituting this dataset |
| [software_authors](software_authors.md) | Author name(s) in 'Surname, Firstname' format, multiple authors separated by ... |
| [software_description](software_description.md) | Free-text description of the algorithm used, sufficient to guarantee reproduc... |
| [software_parameters](software_parameters.md) | Free-text description of the input parameters used for the specific analysis ... |
| [software_preferred_citation_id](software_preferred_citation_id.md) | Unique identifier (DOI, PMCID, ArXiv ID, etc |
| [software_repository](software_repository.md) | URL of the repository where the software release can be obtained |
| [software_title](software_title.md) | Name of the software tool |
| [software_type](software_type.md) | Functional category of the software tool |
| [softwares](softwares.md) | One or more Software entries documenting every tool used to produce or proces... |
| [spot_biological_records](spot_biological_records.md) | The complete collection of SpotBiologicalRecord rows constituting this datase... |
| [spot_id](spot_id.md) | Unique identifier for a bright DNA Spot |
| [spot_quality_records](spot_quality_records.md) | The complete collection of SpotQualityRecord rows constituting this dataset |
| [spots](spots.md) | The complete collection of Spots constituting this dataset |
| [sub_cell_roi_id](sub_cell_roi_id.md) | Unique identifier for a sub-cellular structure ROI (e |
| [sub_cell_roi_type](sub_cell_roi_type.md) | The type of sub-cellular structure ROI documented in this table or mapping fi... |
| [sub_cell_rois](sub_cell_rois.md) | The complete collection of sub-cellular ROIs constituting this dataset |
| [table_namespace](table_namespace.md) | Identifier for this table type |
| [the_z](the_z.md) | Identifier of the focal Z-plane in which this localization event was detected |
| [time_unit](time_unit.md) | Unit used to represent time intervals in this table |
| [trace_id](trace_id.md) | Unique identifier for a chromatin Trace |
| [traces](traces.md) | The complete collection of Traces constituting this dataset |
| [transcript_id](transcript_id.md) | Official transcript identifier for the specific transcript targeted by the FI... |
| [transcript_id_type](transcript_id_type.md) | Type of transcript identifier used in the transcript_id column (e |
| [vcf_file_name](vcf_file_name.md) | Name of the Variant Call Format (VCF) file that must be submitted alongside t... |
| [vcf_version](vcf_version.md) | Version of the VCF format used for the accompanying VCF file |
| [x](x.md) | Sub-pixel X coordinate of this detected event (Spot or localisation) in the u... |
| [x_chromatic_shift](x_chromatic_shift.md) | Chromatic aberration correction offset applied to the X coordinate |
| [x_drift](x_drift.md) | Drift correction offset applied to the X coordinate |
| [x_loc_error](x_loc_error.md) | Localization error estimate for the X coordinate (e |
| [x_precision](x_precision.md) | Metric quantifying the precision of the X-axis localization estimate |
| [xyz_unit](xyz_unit.md) | Unit used to represent X, Y, Z spatial coordinates or distances in this table |
| [y](y.md) | Sub-pixel Y coordinate of this detected event (Spot or localisation) in the u... |
| [y_chromatic_shift](y_chromatic_shift.md) | Chromatic aberration correction offset applied to the Y coordinate |
| [y_drift](y_drift.md) | Drift correction offset applied to the Y coordinate |
| [y_loc_error](y_loc_error.md) | Localization error estimate for the Y coordinate |
| [y_precision](y_precision.md) | Metric quantifying the precision of the Y-axis localization estimate |
| [z](z.md) | Sub-pixel Z coordinate of this detected event (Spot or localisation) in the u... |
| [z_chromatic_shift](z_chromatic_shift.md) | Chromatic aberration correction offset applied to the Z coordinate |
| [z_drift](z_drift.md) | Drift correction offset applied to the Z coordinate |
| [z_loc_error](z_loc_error.md) | Localization error estimate for the Z coordinate |
| [z_precision](z_precision.md) | Metric quantifying the precision of the Z-axis localization estimate |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ROIBoundariesFormatTypeEnum](ROIBoundariesFormatTypeEnum.md) | Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI Mappi... |
| [SoftwareTypeEnum](SoftwareTypeEnum.md) | Allowed functional categories for software tools (per the FOF-CT RTD "Allowab... |
| [TableNamespaceEnum](TableNamespaceEnum.md) | Allowed namespace identifiers for FOF-CT tables that may be listed in the add... |
| [TimeUnitEnum](TimeUnitEnum.md) | Allowed units for time intervals |
| [XYZUnitEnum](XYZUnitEnum.md) | Allowed units for X, Y, Z spatial coordinates or distances |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
