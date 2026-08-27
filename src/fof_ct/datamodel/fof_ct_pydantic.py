from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'fof_ct',
     'default_range': 'string',
     'description': 'Root schema for the FISH Omics Format for Chromatin Tracing '
                    '(FOF-CT). Covers both modalities: FOF-bas-CT (ball-and-stick, '
                    'tables 1–12) and FOF-vol-CT (volumetric, tables 13–15). '
                    'Imports all fifteen table schemas that together constitute '
                    'the complete FOF-CT data model. Each table schema in turn '
                    'imports fof_bas_ct_common for shared slots, the Software '
                    'class, and enumerations.',
     'id': 'https://w3id.org/fof-ct',
     'imports': ['linkml:types',
                 'fof_bas_ct_common',
                 'fof_bas_ct_core',
                 'fof_bas_ct_demultiplexing',
                 'fof_bas_ct_trace',
                 'fof_bas_ct_rna',
                 'fof_bas_ct_quality',
                 'fof_bas_ct_rna_quality',
                 'fof_bas_ct_bio',
                 'fof_bas_ct_rna_bio',
                 'fof_bas_ct_cell',
                 'fof_bas_ct_extracell',
                 'fof_bas_ct_subcell',
                 'fof_bas_ct_mapping',
                 'fof_vol_ct_core',
                 'fof_vol_ct_quality',
                 'fof_vol_ct_undecoded'],
     'license': 'MIT',
     'name': 'fof_ct',
     'prefixes': {'fof_ct': {'prefix_prefix': 'fof_ct',
                             'prefix_reference': 'https://w3id.org/fof-ct/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://4dn-dcic.github.io/fof-ct',
                  'https://fish-omics-format.readthedocs.io/'],
     'source_file': 'src/fof_ct/schema/fof_ct.yaml',
     'title': 'FISH Omics Format for Chromatin Tracing (FOF-CT)'} )

class XYZUnitEnum(str, Enum):
    """
    Allowed units for X, Y, Z spatial coordinates or distances.
    """
    nm = "nm"
    """
    Nanometres
    """
    micron = "micron"
    """
    Micrometres. Use 'micron' rather than the Greek symbol μm to avoid encoding issues.
    """
    mm = "mm"
    """
    Millimetres
    """


class TimeUnitEnum(str, Enum):
    """
    Allowed units for time intervals.
    """
    s = "s"
    """
    Seconds (SI base unit)
    """
    sec = "sec"
    """
    Seconds (alternative spelling accepted by FOF-CT)
    """
    ms = "ms"
    """
    Milliseconds
    """
    msec = "msec"
    """
    Milliseconds (alternative spelling accepted by FOF-CT)
    """
    min = "min"
    """
    Minutes
    """
    hr = "hr"
    """
    Hours
    """


class SoftwareTypeEnum(str, Enum):
    """
    Allowed functional categories for software tools (per the FOF-CT RTD "Allowable value lists" table for Software_Type).
    """
    Distance_Calculation = "Distance Calculation"
    """
    Distance calculation software
    """
    DriftCorrection = "DriftCorrection"
    """
    Drift correction software
    """
    Precision_Assessment = "Precision Assessment"
    """
    Localization/tracing precision assessment software
    """
    Segmentation = "Segmentation"
    """
    Image segmentation software
    """
    Single_Molecule_Localization = "Single Molecule Localization"
    """
    Single-molecule localization software (FOF-vol-CT)
    """
    SpotLoc = "SpotLoc"
    """
    Spot localisation software
    """
    SpotLocPLUS_SIGNTracing = "SpotLoc+Tracing"
    """
    Combined spot localisation and tracing software
    """
    Tracing = "Tracing"
    """
    Chromatin tracing software
    """
    Other = "Other"
    """
    Other software type
    """


class TableNamespaceEnum(str, Enum):
    """
    Allowed namespace identifiers for FOF-CT tables that may be listed in the additional_tables field. Note: per the FOF-CT RTD, the three FOF-vol-CT-exclusive namespaces (vol_core, vol_quality, undecoded) intentionally omit the 4dn_ prefix used by the 12 shared tables, to reflect the format's continued stewardship by the broader community beyond 4DN.
    """
    number_4dn_FOF_CT_core = "4dn_FOF-CT_core"
    """
    DNA-Spot/Trace Data core table (table 1)
    """
    number_4dn_FOF_CT_demultiplexing = "4dn_FOF-CT_demultiplexing"
    """
    Spot Demultiplexing table (table 2)
    """
    number_4dn_FOF_CT_trace = "4dn_FOF-CT_trace"
    """
    Trace Data table (table 3)
    """
    number_4dn_FOF_CT_rna = "4dn_FOF-CT_rna"
    """
    RNA Spot Data table (table 4)
    """
    number_4dn_FOF_CT_quality = "4dn_FOF-CT_quality"
    """
    Spot Quality table (table 5)
    """
    number_4dn_FOF_CT_rna_quality = "4dn_FOF-CT_rna_quality"
    """
    RNA Spot Quality table (table 6)
    """
    number_4dn_FOF_CT_bio = "4dn_FOF-CT_bio"
    """
    Spot Biological Data table (table 7)
    """
    number_4dn_FOF_CT_rna_bio = "4dn_FOF-CT_rna_bio"
    """
    RNA Spot Biological Data table (table 8)
    """
    number_4dn_FOF_CT_cell = "4dn_FOF-CT_cell"
    """
    Cell Data table (table 9)
    """
    number_4dn_FOF_CT_extracell = "4dn_FOF-CT_extracell"
    """
    Extra-Cell ROI Data table (table 10)
    """
    number_4dn_FOF_CT_subcell = "4dn_FOF-CT_subcell"
    """
    Sub-Cell ROI Data table (table 11)
    """
    number_4dn_FOF_CT_mapping = "4dn_FOF-CT_mapping"
    """
    Cell/ROI Mapping table (table 12)
    """
    FOF_CT_vol_core = "FOF-CT_vol_core"
    """
    SM Localization Data table — FOF-vol-CT (table 13). No 4dn_ prefix (see enum-level note).
    """
    FOF_CT_vol_quality = "FOF-CT_vol_quality"
    """
    SM Localization Quality table — FOF-vol-CT (table 14). No 4dn_ prefix (see enum-level note).
    """
    FOF_CT_undecoded = "FOF-CT_undecoded"
    """
    Undecoded SM Localization Data table — FOF-vol-CT (table 15). No 4dn_ prefix (see enum-level note).
    """


class ROIBoundariesFormatTypeEnum(str, Enum):
    """
    Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI Mapping table (per the FOF-CT RTD "Allowable value lists" table). Default value is OME_Polygon.
    """
    OME_Polygon = "OME_Polygon"
    """
    OME ROI data model, polygon representation (default).
    """
    OME_Mask = "OME_Mask"
    """
    OME ROI data model, mask representation.
    """
    Mesh_OBJ = "Mesh_OBJ"
    """
    3D mesh boundary described using the Wavefront OBJ format.
    """
    Mesh_STL = "Mesh_STL"
    """
    3D mesh boundary described using the STL format.
    """
    Mesh_PLY = "Mesh_PLY"
    """
    3D mesh boundary described using the PLY format.
    """
    GeoJSON = "GeoJSON"
    """
    Boundary described using the GeoJSON format.
    """
    WKT = "WKT"
    """
    Boundary described using Well-Known Text.
    """
    Label_Mask_Image = "Label_Mask_Image"
    """
    Boundary described as a labeled mask image.
    """
    Other = "Other"
    """
    Any other boundary format. When used, ROI_Boundaries_Format_Description becomes mandatory.
    """



class Software(ConfiguredBaseModel):
    """
    Provenance metadata for a single software tool used to produce or process data in a FOF-CT table. If more than one tool was used, a separate Software entry must be provided for each. Written as a repeating block of #Software_* fields in the file header.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/common'})

    software_title: str = Field(default=..., description="""Name of the software tool. Written as #Software_Title:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'], 'examples': [{'value': 'ChrTracer3'}]} })
    software_type: SoftwareTypeEnum = Field(default=..., description="""Functional category of the software tool. Written as #Software_Type:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'], 'examples': [{'value': 'SpotLoc+Tracing'}]} })
    software_authors: str = Field(default=..., description="""Author name(s) in 'Surname, Firstname' format, multiple authors separated by semicolons. Written as #Software_Authors:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'],
         'examples': [{'value': 'Mateo, LJ; Sinnott-Armstrong, N; Boettiger, AN'}]} })
    software_description: str = Field(default=..., description="""Free-text description of the algorithm used, sufficient to guarantee reproducibility. Written as #Software_Description:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software']} })
    software_parameters: str = Field(default=..., description="""Free-text description of the input parameters used for the specific analysis run performed using this Software. Should provide sufficient detail about the analysis parameters used to guarantee interpretation and reproducibility (e.g. input parameters used for assessing the precision of single molecule localization or drift correction in X, Y and Z). Written as #Software_Parameters:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'],
         'examples': [{'value': 'X_Loc_Precision Parameter = 1.01'}]} })
    software_repository: str = Field(default=..., description="""URL of the repository where the software release can be obtained. Written as #Software_Repository:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'],
         'examples': [{'value': 'https://github.com/BoettigerLab/ORCA-public'}]} })
    software_preferred_citation_id: str = Field(default=..., description="""Unique identifier (DOI, PMCID, ArXiv ID, etc.) for the primary publication describing this software. Written as #Software_PreferredCitationID:.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Software'],
         'examples': [{'value': 'https://doi.org/10.1038/s41596-020-00478-x'}]} })


class LocalizationMixin(ConfiguredBaseModel):
    """
    Mixin capturing the shared concept of a single localization event across FOF-CT modalities. Used by Localization (demultiplexing), SMLocalization (vol_core), and UndecodedLocalization (undecoded). All three classes represent the same atomic measurement unit — the sub-pixel position of a detected fluorescence emission event — but differ in context, mandatory columns, and table role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/common', 'mixin': True})

    loc_id: Optional[int] = Field(default=None, description="""A unique integer identifier for an individual localization event. Loc_ID values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing, SM Localization Data, SM Localization Quality, and Undecoded SM Localization tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SMLocalizationQualityRecord'],
         'examples': [{'value': '1'}]} })
    x: Optional[float] = Field(default=None, description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: Optional[float] = Field(default=None, description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: Optional[float] = Field(default=None, description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })


class SpotMixin(ConfiguredBaseModel):
    """
    Mixin capturing slots shared between DNA Spots (Spot, core table) and RNA Spots (RNASpot, RNA Spot Data table): 3D position and the optional spatial-context cross-references. Does NOT include the identifier slot, since Spot and RNASpot use different RTD-aligned identifier column names (Spot_ID vs. RNA_Spot_ID) and LinkML cannot rename an inherited identifier slot per subclass.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/common', 'mixin': True})

    x: Optional[float] = Field(default=None, description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: Optional[float] = Field(default=None, description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: Optional[float] = Field(default=None, description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })
    sub_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Unique identifier for a Cell. Links to the Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class Spot(SpotMixin):
    """
    A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT core table and represents a specific genomic target sequence localised in 3D space and assigned to a chromatin Trace.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/core',
         'mixins': ['SpotMixin'],
         'slot_usage': {'chrom': {'name': 'chrom', 'required': True},
                        'chrom_end': {'name': 'chrom_end', 'required': True},
                        'chrom_start': {'name': 'chrom_start', 'required': True},
                        'spot_id': {'identifier': True,
                                    'inlined': False,
                                    'name': 'spot_id',
                                    'range': 'integer',
                                    'required': True},
                        'trace_id': {'name': 'trace_id', 'required': True},
                        'x': {'name': 'x', 'required': True},
                        'y': {'name': 'y', 'required': True},
                        'z': {'name': 'z', 'required': True}}})

    spot_id: int = Field(default=..., description="""Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table. In FOF-vol-CT (table 13, SM Localization Data), this same Spot_ID concept is derived by clustering Single-Molecule (SM) Localization events rather than by direct optical detection, and every SM Localization event MUST report its associated Spot_ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot',
                       'Localization',
                       'SpotQualityRecord',
                       'SpotBiologicalRecord',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    trace_id: int = Field(default=..., description="""Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily) in the FOF-vol-CT SM Localization Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'Trace', 'RNASpot', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    chrom: str = Field(default=..., description="""Chromosome name/identifier using BED (Browser Extensible Data) convention (e.g., chr3, chrY, chr2_random). Used by both the core (Spot) and vol_core (SMLocalization) tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'],
         'examples': [{'value': 'chr3'}, {'value': 'chrY'}, {'value': 'chr2_random'}]} })
    chrom_start: int = Field(default=..., description="""0-based start coordinate on the chromosome for the genomic target sequence, following BED convention. Used by both the core (Spot) and vol_core (SMLocalization) tables.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'], 'examples': [{'value': '0'}]} })
    chrom_end: int = Field(default=..., description="""Non-inclusive end coordinate on the chromosome for the genomic target sequence, following BED convention. Used by both the core (Spot) and vol_core (SMLocalization) tables.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'], 'examples': [{'value': '1000'}]} })
    x: float = Field(default=..., description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: float = Field(default=..., description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: float = Field(default=..., description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })
    sub_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Unique identifier for a Cell. Links to the Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class SpotTable(ConfiguredBaseModel):
    """
    The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_core). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/core',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'genome_assembly': {'name': 'genome_assembly',
                                            'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'name': 'softwares', 'required': True},
                        'spots': {'name': 'spots', 'required': True},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_core',
                                            'name': 'table_namespace',
                                            'required': True},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_core"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_core'} })
    genome_assembly: str = Field(default=..., description="""Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'RNASpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'GRCh38'},
                      {'value': 'custom-build:GRCm38+pJT039(insertion)'}]} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    spots: list[Spot] = Field(default=..., description="""The complete collection of Spots constituting this dataset. Each Spot corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'SpotTable', 'domain_of': ['SpotTable']} })
    modification: Optional[str] = Field(default=None, description="""Description of the nature and genomic position of a DNA insertion or deletion in the genome under study. Conditionally required (content- triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##Modification= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'pJT039:chr3(insertion 0001-2500)'}]} })
    vcf_file_name: Optional[str] = Field(default=None, description="""Name of the Variant Call Format (VCF) file that must be submitted alongside the dataset to describe the genome insertion or deletion. Conditionally required (content-triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_File_Name= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'pJT039:chr3.vcf'}]} })
    vcf_version: Optional[str] = Field(default=None, description="""Version of the VCF format used for the accompanying VCF file. Conditionally required (content-triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_Version= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'v4.2'}]} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class Localization(LocalizationMixin):
    """
    A single individual localisation event contributing to the final position of a bright DNA Spot in a multiplexed FISH experiment (e.g. MERFISH). Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Spot Demultiplexing table. The spot_id field links each Localization to its parent Spot in the core table (or RNA Spot Data table). This class accepts additional user-defined optional columns (e.g. Hyb, Brightness, Fit_Quality).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/demultiplexing',
         'mixins': ['LocalizationMixin'],
         'slot_usage': {'channel_name': {'name': 'channel_name', 'required': True},
                        'fluorophore_name': {'name': 'fluorophore_name',
                                             'required': True},
                        'loc_id': {'identifier': True,
                                   'name': 'loc_id',
                                   'required': True},
                        'spot_id': {'name': 'spot_id', 'required': True},
                        'x': {'name': 'x', 'required': True},
                        'y': {'name': 'y', 'required': True},
                        'z': {'name': 'z', 'required': True}}})

    spot_id: int = Field(default=..., description="""Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table. In FOF-vol-CT (table 13, SM Localization Data), this same Spot_ID concept is derived by clustering Single-Molecule (SM) Localization events rather than by direct optical detection, and every SM Localization event MUST report its associated Spot_ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot',
                       'Localization',
                       'SpotQualityRecord',
                       'SpotBiologicalRecord',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    channel_name: str = Field(default=..., description="""The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': '510/25'}, {'value': '695/81'}]} })
    fluorophore_name: str = Field(default=..., description="""The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': 'AlexaFluor_488'}, {'value': 'Cy5'}]} })
    loc_id: int = Field(default=..., description="""A unique integer identifier for an individual localization event. Loc_ID values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing, SM Localization Data, SM Localization Quality, and Undecoded SM Localization tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SMLocalizationQualityRecord'],
         'examples': [{'value': '1'}]} })
    x: float = Field(default=..., description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: float = Field(default=..., description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: float = Field(default=..., description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })


class DemultiplexingTable(ConfiguredBaseModel):
    """
    The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_demultiplexing). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of Localization events (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended for multiplexed FISH experiments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/demultiplexing',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'localizations': {'name': 'localizations', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': True},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_demultiplexing',
                                            'name': 'table_namespace',
                                            'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_demultiplexing"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_demultiplexing'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    localizations: list[Localization] = Field(default=..., description="""The complete collection of Localization events constituting this dataset. Each Localization corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'DemultiplexingTable', 'domain_of': ['DemultiplexingTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class Trace(ConfiguredBaseModel):
    """
    A single chromatin Trace representing global properties associated with an entire polymeric trace rather than with individual Spots. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Trace Data table. The trace_id links each Trace to the core table and to the RNA Spot Data table. IMPORTANT: this class MUST contain at least one user-defined optional column describing trace-level properties (e.g., Allele, RNA_Expression, Lamina_Distance). User-defined columns are accommodated via open schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/trace',
         'slot_usage': {'trace_id': {'identifier': True,
                                     'inlined': False,
                                     'name': 'trace_id',
                                     'range': 'integer',
                                     'required': True}}})

    trace_id: int = Field(default=..., description="""Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily) in the FOF-vol-CT SM Localization Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'Trace', 'RNASpot', 'SMLocalization'],
         'examples': [{'value': '1'}]} })


class TraceTable(ConfiguredBaseModel):
    """
    The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of Traces (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended when trace-level properties are recorded.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/trace',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_trace',
                                            'name': 'table_namespace',
                                            'required': True},
                        'traces': {'name': 'traces', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_trace"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_trace'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    traces: list[Trace] = Field(default=..., description="""The complete collection of Traces constituting this dataset. Each Trace corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'TraceTable', 'domain_of': ['TraceTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class RNASpot(SpotMixin):
    """
    A single detected RNA bright Spot corresponding to one RNA transcript location detected alongside Chromatin Tracing. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT RNA Spot Data table. The rna_spot_id links each RNASpot to the RNA Quality and RNA Biological Data tables; the trace_id links this RNA Spot to a DNA chromatin Trace in the core table and Trace Data table. This table's column list is fixed by the RTD (rna_columns.csv defines no Optional_Column placeholders); it does not accept additional user-defined columns.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/rna',
         'mixins': ['SpotMixin'],
         'slot_usage': {'gene_id': {'name': 'gene_id', 'required': True},
                        'rna_name': {'name': 'rna_name', 'required': True},
                        'rna_spot_id': {'identifier': True,
                                        'inlined': False,
                                        'name': 'rna_spot_id',
                                        'range': 'integer',
                                        'required': True},
                        'trace_id': {'name': 'trace_id', 'required': True},
                        'x': {'name': 'x', 'required': True},
                        'y': {'name': 'y', 'required': True},
                        'z': {'name': 'z', 'required': True}}})

    rna_spot_id: int = Field(default=..., description="""Unique identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RNASpot', 'RNASpotQualityRecord', 'RNASpotBiologicalRecord'],
         'examples': [{'value': '1'}]} })
    rna_name: str = Field(default=..., description="""Official name of the gene from which the targeted RNA is transcribed (e.g. ACTB, GAPDH). Should follow HGNC (human) or MGI (mouse) gene nomenclature.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpot',
         'domain_of': ['RNASpot'],
         'examples': [{'value': 'ACTB'}, {'value': 'GAPDH'}]} })
    gene_id: str = Field(default=..., description="""Official gene identifier corresponding to rna_name. The type of identifier used (e.g. Ensembl gene ID, NCBI Gene ID) must be declared in the gene_id_type header field.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpot',
         'domain_of': ['RNASpot'],
         'examples': [{'value': 'ENSG00000075624'}, {'value': 'ENSG00000111640'}]} })
    trace_id: int = Field(default=..., description="""Unique identifier for a chromatin Trace. Used as a primary key in the Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily) in the FOF-vol-CT SM Localization Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'Trace', 'RNASpot', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    transcript_id: Optional[str] = Field(default=None, description="""Official transcript identifier for the specific transcript targeted by the FISH probe. Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. The type of identifier used must be declared in the transcript_id_type header field.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpot',
         'domain_of': ['RNASpot'],
         'examples': [{'value': 'ENST00000331789'}, {'value': 'NM_001101.5'}]} })
    x: float = Field(default=..., description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: float = Field(default=..., description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: float = Field(default=..., description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })
    sub_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Unique identifier for a Cell. Links to the Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class RNASpotTable(ConfiguredBaseModel):
    """
    The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with the full collection of RNA Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is optional but recommended when RNA data are collected alongside Chromatin Tracing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/rna',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'gene_id_type': {'name': 'gene_id_type', 'required': True},
                        'genome_assembly': {'name': 'genome_assembly',
                                            'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'rna_spots': {'name': 'rna_spots', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': True},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_rna',
                                            'name': 'table_namespace',
                                            'required': True},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_rna"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_rna'} })
    genome_assembly: str = Field(default=..., description="""Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'RNASpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'GRCh38'},
                      {'value': 'custom-build:GRCm38+pJT039(insertion)'}]} })
    gene_id_type: str = Field(default=..., description="""Type of gene identifier used in the gene_id column (e.g. Ensembl_V38, NCBI_Gene). Written as ##Gene_ID_Type= in the file header.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpotTable',
         'domain_of': ['RNASpotTable'],
         'examples': [{'value': 'Ensembl_V38'}, {'value': 'NCBI_Gene'}]} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    transcript_id_type: Optional[str] = Field(default=None, description="""Type of transcript identifier used in the transcript_id column (e.g. Ensembl_V38, RefSeq). Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. Written as ##Transcript_ID_Type= in the file header.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpotTable',
         'domain_of': ['RNASpotTable'],
         'examples': [{'value': 'Ensembl_V38'}, {'value': 'RefSeq'}]} })
    rna_spots: list[RNASpot] = Field(default=..., description="""The complete collection of RNA Spots constituting this dataset. Each RNASpot corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpotTable', 'domain_of': ['RNASpotTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class SpotQualityRecord(ConfiguredBaseModel):
    """
    A single row in the Spot Quality table. Each instance captures one or more quality metrics for a specific DNA bright Spot identified by Spot_ID. At least one user-defined quality metric column MUST be present; users declare these via #^ header lines.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/quality',
         'slot_usage': {'centroid_intensity': {'name': 'centroid_intensity',
                                               'required': False},
                        'channel_name': {'name': 'channel_name', 'required': True},
                        'fluorophore_name': {'name': 'fluorophore_name',
                                             'required': True},
                        'goodness_of_fit': {'name': 'goodness_of_fit',
                                            'required': False},
                        'peak_intensity': {'name': 'peak_intensity', 'required': False},
                        'photon_count': {'description': 'Optional standardised name '
                                                        'for photon count',
                                         'name': 'photon_count',
                                         'required': False},
                        'raw_x': {'name': 'raw_x', 'required': False},
                        'raw_y': {'name': 'raw_y', 'required': False},
                        'raw_z': {'name': 'raw_z', 'required': False},
                        'spot_id': {'description': 'Unique identifier for the DNA '
                                                   'bright Spot to which these quality '
                                                   'metrics belong. Links to the '
                                                   'corresponding Spot record in the '
                                                   'core table (table 1). Must be '
                                                   'unique within this table.',
                                    'identifier': True,
                                    'name': 'spot_id',
                                    'required': True},
                        'x_chromatic_shift': {'name': 'x_chromatic_shift',
                                              'required': False},
                        'x_drift': {'name': 'x_drift', 'required': False},
                        'x_loc_error': {'name': 'x_loc_error', 'required': False},
                        'x_precision': {'description': 'Recommended: metric for X '
                                                       'localization precision',
                                        'name': 'x_precision',
                                        'required': False},
                        'y_chromatic_shift': {'name': 'y_chromatic_shift',
                                              'required': False},
                        'y_drift': {'name': 'y_drift', 'required': False},
                        'y_loc_error': {'name': 'y_loc_error', 'required': False},
                        'y_precision': {'name': 'y_precision', 'required': False},
                        'z_chromatic_shift': {'name': 'z_chromatic_shift',
                                              'required': False},
                        'z_drift': {'name': 'z_drift', 'required': False},
                        'z_loc_error': {'name': 'z_loc_error', 'required': False},
                        'z_precision': {'name': 'z_precision', 'required': False}}})

    spot_id: int = Field(default=..., description="""Unique identifier for the DNA bright Spot to which these quality metrics belong. Links to the corresponding Spot record in the core table (table 1). Must be unique within this table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot',
                       'Localization',
                       'SpotQualityRecord',
                       'SpotBiologicalRecord',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    channel_name: str = Field(default=..., description="""The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': '510/25'}, {'value': '695/81'}]} })
    fluorophore_name: str = Field(default=..., description="""The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': 'AlexaFluor_488'}, {'value': 'Cy5'}]} })
    x_precision: Optional[float] = Field(default=None, description="""Recommended: metric for X localization precision""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    y_precision: Optional[float] = Field(default=None, description="""Metric quantifying the precision of the Y-axis localization estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Written as the reserved Y_Loc_Precision column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    z_precision: Optional[float] = Field(default=None, description="""Metric quantifying the precision of the Z-axis localization estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Written as the reserved Z_Loc_Precision column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    photon_count: Optional[int] = Field(default=None, description="""Optional standardised name for photon count""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1500'}]} })
    goodness_of_fit: Optional[float] = Field(default=None, description="""Metric quantifying how well the fitted model matches the observed signal (e.g. chi-squared, R-squared). Reserved, conditionally-required column name (Goodness_of_Fit) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.95'}]} })
    centroid_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the centroid pixel of the Spot / localization. Reserved, conditionally-required column name (Centroid_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '2500.0'}]} })
    peak_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the brightest pixel within the Spot / localization boundary. Reserved, conditionally-required column name (Peak_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '3200.0'}]} })
    raw_x: Optional[float] = Field(default=None, description="""X coordinate before any post-processing corrections (drift correction, chromatic correction, etc.). Same unit as X. Reserved, conditionally-required column name (Raw_X) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '14.30'}]} })
    raw_y: Optional[float] = Field(default=None, description="""Y coordinate before any post-processing corrections. Same unit as Y. Reserved, conditionally-required column name (Raw_Y) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '41.20'}]} })
    raw_z: Optional[float] = Field(default=None, description="""Z coordinate before any post-processing corrections. Same unit as Z. Reserved, conditionally-required column name (Raw_Z) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1.10'}]} })
    x_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the X coordinate. Same unit as X. Reserved, conditionally-required column name (X_Drift) in the Spot Quality and RNA Spot Quality tables. Not part of the reserved vocabulary of the SM Localization Quality table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.13'}]} })
    y_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Drift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.23'}]} })
    z_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Drift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.13'}]} })
    x_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the X coordinate. Same unit as X. Reserved, conditionally-required column name (X_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.05'}]} })
    y_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.04'}]} })
    z_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    x_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the X coordinate (e.g. standard deviation of repeated measurements). Same unit as X. Reserved, conditionally-required column name (X_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    y_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    z_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.05'}]} })


class SpotQualityTable(ConfiguredBaseModel):
    """
    The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of SpotQualityRecord rows. Submission of this table is optional but recommended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/quality',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'description': 'Method used '
                                                                        'to perform '
                                                                        'intensity '
                                                                        'measurements. '
                                                                        'Conditionally '
                                                                        'required when '
                                                                        'any intensity '
                                                                        'metric is '
                                                                        'present. '
                                                                        'Written as '
                                                                        '#Intensity_Measurement_Method: '
                                                                        'in the file '
                                                                        'header.',
                                                         'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'description': 'Unit used for any intensity '
                                                          'metric reported in '
                                                          'user-defined columns. '
                                                          'Conditionally required when '
                                                          'any such metric is present. '
                                                          'Written as '
                                                          '##Intensity_Unit= in the '
                                                          'file header.',
                                           'name': 'intensity_unit',
                                           'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'description': 'One or more Software entries '
                                                     'documenting every tool used to '
                                                     'produce or process data in this '
                                                     'table. Required only when '
                                                     'software was used; omit the '
                                                     'block entirely if no software '
                                                     'was applied. Written as '
                                                     'repeating #Software_* blocks in '
                                                     'the file header.',
                                      'name': 'softwares',
                                      'required': False},
                        'spot_quality_records': {'name': 'spot_quality_records',
                                                 'required': True},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'4dn_FOF-CT_quality'. "
                                                           'Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': '4dn_FOF-CT_quality',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'description': 'Unit used for any time metric '
                                                     'reported in user-defined '
                                                     'columns. Conditionally required '
                                                     'when any such metric is present. '
                                                     'Written as ##Time_Unit= in the '
                                                     'file header.',
                                      'name': 'time_unit',
                                      'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_quality"] = Field(default=..., description="""Identifier for this table type. Must always be '4dn_FOF-CT_quality'. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_quality'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Required only when software was used; omit the block entirely if no software was applied. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    spot_quality_records: list[SpotQualityRecord] = Field(default=..., description="""The complete collection of SpotQualityRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined quality metric column.""", json_schema_extra = { "linkml_meta": {'domain': 'SpotQualityTable', 'domain_of': ['SpotQualityTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class RNASpotQualityRecord(ConfiguredBaseModel):
    """
    A single row in the RNA Spot Quality table. Each instance captures one or more quality metrics for a specific RNA bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the dataset, linking to the corresponding record in the RNA Spot Data table (table 4). RNA_Spot_ID, Channel and Fluor are mandatory; all other reserved quality-metric columns are conditionally required (the same reserved vocabulary as the Spot Quality table) or fully free-form; users declare the latter via #^ header lines.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/rna_quality',
         'slot_usage': {'centroid_intensity': {'name': 'centroid_intensity',
                                               'required': False},
                        'channel_name': {'name': 'channel_name', 'required': True},
                        'fluorophore_name': {'name': 'fluorophore_name',
                                             'required': True},
                        'goodness_of_fit': {'name': 'goodness_of_fit',
                                            'required': False},
                        'peak_intensity': {'name': 'peak_intensity', 'required': False},
                        'photon_count': {'name': 'photon_count', 'required': False},
                        'raw_x': {'name': 'raw_x', 'required': False},
                        'raw_y': {'name': 'raw_y', 'required': False},
                        'raw_z': {'name': 'raw_z', 'required': False},
                        'rna_spot_id': {'identifier': True,
                                        'name': 'rna_spot_id',
                                        'required': True},
                        'x_chromatic_shift': {'name': 'x_chromatic_shift',
                                              'required': False},
                        'x_drift': {'name': 'x_drift', 'required': False},
                        'x_loc_error': {'name': 'x_loc_error', 'required': False},
                        'x_precision': {'name': 'x_precision', 'required': False},
                        'y_chromatic_shift': {'name': 'y_chromatic_shift',
                                              'required': False},
                        'y_drift': {'name': 'y_drift', 'required': False},
                        'y_loc_error': {'name': 'y_loc_error', 'required': False},
                        'y_precision': {'name': 'y_precision', 'required': False},
                        'z_chromatic_shift': {'name': 'z_chromatic_shift',
                                              'required': False},
                        'z_drift': {'name': 'z_drift', 'required': False},
                        'z_loc_error': {'name': 'z_loc_error', 'required': False},
                        'z_precision': {'name': 'z_precision', 'required': False}}})

    rna_spot_id: int = Field(default=..., description="""Unique identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RNASpot', 'RNASpotQualityRecord', 'RNASpotBiologicalRecord'],
         'examples': [{'value': '1'}]} })
    channel_name: str = Field(default=..., description="""The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': '510/25'}, {'value': '695/81'}]} })
    fluorophore_name: str = Field(default=..., description="""The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': 'AlexaFluor_488'}, {'value': 'Cy5'}]} })
    x_precision: Optional[float] = Field(default=None, description="""Metric quantifying the precision of the X-axis localization estimate. Typically the Cramer-Rao lower bound or Thompson method estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Must be accompanied by a description in the file header. Written as the reserved X_Loc_Precision column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    y_precision: Optional[float] = Field(default=None, description="""Metric quantifying the precision of the Y-axis localization estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Written as the reserved Y_Loc_Precision column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    z_precision: Optional[float] = Field(default=None, description="""Metric quantifying the precision of the Z-axis localization estimate. Highly recommended (not literally mandatory) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables. Written as the reserved Z_Loc_Precision column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    photon_count: Optional[int] = Field(default=None, description="""Number of photons detected for this localization event or Spot. Reserved, conditionally-required column name (Photon_Count) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables; highly recommended in the latter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1500'}]} })
    goodness_of_fit: Optional[float] = Field(default=None, description="""Metric quantifying how well the fitted model matches the observed signal (e.g. chi-squared, R-squared). Reserved, conditionally-required column name (Goodness_of_Fit) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.95'}]} })
    centroid_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the centroid pixel of the Spot / localization. Reserved, conditionally-required column name (Centroid_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '2500.0'}]} })
    peak_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the brightest pixel within the Spot / localization boundary. Reserved, conditionally-required column name (Peak_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '3200.0'}]} })
    raw_x: Optional[float] = Field(default=None, description="""X coordinate before any post-processing corrections (drift correction, chromatic correction, etc.). Same unit as X. Reserved, conditionally-required column name (Raw_X) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '14.30'}]} })
    raw_y: Optional[float] = Field(default=None, description="""Y coordinate before any post-processing corrections. Same unit as Y. Reserved, conditionally-required column name (Raw_Y) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '41.20'}]} })
    raw_z: Optional[float] = Field(default=None, description="""Z coordinate before any post-processing corrections. Same unit as Z. Reserved, conditionally-required column name (Raw_Z) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1.10'}]} })
    x_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the X coordinate. Same unit as X. Reserved, conditionally-required column name (X_Drift) in the Spot Quality and RNA Spot Quality tables. Not part of the reserved vocabulary of the SM Localization Quality table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.13'}]} })
    y_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Drift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.23'}]} })
    z_drift: Optional[float] = Field(default=None, description="""Drift correction offset applied to the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Drift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.13'}]} })
    x_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the X coordinate. Same unit as X. Reserved, conditionally-required column name (X_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.05'}]} })
    y_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.04'}]} })
    z_chromatic_shift: Optional[float] = Field(default=None, description="""Chromatic aberration correction offset applied to the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Chromatic_Shift) in the Spot Quality and RNA Spot Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord', 'RNASpotQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    x_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the X coordinate (e.g. standard deviation of repeated measurements). Same unit as X. Reserved, conditionally-required column name (X_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    y_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    z_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.05'}]} })


class RNASpotQualityTable(ConfiguredBaseModel):
    """
    The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_quality). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of RNASpotQualityRecord rows. Submission of this table is optional but recommended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/rna_quality',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'description': 'Method used '
                                                                        'to perform '
                                                                        'intensity '
                                                                        'measurements. '
                                                                        'Conditionally '
                                                                        'required when '
                                                                        'any intensity '
                                                                        'metric is '
                                                                        'present. '
                                                                        'Written as '
                                                                        '#Intensity_Measurement_Method: '
                                                                        'in the file '
                                                                        'header.',
                                                         'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'description': 'Unit used for any intensity '
                                                          'metric reported in '
                                                          'user-defined columns. '
                                                          'Conditionally required when '
                                                          'any such metric is present. '
                                                          'Written as '
                                                          '##Intensity_Unit= in the '
                                                          'file header.',
                                           'name': 'intensity_unit',
                                           'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'rna_spot_quality_records': {'name': 'rna_spot_quality_records',
                                                     'required': True},
                        'softwares': {'description': 'One or more Software entries '
                                                     'documenting every tool used to '
                                                     'produce or process data in this '
                                                     'table. Required only when '
                                                     'software was used; omit the '
                                                     'block entirely if no software '
                                                     'was applied. Written as '
                                                     'repeating #Software_* blocks in '
                                                     'the file header.',
                                      'name': 'softwares',
                                      'required': False},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'4dn_FOF-CT_rna_quality'. "
                                                           'Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': '4dn_FOF-CT_rna_quality',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'description': 'Unit used for any time metric '
                                                     'reported in user-defined '
                                                     'columns. Conditionally required '
                                                     'when any such metric is present. '
                                                     'Written as ##Time_Unit= in the '
                                                     'file header.',
                                      'name': 'time_unit',
                                      'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_rna_quality"] = Field(default=..., description="""Identifier for this table type. Must always be '4dn_FOF-CT_rna_quality'. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_rna_quality'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Required only when software was used; omit the block entirely if no software was applied. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    rna_spot_quality_records: list[RNASpotQualityRecord] = Field(default=..., description="""The complete collection of RNASpotQualityRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined quality metric column.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpotQualityTable', 'domain_of': ['RNASpotQualityTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class SpotBiologicalRecord(ConfiguredBaseModel):
    """
    A single row in the Spot Biological Data table. Each instance captures one or more user-defined biological properties for a specific DNA bright Spot identified by Spot_ID. Spot_ID values must be unique across the dataset, linking to the corresponding Spot record in the core table (table 1). At least one user-defined biological property column MUST be present; users declare these via #^ header lines.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/bio',
         'slot_usage': {'spot_id': {'description': 'Unique identifier for the DNA '
                                                   'bright Spot to which these '
                                                   'biological properties belong. '
                                                   'Links to the corresponding Spot '
                                                   'record in the core table (table '
                                                   '1). Must be unique within this '
                                                   'table and across the entire '
                                                   'dataset.',
                                    'identifier': True,
                                    'name': 'spot_id',
                                    'required': True}}})

    spot_id: int = Field(default=..., description="""Unique identifier for the DNA bright Spot to which these biological properties belong. Links to the corresponding Spot record in the core table (table 1). Must be unique within this table and across the entire dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot',
                       'Localization',
                       'SpotQualityRecord',
                       'SpotBiologicalRecord',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class SpotBiologicalTable(ConfiguredBaseModel):
    """
    The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_bio). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of SpotBiologicalRecord rows. Submission of this table is optional but highly recommended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/bio',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'description': 'Method used '
                                                                        'to perform '
                                                                        'intensity '
                                                                        'measurements. '
                                                                        'Conditionally '
                                                                        'required when '
                                                                        'any intensity '
                                                                        'metric is '
                                                                        'present. '
                                                                        'Written as '
                                                                        '#Intensity_Measurement_Method: '
                                                                        'in the file '
                                                                        'header.',
                                                         'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'description': 'Unit used for any intensity '
                                                          'metric reported in '
                                                          'user-defined columns. '
                                                          'Conditionally required when '
                                                          'any such metric is present. '
                                                          'Written as '
                                                          '##Intensity_Unit= in the '
                                                          'file header.',
                                           'name': 'intensity_unit',
                                           'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'description': 'One or more Software entries '
                                                     'documenting every tool used to '
                                                     'produce or process data in this '
                                                     'table. Required only when '
                                                     'software was used; omit the '
                                                     'block entirely if no software '
                                                     'was applied. Written as '
                                                     'repeating #Software_* blocks in '
                                                     'the file header.',
                                      'name': 'softwares',
                                      'required': False},
                        'spot_biological_records': {'name': 'spot_biological_records',
                                                    'required': True},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'4dn_FOF-CT_bio'. Written "
                                                           'as ##Table_Namespace= in '
                                                           'the file header.',
                                            'equals_string': '4dn_FOF-CT_bio',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'description': 'Unit used for any time metric '
                                                     'reported in user-defined '
                                                     'columns. Conditionally required '
                                                     'when any such metric is present. '
                                                     'Written as ##Time_Unit= in the '
                                                     'file header.',
                                      'name': 'time_unit',
                                      'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_bio"] = Field(default=..., description="""Identifier for this table type. Must always be '4dn_FOF-CT_bio'. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_bio'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Required only when software was used; omit the block entirely if no software was applied. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    spot_biological_records: list[SpotBiologicalRecord] = Field(default=..., description="""The complete collection of SpotBiologicalRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined biological property column.""", json_schema_extra = { "linkml_meta": {'domain': 'SpotBiologicalTable', 'domain_of': ['SpotBiologicalTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class RNASpotBiologicalRecord(ConfiguredBaseModel):
    """
    A single row in the RNA Spot Biological Data table. Each instance captures one or more user-defined biological properties for a specific RNA bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the dataset, linking to the corresponding record in the RNA Spot Data table (table 4). At least one user-defined biological property column MUST be present; users declare these via #^ header lines.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/rna_bio',
         'slot_usage': {'rna_spot_id': {'identifier': True,
                                        'name': 'rna_spot_id',
                                        'required': True}}})

    rna_spot_id: int = Field(default=..., description="""Unique identifier for an RNA bright Spot, unique across the entire dataset. Used as a primary key in the RNA Spot Data table and as a foreign key in the RNA Quality and RNA Biological Data tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RNASpot', 'RNASpotQualityRecord', 'RNASpotBiologicalRecord'],
         'examples': [{'value': '1'}]} })


class RNASpotBiologicalTable(ConfiguredBaseModel):
    """
    The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_bio). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of RNASpotBiologicalRecord rows. Submission of this table is optional but highly recommended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/rna_bio',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'description': 'Method used '
                                                                        'to perform '
                                                                        'intensity '
                                                                        'measurements. '
                                                                        'Conditionally '
                                                                        'required when '
                                                                        'any intensity '
                                                                        'metric is '
                                                                        'present. '
                                                                        'Written as '
                                                                        '#Intensity_Measurement_Method: '
                                                                        'in the file '
                                                                        'header.',
                                                         'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'description': 'Unit used for any intensity '
                                                          'metric reported in '
                                                          'user-defined columns. '
                                                          'Conditionally required when '
                                                          'any such metric is present. '
                                                          'Written as '
                                                          '##Intensity_Unit= in the '
                                                          'file header.',
                                           'name': 'intensity_unit',
                                           'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'rna_spot_biological_records': {'name': 'rna_spot_biological_records',
                                                        'required': True},
                        'softwares': {'description': 'One or more Software entries '
                                                     'documenting every tool used to '
                                                     'produce or process data in this '
                                                     'table. Required only when '
                                                     'software was used; omit the '
                                                     'block entirely if no software '
                                                     'was applied. Written as '
                                                     'repeating #Software_* blocks in '
                                                     'the file header.',
                                      'name': 'softwares',
                                      'required': False},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'4dn_FOF-CT_rna_bio'. "
                                                           'Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': '4dn_FOF-CT_rna_bio',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'description': 'Unit used for any time metric '
                                                     'reported in user-defined '
                                                     'columns. Conditionally required '
                                                     'when any such metric is present. '
                                                     'Written as ##Time_Unit= in the '
                                                     'file header.',
                                      'name': 'time_unit',
                                      'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_rna_bio"] = Field(default=..., description="""Identifier for this table type. Must always be '4dn_FOF-CT_rna_bio'. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_rna_bio'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Required only when software was used; omit the block entirely if no software was applied. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used for any time metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Time_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used for any intensity metric reported in user-defined columns. Conditionally required when any such metric is present. Written as ##Intensity_Unit= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements. Conditionally required when any intensity metric is present. Written as #Intensity_Measurement_Method: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    rna_spot_biological_records: list[RNASpotBiologicalRecord] = Field(default=..., description="""The complete collection of RNASpotBiologicalRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined biological property column.""", json_schema_extra = { "linkml_meta": {'domain': 'RNASpotBiologicalTable', 'domain_of': ['RNASpotBiologicalTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class Cell(ConfiguredBaseModel):
    """
    A single Cell identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Cell Data table. The cell_id field uniquely identifies each Cell and links to the core table, the Sub-Cell ROI Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined optional columns (e.g. Cell_Size, Cell_Volume, Cell_Cycle_State, RNA_Spot_Count) via open schema. At least one such user-defined column MUST be present per submission.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/cell',
         'slot_usage': {'cell_id': {'description': 'Unique integer identifier for this '
                                                   'Cell. Cell_ID values are unique '
                                                   'across the entire dataset, '
                                                   'enabling unambiguous '
                                                   'cross-referencing with the core '
                                                   'table, the Sub-Cell ROI Data '
                                                   'table, and the Cell/ROI Mapping '
                                                   'table.',
                                    'identifier': True,
                                    'inlined': False,
                                    'name': 'cell_id',
                                    'range': 'integer',
                                    'required': True},
                        'extra_cell_roi_id': {'description': 'Identifier of the '
                                                             'extracellular structure '
                                                             'ROI (e.g. tissue '
                                                             'section, organoid) that '
                                                             'contains this Cell. '
                                                             'Conditionally required '
                                                             'when this Cell can be '
                                                             'associated with an '
                                                             'extracellular ROI '
                                                             'identified as part of '
                                                             'this experiment and '
                                                             'reported in a dedicated '
                                                             'Extra-Cell ROI Data '
                                                             'table.',
                                              'name': 'extra_cell_roi_id',
                                              'required': False}}})

    cell_id: int = Field(default=..., description="""Unique integer identifier for this Cell. Cell_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the Sub-Cell ROI Data table, and the Cell/ROI Mapping table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Identifier of the extracellular structure ROI (e.g. tissue section, organoid) that contains this Cell. Conditionally required when this Cell can be associated with an extracellular ROI identified as part of this experiment and reported in a dedicated Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class CellTable(ConfiguredBaseModel):
    """
    The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of Cells (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/cell',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'cell_type': {'name': 'cell_type', 'required': True},
                        'cells': {'name': 'cells', 'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'extra_cell_roi_type': {'name': 'extra_cell_roi_type',
                                                'required': False},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'name': 'intensity_unit', 'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': False},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_cell',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'name': 'time_unit', 'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_cell"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_cell'} })
    cell_type: str = Field(default=..., description="""The type of cells present in this dataset, reported as an ontology term ID from the Experimental Factor Ontology (EFO), followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Cell in tissue)\" -- look up the real EFO ID before use. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Cell_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'SubCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Cell in tissue)'},
                      {'value': 'EFO:XXXXXXX (Cell in organoid)'},
                      {'value': 'Other'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    extra_cell_roi_type: Optional[str] = Field(default=None, description="""The type of extracellular structure ROI within which cells are embedded, reported as an ontology term ID from EFO's 'organism part' branch, followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Tissue)\" -- look up the real EFO ID before use. Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Extra_Cell_ROI_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'ExtraCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Tissue)'},
                      {'value': 'EFO:XXXXXXX (Organoid)'},
                      {'value': 'Other'}]} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    cells: list[Cell] = Field(default=..., description="""The complete collection of Cells constituting this dataset. Each Cell corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. Cell_Size, Cell_Volume) MUST be present in every submitted Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain': 'CellTable', 'domain_of': ['CellTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('cell_type')
    def pattern_cell_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cell_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cell_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('extra_cell_roi_type')
    def pattern_extra_cell_roi_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid extra_cell_roi_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid extra_cell_roi_type format: {v}"
            raise ValueError(err_msg)
        return v


class ExtraCellROI(ConfiguredBaseModel):
    """
    A single extracellular structure ROI (e.g. a tissue section or organoid) identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Extra-Cell ROI Data table. The extra_cell_roi_id field uniquely identifies each ROI and links to the core table, the RNA Spot Data table, and the Cell Data table. This class accepts additional user-defined optional columns (e.g. ROI_Volume, Cell_Count). At least one such user-defined column MUST be present per submission.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/extracell',
         'slot_usage': {'extra_cell_roi_id': {'description': 'Unique integer '
                                                             'identifier for this '
                                                             'extracellular structure '
                                                             'ROI. Extra_Cell_ROI_ID '
                                                             'values are unique across '
                                                             'the entire dataset, '
                                                             'enabling unambiguous '
                                                             'cross-referencing with '
                                                             'the core table, the RNA '
                                                             'Spot Data table, and the '
                                                             'Cell Data table.',
                                              'identifier': True,
                                              'inlined': False,
                                              'name': 'extra_cell_roi_id',
                                              'range': 'integer',
                                              'required': True}}})

    extra_cell_roi_id: int = Field(default=..., description="""Unique integer identifier for this extracellular structure ROI. Extra_Cell_ROI_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the RNA Spot Data table, and the Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class ExtraCellROITable(ConfiguredBaseModel):
    """
    The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of extracellular ROIs (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/extracell',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'extra_cell_roi_type': {'name': 'extra_cell_roi_type',
                                                'required': True},
                        'extra_cell_rois': {'name': 'extra_cell_rois',
                                            'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'name': 'intensity_unit', 'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': False},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_extracell',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'name': 'time_unit', 'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_extracell"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_extracell'} })
    extra_cell_roi_type: str = Field(default=..., description="""The type of extracellular structure ROI within which cells are embedded, reported as an ontology term ID from EFO's 'organism part' branch, followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Tissue)\" -- look up the real EFO ID before use. Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Extra_Cell_ROI_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'ExtraCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Tissue)'},
                      {'value': 'EFO:XXXXXXX (Organoid)'},
                      {'value': 'Other'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    extra_cell_rois: list[ExtraCellROI] = Field(default=..., description="""The complete collection of extracellular ROIs constituting this dataset. Each ExtraCellROI corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. ROI_Volume, Cell_Count) MUST be present in every submitted Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain': 'ExtraCellROITable', 'domain_of': ['ExtraCellROITable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('extra_cell_roi_type')
    def pattern_extra_cell_roi_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid extra_cell_roi_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid extra_cell_roi_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class SubCellROI(ConfiguredBaseModel):
    """
    A single sub-cellular structure ROI (e.g. nucleolus, nuclear lamina, PML body, chromosome domain) identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Sub-Cell ROI Data table. The sub_cell_roi_id field uniquely identifies each ROI and links to the core table, the Cell Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined optional columns (e.g. ROI_Volume, ROI_Area). At least one such user-defined column MUST be present per submission.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/subcell',
         'slot_usage': {'cell_id': {'description': 'Identifier of the Cell to which '
                                                   'this sub-cellular ROI belongs. '
                                                   'Conditionally required when this '
                                                   'ROI can be associated with a Cell '
                                                   'identified as part of this '
                                                   'experiment and reported in a '
                                                   'dedicated Cell Data table.',
                                    'name': 'cell_id',
                                    'required': False},
                        'sub_cell_roi_id': {'description': 'Unique integer identifier '
                                                           'for this sub-cellular '
                                                           'structure ROI. '
                                                           'Sub_Cell_ROI_ID values are '
                                                           'unique across the entire '
                                                           'dataset, enabling '
                                                           'unambiguous '
                                                           'cross-referencing with the '
                                                           'core table, the Cell Data '
                                                           'table, and the Cell/ROI '
                                                           'Mapping table.',
                                            'identifier': True,
                                            'inlined': False,
                                            'name': 'sub_cell_roi_id',
                                            'range': 'integer',
                                            'required': True}}})

    sub_cell_roi_id: int = Field(default=..., description="""Unique integer identifier for this sub-cellular structure ROI. Sub_Cell_ROI_ID values are unique across the entire dataset, enabling unambiguous cross-referencing with the core table, the Cell Data table, and the Cell/ROI Mapping table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Identifier of the Cell to which this sub-cellular ROI belongs. Conditionally required when this ROI can be associated with a Cell identified as part of this experiment and reported in a dedicated Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })


class SubCellROITable(ConfiguredBaseModel):
    """
    The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_subcell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of sub-cellular ROIs (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/subcell',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'cell_type': {'name': 'cell_type', 'required': False},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'name': 'intensity_unit', 'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': False},
                        'sub_cell_roi_type': {'name': 'sub_cell_roi_type',
                                              'required': True},
                        'sub_cell_rois': {'name': 'sub_cell_rois', 'required': True},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_subcell',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'name': 'time_unit', 'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_subcell"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_subcell'} })
    sub_cell_roi_type: str = Field(default=..., description="""The type of sub-cellular structure ROI documented in this table or mapping file, reported as an ontology term ID from GO's 'cellular_component' branch, followed by its human-readable label in parentheses, e.g. \"GO:XXXXXXX (Nucleolus)\" -- look up the real GO ID before use. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Sub_Cell_ROI_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'GO:XXXXXXX (Nucleolus)'},
                      {'value': 'GO:XXXXXXX (Nuclear Lamina (NL))'},
                      {'value': 'GO:XXXXXXX (Chromosome_Domain)'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    cell_type: Optional[str] = Field(default=None, description="""The type of cells present in this dataset, reported as an ontology term ID from the Experimental Factor Ontology (EFO), followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Cell in tissue)\" -- look up the real EFO ID before use. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Cell_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'SubCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Cell in tissue)'},
                      {'value': 'EFO:XXXXXXX (Cell in organoid)'},
                      {'value': 'Other'}]} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    sub_cell_rois: list[SubCellROI] = Field(default=..., description="""The complete collection of sub-cellular ROIs constituting this dataset. Each SubCellROI corresponds to one data row in the TSV serialisation. At least one user-defined optional column (e.g. ROI_Volume, ROI_Area) MUST be present in every submitted Sub-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain': 'SubCellROITable', 'domain_of': ['SubCellROITable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sub_cell_roi_type')
    def pattern_sub_cell_roi_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sub_cell_roi_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sub_cell_roi_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('cell_type')
    def pattern_cell_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cell_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cell_type format: {v}"
            raise ValueError(err_msg)
        return v


class ROIMapping(ConfiguredBaseModel):
    """
    A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a FOF-bas-CT experiment. Each instance corresponds to one row in the TSV data section of the FOF-CT Cell/ROI Mapping table. Exactly one of the three identifier slots (sub_cell_roi_id, cell_id, extra_cell_roi_id) must be populated per file; the choice of identifier must be consistent across all rows of a given submission. The roi_boundaries slot holds the boundary coordinates in the format specified by roi_boundaries_format in the table header. This class accepts additional user-defined optional columns.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exactly_one_of': [{'slot_conditions': {'cell_id': {'name': 'cell_id',
                                                             'value_presence': 'ABSENT'},
                                                 'extra_cell_roi_id': {'name': 'extra_cell_roi_id',
                                                                       'value_presence': 'ABSENT'},
                                                 'sub_cell_roi_id': {'name': 'sub_cell_roi_id',
                                                                     'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'cell_id': {'name': 'cell_id',
                                                             'value_presence': 'PRESENT'},
                                                 'extra_cell_roi_id': {'name': 'extra_cell_roi_id',
                                                                       'value_presence': 'ABSENT'},
                                                 'sub_cell_roi_id': {'name': 'sub_cell_roi_id',
                                                                     'value_presence': 'ABSENT'}}},
                            {'slot_conditions': {'cell_id': {'name': 'cell_id',
                                                             'value_presence': 'ABSENT'},
                                                 'extra_cell_roi_id': {'name': 'extra_cell_roi_id',
                                                                       'value_presence': 'PRESENT'},
                                                 'sub_cell_roi_id': {'name': 'sub_cell_roi_id',
                                                                     'value_presence': 'ABSENT'}}}],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/mapping',
         'slot_usage': {'cell_id': {'description': 'Unique identifier for the Cell '
                                                   'whose boundaries are described in '
                                                   'this row. Conditionally required '
                                                   'when this file contains Cell '
                                                   'boundary data. Exactly one of '
                                                   'sub_cell_roi_id, cell_id, or '
                                                   'extra_cell_roi_id must be used '
                                                   'consistently throughout the file.',
                                    'name': 'cell_id',
                                    'required': False},
                        'extra_cell_roi_id': {'description': 'Unique identifier for '
                                                             'the extracellular '
                                                             'structure ROI whose '
                                                             'boundaries are described '
                                                             'in this row. '
                                                             'Conditionally required '
                                                             'when this file contains '
                                                             'Extra-Cell ROI boundary '
                                                             'data. Exactly one of '
                                                             'sub_cell_roi_id, '
                                                             'cell_id, or '
                                                             'extra_cell_roi_id must '
                                                             'be used consistently '
                                                             'throughout the file.',
                                              'name': 'extra_cell_roi_id',
                                              'required': False},
                        'roi_boundaries': {'name': 'roi_boundaries', 'required': True},
                        'sub_cell_roi_id': {'description': 'Unique identifier for the '
                                                           'Sub-Cell ROI whose '
                                                           'boundaries are described '
                                                           'in this row. Conditionally '
                                                           'required when this file '
                                                           'contains sub- cellular ROI '
                                                           'boundary data. Exactly one '
                                                           'of sub_cell_roi_id, '
                                                           'cell_id, or '
                                                           'extra_cell_roi_id must be '
                                                           'used consistently '
                                                           'throughout the file.',
                                            'name': 'sub_cell_roi_id',
                                            'required': False}}})

    sub_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for the Sub-Cell ROI whose boundaries are described in this row. Conditionally required when this file contains sub- cellular ROI boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Unique identifier for the Cell whose boundaries are described in this row. Conditionally required when this file contains Cell boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for the extracellular structure ROI whose boundaries are described in this row. Conditionally required when this file contains Extra-Cell ROI boundary data. Exactly one of sub_cell_roi_id, cell_id, or extra_cell_roi_id must be used consistently throughout the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    roi_boundaries: str = Field(default=..., description="""Boundary coordinates for this Cell or ROI, encoded in the format specified by roi_boundaries_format in the table header. For the OME ROI Polygon model, coordinates are provided as a space-separated list of \"x,y\" pairs (e.g. \"12.5,40.2 13.1,41.0 ...\"). For OBJ 3D mesh format, the field contains the vertex and face list for the boundary mesh.""", json_schema_extra = { "linkml_meta": {'domain': 'ROIMapping',
         'domain_of': ['ROIMapping'],
         'examples': [{'value': '12.5,40.2 13.1,41.0 14.0,40.5 13.5,39.8'},
                      {'value': 'v 1.0 2.0 3.0\nv 4.0 5.0 6.0\nf 1 2 3'}]} })


class ROIMappingTable(ConfiguredBaseModel):
    """
    The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_mapping). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of ROI boundary records (recorded as data rows). This table is conditionally required whenever a Cell Data table, a Sub-Cell ROI Data table, or an Extra-Cell ROI Data table is deposited. Analogous to the MappingSet class in SSSOM.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/mapping',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'cell_type': {'name': 'cell_type', 'required': False},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'extra_cell_roi_type': {'name': 'extra_cell_roi_type',
                                                'required': False},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'intensity_measurement_method': {'name': 'intensity_measurement_method',
                                                         'required': False},
                        'intensity_unit': {'name': 'intensity_unit', 'required': False},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'roi_boundaries_format_description': {'description': 'Free-text '
                                                                             'description '
                                                                             'of how '
                                                                             'ROI '
                                                                             'boundaries '
                                                                             'are '
                                                                             'encoded, '
                                                                             'beyond '
                                                                             'what the '
                                                                             'format '
                                                                             'name '
                                                                             'alone '
                                                                             'conveys '
                                                                             '(e.g. '
                                                                             'coordinate '
                                                                             'order, '
                                                                             'dimensionality, '
                                                                             'or an '
                                                                             'external '
                                                                             'file '
                                                                             'reference). '
                                                                             'Conditionally '
                                                                             'required '
                                                                             '(content-triggered): '
                                                                             'MANDATORY '
                                                                             'when '
                                                                             'roi_boundaries_format_type '
                                                                             'is '
                                                                             "'Other'; "
                                                                             'otherwise '
                                                                             'recommended.',
                                                              'name': 'roi_boundaries_format_description',
                                                              'required': False},
                        'roi_boundaries_format_type': {'name': 'roi_boundaries_format_type',
                                                       'required': True},
                        'roi_mappings': {'name': 'roi_mappings', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': False},
                        'sub_cell_roi_type': {'name': 'sub_cell_roi_type',
                                              'required': False},
                        'table_namespace': {'equals_string': '4dn_FOF-CT_mapping',
                                            'name': 'table_namespace',
                                            'required': True},
                        'time_unit': {'name': 'time_unit', 'required': False},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["4dn_FOF-CT_mapping"] = Field(default=..., description="""Identifier for this table type. The required value is specific to each table. Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': '4dn_FOF-CT_mapping'} })
    roi_boundaries_format_type: ROIBoundariesFormatTypeEnum = Field(default=..., description="""Controlled-vocabulary identifier of the standard used to encode ROI boundaries in global coordinates (e.g. OME_Polygon for the OME ROI data model, or Mesh_OBJ for a 3D OBJ mesh). Written as ##ROI_Boundaries_Format_Type= in the file header. Default value is OME_Polygon.""", json_schema_extra = { "linkml_meta": {'domain': 'ROIMappingTable',
         'domain_of': ['ROIMappingTable'],
         'examples': [{'value': 'OME_Polygon'}, {'value': 'Mesh_OBJ'}]} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    roi_boundaries_format_description: Optional[str] = Field(default=None, description="""Free-text description of how ROI boundaries are encoded, beyond what the format name alone conveys (e.g. coordinate order, dimensionality, or an external file reference). Conditionally required (content-triggered): MANDATORY when roi_boundaries_format_type is 'Other'; otherwise recommended.""", json_schema_extra = { "linkml_meta": {'domain': 'ROIMappingTable',
         'domain_of': ['ROIMappingTable'],
         'examples': [{'value': 'Cell boundaries are reported in global coordinates as '
                                'lists of comma separated x,y coordinates separated by '
                                'spaces like "x1,y1 x2,y2 x3,y3" (e.g. "0,0 1,2 '
                                '3,5").'}]} })
    cell_type: Optional[str] = Field(default=None, description="""The type of cells present in this dataset, reported as an ontology term ID from the Experimental Factor Ontology (EFO), followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Cell in tissue)\" -- look up the real EFO ID before use. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Cell_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'SubCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Cell in tissue)'},
                      {'value': 'EFO:XXXXXXX (Cell in organoid)'},
                      {'value': 'Other'}]} })
    sub_cell_roi_type: Optional[str] = Field(default=None, description="""The type of sub-cellular structure ROI documented in this table or mapping file, reported as an ontology term ID from GO's 'cellular_component' branch, followed by its human-readable label in parentheses, e.g. \"GO:XXXXXXX (Nucleolus)\" -- look up the real GO ID before use. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Sub_Cell_ROI_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'GO:XXXXXXX (Nucleolus)'},
                      {'value': 'GO:XXXXXXX (Nuclear Lamina (NL))'},
                      {'value': 'GO:XXXXXXX (Chromosome_Domain)'}]} })
    extra_cell_roi_type: Optional[str] = Field(default=None, description="""The type of extracellular structure ROI within which cells are embedded, reported as an ontology term ID from EFO's 'organism part' branch, followed by its human-readable label in parentheses, e.g. \"EFO:XXXXXXX (Tissue)\" -- look up the real EFO ID before use. Conditionally required when extracellular structure ROIs are identified and reported in a dedicated Extra-Cell ROI Data table. \"Other\" is accepted as a literal value when no ontology term applies. Written as #Extra_Cell_ROI_Type: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTable', 'ExtraCellROITable', 'ROIMappingTable'],
         'examples': [{'value': 'EFO:XXXXXXX (Tissue)'},
                      {'value': 'EFO:XXXXXXX (Organoid)'},
                      {'value': 'Other'}]} })
    softwares: Optional[list[Software]] = Field(default=None, description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    roi_mappings: list[ROIMapping] = Field(default=..., description="""The complete collection of ROI boundary records constituting this dataset. Each ROIMapping corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'ROIMappingTable', 'domain_of': ['ROIMappingTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('cell_type')
    def pattern_cell_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cell_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cell_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sub_cell_roi_type')
    def pattern_sub_cell_roi_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sub_cell_roi_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sub_cell_roi_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('extra_cell_roi_type')
    def pattern_extra_cell_roi_type(cls, v):
        pattern=re.compile(r"^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid extra_cell_roi_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid extra_cell_roi_type format: {v}"
            raise ValueError(err_msg)
        return v


class SMLocalization(LocalizationMixin):
    """
    A single individual single-molecule (SM) localization event in a FOF-vol-CT dataset. Each instance corresponds to one row in the TSV data section of the SM Localization Data table. The loc_id field is the primary key; spot_id links this localization to its parent Spot (if Spot/Trace post-processing was performed); trace_id links it to its parent Trace. Sub_Cell_ROI_ID, Cell_ID and Extra_Cell_ROI_ID optionally link the localization to spatial context tables.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/vol_core',
         'mixins': ['LocalizationMixin'],
         'slot_usage': {'cell_id': {'name': 'cell_id', 'required': False},
                        'chrom': {'name': 'chrom', 'required': True},
                        'chrom_end': {'name': 'chrom_end', 'required': True},
                        'chrom_start': {'name': 'chrom_start', 'required': True},
                        'extra_cell_roi_id': {'name': 'extra_cell_roi_id',
                                              'required': False},
                        'loc_id': {'description': 'Unique integer identifier for this '
                                                  'SM localization event. Loc_ID '
                                                  'values are unique across the entire '
                                                  'dataset.',
                                   'identifier': True,
                                   'name': 'loc_id',
                                   'required': True},
                        'spot_id': {'description': 'Identifier of the Spot (centroid '
                                                   'of the SM localization cloud, '
                                                   'derived by clustering SM '
                                                   'Localization events) to which this '
                                                   'localization belongs. Mandatory '
                                                   'for every SM Localization event '
                                                   '(see vol_core.rst: "A valid '
                                                   'FOF-vol-CT deposition MUST '
                                                   'mandatorily report Loc_ID together '
                                                   'with its associated Spot_ID and '
                                                   'Trace_ID for every SM Localization '
                                                   'event.").',
                                    'name': 'spot_id',
                                    'required': True},
                        'sub_cell_roi_id': {'name': 'sub_cell_roi_id',
                                            'required': False},
                        'trace_id': {'description': 'Identifier of the chromatin Trace '
                                                    'to which this localization and '
                                                    'its parent Spot belong. Mandatory '
                                                    'for every SM Localization event '
                                                    '(see vol_core.rst).',
                                     'name': 'trace_id',
                                     'required': True},
                        'x': {'description': 'Sub-pixel X coordinate of this SM '
                                             'localization event in the unit specified '
                                             'by xyz_unit. The reported value is the '
                                             'final position after all post-processing '
                                             'corrections.',
                              'name': 'x',
                              'required': True},
                        'y': {'name': 'y', 'required': True},
                        'z': {'name': 'z', 'required': True}}})

    spot_id: int = Field(default=..., description="""Identifier of the Spot (centroid of the SM localization cloud, derived by clustering SM Localization events) to which this localization belongs. Mandatory for every SM Localization event (see vol_core.rst: \"A valid FOF-vol-CT deposition MUST mandatorily report Loc_ID together with its associated Spot_ID and Trace_ID for every SM Localization event.\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot',
                       'Localization',
                       'SpotQualityRecord',
                       'SpotBiologicalRecord',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    trace_id: int = Field(default=..., description="""Identifier of the chromatin Trace to which this localization and its parent Spot belong. Mandatory for every SM Localization event (see vol_core.rst).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'Trace', 'RNASpot', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    chrom: str = Field(default=..., description="""Chromosome name/identifier using BED (Browser Extensible Data) convention (e.g., chr3, chrY, chr2_random). Used by both the core (Spot) and vol_core (SMLocalization) tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'],
         'examples': [{'value': 'chr3'}, {'value': 'chrY'}, {'value': 'chr2_random'}]} })
    chrom_start: int = Field(default=..., description="""0-based start coordinate on the chromosome for the genomic target sequence, following BED convention. Used by both the core (Spot) and vol_core (SMLocalization) tables.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'], 'examples': [{'value': '0'}]} })
    chrom_end: int = Field(default=..., description="""Non-inclusive end coordinate on the chromosome for the genomic target sequence, following BED convention. Used by both the core (Spot) and vol_core (SMLocalization) tables.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Spot', 'SMLocalization'], 'examples': [{'value': '1000'}]} })
    sub_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for a sub-cellular structure ROI (e.g., nucleus, nucleolus). Links to the Sub-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin', 'SubCellROI', 'ROIMapping', 'SMLocalization'],
         'examples': [{'value': '1'}]} })
    cell_id: Optional[int] = Field(default=None, description="""Unique identifier for a Cell. Links to the Cell Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'SubCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    extra_cell_roi_id: Optional[int] = Field(default=None, description="""Unique identifier for an extracellular structure ROI (e.g., tissue, organoid). Links to the Extra-Cell ROI Data table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotMixin',
                       'Cell',
                       'ExtraCellROI',
                       'ROIMapping',
                       'SMLocalization'],
         'examples': [{'value': '1'}]} })
    loc_id: int = Field(default=..., description="""Unique integer identifier for this SM localization event. Loc_ID values are unique across the entire dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SMLocalizationQualityRecord'],
         'examples': [{'value': '1'}]} })
    x: float = Field(default=..., description="""Sub-pixel X coordinate of this SM localization event in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: float = Field(default=..., description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: float = Field(default=..., description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })


class SMLocalizationTable(ConfiguredBaseModel):
    """
    The SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_vol_core, no 4dn_ prefix). This is the mandatory primary data table for volumetric FOF-CT submissions. Each row corresponds to one SM localization event. The Spot/Trace Data table is optional for FOF-vol-CT submissions but may be included to report post-processing results derived from the localization data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/vol_core',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'genome_assembly': {'name': 'genome_assembly',
                                            'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'sm_localizations': {'name': 'sm_localizations',
                                             'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': True},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'FOF-CT_vol_core' (no 4dn_ "
                                                           'prefix — this '
                                                           'FOF-vol-CT-exclusive '
                                                           'namespace intentionally '
                                                           'omits it). Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': 'FOF-CT_vol_core',
                                            'name': 'table_namespace',
                                            'required': True},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["FOF-CT_vol_core"] = Field(default=..., description="""Identifier for this table type. Must always be 'FOF-CT_vol_core' (no 4dn_ prefix — this FOF-vol-CT-exclusive namespace intentionally omits it). Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': 'FOF-CT_vol_core'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    genome_assembly: str = Field(default=..., description="""Genome build used for Chrom, Chrom_Start and Chrom_End coordinates. The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome under study contains an INSERTION or DELETION the value must use the mandatory 'custom-build:' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)). Written as ##Genome_Assembly= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'RNASpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'GRCh38'},
                      {'value': 'custom-build:GRCm38+pJT039(insertion)'}]} })
    modification: Optional[str] = Field(default=None, description="""Description of the nature and genomic position of a DNA insertion or deletion in the genome under study. Conditionally required (content- triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##Modification= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'pJT039:chr3(insertion 0001-2500)'}]} })
    vcf_file_name: Optional[str] = Field(default=None, description="""Name of the Variant Call Format (VCF) file that must be submitted alongside the dataset to describe the genome insertion or deletion. Conditionally required (content-triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_File_Name= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'pJT039:chr3.vcf'}]} })
    vcf_version: Optional[str] = Field(default=None, description="""Version of the VCF format used for the accompanying VCF file. Conditionally required (content-triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##VCF_Version= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable', 'SMLocalizationTable'],
         'examples': [{'value': 'v4.2'}]} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    sm_localizations: list[SMLocalization] = Field(default=..., description="""The complete collection of SMLocalization events constituting this dataset. Each entry corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'SMLocalizationTable', 'domain_of': ['SMLocalizationTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class SMLocalizationQualityRecord(ConfiguredBaseModel):
    """
    A single row in the SM Localization Quality table. Each instance captures quality metrics for one SM localization event identified by Loc_ID. Loc_ID, Channel and Fluor are mandatory. X_Loc_Precision, Y_Loc_Precision, Z_Loc_Precision and Photon_Count are highly recommended but not literally mandatory. All other reserved metric columns are conditionally required (use of the reserved name is optional, but mandatory if that metric is reported). Additional user-defined optional columns must be described in the file header.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/vol_quality',
         'slot_usage': {'centroid_intensity': {'name': 'centroid_intensity',
                                               'required': False},
                        'channel_name': {'name': 'channel_name', 'required': True},
                        'fluorophore_name': {'name': 'fluorophore_name',
                                             'required': True},
                        'goodness_of_fit': {'name': 'goodness_of_fit',
                                            'required': False},
                        'loc_id': {'description': 'Unique integer identifier for the '
                                                  'SM localization event to which '
                                                  'these quality metrics belong. Links '
                                                  'to the corresponding SMLocalization '
                                                  'record in the SM Localization Data '
                                                  'table (table 13).',
                                   'identifier': True,
                                   'name': 'loc_id',
                                   'required': True},
                        'peak_intensity': {'name': 'peak_intensity', 'required': False},
                        'photon_count': {'description': 'Highly recommended: number of '
                                                        'photons detected for this '
                                                        'localization.',
                                         'name': 'photon_count',
                                         'required': False},
                        'raw_x': {'name': 'raw_x', 'required': False},
                        'raw_y': {'name': 'raw_y', 'required': False},
                        'raw_z': {'name': 'raw_z', 'required': False},
                        'x_loc_error': {'name': 'x_loc_error', 'required': False},
                        'x_precision': {'description': 'Highly recommended (not '
                                                       'literally mandatory): '
                                                       'X_Loc_Precision.',
                                        'name': 'x_precision',
                                        'required': False},
                        'y_loc_error': {'name': 'y_loc_error', 'required': False},
                        'y_precision': {'description': 'Highly recommended (not '
                                                       'literally mandatory): '
                                                       'Y_Loc_Precision.',
                                        'name': 'y_precision',
                                        'required': False},
                        'z_loc_error': {'name': 'z_loc_error', 'required': False},
                        'z_precision': {'description': 'Highly recommended (not '
                                                       'literally mandatory): '
                                                       'Z_Loc_Precision.',
                                        'name': 'z_precision',
                                        'required': False}}})

    loc_id: int = Field(default=..., description="""Unique integer identifier for the SM localization event to which these quality metrics belong. Links to the corresponding SMLocalization record in the SM Localization Data table (table 13).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SMLocalizationQualityRecord'],
         'examples': [{'value': '1'}]} })
    channel_name: str = Field(default=..., description="""The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': '510/25'}, {'value': '695/81'}]} })
    fluorophore_name: str = Field(default=..., description="""The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': 'AlexaFluor_488'}, {'value': 'Cy5'}]} })
    x_precision: Optional[float] = Field(default=None, description="""Highly recommended (not literally mandatory): X_Loc_Precision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    y_precision: Optional[float] = Field(default=None, description="""Highly recommended (not literally mandatory): Y_Loc_Precision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.01'}]} })
    z_precision: Optional[float] = Field(default=None, description="""Highly recommended (not literally mandatory): Z_Loc_Precision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    photon_count: Optional[int] = Field(default=None, description="""Highly recommended: number of photons detected for this localization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1500'}]} })
    goodness_of_fit: Optional[float] = Field(default=None, description="""Metric quantifying how well the fitted model matches the observed signal (e.g. chi-squared, R-squared). Reserved, conditionally-required column name (Goodness_of_Fit) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.95'}]} })
    centroid_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the centroid pixel of the Spot / localization. Reserved, conditionally-required column name (Centroid_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '2500.0'}]} })
    peak_intensity: Optional[float] = Field(default=None, description="""Signal intensity of the brightest pixel within the Spot / localization boundary. Reserved, conditionally-required column name (Peak_Intensity) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '3200.0'}]} })
    raw_x: Optional[float] = Field(default=None, description="""X coordinate before any post-processing corrections (drift correction, chromatic correction, etc.). Same unit as X. Reserved, conditionally-required column name (Raw_X) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '14.30'}]} })
    raw_y: Optional[float] = Field(default=None, description="""Y coordinate before any post-processing corrections. Same unit as Y. Reserved, conditionally-required column name (Raw_Y) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '41.20'}]} })
    raw_z: Optional[float] = Field(default=None, description="""Z coordinate before any post-processing corrections. Same unit as Z. Reserved, conditionally-required column name (Raw_Z) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '1.10'}]} })
    x_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the X coordinate (e.g. standard deviation of repeated measurements). Same unit as X. Reserved, conditionally-required column name (X_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    y_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Y coordinate. Same unit as Y. Reserved, conditionally-required column name (Y_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.02'}]} })
    z_loc_error: Optional[float] = Field(default=None, description="""Localization error estimate for the Z coordinate. Same unit as Z. Reserved, conditionally-required column name (Z_Loc_Error) in the Spot Quality, RNA Spot Quality, and SM Localization Quality tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord'],
         'examples': [{'value': '0.05'}]} })


class SMLocalizationQualityTable(ConfiguredBaseModel):
    """
    The SM Localization Quality table of a FOF-vol-CT dataset (namespace: FOF-CT_vol_quality, no 4dn_ prefix). Requirement level: optional (recommended). Only vol_core (table 13) is mandatory for FOF-vol-CT submissions; this table provides localization quality metrics indexed by Loc_ID when submitted.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/vol_quality',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'sm_localization_quality_records': {'name': 'sm_localization_quality_records',
                                                            'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': True},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'FOF-CT_vol_quality' (no "
                                                           '4dn_ prefix — this '
                                                           'FOF-vol-CT-exclusive '
                                                           'namespace intentionally '
                                                           'omits it). Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': 'FOF-CT_vol_quality',
                                            'name': 'table_namespace',
                                            'required': True},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["FOF-CT_vol_quality"] = Field(default=..., description="""Identifier for this table type. Must always be 'FOF-CT_vol_quality' (no 4dn_ prefix — this FOF-vol-CT-exclusive namespace intentionally omits it). Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': 'FOF-CT_vol_quality'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    sm_localization_quality_records: list[SMLocalizationQualityRecord] = Field(default=..., description="""The complete collection of SMLocalizationQualityRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'SMLocalizationQualityTable',
         'domain_of': ['SMLocalizationQualityTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


class UndecodedLocalization(LocalizationMixin):
    """
    A single raw, undecoded SM localization event in a FOF-vol-CT dataset. Each instance corresponds to one row in the TSV data section of the Undecoded SM Localization Data table. This class uses LocalizationMixin for the shared loc_id, x, y, z slots. The 8 mandatory columns, in order, are: Loc_ID, Hyb_ID, Image_Frame_ID, X, Y, Z, Channel, Fluor. TheZ (the_z) is a reserved, conditionally-required column for the focal Z-plane identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/fof-ct/undecoded',
         'mixins': ['LocalizationMixin'],
         'slot_usage': {'channel_name': {'name': 'channel_name', 'required': True},
                        'fluorophore_name': {'name': 'fluorophore_name',
                                             'required': True},
                        'hyb_id': {'name': 'hyb_id', 'required': True},
                        'image_frame_id': {'name': 'image_frame_id', 'required': True},
                        'loc_id': {'description': 'Unique integer identifier for this '
                                                  'undecoded localization event. '
                                                  'Loc_ID values are unique across the '
                                                  'entire dataset.',
                                   'identifier': True,
                                   'name': 'loc_id',
                                   'required': True},
                        'the_z': {'name': 'the_z', 'required': False},
                        'x': {'name': 'x', 'required': True},
                        'y': {'name': 'y', 'required': True},
                        'z': {'name': 'z', 'required': True}}})

    hyb_id: int = Field(default=..., description="""Unique identifier for the hybridization round in which this localization event was detected. Written as the Hyb_ID column. Mandatory in the Undecoded SM Localization table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UndecodedLocalization'], 'examples': [{'value': '1'}]} })
    image_frame_id: int = Field(default=..., description="""Unique integer identifier for the imaging frame in which this undecoded localization event was detected. Written as the Image_Frame_ID column. Mandatory in the Undecoded SM Localization table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UndecodedLocalization'], 'examples': [{'value': '1'}]} })
    channel_name: str = Field(default=..., description="""The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': '510/25'}, {'value': '695/81'}]} })
    fluorophore_name: str = Field(default=..., description="""The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Localization',
                       'SpotQualityRecord',
                       'RNASpotQualityRecord',
                       'SMLocalizationQualityRecord',
                       'UndecodedLocalization'],
         'examples': [{'value': 'AlexaFluor_488'}, {'value': 'Cy5'}]} })
    the_z: Optional[int] = Field(default=None, description="""Identifier of the focal Z-plane in which this localization event was detected. Reserved, conditionally-required column name (TheZ) in the Undecoded SM Localization table: optional to use, but if the focal Z-plane is reported this exact reserved column name MUST be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UndecodedLocalization'], 'examples': [{'value': '10'}]} })
    loc_id: int = Field(default=..., description="""Unique integer identifier for this undecoded localization event. Loc_ID values are unique across the entire dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SMLocalizationQualityRecord'],
         'examples': [{'value': '1'}]} })
    x: float = Field(default=..., description="""Sub-pixel X coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections (drift correction, chromatic correction, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '14.43'}]} })
    y: float = Field(default=..., description="""Sub-pixel Y coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '41.43'}]} })
    z: float = Field(default=..., description="""Sub-pixel Z coordinate of this detected event (Spot or localisation) in the unit specified by xyz_unit. The reported value is the final position after all post-processing corrections.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizationMixin', 'SpotMixin'],
         'examples': [{'value': '1.23'}]} })


class UndecodedLocalizationTable(ConfiguredBaseModel):
    """
    The Undecoded SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_undecoded, no 4dn_ prefix). This table is optional but recommended. It records raw localization detections prior to any decoding or assignment step. Submission is recommended when the raw detections are available and reproducibility of the decoding pipeline is desired.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fof-ct/undecoded',
         'slot_usage': {'additional_tables': {'name': 'additional_tables',
                                              'required': True},
                        'description': {'name': 'description', 'required': True},
                        'experimenter_contact': {'name': 'experimenter_contact',
                                                 'required': True},
                        'experimenter_name': {'name': 'experimenter_name',
                                              'required': True},
                        'fof_ct_version': {'name': 'fof_ct_version', 'required': True},
                        'lab_name': {'name': 'lab_name', 'required': True},
                        'softwares': {'multivalued': True,
                                      'name': 'softwares',
                                      'range': 'Software',
                                      'required': True},
                        'table_namespace': {'description': 'Identifier for this table '
                                                           'type. Must always be '
                                                           "'FOF-CT_undecoded' (no "
                                                           '4dn_ prefix — this '
                                                           'FOF-vol-CT-exclusive '
                                                           'namespace intentionally '
                                                           'omits it). Written as '
                                                           '##Table_Namespace= in the '
                                                           'file header.',
                                            'equals_string': 'FOF-CT_undecoded',
                                            'name': 'table_namespace',
                                            'required': True},
                        'undecoded_localizations': {'name': 'undecoded_localizations',
                                                    'required': True},
                        'xyz_unit': {'name': 'xyz_unit', 'required': True}},
         'tree_root': True})

    fof_ct_version: str = Field(default=..., description="""Version of the FOF-CT format used in this file. Always the first line of the file header (##FOF-CT_Version=).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'v1.0'}]} })
    table_namespace: Literal["FOF-CT_undecoded"] = Field(default=..., description="""Identifier for this table type. Must always be 'FOF-CT_undecoded' (no 4dn_ prefix — this FOF-vol-CT-exclusive namespace intentionally omits it). Written as ##Table_Namespace= in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'equals_string': 'FOF-CT_undecoded'} })
    lab_name: str = Field(default=..., description="""Name of the laboratory where the experiment was performed. Written as #Lab_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Nobel'}]} })
    experimenter_name: str = Field(default=..., description="""Full name of the person who performed the experiment. Written as #Experimenter_Name: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'John Doe'}]} })
    experimenter_contact: str = Field(default=..., description="""Email address of the person who performed the experiment. Written as #Experimenter_Contact: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'john.doe@email.com'}]} })
    description: str = Field(default=..., description="""Free-text description of the experiment and of the data recorded in this table. Should provide sufficient detail for interpretation and reproducibility. Written as #Description: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    softwares: list[Software] = Field(default=..., description="""One or more Software entries documenting every tool used to produce or process data in this table. Written as repeating #Software_* blocks in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    additional_tables: list[TableNamespaceEnum] = Field(default=..., description="""List of additional FOF-CT table namespaces being submitted alongside this table, separated by commas in the TSV header. Written as #Additional_Tables: in the file header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable']} })
    xyz_unit: XYZUnitEnum = Field(default=..., description="""Unit used to represent X, Y, Z spatial coordinates or distances in this table. Use 'micron' to avoid issues with Greek symbols. Values should be drawn from SI units of length. Written as ##XYZ_Unit= in the file header. Mandatory in every FOF-CT table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpotTable',
                       'DemultiplexingTable',
                       'TraceTable',
                       'RNASpotTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'micron'}]} })
    time_unit: Optional[TimeUnitEnum] = Field(default=None, description="""Unit used to represent time intervals in this table. Allowed values are SI time units plus 'min' and 'hr'. Written as ##Time_Unit= in the file header. Conditionally required (metric- triggered) when any time metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'sec'}]} })
    intensity_unit: Optional[str] = Field(default=None, description="""Unit used to represent intensity measurements in this table. Written as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered) when any intensity metric is reported in an optional column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'a.u.'}, {'value': 'photons'}]} })
    intensity_measurement_method: Optional[str] = Field(default=None, description="""Method used to perform intensity measurements, including how digital signals were converted to photon counts. Written as #Intensity_Measurement_Method: in the file header. Conditionally required (metric-triggered) when any intensity metric is reported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemultiplexingTable',
                       'TraceTable',
                       'SpotQualityTable',
                       'RNASpotQualityTable',
                       'SpotBiologicalTable',
                       'RNASpotBiologicalTable',
                       'CellTable',
                       'ExtraCellROITable',
                       'SubCellROITable',
                       'ROIMappingTable',
                       'SMLocalizationQualityTable',
                       'UndecodedLocalizationTable'],
         'examples': [{'value': 'Localization centroid intensity'},
                      {'value': 'Mean Fluorescence Intensity'}]} })
    undecoded_localizations: list[UndecodedLocalization] = Field(default=..., description="""The complete collection of UndecodedLocalization events constituting this dataset. Each entry corresponds to one data row in the TSV serialisation.""", json_schema_extra = { "linkml_meta": {'domain': 'UndecodedLocalizationTable',
         'domain_of': ['UndecodedLocalizationTable']} })

    @field_validator('fof_ct_version')
    def pattern_fof_ct_version(cls, v):
        pattern=re.compile(r"^v[0-9]+\.[0-9]+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fof_ct_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fof_ct_version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('experimenter_contact')
    def pattern_experimenter_contact(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experimenter_contact format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experimenter_contact format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Software.model_rebuild()
LocalizationMixin.model_rebuild()
SpotMixin.model_rebuild()
Spot.model_rebuild()
SpotTable.model_rebuild()
Localization.model_rebuild()
DemultiplexingTable.model_rebuild()
Trace.model_rebuild()
TraceTable.model_rebuild()
RNASpot.model_rebuild()
RNASpotTable.model_rebuild()
SpotQualityRecord.model_rebuild()
SpotQualityTable.model_rebuild()
RNASpotQualityRecord.model_rebuild()
RNASpotQualityTable.model_rebuild()
SpotBiologicalRecord.model_rebuild()
SpotBiologicalTable.model_rebuild()
RNASpotBiologicalRecord.model_rebuild()
RNASpotBiologicalTable.model_rebuild()
Cell.model_rebuild()
CellTable.model_rebuild()
ExtraCellROI.model_rebuild()
ExtraCellROITable.model_rebuild()
SubCellROI.model_rebuild()
SubCellROITable.model_rebuild()
ROIMapping.model_rebuild()
ROIMappingTable.model_rebuild()
SMLocalization.model_rebuild()
SMLocalizationTable.model_rebuild()
SMLocalizationQualityRecord.model_rebuild()
SMLocalizationQualityTable.model_rebuild()
UndecodedLocalization.model_rebuild()
UndecodedLocalizationTable.model_rebuild()
