-- # Class: Software Description: Provenance metadata for a single software tool used to produce or process data in a FOF-CT table. If more than one tool was used, a separate Software entry must be provided for each. Written as a repeating block of #Software_* fields in the file header.
--     * Slot: id
--     * Slot: software_title Description: Name of the software tool. Written as #Software_Title:.
--     * Slot: software_type Description: Functional category of the software tool. Written as #Software_Type:.
--     * Slot: software_authors Description: Author name(s) in 'Surname, Firstname' format, multiple authors separated by semicolons. Written as #Software_Authors:.
--     * Slot: software_description Description: Free-text description of the algorithm and analysis parameters, sufficient to guarantee reproducibility. Written as #Software_Description:.
--     * Slot: software_repository Description: URL of the repository where the software release can be obtained. Written as #Software_Repository:.
--     * Slot: software_preferred_citation_id Description: Unique identifier (DOI, PMCID, ArXiv ID, etc.) for the primary publication describing this software. Written as #Software_PreferredCitationID:.
--     * Slot: SpotTable_id Description: Autocreated FK slot
--     * Slot: LocalizationTable_id Description: Autocreated FK slot
--     * Slot: TraceTable_id Description: Autocreated FK slot
--     * Slot: RNASpotTable_id Description: Autocreated FK slot
--     * Slot: SpotQualityTable_id Description: Autocreated FK slot
--     * Slot: RNASpotQualityTable_id Description: Autocreated FK slot
--     * Slot: SpotBiologicalTable_id Description: Autocreated FK slot
--     * Slot: RNASpotBiologicalTable_id Description: Autocreated FK slot
--     * Slot: CellTable_id Description: Autocreated FK slot
--     * Slot: ExtraCellROITable_id Description: Autocreated FK slot
--     * Slot: SubCellROITable_id Description: Autocreated FK slot
--     * Slot: ROIMappingTable_id Description: Autocreated FK slot
-- # Class: Spot Description: A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT core table and represents a specific genomic target sequence localised in 3D space and assigned to a chromatin Trace.
--     * Slot: spot_id Description: Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table.
--     * Slot: trace_id Description: Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table.
--     * Slot: x Description: Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).
--     * Slot: y Description: Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: z Description: Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: chrom Description: Chromosome name using BED (Browser Extensible Data) convention (e.g., chr3, chrY, chr2_random).
--     * Slot: chrom_start Description: 0-based start coordinate on the chromosome for the genomic target sequence associated with this Spot, following BED convention.
--     * Slot: chrom_end Description: Non-inclusive end coordinate on the chromosome for the genomic target sequence associated with this Spot, following BED convention.
--     * Slot: sub_cell_roi_id Description: Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.
--     * Slot: cell_id Description: Unique identifier for a Cell. Links to the Cell Data table.
--     * Slot: extra_cell_roi_id Description: Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.
--     * Slot: SpotTable_id Description: Autocreated FK slot
-- # Class: SpotTable Description: The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_core). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: genome_assembly Description: Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: modification Description: Description of the nature and genomic position of a DNA insertion or deletion in the genome under study. Conditionally required when genome_assembly uses the 'custom-build:' prefix. Written as ##Modification= in the file header.
--     * Slot: vcf_file_name Description: Name of the Variant Call Format (VCF) file that must be submitted alongside the dataset to describe the genome insertion or deletion. Conditionally required when genome_assembly uses the 'custom-build:' prefix. Written as ##VCF_File_Name= in the file header.
--     * Slot: vcf_version Description: Version of the VCF format used for the accompanying VCF file. Conditionally required when genome_assembly uses the 'custom-build:' prefix. Written as ##VCF_Version= in the file header.
-- # Class: Localization Description: A single individual localisation event contributing to the final position of a bright DNA Spot in a multiplexed FISH experiment (e.g. MERFISH). Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Spot Demultiplexing table. The spot_id field links each Localization to its parent Spot in the core table (or RNA Spot Data table); it may be NA when the localisation could not be assigned to any Spot. This class accepts additional user-defined optional columns (e.g. Hyb, Brightness, Fit_Quality).
--     * Slot: loc_id Description: A unique integer identifier for this individual localisation event. Loc_ID values are unique across the entire dataset.
--     * Slot: spot_id Description: Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table.
--     * Slot: x Description: Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).
--     * Slot: y Description: Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: z Description: Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: fluor Description: Fluorescent channel in which this individual localisation event was detected (e.g. DAPI, GFP, Cy5, Alexa647).
--     * Slot: LocalizationTable_id Description: Autocreated FK slot
-- # Class: LocalizationTable Description: The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_demultiplexing). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of Localization events (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended for multiplexed FISH experiments.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: Trace Description: A single chromatin Trace representing global properties associated with an entire polymeric trace rather than with individual Spots. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Trace Data table. The trace_id links each Trace to the core table and to the RNA Spot Data table. IMPORTANT: this class MUST contain at least one user-defined optional column describing trace-level properties (e.g., Allele, RNA_Expression, Lamina_Distance). User-defined columns are accommodated via open schema.
--     * Slot: trace_id Description: Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table.
--     * Slot: TraceTable_id Description: Autocreated FK slot
-- # Class: TraceTable Description: The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of Traces (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended when trace-level properties are recorded.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: RNASpot Description: A single detected RNA bright Spot corresponding to one RNA transcript location detected alongside Chromatin Tracing. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT RNA Spot Data table. The rna_spot_id links each RNASpot to the RNA Quality and RNA Biological Data tables; the trace_id links this RNA Spot to a DNA chromatin Trace in the core table and Trace Data table. This class accepts additional user-defined optional columns via open schema.
--     * Slot: id
--     * Slot: rna_spot_id Description: Unique integer identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.
--     * Slot: x Description: Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).
--     * Slot: y Description: Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: z Description: Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.
--     * Slot: rna_name Description: Official name of the gene from which the targeted RNA is transcribed (e.g. ACTB, GAPDH). Should follow HGNC (human) or MGI (mouse) gene nomenclature.
--     * Slot: gene_id Description: Official gene identifier corresponding to rna_name. The type of identifier used (e.g. Ensembl gene ID, NCBI Gene ID) must be declared in the gene_id_type header field.
--     * Slot: trace_id Description: Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table.
--     * Slot: transcript_id Description: Official transcript identifier for the specific transcript targeted by the FISH probe. Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. The type of identifier used must be declared in the transcript_id_type header field.
--     * Slot: sub_cell_roi_id Description: Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.
--     * Slot: cell_id Description: Unique identifier for a Cell. Links to the Cell Data table.
--     * Slot: extra_cell_roi_id Description: Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.
--     * Slot: RNASpotTable_id Description: Autocreated FK slot
-- # Class: RNASpotTable Description: The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of RNA Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended when RNA data are collected alongside Chromatin Tracing.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: genome_assembly Description: Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header.
--     * Slot: gene_id_type Description: Type of gene identifier used in the gene_id column (e.g. Ensembl_V38, NCBI_Gene). Written as ##Gene_ID_Type= in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: transcript_id_type Description: Type of transcript identifier used in the transcript_id column (e.g. Ensembl_V38, RefSeq). Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. Written as ##Transcript_ID_Type= in the file header.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: SpotQualityRecord Description: A single row in the Spot Quality table. Each instance captures one or more quality metrics for a specific DNA bright Spot identified by Spot_ID. At least one user-defined quality metric column MUST be present; users declare these via #^ header lines.
--     * Slot: spot_id Description: Unique integer identifier for the DNA bright Spot to which these quality metrics belong. Links to the corresponding Spot record in the core table (table 1). Must be unique within this table.
--     * Slot: SpotQualityTable_id Description: Autocreated FK slot
-- # Class: SpotQualityTable Description: The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of SpotQualityRecord rows. Submission of this table is optional but recommended.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. Must always be '4dn_FOF-CT_quality'. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used for any spatial coordinate or distance metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##XYZ_Unit= in the file header.
--     * Slot: time_unit Description: Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.
--     * Slot: intensity_unit Description: Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.
-- # Class: RNASpotQualityRecord Description: A single row in the RNA Spot Quality table. Each instance captures one or more quality metrics for a specific RNA bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the dataset, linking to the corresponding record in the RNA Spot Data table (table 4). At least one user-defined quality metric column MUST be present; users declare these via #^ header lines.
--     * Slot: rna_spot_id Description: Unique integer identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.
--     * Slot: RNASpotQualityTable_id Description: Autocreated FK slot
-- # Class: RNASpotQualityTable Description: The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_quality). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of RNASpotQualityRecord rows. Submission of this table is optional but recommended.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. Must always be '4dn_FOF-CT_rna_quality'. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used for any spatial coordinate or distance metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##XYZ_Unit= in the file header.
--     * Slot: time_unit Description: Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.
--     * Slot: intensity_unit Description: Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.
-- # Class: SpotBiologicalRecord Description: A single row in the Spot Biological Data table. Each instance captures one or more user-defined biological properties for a specific DNA bright Spot identified by Spot_ID. Spot_ID values must be unique across the dataset, linking to the corresponding Spot record in the core table (table 1). At least one user-defined biological property column MUST be present; users declare these via #^ header lines.
--     * Slot: spot_id Description: Unique integer identifier for the DNA bright Spot to which these biological properties belong. Links to the corresponding Spot record in the core table (table 1). Must be unique within this table and across the entire dataset.
--     * Slot: SpotBiologicalTable_id Description: Autocreated FK slot
-- # Class: SpotBiologicalTable Description: The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_bio). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of SpotBiologicalRecord rows. Submission of this table is optional but highly recommended.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. Must always be '4dn_FOF-CT_bio'. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used for any spatial coordinate or distance metric reported in user-defined columns (e.g. distance from nuclear lamina). Conditionally required when any such metric is present. Written as ##XYZ_Unit= in the file header.
--     * Slot: time_unit Description: Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.
--     * Slot: intensity_unit Description: Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.
-- # Class: RNASpotBiologicalRecord Description: A single row in the RNA Spot Biological Data table. Each instance captures one or more user-defined biological properties for a specific RNA bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the dataset, linking to the corresponding record in the RNA Spot Data table (table 4). At least one user-defined biological property column MUST be present; users declare these via #^ header lines.
--     * Slot: rna_spot_id Description: Unique integer identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.
--     * Slot: RNASpotBiologicalTable_id Description: Autocreated FK slot
-- # Class: RNASpotBiologicalTable Description: The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_bio). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of RNASpotBiologicalRecord rows. Submission of this table is optional but highly recommended.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. Must always be '4dn_FOF-CT_rna_bio'. Written as ##Table_Namespace= in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used for any spatial coordinate or distance metric reported in user-defined columns (e.g. distance from nuclear lamina). Conditionally required when any such metric is present. Written as ##XYZ_Unit= in the file header.
--     * Slot: time_unit Description: Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.
--     * Slot: intensity_unit Description: Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.
-- # Class: Cell Description: A single Cell identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Cell Data table. The cell_id field uniquely identifies each Cell and links to the core table, the Sub-Cell ROI Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined optional columns (e.g. Cell_Size, Cell_Volume, Cell_Cycle_State, RNA_Spot_Count) via open schema. At least one such user-defined column MUST be present per submission.
--     * Slot: cell_id Description: Unique integer identifier for this Cell. Cell_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the Sub-Cell ROI Data table, and the Cell/ROI Mapping table.
--     * Slot: extra_cell_roi_id Description: Identifier of the extracellular structure ROI (e.g. tissue section, organoid) that contains this Cell. Conditionally required when this Cell can be associated with an extracellular ROI identified as part of this experiment and reported in a dedicated Extra-Cell ROI Data table.
--     * Slot: CellTable_id Description: Autocreated FK slot
-- # Class: CellTable Description: The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of Cells (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: cell_type Description: The type of cells present in this dataset, expressed using an ontology term from the Experimental Factor Ontology (EFO). Examples include "Cell in tissue" or "Cell in organoid". Written as #Cell_Type: in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: extra_cell_roi_type Description: The type of extracellular structure ROI within which cells are embedded, expressed using an EFO 'organism part' child term (e.g. Tissue, Organoid). Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: ExtraCellROI Description: A single extracellular structure ROI (e.g. a tissue section or organoid) identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Extra-Cell ROI Data table. The extra_cell_roi_id field uniquely identifies each ROI and links to the core table, the RNA Spot Data table, and the Cell Data table. This class accepts additional user-defined optional columns (e.g. ROI_Volume, Cell_Count). At least one such user-defined column MUST be present per submission.
--     * Slot: extra_cell_roi_id Description: Unique integer identifier for this extracellular structure ROI. Extra_Cell_ROI_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the RNA Spot Data table, and the Cell Data table.
--     * Slot: ExtraCellROITable_id Description: Autocreated FK slot
-- # Class: ExtraCellROITable Description: The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of extracellular ROIs (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: extra_cell_roi_type Description: The type of extracellular structure ROI within which cells are embedded, expressed using an EFO 'organism part' child term (e.g. Tissue, Organoid). Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type: in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: SubCellROI Description: A single sub-cellular structure ROI (e.g. nucleolus, nuclear lamina, PML body, chromosome domain) identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Sub-Cell ROI Data table. The sub_cell_roi_id field uniquely identifies each ROI and links to the core table, the Cell Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined optional columns (e.g. ROI_Volume, ROI_Area). At least one such user-defined column MUST be present per submission.
--     * Slot: sub_cell_roi_id Description: Unique integer identifier for this sub-cellular structure ROI. Sub_Cell_ROI_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the Cell Data table, and the Cell/ROI Mapping table.
--     * Slot: cell_id Description: Identifier of the Cell to which this sub-cellular ROI belongs. Conditionally required when this ROI can be associated with a Cell identified as part of this experiment and reported in a dedicated Cell Data table.
--     * Slot: SubCellROITable_id Description: Autocreated FK slot
-- # Class: SubCellROITable Description: The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_subcell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of sub-cellular ROIs (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: sub_cell_roi_type Description: The type of sub-cellular structure ROI documented in this table or mapping file. It is recommended to use an EFO 'cellular_component' child term. Examples include Nucleolus, NL (nuclear lamina), NPC (nuclear pore complex), PML_body, Cajal_body, Chromosome_Domain. Written as #Sub_Cell_ROI_Type: in the file header.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: cell_type Description: The type of cells present in this dataset, expressed using an ontology term from the Experimental Factor Ontology (EFO). Examples include "Cell in tissue" or "Cell in organoid". Written as #Cell_Type: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: ROIMapping Description: A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a FOF-bas-CT experiment. Each instance corresponds to one row in the TSV data section of the FOF-CT Cell/ROI Mapping table. Exactly one of the three identifier slots (sub_cell_roi_id, cell_id, extra_cell_roi_id) must be populated per file; the choice of identifier must be consistent across all rows of a given submission. The roi_boundaries slot holds the boundary coordinates in the format specified by roi_boundaries_format in the table header. This class accepts additional user-defined optional columns.
--     * Slot: id
--     * Slot: sub_cell_roi_id Description: Unique identifier for the Sub-Cell ROI whose boundaries are described in this row. Conditionally required when this file contains sub- cellular ROI boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.
--     * Slot: cell_id Description: Unique identifier for the Cell whose boundaries are described in this row. Conditionally required when this file contains Cell boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.
--     * Slot: extra_cell_roi_id Description: Unique identifier for the extracellular structure ROI whose boundaries are described in this row. Conditionally required when this file contains Extra-Cell ROI boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.
--     * Slot: roi_boundaries Description: Boundary coordinates for this Cell or ROI, encoded in the format specified by roi_boundaries_format in the table header. For the OME ROI Polygon model, coordinates are provided as a space-separated list of "x,y" pairs (e.g. "12.5,40.2 13.1,41.0 ..."). For OBJ 3D mesh format, the field contains the vertex and face list for the boundary mesh.
--     * Slot: ROIMappingTable_id Description: Autocreated FK slot
-- # Class: ROIMappingTable Description: The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_mapping). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of ROI boundary records (recorded as data rows). This table is conditionally required whenever a Cell Data table, a Sub-Cell ROI Data table, or an Extra-Cell ROI Data table is deposited. Analogous to the MappingSet class in SSSOM.
--     * Slot: id
--     * Slot: fof_ct_version Description: Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).
--     * Slot: table_namespace Description: Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.
--     * Slot: roi_boundaries_format Description: Description of the coordinate format used to encode boundary data in the roi_boundaries column. Examples include the OME ROI Polygon model (coordinates as "x1,y1 x2,y2 ...") and the OBJ 3D mesh format (vertex and face lists). Must be sufficient for unambiguous parsing of all roi_boundaries values in this file. Written as #ROI_Boundaries_Format: in the file header.
--     * Slot: xyz_unit Description: Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Conditionally required when any location or distance metric is reported.
--     * Slot: lab_name Description: Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.
--     * Slot: experimenter_name Description: Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.
--     * Slot: experimenter_contact Description: Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.
--     * Slot: description Description: Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.
--     * Slot: cell_type Description: The type of cells present in this dataset, expressed using an ontology term from the Experimental Factor Ontology (EFO). Examples include "Cell in tissue" or "Cell in organoid". Written as #Cell_Type: in the file header.
--     * Slot: sub_cell_roi_type Description: The type of sub-cellular structure ROI documented in this table or mapping file. It is recommended to use an EFO 'cellular_component' child term. Examples include Nucleolus, NL (nuclear lamina), NPC (nuclear pore complex), PML_body, Cajal_body, Chromosome_Domain. Written as #Sub_Cell_ROI_Type: in the file header.
--     * Slot: extra_cell_roi_type Description: The type of extracellular structure ROI within which cells are embedded, expressed using an EFO 'organism part' child term (e.g. Tissue, Organoid). Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type: in the file header.
--     * Slot: time_unit Description: Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required when any time metric is reported.
--     * Slot: intensity_unit Description: Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required when any intensity metric is reported.
--     * Slot: intensity_measurement_method Description: Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required when any intensity metric is reported.
-- # Class: SpotTable_additional_tables
--     * Slot: SpotTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: LocalizationTable_additional_tables
--     * Slot: LocalizationTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: TraceTable_additional_tables
--     * Slot: TraceTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: RNASpotTable_additional_tables
--     * Slot: RNASpotTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: SpotQualityTable_additional_tables
--     * Slot: SpotQualityTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: RNASpotQualityTable_additional_tables
--     * Slot: RNASpotQualityTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: SpotBiologicalTable_additional_tables
--     * Slot: SpotBiologicalTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: RNASpotBiologicalTable_additional_tables
--     * Slot: RNASpotBiologicalTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: CellTable_additional_tables
--     * Slot: CellTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: ExtraCellROITable_additional_tables
--     * Slot: ExtraCellROITable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: SubCellROITable_additional_tables
--     * Slot: SubCellROITable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.
-- # Class: ROIMappingTable_additional_tables
--     * Slot: ROIMappingTable_id Description: Autocreated FK slot
--     * Slot: additional_tables Description: List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.

CREATE TABLE "SpotTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	genome_assembly TEXT NOT NULL,
	xyz_unit VARCHAR(6) NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	modification TEXT,
	vcf_file_name TEXT,
	vcf_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SpotTable_id" ON "SpotTable" (id);

CREATE TABLE "LocalizationTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LocalizationTable_id" ON "LocalizationTable" (id);

CREATE TABLE "TraceTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TraceTable_id" ON "TraceTable" (id);

CREATE TABLE "RNASpotTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	genome_assembly TEXT NOT NULL,
	gene_id_type TEXT NOT NULL,
	xyz_unit VARCHAR(6) NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	transcript_id_type TEXT,
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RNASpotTable_id" ON "RNASpotTable" (id);

CREATE TABLE "SpotQualityTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SpotQualityTable_id" ON "SpotQualityTable" (id);

CREATE TABLE "RNASpotQualityTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RNASpotQualityTable_id" ON "RNASpotQualityTable" (id);

CREATE TABLE "SpotBiologicalTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SpotBiologicalTable_id" ON "SpotBiologicalTable" (id);

CREATE TABLE "RNASpotBiologicalTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RNASpotBiologicalTable_id" ON "RNASpotBiologicalTable" (id);

CREATE TABLE "CellTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	cell_type TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	extra_cell_roi_type TEXT,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CellTable_id" ON "CellTable" (id);

CREATE TABLE "ExtraCellROITable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	extra_cell_roi_type TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ExtraCellROITable_id" ON "ExtraCellROITable" (id);

CREATE TABLE "SubCellROITable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	sub_cell_roi_type TEXT NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	cell_type TEXT,
	xyz_unit VARCHAR(6),
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SubCellROITable_id" ON "SubCellROITable" (id);

CREATE TABLE "ROIMappingTable" (
	id INTEGER NOT NULL,
	fof_ct_version TEXT NOT NULL,
	table_namespace TEXT NOT NULL,
	roi_boundaries_format TEXT NOT NULL,
	xyz_unit VARCHAR(6) NOT NULL,
	lab_name TEXT NOT NULL,
	experimenter_name TEXT NOT NULL,
	experimenter_contact TEXT NOT NULL,
	description TEXT NOT NULL,
	cell_type TEXT,
	sub_cell_roi_type TEXT,
	extra_cell_roi_type TEXT,
	time_unit VARCHAR(3),
	intensity_unit TEXT,
	intensity_measurement_method TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ROIMappingTable_id" ON "ROIMappingTable" (id);

CREATE TABLE "Software" (
	id INTEGER NOT NULL,
	software_title TEXT NOT NULL,
	software_type VARCHAR(15) NOT NULL,
	software_authors TEXT NOT NULL,
	software_description TEXT NOT NULL,
	software_repository TEXT NOT NULL,
	software_preferred_citation_id TEXT NOT NULL,
	"SpotTable_id" INTEGER,
	"LocalizationTable_id" INTEGER,
	"TraceTable_id" INTEGER,
	"RNASpotTable_id" INTEGER,
	"SpotQualityTable_id" INTEGER,
	"RNASpotQualityTable_id" INTEGER,
	"SpotBiologicalTable_id" INTEGER,
	"RNASpotBiologicalTable_id" INTEGER,
	"CellTable_id" INTEGER,
	"ExtraCellROITable_id" INTEGER,
	"SubCellROITable_id" INTEGER,
	"ROIMappingTable_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SpotTable_id") REFERENCES "SpotTable" (id),
	FOREIGN KEY("LocalizationTable_id") REFERENCES "LocalizationTable" (id),
	FOREIGN KEY("TraceTable_id") REFERENCES "TraceTable" (id),
	FOREIGN KEY("RNASpotTable_id") REFERENCES "RNASpotTable" (id),
	FOREIGN KEY("SpotQualityTable_id") REFERENCES "SpotQualityTable" (id),
	FOREIGN KEY("RNASpotQualityTable_id") REFERENCES "RNASpotQualityTable" (id),
	FOREIGN KEY("SpotBiologicalTable_id") REFERENCES "SpotBiologicalTable" (id),
	FOREIGN KEY("RNASpotBiologicalTable_id") REFERENCES "RNASpotBiologicalTable" (id),
	FOREIGN KEY("CellTable_id") REFERENCES "CellTable" (id),
	FOREIGN KEY("ExtraCellROITable_id") REFERENCES "ExtraCellROITable" (id),
	FOREIGN KEY("SubCellROITable_id") REFERENCES "SubCellROITable" (id),
	FOREIGN KEY("ROIMappingTable_id") REFERENCES "ROIMappingTable" (id)
);
CREATE INDEX "ix_Software_id" ON "Software" (id);

CREATE TABLE "Spot" (
	spot_id INTEGER NOT NULL,
	trace_id INTEGER NOT NULL,
	x FLOAT NOT NULL,
	y FLOAT NOT NULL,
	z FLOAT NOT NULL,
	chrom TEXT NOT NULL,
	chrom_start INTEGER NOT NULL,
	chrom_end INTEGER NOT NULL,
	sub_cell_roi_id INTEGER,
	cell_id INTEGER,
	extra_cell_roi_id INTEGER,
	"SpotTable_id" INTEGER,
	PRIMARY KEY (spot_id),
	FOREIGN KEY("SpotTable_id") REFERENCES "SpotTable" (id)
);
CREATE INDEX "ix_Spot_spot_id" ON "Spot" (spot_id);

CREATE TABLE "Localization" (
	loc_id INTEGER NOT NULL,
	spot_id INTEGER NOT NULL,
	x FLOAT NOT NULL,
	y FLOAT NOT NULL,
	z FLOAT NOT NULL,
	fluor TEXT NOT NULL,
	"LocalizationTable_id" INTEGER,
	PRIMARY KEY (loc_id),
	FOREIGN KEY("LocalizationTable_id") REFERENCES "LocalizationTable" (id)
);
CREATE INDEX "ix_Localization_loc_id" ON "Localization" (loc_id);

CREATE TABLE "Trace" (
	trace_id INTEGER NOT NULL,
	"TraceTable_id" INTEGER,
	PRIMARY KEY (trace_id),
	FOREIGN KEY("TraceTable_id") REFERENCES "TraceTable" (id)
);
CREATE INDEX "ix_Trace_trace_id" ON "Trace" (trace_id);

CREATE TABLE "RNASpot" (
	id INTEGER NOT NULL,
	rna_spot_id INTEGER NOT NULL,
	x FLOAT NOT NULL,
	y FLOAT NOT NULL,
	z FLOAT NOT NULL,
	rna_name TEXT NOT NULL,
	gene_id TEXT NOT NULL,
	trace_id INTEGER NOT NULL,
	transcript_id TEXT,
	sub_cell_roi_id INTEGER,
	cell_id INTEGER,
	extra_cell_roi_id INTEGER,
	"RNASpotTable_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RNASpotTable_id") REFERENCES "RNASpotTable" (id)
);
CREATE INDEX "ix_RNASpot_id" ON "RNASpot" (id);

CREATE TABLE "SpotQualityRecord" (
	spot_id INTEGER NOT NULL,
	"SpotQualityTable_id" INTEGER,
	PRIMARY KEY (spot_id),
	FOREIGN KEY("SpotQualityTable_id") REFERENCES "SpotQualityTable" (id)
);
CREATE INDEX "ix_SpotQualityRecord_spot_id" ON "SpotQualityRecord" (spot_id);

CREATE TABLE "RNASpotQualityRecord" (
	rna_spot_id INTEGER NOT NULL,
	"RNASpotQualityTable_id" INTEGER,
	PRIMARY KEY (rna_spot_id),
	FOREIGN KEY("RNASpotQualityTable_id") REFERENCES "RNASpotQualityTable" (id)
);
CREATE INDEX "ix_RNASpotQualityRecord_rna_spot_id" ON "RNASpotQualityRecord" (rna_spot_id);

CREATE TABLE "SpotBiologicalRecord" (
	spot_id INTEGER NOT NULL,
	"SpotBiologicalTable_id" INTEGER,
	PRIMARY KEY (spot_id),
	FOREIGN KEY("SpotBiologicalTable_id") REFERENCES "SpotBiologicalTable" (id)
);
CREATE INDEX "ix_SpotBiologicalRecord_spot_id" ON "SpotBiologicalRecord" (spot_id);

CREATE TABLE "RNASpotBiologicalRecord" (
	rna_spot_id INTEGER NOT NULL,
	"RNASpotBiologicalTable_id" INTEGER,
	PRIMARY KEY (rna_spot_id),
	FOREIGN KEY("RNASpotBiologicalTable_id") REFERENCES "RNASpotBiologicalTable" (id)
);
CREATE INDEX "ix_RNASpotBiologicalRecord_rna_spot_id" ON "RNASpotBiologicalRecord" (rna_spot_id);

CREATE TABLE "Cell" (
	cell_id INTEGER NOT NULL,
	extra_cell_roi_id INTEGER,
	"CellTable_id" INTEGER,
	PRIMARY KEY (cell_id),
	FOREIGN KEY("CellTable_id") REFERENCES "CellTable" (id)
);
CREATE INDEX "ix_Cell_cell_id" ON "Cell" (cell_id);

CREATE TABLE "ExtraCellROI" (
	extra_cell_roi_id INTEGER NOT NULL,
	"ExtraCellROITable_id" INTEGER,
	PRIMARY KEY (extra_cell_roi_id),
	FOREIGN KEY("ExtraCellROITable_id") REFERENCES "ExtraCellROITable" (id)
);
CREATE INDEX "ix_ExtraCellROI_extra_cell_roi_id" ON "ExtraCellROI" (extra_cell_roi_id);

CREATE TABLE "SubCellROI" (
	sub_cell_roi_id INTEGER NOT NULL,
	cell_id INTEGER,
	"SubCellROITable_id" INTEGER,
	PRIMARY KEY (sub_cell_roi_id),
	FOREIGN KEY("SubCellROITable_id") REFERENCES "SubCellROITable" (id)
);
CREATE INDEX "ix_SubCellROI_sub_cell_roi_id" ON "SubCellROI" (sub_cell_roi_id);

CREATE TABLE "ROIMapping" (
	id INTEGER NOT NULL,
	sub_cell_roi_id INTEGER,
	cell_id INTEGER,
	extra_cell_roi_id INTEGER,
	roi_boundaries TEXT NOT NULL,
	"ROIMappingTable_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ROIMappingTable_id") REFERENCES "ROIMappingTable" (id)
);
CREATE INDEX "ix_ROIMapping_id" ON "ROIMapping" (id);

CREATE TABLE "SpotTable_additional_tables" (
	"SpotTable_id" INTEGER,
	additional_tables VARCHAR(25),
	PRIMARY KEY ("SpotTable_id", additional_tables),
	FOREIGN KEY("SpotTable_id") REFERENCES "SpotTable" (id)
);
CREATE INDEX "ix_SpotTable_additional_tables_SpotTable_id" ON "SpotTable_additional_tables" ("SpotTable_id");
CREATE INDEX "ix_SpotTable_additional_tables_additional_tables" ON "SpotTable_additional_tables" (additional_tables);

CREATE TABLE "LocalizationTable_additional_tables" (
	"LocalizationTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("LocalizationTable_id", additional_tables),
	FOREIGN KEY("LocalizationTable_id") REFERENCES "LocalizationTable" (id)
);
CREATE INDEX "ix_LocalizationTable_additional_tables_LocalizationTable_id" ON "LocalizationTable_additional_tables" ("LocalizationTable_id");
CREATE INDEX "ix_LocalizationTable_additional_tables_additional_tables" ON "LocalizationTable_additional_tables" (additional_tables);

CREATE TABLE "TraceTable_additional_tables" (
	"TraceTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("TraceTable_id", additional_tables),
	FOREIGN KEY("TraceTable_id") REFERENCES "TraceTable" (id)
);
CREATE INDEX "ix_TraceTable_additional_tables_TraceTable_id" ON "TraceTable_additional_tables" ("TraceTable_id");
CREATE INDEX "ix_TraceTable_additional_tables_additional_tables" ON "TraceTable_additional_tables" (additional_tables);

CREATE TABLE "RNASpotTable_additional_tables" (
	"RNASpotTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("RNASpotTable_id", additional_tables),
	FOREIGN KEY("RNASpotTable_id") REFERENCES "RNASpotTable" (id)
);
CREATE INDEX "ix_RNASpotTable_additional_tables_additional_tables" ON "RNASpotTable_additional_tables" (additional_tables);
CREATE INDEX "ix_RNASpotTable_additional_tables_RNASpotTable_id" ON "RNASpotTable_additional_tables" ("RNASpotTable_id");

CREATE TABLE "SpotQualityTable_additional_tables" (
	"SpotQualityTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("SpotQualityTable_id", additional_tables),
	FOREIGN KEY("SpotQualityTable_id") REFERENCES "SpotQualityTable" (id)
);
CREATE INDEX "ix_SpotQualityTable_additional_tables_additional_tables" ON "SpotQualityTable_additional_tables" (additional_tables);
CREATE INDEX "ix_SpotQualityTable_additional_tables_SpotQualityTable_id" ON "SpotQualityTable_additional_tables" ("SpotQualityTable_id");

CREATE TABLE "RNASpotQualityTable_additional_tables" (
	"RNASpotQualityTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("RNASpotQualityTable_id", additional_tables),
	FOREIGN KEY("RNASpotQualityTable_id") REFERENCES "RNASpotQualityTable" (id)
);
CREATE INDEX "ix_RNASpotQualityTable_additional_tables_RNASpotQualityTable_id" ON "RNASpotQualityTable_additional_tables" ("RNASpotQualityTable_id");
CREATE INDEX "ix_RNASpotQualityTable_additional_tables_additional_tables" ON "RNASpotQualityTable_additional_tables" (additional_tables);

CREATE TABLE "SpotBiologicalTable_additional_tables" (
	"SpotBiologicalTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("SpotBiologicalTable_id", additional_tables),
	FOREIGN KEY("SpotBiologicalTable_id") REFERENCES "SpotBiologicalTable" (id)
);
CREATE INDEX "ix_SpotBiologicalTable_additional_tables_additional_tables" ON "SpotBiologicalTable_additional_tables" (additional_tables);
CREATE INDEX "ix_SpotBiologicalTable_additional_tables_SpotBiologicalTable_id" ON "SpotBiologicalTable_additional_tables" ("SpotBiologicalTable_id");

CREATE TABLE "RNASpotBiologicalTable_additional_tables" (
	"RNASpotBiologicalTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("RNASpotBiologicalTable_id", additional_tables),
	FOREIGN KEY("RNASpotBiologicalTable_id") REFERENCES "RNASpotBiologicalTable" (id)
);
CREATE INDEX "ix_RNASpotBiologicalTable_additional_tables_RNASpotBiologicalTable_id" ON "RNASpotBiologicalTable_additional_tables" ("RNASpotBiologicalTable_id");
CREATE INDEX "ix_RNASpotBiologicalTable_additional_tables_additional_tables" ON "RNASpotBiologicalTable_additional_tables" (additional_tables);

CREATE TABLE "CellTable_additional_tables" (
	"CellTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("CellTable_id", additional_tables),
	FOREIGN KEY("CellTable_id") REFERENCES "CellTable" (id)
);
CREATE INDEX "ix_CellTable_additional_tables_additional_tables" ON "CellTable_additional_tables" (additional_tables);
CREATE INDEX "ix_CellTable_additional_tables_CellTable_id" ON "CellTable_additional_tables" ("CellTable_id");

CREATE TABLE "ExtraCellROITable_additional_tables" (
	"ExtraCellROITable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("ExtraCellROITable_id", additional_tables),
	FOREIGN KEY("ExtraCellROITable_id") REFERENCES "ExtraCellROITable" (id)
);
CREATE INDEX "ix_ExtraCellROITable_additional_tables_additional_tables" ON "ExtraCellROITable_additional_tables" (additional_tables);
CREATE INDEX "ix_ExtraCellROITable_additional_tables_ExtraCellROITable_id" ON "ExtraCellROITable_additional_tables" ("ExtraCellROITable_id");

CREATE TABLE "SubCellROITable_additional_tables" (
	"SubCellROITable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("SubCellROITable_id", additional_tables),
	FOREIGN KEY("SubCellROITable_id") REFERENCES "SubCellROITable" (id)
);
CREATE INDEX "ix_SubCellROITable_additional_tables_additional_tables" ON "SubCellROITable_additional_tables" (additional_tables);
CREATE INDEX "ix_SubCellROITable_additional_tables_SubCellROITable_id" ON "SubCellROITable_additional_tables" ("SubCellROITable_id");

CREATE TABLE "ROIMappingTable_additional_tables" (
	"ROIMappingTable_id" INTEGER,
	additional_tables VARCHAR(25) NOT NULL,
	PRIMARY KEY ("ROIMappingTable_id", additional_tables),
	FOREIGN KEY("ROIMappingTable_id") REFERENCES "ROIMappingTable" (id)
);
CREATE INDEX "ix_ROIMappingTable_additional_tables_ROIMappingTable_id" ON "ROIMappingTable_additional_tables" ("ROIMappingTable_id");
CREATE INDEX "ix_ROIMappingTable_additional_tables_additional_tables" ON "ROIMappingTable_additional_tables" (additional_tables);
