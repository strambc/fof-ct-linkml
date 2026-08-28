# Auto generated from fof_ct.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-28T13:28:13
# Schema: fof_ct
#
# id: https://w3id.org/fof-ct
# description: Root schema for the FISH Omics Format for Chromatin Tracing (FOF-CT). Covers both modalities: FOF-bas-CT (ball-and-stick, tables 1–12) and FOF-vol-CT (volumetric, tables 13–15). Imports all fifteen table schemas that together constitute the complete FOF-CT data model. Each table schema in turn imports fof_bas_ct_common for shared slots, the Software class, and enumerations.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
FOF_CT = CurieNamespace('fof_ct', 'https://w3id.org/fof-ct/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FOF_CT


# Types

# Class references
class SpotSpotId(extended_int):
    pass


class LocalizationLocId(extended_int):
    pass


class TraceTraceId(extended_int):
    pass


class RNASpotRnaSpotId(extended_int):
    pass


class SpotQualityRecordSpotId(SpotSpotId):
    pass


class RNASpotQualityRecordRnaSpotId(RNASpotRnaSpotId):
    pass


class SpotBiologicalRecordSpotId(SpotSpotId):
    pass


class RNASpotBiologicalRecordRnaSpotId(RNASpotRnaSpotId):
    pass


class CellCellId(extended_int):
    pass


class ExtraCellROIExtraCellRoiId(extended_int):
    pass


class SubCellROISubCellRoiId(extended_int):
    pass


class SMLocalizationLocId(extended_int):
    pass


class SMLocalizationQualityRecordLocId(SMLocalizationLocId):
    pass


class UndecodedLocalizationLocId(extended_int):
    pass


@dataclass(repr=False)
class Software(YAMLRoot):
    """
    Provenance metadata for a single software tool used to produce or process data in a FOF-CT table. If more than one
    tool was used, a separate Software entry must be provided for each. Written as a repeating block of #Software_*
    fields in the file header.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["Software"]
    class_class_curie: ClassVar[str] = "fof_ct:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = FOF_CT.Software

    software_title: str = None
    software_type: Union[str, "SoftwareTypeEnum"] = None
    software_authors: str = None
    software_description: str = None
    software_parameters: str = None
    software_repository: Union[str, URI] = None
    software_preferred_citation_id: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.software_title):
            self.MissingRequiredField("software_title")
        if not isinstance(self.software_title, str):
            self.software_title = str(self.software_title)

        if self._is_empty(self.software_type):
            self.MissingRequiredField("software_type")
        if not isinstance(self.software_type, SoftwareTypeEnum):
            self.software_type = SoftwareTypeEnum(self.software_type)

        if self._is_empty(self.software_authors):
            self.MissingRequiredField("software_authors")
        if not isinstance(self.software_authors, str):
            self.software_authors = str(self.software_authors)

        if self._is_empty(self.software_description):
            self.MissingRequiredField("software_description")
        if not isinstance(self.software_description, str):
            self.software_description = str(self.software_description)

        if self._is_empty(self.software_parameters):
            self.MissingRequiredField("software_parameters")
        if not isinstance(self.software_parameters, str):
            self.software_parameters = str(self.software_parameters)

        if self._is_empty(self.software_repository):
            self.MissingRequiredField("software_repository")
        if not isinstance(self.software_repository, URI):
            self.software_repository = URI(self.software_repository)

        if self._is_empty(self.software_preferred_citation_id):
            self.MissingRequiredField("software_preferred_citation_id")
        if not isinstance(self.software_preferred_citation_id, URI):
            self.software_preferred_citation_id = URI(self.software_preferred_citation_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalizationMixin(YAMLRoot):
    """
    Mixin capturing the shared concept of a single localization event across FOF-CT modalities. Used by Localization
    (demultiplexing), SMLocalization (vol_core), and UndecodedLocalization (undecoded). All three classes represent
    the same atomic measurement unit — the sub-pixel position of a detected fluorescence emission event — but differ
    in context, mandatory columns, and table role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["LocalizationMixin"]
    class_class_curie: ClassVar[str] = "fof_ct:LocalizationMixin"
    class_name: ClassVar[str] = "LocalizationMixin"
    class_model_uri: ClassVar[URIRef] = FOF_CT.LocalizationMixin

    loc_id: Optional[int] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.loc_id is not None and not isinstance(self.loc_id, int):
            self.loc_id = int(self.loc_id)

        if self.x is not None and not isinstance(self.x, float):
            self.x = float(self.x)

        if self.y is not None and not isinstance(self.y, float):
            self.y = float(self.y)

        if self.z is not None and not isinstance(self.z, float):
            self.z = float(self.z)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotMixin(YAMLRoot):
    """
    Mixin capturing slots shared between DNA Spots (Spot, core table) and RNA Spots (RNASpot, RNA Spot Data table): 3D
    position and the optional spatial-context cross-references. Does NOT include the identifier slot, since Spot and
    RNASpot use different RTD-aligned identifier column names (Spot_ID vs. RNA_Spot_ID) and LinkML cannot rename an
    inherited identifier slot per subclass.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotMixin"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotMixin"
    class_name: ClassVar[str] = "SpotMixin"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotMixin

    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    sub_cell_roi_id: Optional[Union[int, SubCellROISubCellRoiId]] = None
    cell_id: Optional[Union[int, CellCellId]] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.x is not None and not isinstance(self.x, float):
            self.x = float(self.x)

        if self.y is not None and not isinstance(self.y, float):
            self.y = float(self.y)

        if self.z is not None and not isinstance(self.z, float):
            self.z = float(self.z)

        if self.sub_cell_roi_id is not None and not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Spot(YAMLRoot):
    """
    A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing experiment. Each instance of this
    class corresponds to one row in the TSV data section of the FOF-CT core table and represents a specific genomic
    target sequence localised in 3D space and assigned to a chromatin Trace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["Spot"]
    class_class_curie: ClassVar[str] = "fof_ct:Spot"
    class_name: ClassVar[str] = "Spot"
    class_model_uri: ClassVar[URIRef] = FOF_CT.Spot

    spot_id: Union[int, SpotSpotId] = None
    trace_id: Union[int, TraceTraceId] = None
    chrom: str = None
    chrom_start: int = None
    chrom_end: int = None
    x: float = None
    y: float = None
    z: float = None
    sub_cell_roi_id: Optional[Union[int, SubCellROISubCellRoiId]] = None
    cell_id: Optional[Union[int, CellCellId]] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spot_id):
            self.MissingRequiredField("spot_id")
        if not isinstance(self.spot_id, SpotSpotId):
            self.spot_id = SpotSpotId(self.spot_id)

        if self._is_empty(self.trace_id):
            self.MissingRequiredField("trace_id")
        if not isinstance(self.trace_id, TraceTraceId):
            self.trace_id = TraceTraceId(self.trace_id)

        if self._is_empty(self.chrom):
            self.MissingRequiredField("chrom")
        if not isinstance(self.chrom, str):
            self.chrom = str(self.chrom)

        if self._is_empty(self.chrom_start):
            self.MissingRequiredField("chrom_start")
        if not isinstance(self.chrom_start, int):
            self.chrom_start = int(self.chrom_start)

        if self._is_empty(self.chrom_end):
            self.MissingRequiredField("chrom_end")
        if not isinstance(self.chrom_end, int):
            self.chrom_end = int(self.chrom_end)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        if self.sub_cell_roi_id is not None and not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotTable(YAMLRoot):
    """
    The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_core). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotTable"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotTable"
    class_name: ClassVar[str] = "SpotTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotTable

    fof_ct_version: str = None
    table_namespace: str = None
    genome_assembly: str = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    spots: Union[dict[Union[int, SpotSpotId], Union[dict, Spot]], list[Union[dict, Spot]]] = empty_dict()
    modification: Optional[str] = None
    vcf_file_name: Optional[str] = None
    vcf_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.genome_assembly):
            self.MissingRequiredField("genome_assembly")
        if not isinstance(self.genome_assembly, str):
            self.genome_assembly = str(self.genome_assembly)

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.spots):
            self.MissingRequiredField("spots")
        self._normalize_inlined_as_list(slot_name="spots", slot_type=Spot, key_name="spot_id", keyed=True)

        if self.modification is not None and not isinstance(self.modification, str):
            self.modification = str(self.modification)

        if self.vcf_file_name is not None and not isinstance(self.vcf_file_name, str):
            self.vcf_file_name = str(self.vcf_file_name)

        if self.vcf_version is not None and not isinstance(self.vcf_version, str):
            self.vcf_version = str(self.vcf_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Localization(YAMLRoot):
    """
    A single individual localisation event contributing to the final position of a bright DNA Spot in a multiplexed
    FISH experiment (e.g. MERFISH). Each instance of this class corresponds to one row in the CSV data section of the
    FOF-CT Spot Demultiplexing table. The spot_id field links each Localization to its parent Spot in the core table
    (or RNA Spot Data table). This class accepts additional user-defined optional columns (e.g. Hyb, Brightness,
    Fit_Quality).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["Localization"]
    class_class_curie: ClassVar[str] = "fof_ct:Localization"
    class_name: ClassVar[str] = "Localization"
    class_model_uri: ClassVar[URIRef] = FOF_CT.Localization

    loc_id: Union[int, LocalizationLocId] = None
    spot_id: Union[int, SpotSpotId] = None
    channel_name: str = None
    fluorophore_name: str = None
    x: float = None
    y: float = None
    z: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.loc_id):
            self.MissingRequiredField("loc_id")
        if not isinstance(self.loc_id, LocalizationLocId):
            self.loc_id = LocalizationLocId(self.loc_id)

        if self._is_empty(self.spot_id):
            self.MissingRequiredField("spot_id")
        if not isinstance(self.spot_id, SpotSpotId):
            self.spot_id = SpotSpotId(self.spot_id)

        if self._is_empty(self.channel_name):
            self.MissingRequiredField("channel_name")
        if not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self._is_empty(self.fluorophore_name):
            self.MissingRequiredField("fluorophore_name")
        if not isinstance(self.fluorophore_name, str):
            self.fluorophore_name = str(self.fluorophore_name)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DemultiplexingTable(YAMLRoot):
    """
    The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_demultiplexing). This class
    represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV
    serialisation) together with the full collection of Localization events (recorded as data rows). Analogous to the
    MappingSet class in SSSOM. This table is optional but recommended for multiplexed FISH experiments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["DemultiplexingTable"]
    class_class_curie: ClassVar[str] = "fof_ct:DemultiplexingTable"
    class_name: ClassVar[str] = "DemultiplexingTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.DemultiplexingTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    localizations: Union[dict[Union[int, LocalizationLocId], Union[dict, Localization]], list[Union[dict, Localization]]] = empty_dict()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.localizations):
            self.MissingRequiredField("localizations")
        self._normalize_inlined_as_list(slot_name="localizations", slot_type=Localization, key_name="loc_id", keyed=True)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Trace(YAMLRoot):
    """
    A single chromatin Trace representing global properties associated with an entire polymeric trace rather than with
    individual Spots. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Trace
    Data table. The trace_id links each Trace to the core table and to the RNA Spot Data table. IMPORTANT: this class
    MUST contain at least one user-defined optional column describing trace-level properties (e.g., Allele,
    RNA_Expression, Lamina_Distance). User-defined columns are accommodated via open schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["Trace"]
    class_class_curie: ClassVar[str] = "fof_ct:Trace"
    class_name: ClassVar[str] = "Trace"
    class_model_uri: ClassVar[URIRef] = FOF_CT.Trace

    trace_id: Union[int, TraceTraceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trace_id):
            self.MissingRequiredField("trace_id")
        if not isinstance(self.trace_id, TraceTraceId):
            self.trace_id = TraceTraceId(self.trace_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TraceTable(YAMLRoot):
    """
    The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace). This class represents the entire file:
    it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together with
    the full collection of Traces (recorded as data rows). Analogous to the MappingSet class in SSSOM. This table is
    optional but recommended when trace-level properties are recorded.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["TraceTable"]
    class_class_curie: ClassVar[str] = "fof_ct:TraceTable"
    class_name: ClassVar[str] = "TraceTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.TraceTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    traces: Union[list[Union[int, TraceTraceId]], dict[Union[int, TraceTraceId], Union[dict, Trace]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.traces):
            self.MissingRequiredField("traces")
        self._normalize_inlined_as_list(slot_name="traces", slot_type=Trace, key_name="trace_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpot(YAMLRoot):
    """
    A single detected RNA bright Spot corresponding to one RNA transcript location detected alongside Chromatin
    Tracing. Each instance of this class corresponds to one row in the CSV data section of the FOF-CT RNA Spot Data
    table. The rna_spot_id links each RNASpot to the RNA Quality and RNA Biological Data tables; the trace_id links
    this RNA Spot to a DNA chromatin Trace in the core table and Trace Data table. This table's column list is fixed
    by the RTD (rna_columns.csv defines no Optional_Column placeholders); it does not accept additional user-defined
    columns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpot"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpot"
    class_name: ClassVar[str] = "RNASpot"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpot

    rna_spot_id: Union[int, RNASpotRnaSpotId] = None
    rna_name: str = None
    gene_id: str = None
    trace_id: Union[int, TraceTraceId] = None
    x: float = None
    y: float = None
    z: float = None
    transcript_id: Optional[str] = None
    sub_cell_roi_id: Optional[Union[int, SubCellROISubCellRoiId]] = None
    cell_id: Optional[Union[int, CellCellId]] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rna_spot_id):
            self.MissingRequiredField("rna_spot_id")
        if not isinstance(self.rna_spot_id, RNASpotRnaSpotId):
            self.rna_spot_id = RNASpotRnaSpotId(self.rna_spot_id)

        if self._is_empty(self.rna_name):
            self.MissingRequiredField("rna_name")
        if not isinstance(self.rna_name, str):
            self.rna_name = str(self.rna_name)

        if self._is_empty(self.gene_id):
            self.MissingRequiredField("gene_id")
        if not isinstance(self.gene_id, str):
            self.gene_id = str(self.gene_id)

        if self._is_empty(self.trace_id):
            self.MissingRequiredField("trace_id")
        if not isinstance(self.trace_id, TraceTraceId):
            self.trace_id = TraceTraceId(self.trace_id)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        if self.transcript_id is not None and not isinstance(self.transcript_id, str):
            self.transcript_id = str(self.transcript_id)

        if self.sub_cell_roi_id is not None and not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpotTable(YAMLRoot):
    """
    The RNA Spot Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna). This class represents the entire
    file: it holds all dataset-level provenance metadata (recorded as header lines in the CSV serialisation) together
    with the full collection of RNA Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM. This
    table is optional but recommended when RNA data are collected alongside Chromatin Tracing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpotTable"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpotTable"
    class_name: ClassVar[str] = "RNASpotTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpotTable

    fof_ct_version: str = None
    table_namespace: str = None
    genome_assembly: str = None
    gene_id_type: str = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    rna_spots: Union[dict[Union[int, RNASpotRnaSpotId], Union[dict, RNASpot]], list[Union[dict, RNASpot]]] = empty_dict()
    transcript_id_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.genome_assembly):
            self.MissingRequiredField("genome_assembly")
        if not isinstance(self.genome_assembly, str):
            self.genome_assembly = str(self.genome_assembly)

        if self._is_empty(self.gene_id_type):
            self.MissingRequiredField("gene_id_type")
        if not isinstance(self.gene_id_type, str):
            self.gene_id_type = str(self.gene_id_type)

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.rna_spots):
            self.MissingRequiredField("rna_spots")
        self._normalize_inlined_as_list(slot_name="rna_spots", slot_type=RNASpot, key_name="rna_spot_id", keyed=True)

        if self.transcript_id_type is not None and not isinstance(self.transcript_id_type, str):
            self.transcript_id_type = str(self.transcript_id_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotQualityRecord(YAMLRoot):
    """
    A single row in the Spot Quality table. Each instance captures one or more quality metrics for a specific DNA
    bright Spot identified by Spot_ID. At least one user-defined quality metric column MUST be present; users declare
    these via #^ header lines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotQualityRecord"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotQualityRecord"
    class_name: ClassVar[str] = "SpotQualityRecord"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotQualityRecord

    spot_id: Union[int, SpotQualityRecordSpotId] = None
    channel_name: str = None
    fluorophore_name: str = None
    x_precision: Optional[float] = None
    y_precision: Optional[float] = None
    z_precision: Optional[float] = None
    photon_count: Optional[int] = None
    goodness_of_fit: Optional[float] = None
    centroid_intensity: Optional[float] = None
    peak_intensity: Optional[float] = None
    raw_x: Optional[float] = None
    raw_y: Optional[float] = None
    raw_z: Optional[float] = None
    x_drift: Optional[float] = None
    y_drift: Optional[float] = None
    z_drift: Optional[float] = None
    x_chromatic_shift: Optional[float] = None
    y_chromatic_shift: Optional[float] = None
    z_chromatic_shift: Optional[float] = None
    x_loc_error: Optional[float] = None
    y_loc_error: Optional[float] = None
    z_loc_error: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spot_id):
            self.MissingRequiredField("spot_id")
        if not isinstance(self.spot_id, SpotQualityRecordSpotId):
            self.spot_id = SpotQualityRecordSpotId(self.spot_id)

        if self._is_empty(self.channel_name):
            self.MissingRequiredField("channel_name")
        if not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self._is_empty(self.fluorophore_name):
            self.MissingRequiredField("fluorophore_name")
        if not isinstance(self.fluorophore_name, str):
            self.fluorophore_name = str(self.fluorophore_name)

        if self.x_precision is not None and not isinstance(self.x_precision, float):
            self.x_precision = float(self.x_precision)

        if self.y_precision is not None and not isinstance(self.y_precision, float):
            self.y_precision = float(self.y_precision)

        if self.z_precision is not None and not isinstance(self.z_precision, float):
            self.z_precision = float(self.z_precision)

        if self.photon_count is not None and not isinstance(self.photon_count, int):
            self.photon_count = int(self.photon_count)

        if self.goodness_of_fit is not None and not isinstance(self.goodness_of_fit, float):
            self.goodness_of_fit = float(self.goodness_of_fit)

        if self.centroid_intensity is not None and not isinstance(self.centroid_intensity, float):
            self.centroid_intensity = float(self.centroid_intensity)

        if self.peak_intensity is not None and not isinstance(self.peak_intensity, float):
            self.peak_intensity = float(self.peak_intensity)

        if self.raw_x is not None and not isinstance(self.raw_x, float):
            self.raw_x = float(self.raw_x)

        if self.raw_y is not None and not isinstance(self.raw_y, float):
            self.raw_y = float(self.raw_y)

        if self.raw_z is not None and not isinstance(self.raw_z, float):
            self.raw_z = float(self.raw_z)

        if self.x_drift is not None and not isinstance(self.x_drift, float):
            self.x_drift = float(self.x_drift)

        if self.y_drift is not None and not isinstance(self.y_drift, float):
            self.y_drift = float(self.y_drift)

        if self.z_drift is not None and not isinstance(self.z_drift, float):
            self.z_drift = float(self.z_drift)

        if self.x_chromatic_shift is not None and not isinstance(self.x_chromatic_shift, float):
            self.x_chromatic_shift = float(self.x_chromatic_shift)

        if self.y_chromatic_shift is not None and not isinstance(self.y_chromatic_shift, float):
            self.y_chromatic_shift = float(self.y_chromatic_shift)

        if self.z_chromatic_shift is not None and not isinstance(self.z_chromatic_shift, float):
            self.z_chromatic_shift = float(self.z_chromatic_shift)

        if self.x_loc_error is not None and not isinstance(self.x_loc_error, float):
            self.x_loc_error = float(self.x_loc_error)

        if self.y_loc_error is not None and not isinstance(self.y_loc_error, float):
            self.y_loc_error = float(self.y_loc_error)

        if self.z_loc_error is not None and not isinstance(self.z_loc_error, float):
            self.z_loc_error = float(self.z_loc_error)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotQualityTable(YAMLRoot):
    """
    The Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_quality). This class represents the entire
    file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together
    with the full collection of SpotQualityRecord rows. Submission of this table is optional but recommended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotQualityTable"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotQualityTable"
    class_name: ClassVar[str] = "SpotQualityTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotQualityTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    spot_quality_records: Union[dict[Union[int, SpotQualityRecordSpotId], Union[dict, SpotQualityRecord]], list[Union[dict, SpotQualityRecord]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.spot_quality_records):
            self.MissingRequiredField("spot_quality_records")
        self._normalize_inlined_as_list(slot_name="spot_quality_records", slot_type=SpotQualityRecord, key_name="spot_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpotQualityRecord(YAMLRoot):
    """
    A single row in the RNA Spot Quality table. Each instance captures one or more quality metrics for a specific RNA
    bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the dataset, linking to the
    corresponding record in the RNA Spot Data table (table 4). RNA_Spot_ID, Channel and Fluor are mandatory; all other
    reserved quality-metric columns are conditionally required (the same reserved vocabulary as the Spot Quality
    table) or fully free-form; users declare the latter via #^ header lines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpotQualityRecord"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpotQualityRecord"
    class_name: ClassVar[str] = "RNASpotQualityRecord"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpotQualityRecord

    rna_spot_id: Union[int, RNASpotQualityRecordRnaSpotId] = None
    channel_name: str = None
    fluorophore_name: str = None
    x_precision: Optional[float] = None
    y_precision: Optional[float] = None
    z_precision: Optional[float] = None
    photon_count: Optional[int] = None
    goodness_of_fit: Optional[float] = None
    centroid_intensity: Optional[float] = None
    peak_intensity: Optional[float] = None
    raw_x: Optional[float] = None
    raw_y: Optional[float] = None
    raw_z: Optional[float] = None
    x_drift: Optional[float] = None
    y_drift: Optional[float] = None
    z_drift: Optional[float] = None
    x_chromatic_shift: Optional[float] = None
    y_chromatic_shift: Optional[float] = None
    z_chromatic_shift: Optional[float] = None
    x_loc_error: Optional[float] = None
    y_loc_error: Optional[float] = None
    z_loc_error: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rna_spot_id):
            self.MissingRequiredField("rna_spot_id")
        if not isinstance(self.rna_spot_id, RNASpotQualityRecordRnaSpotId):
            self.rna_spot_id = RNASpotQualityRecordRnaSpotId(self.rna_spot_id)

        if self._is_empty(self.channel_name):
            self.MissingRequiredField("channel_name")
        if not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self._is_empty(self.fluorophore_name):
            self.MissingRequiredField("fluorophore_name")
        if not isinstance(self.fluorophore_name, str):
            self.fluorophore_name = str(self.fluorophore_name)

        if self.x_precision is not None and not isinstance(self.x_precision, float):
            self.x_precision = float(self.x_precision)

        if self.y_precision is not None and not isinstance(self.y_precision, float):
            self.y_precision = float(self.y_precision)

        if self.z_precision is not None and not isinstance(self.z_precision, float):
            self.z_precision = float(self.z_precision)

        if self.photon_count is not None and not isinstance(self.photon_count, int):
            self.photon_count = int(self.photon_count)

        if self.goodness_of_fit is not None and not isinstance(self.goodness_of_fit, float):
            self.goodness_of_fit = float(self.goodness_of_fit)

        if self.centroid_intensity is not None and not isinstance(self.centroid_intensity, float):
            self.centroid_intensity = float(self.centroid_intensity)

        if self.peak_intensity is not None and not isinstance(self.peak_intensity, float):
            self.peak_intensity = float(self.peak_intensity)

        if self.raw_x is not None and not isinstance(self.raw_x, float):
            self.raw_x = float(self.raw_x)

        if self.raw_y is not None and not isinstance(self.raw_y, float):
            self.raw_y = float(self.raw_y)

        if self.raw_z is not None and not isinstance(self.raw_z, float):
            self.raw_z = float(self.raw_z)

        if self.x_drift is not None and not isinstance(self.x_drift, float):
            self.x_drift = float(self.x_drift)

        if self.y_drift is not None and not isinstance(self.y_drift, float):
            self.y_drift = float(self.y_drift)

        if self.z_drift is not None and not isinstance(self.z_drift, float):
            self.z_drift = float(self.z_drift)

        if self.x_chromatic_shift is not None and not isinstance(self.x_chromatic_shift, float):
            self.x_chromatic_shift = float(self.x_chromatic_shift)

        if self.y_chromatic_shift is not None and not isinstance(self.y_chromatic_shift, float):
            self.y_chromatic_shift = float(self.y_chromatic_shift)

        if self.z_chromatic_shift is not None and not isinstance(self.z_chromatic_shift, float):
            self.z_chromatic_shift = float(self.z_chromatic_shift)

        if self.x_loc_error is not None and not isinstance(self.x_loc_error, float):
            self.x_loc_error = float(self.x_loc_error)

        if self.y_loc_error is not None and not isinstance(self.y_loc_error, float):
            self.y_loc_error = float(self.y_loc_error)

        if self.z_loc_error is not None and not isinstance(self.z_loc_error, float):
            self.z_loc_error = float(self.z_loc_error)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpotQualityTable(YAMLRoot):
    """
    The RNA Spot Quality table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_quality). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of RNASpotQualityRecord rows. Submission of this table is optional but
    recommended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpotQualityTable"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpotQualityTable"
    class_name: ClassVar[str] = "RNASpotQualityTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpotQualityTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    rna_spot_quality_records: Union[dict[Union[int, RNASpotQualityRecordRnaSpotId], Union[dict, RNASpotQualityRecord]], list[Union[dict, RNASpotQualityRecord]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.rna_spot_quality_records):
            self.MissingRequiredField("rna_spot_quality_records")
        self._normalize_inlined_as_list(slot_name="rna_spot_quality_records", slot_type=RNASpotQualityRecord, key_name="rna_spot_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotBiologicalRecord(YAMLRoot):
    """
    A single row in the Spot Biological Data table. Each instance captures one or more user-defined biological
    properties for a specific DNA bright Spot identified by Spot_ID. Spot_ID values must be unique across the dataset,
    linking to the corresponding Spot record in the core table (table 1). At least one user-defined biological
    property column MUST be present; users declare these via #^ header lines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotBiologicalRecord"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotBiologicalRecord"
    class_name: ClassVar[str] = "SpotBiologicalRecord"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotBiologicalRecord

    spot_id: Union[int, SpotBiologicalRecordSpotId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spot_id):
            self.MissingRequiredField("spot_id")
        if not isinstance(self.spot_id, SpotBiologicalRecordSpotId):
            self.spot_id = SpotBiologicalRecordSpotId(self.spot_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpotBiologicalTable(YAMLRoot):
    """
    The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_bio). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of SpotBiologicalRecord rows. Submission of this table is optional but highly
    recommended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SpotBiologicalTable"]
    class_class_curie: ClassVar[str] = "fof_ct:SpotBiologicalTable"
    class_name: ClassVar[str] = "SpotBiologicalTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SpotBiologicalTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    spot_biological_records: Union[list[Union[int, SpotBiologicalRecordSpotId]], dict[Union[int, SpotBiologicalRecordSpotId], Union[dict, SpotBiologicalRecord]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.spot_biological_records):
            self.MissingRequiredField("spot_biological_records")
        self._normalize_inlined_as_list(slot_name="spot_biological_records", slot_type=SpotBiologicalRecord, key_name="spot_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpotBiologicalRecord(YAMLRoot):
    """
    A single row in the RNA Spot Biological Data table. Each instance captures one or more user-defined biological
    properties for a specific RNA bright Spot identified by RNA_Spot_ID. RNA_Spot_ID values must be unique across the
    dataset, linking to the corresponding record in the RNA Spot Data table (table 4). At least one user-defined
    biological property column MUST be present; users declare these via #^ header lines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpotBiologicalRecord"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpotBiologicalRecord"
    class_name: ClassVar[str] = "RNASpotBiologicalRecord"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpotBiologicalRecord

    rna_spot_id: Union[int, RNASpotBiologicalRecordRnaSpotId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rna_spot_id):
            self.MissingRequiredField("rna_spot_id")
        if not isinstance(self.rna_spot_id, RNASpotBiologicalRecordRnaSpotId):
            self.rna_spot_id = RNASpotBiologicalRecordRnaSpotId(self.rna_spot_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNASpotBiologicalTable(YAMLRoot):
    """
    The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_bio). This class represents
    the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV
    serialisation) together with the full collection of RNASpotBiologicalRecord rows. Submission of this table is
    optional but highly recommended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["RNASpotBiologicalTable"]
    class_class_curie: ClassVar[str] = "fof_ct:RNASpotBiologicalTable"
    class_name: ClassVar[str] = "RNASpotBiologicalTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.RNASpotBiologicalTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    rna_spot_biological_records: Union[list[Union[int, RNASpotBiologicalRecordRnaSpotId]], dict[Union[int, RNASpotBiologicalRecordRnaSpotId], Union[dict, RNASpotBiologicalRecord]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.rna_spot_biological_records):
            self.MissingRequiredField("rna_spot_biological_records")
        self._normalize_inlined_as_list(slot_name="rna_spot_biological_records", slot_type=RNASpotBiologicalRecord, key_name="rna_spot_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cell(YAMLRoot):
    """
    A single Cell identified in a FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV
    data section of the FOF-CT Cell Data table. The cell_id field uniquely identifies each Cell and links to the core
    table, the Sub-Cell ROI Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined
    optional columns (e.g. Cell_Size, Cell_Volume, Cell_Cycle_State, RNA_Spot_Count) via open schema. At least one
    such user-defined column MUST be present per submission.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["Cell"]
    class_class_curie: ClassVar[str] = "fof_ct:Cell"
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = FOF_CT.Cell

    cell_id: Union[int, CellCellId] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cell_id):
            self.MissingRequiredField("cell_id")
        if not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTable(YAMLRoot):
    """
    The Cell Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_cell). This class represents the entire file:
    it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with
    the full collection of Cells (recorded as data rows). This table is optional but recommended. Analogous to the
    MappingSet class in SSSOM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["CellTable"]
    class_class_curie: ClassVar[str] = "fof_ct:CellTable"
    class_name: ClassVar[str] = "CellTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.CellTable

    fof_ct_version: str = None
    table_namespace: str = None
    cell_type: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    cells: Union[dict[Union[int, CellCellId], Union[dict, Cell]], list[Union[dict, Cell]]] = empty_dict()
    extra_cell_roi_type: Optional[str] = None
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.cell_type):
            self.MissingRequiredField("cell_type")
        if not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.cells):
            self.MissingRequiredField("cells")
        self._normalize_inlined_as_list(slot_name="cells", slot_type=Cell, key_name="cell_id", keyed=True)

        if self.extra_cell_roi_type is not None and not isinstance(self.extra_cell_roi_type, str):
            self.extra_cell_roi_type = str(self.extra_cell_roi_type)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtraCellROI(YAMLRoot):
    """
    A single extracellular structure ROI (e.g. a tissue section or organoid) identified in a FOF-bas-CT experiment.
    Each instance of this class corresponds to one row in the TSV data section of the FOF-CT Extra-Cell ROI Data
    table. The extra_cell_roi_id field uniquely identifies each ROI and links to the core table, the RNA Spot Data
    table, and the Cell Data table. This class accepts additional user-defined optional columns (e.g. ROI_Volume,
    Cell_Count). At least one such user-defined column MUST be present per submission.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["ExtraCellROI"]
    class_class_curie: ClassVar[str] = "fof_ct:ExtraCellROI"
    class_name: ClassVar[str] = "ExtraCellROI"
    class_model_uri: ClassVar[URIRef] = FOF_CT.ExtraCellROI

    extra_cell_roi_id: Union[int, ExtraCellROIExtraCellRoiId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.extra_cell_roi_id):
            self.MissingRequiredField("extra_cell_roi_id")
        if not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtraCellROITable(YAMLRoot):
    """
    The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of extracellular ROIs (recorded as data rows). This table is optional but
    recommended. Analogous to the MappingSet class in SSSOM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["ExtraCellROITable"]
    class_class_curie: ClassVar[str] = "fof_ct:ExtraCellROITable"
    class_name: ClassVar[str] = "ExtraCellROITable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.ExtraCellROITable

    fof_ct_version: str = None
    table_namespace: str = None
    extra_cell_roi_type: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    extra_cell_rois: Union[list[Union[int, ExtraCellROIExtraCellRoiId]], dict[Union[int, ExtraCellROIExtraCellRoiId], Union[dict, ExtraCellROI]]] = empty_dict()
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.extra_cell_roi_type):
            self.MissingRequiredField("extra_cell_roi_type")
        if not isinstance(self.extra_cell_roi_type, str):
            self.extra_cell_roi_type = str(self.extra_cell_roi_type)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.extra_cell_rois):
            self.MissingRequiredField("extra_cell_rois")
        self._normalize_inlined_as_list(slot_name="extra_cell_rois", slot_type=ExtraCellROI, key_name="extra_cell_roi_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubCellROI(YAMLRoot):
    """
    A single sub-cellular structure ROI (e.g. nucleolus, nuclear lamina, PML body, chromosome domain) identified in a
    FOF-bas-CT experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT
    Sub-Cell ROI Data table. The sub_cell_roi_id field uniquely identifies each ROI and links to the core table, the
    Cell Data table, and the Cell/ROI Mapping table. This class accepts additional user-defined optional columns (e.g.
    ROI_Volume, ROI_Area). At least one such user-defined column MUST be present per submission.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SubCellROI"]
    class_class_curie: ClassVar[str] = "fof_ct:SubCellROI"
    class_name: ClassVar[str] = "SubCellROI"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SubCellROI

    sub_cell_roi_id: Union[int, SubCellROISubCellRoiId] = None
    cell_id: Optional[Union[int, CellCellId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sub_cell_roi_id):
            self.MissingRequiredField("sub_cell_roi_id")
        if not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubCellROITable(YAMLRoot):
    """
    The Sub-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_subcell). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of sub-cellular ROIs (recorded as data rows). This table is optional but
    recommended. Analogous to the MappingSet class in SSSOM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SubCellROITable"]
    class_class_curie: ClassVar[str] = "fof_ct:SubCellROITable"
    class_name: ClassVar[str] = "SubCellROITable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SubCellROITable

    fof_ct_version: str = None
    table_namespace: str = None
    sub_cell_roi_type: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    sub_cell_rois: Union[dict[Union[int, SubCellROISubCellRoiId], Union[dict, SubCellROI]], list[Union[dict, SubCellROI]]] = empty_dict()
    cell_type: Optional[str] = None
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.sub_cell_roi_type):
            self.MissingRequiredField("sub_cell_roi_type")
        if not isinstance(self.sub_cell_roi_type, str):
            self.sub_cell_roi_type = str(self.sub_cell_roi_type)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.sub_cell_rois):
            self.MissingRequiredField("sub_cell_rois")
        self._normalize_inlined_as_list(slot_name="sub_cell_rois", slot_type=SubCellROI, key_name="sub_cell_roi_id", keyed=True)

        if self.cell_type is not None and not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ROIMapping(YAMLRoot):
    """
    A single boundary record for one Cell, Sub-Cell ROI, or Extra-Cell ROI in a FOF-bas-CT experiment. Each instance
    corresponds to one row in the TSV data section of the FOF-CT Cell/ROI Mapping table. Exactly one of the three
    identifier slots (sub_cell_roi_id, cell_id, extra_cell_roi_id) must be populated per file; the choice of
    identifier must be consistent across all rows of a given submission. The roi_boundaries slot holds the boundary
    coordinates in the format specified by roi_boundaries_format in the table header. This class accepts additional
    user-defined optional columns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["ROIMapping"]
    class_class_curie: ClassVar[str] = "fof_ct:ROIMapping"
    class_name: ClassVar[str] = "ROIMapping"
    class_model_uri: ClassVar[URIRef] = FOF_CT.ROIMapping

    roi_boundaries: str = None
    sub_cell_roi_id: Optional[Union[int, SubCellROISubCellRoiId]] = None
    cell_id: Optional[Union[int, CellCellId]] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.roi_boundaries):
            self.MissingRequiredField("roi_boundaries")
        if not isinstance(self.roi_boundaries, str):
            self.roi_boundaries = str(self.roi_boundaries)

        if self.sub_cell_roi_id is not None and not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ROIMappingTable(YAMLRoot):
    """
    The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_mapping). This class represents the
    entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation)
    together with the full collection of ROI boundary records (recorded as data rows). This table is conditionally
    required whenever a Cell Data table, a Sub-Cell ROI Data table, or an Extra-Cell ROI Data table is deposited.
    Analogous to the MappingSet class in SSSOM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["ROIMappingTable"]
    class_class_curie: ClassVar[str] = "fof_ct:ROIMappingTable"
    class_name: ClassVar[str] = "ROIMappingTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.ROIMappingTable

    fof_ct_version: str = None
    table_namespace: str = None
    roi_boundaries_format_type: Union[str, "ROIBoundariesFormatTypeEnum"] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    roi_mappings: Union[Union[dict, ROIMapping], list[Union[dict, ROIMapping]]] = None
    roi_boundaries_format_description: Optional[str] = None
    cell_type: Optional[str] = None
    sub_cell_roi_type: Optional[str] = None
    extra_cell_roi_type: Optional[str] = None
    softwares: Optional[Union[Union[dict, Software], list[Union[dict, Software]]]] = empty_list()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.roi_boundaries_format_type):
            self.MissingRequiredField("roi_boundaries_format_type")
        if not isinstance(self.roi_boundaries_format_type, ROIBoundariesFormatTypeEnum):
            self.roi_boundaries_format_type = ROIBoundariesFormatTypeEnum(self.roi_boundaries_format_type)

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.roi_mappings):
            self.MissingRequiredField("roi_mappings")
        self._normalize_inlined_as_list(slot_name="roi_mappings", slot_type=ROIMapping, key_name="roi_boundaries", keyed=False)

        if self.roi_boundaries_format_description is not None and not isinstance(self.roi_boundaries_format_description, str):
            self.roi_boundaries_format_description = str(self.roi_boundaries_format_description)

        if self.cell_type is not None and not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        if self.sub_cell_roi_type is not None and not isinstance(self.sub_cell_roi_type, str):
            self.sub_cell_roi_type = str(self.sub_cell_roi_type)

        if self.extra_cell_roi_type is not None and not isinstance(self.extra_cell_roi_type, str):
            self.extra_cell_roi_type = str(self.extra_cell_roi_type)

        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SMLocalization(YAMLRoot):
    """
    A single individual single-molecule (SM) localization event in a FOF-vol-CT dataset. Each instance corresponds to
    one row in the TSV data section of the SM Localization Data table. The loc_id field is the primary key; spot_id
    links this localization to its parent Spot (if Spot/Trace post-processing was performed); trace_id links it to its
    parent Trace. Sub_Cell_ROI_ID, Cell_ID and Extra_Cell_ROI_ID optionally link the localization to spatial context
    tables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SMLocalization"]
    class_class_curie: ClassVar[str] = "fof_ct:SMLocalization"
    class_name: ClassVar[str] = "SMLocalization"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SMLocalization

    loc_id: Union[int, SMLocalizationLocId] = None
    spot_id: Union[int, SpotSpotId] = None
    trace_id: Union[int, TraceTraceId] = None
    chrom: str = None
    chrom_start: int = None
    chrom_end: int = None
    x: float = None
    y: float = None
    z: float = None
    sub_cell_roi_id: Optional[Union[int, SubCellROISubCellRoiId]] = None
    cell_id: Optional[Union[int, CellCellId]] = None
    extra_cell_roi_id: Optional[Union[int, ExtraCellROIExtraCellRoiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.loc_id):
            self.MissingRequiredField("loc_id")
        if not isinstance(self.loc_id, SMLocalizationLocId):
            self.loc_id = SMLocalizationLocId(self.loc_id)

        if self._is_empty(self.spot_id):
            self.MissingRequiredField("spot_id")
        if not isinstance(self.spot_id, SpotSpotId):
            self.spot_id = SpotSpotId(self.spot_id)

        if self._is_empty(self.trace_id):
            self.MissingRequiredField("trace_id")
        if not isinstance(self.trace_id, TraceTraceId):
            self.trace_id = TraceTraceId(self.trace_id)

        if self._is_empty(self.chrom):
            self.MissingRequiredField("chrom")
        if not isinstance(self.chrom, str):
            self.chrom = str(self.chrom)

        if self._is_empty(self.chrom_start):
            self.MissingRequiredField("chrom_start")
        if not isinstance(self.chrom_start, int):
            self.chrom_start = int(self.chrom_start)

        if self._is_empty(self.chrom_end):
            self.MissingRequiredField("chrom_end")
        if not isinstance(self.chrom_end, int):
            self.chrom_end = int(self.chrom_end)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        if self.sub_cell_roi_id is not None and not isinstance(self.sub_cell_roi_id, SubCellROISubCellRoiId):
            self.sub_cell_roi_id = SubCellROISubCellRoiId(self.sub_cell_roi_id)

        if self.cell_id is not None and not isinstance(self.cell_id, CellCellId):
            self.cell_id = CellCellId(self.cell_id)

        if self.extra_cell_roi_id is not None and not isinstance(self.extra_cell_roi_id, ExtraCellROIExtraCellRoiId):
            self.extra_cell_roi_id = ExtraCellROIExtraCellRoiId(self.extra_cell_roi_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SMLocalizationTable(YAMLRoot):
    """
    The SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_vol_core, no 4dn_ prefix). This is the
    mandatory primary data table for volumetric FOF-CT submissions. Each row corresponds to one SM localization event.
    The Spot/Trace Data table is optional for FOF-vol-CT submissions but may be included to report post-processing
    results derived from the localization data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SMLocalizationTable"]
    class_class_curie: ClassVar[str] = "fof_ct:SMLocalizationTable"
    class_name: ClassVar[str] = "SMLocalizationTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SMLocalizationTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    genome_assembly: str = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    sm_localizations: Union[dict[Union[int, SMLocalizationLocId], Union[dict, SMLocalization]], list[Union[dict, SMLocalization]]] = empty_dict()
    modification: Optional[str] = None
    vcf_file_name: Optional[str] = None
    vcf_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.genome_assembly):
            self.MissingRequiredField("genome_assembly")
        if not isinstance(self.genome_assembly, str):
            self.genome_assembly = str(self.genome_assembly)

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.sm_localizations):
            self.MissingRequiredField("sm_localizations")
        self._normalize_inlined_as_list(slot_name="sm_localizations", slot_type=SMLocalization, key_name="loc_id", keyed=True)

        if self.modification is not None and not isinstance(self.modification, str):
            self.modification = str(self.modification)

        if self.vcf_file_name is not None and not isinstance(self.vcf_file_name, str):
            self.vcf_file_name = str(self.vcf_file_name)

        if self.vcf_version is not None and not isinstance(self.vcf_version, str):
            self.vcf_version = str(self.vcf_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SMLocalizationQualityRecord(YAMLRoot):
    """
    A single row in the SM Localization Quality table. Each instance captures quality metrics for one SM localization
    event identified by Loc_ID. Loc_ID, Channel and Fluor are mandatory. X_Loc_Precision, Y_Loc_Precision,
    Z_Loc_Precision and Photon_Count are highly recommended but not literally mandatory. All other reserved metric
    columns are conditionally required (use of the reserved name is optional, but mandatory if that metric is
    reported). Additional user-defined optional columns must be described in the file header.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SMLocalizationQualityRecord"]
    class_class_curie: ClassVar[str] = "fof_ct:SMLocalizationQualityRecord"
    class_name: ClassVar[str] = "SMLocalizationQualityRecord"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SMLocalizationQualityRecord

    loc_id: Union[int, SMLocalizationQualityRecordLocId] = None
    channel_name: str = None
    fluorophore_name: str = None
    x_precision: Optional[float] = None
    y_precision: Optional[float] = None
    z_precision: Optional[float] = None
    photon_count: Optional[int] = None
    goodness_of_fit: Optional[float] = None
    centroid_intensity: Optional[float] = None
    peak_intensity: Optional[float] = None
    raw_x: Optional[float] = None
    raw_y: Optional[float] = None
    raw_z: Optional[float] = None
    x_loc_error: Optional[float] = None
    y_loc_error: Optional[float] = None
    z_loc_error: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.loc_id):
            self.MissingRequiredField("loc_id")
        if not isinstance(self.loc_id, SMLocalizationQualityRecordLocId):
            self.loc_id = SMLocalizationQualityRecordLocId(self.loc_id)

        if self._is_empty(self.channel_name):
            self.MissingRequiredField("channel_name")
        if not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self._is_empty(self.fluorophore_name):
            self.MissingRequiredField("fluorophore_name")
        if not isinstance(self.fluorophore_name, str):
            self.fluorophore_name = str(self.fluorophore_name)

        if self.x_precision is not None and not isinstance(self.x_precision, float):
            self.x_precision = float(self.x_precision)

        if self.y_precision is not None and not isinstance(self.y_precision, float):
            self.y_precision = float(self.y_precision)

        if self.z_precision is not None and not isinstance(self.z_precision, float):
            self.z_precision = float(self.z_precision)

        if self.photon_count is not None and not isinstance(self.photon_count, int):
            self.photon_count = int(self.photon_count)

        if self.goodness_of_fit is not None and not isinstance(self.goodness_of_fit, float):
            self.goodness_of_fit = float(self.goodness_of_fit)

        if self.centroid_intensity is not None and not isinstance(self.centroid_intensity, float):
            self.centroid_intensity = float(self.centroid_intensity)

        if self.peak_intensity is not None and not isinstance(self.peak_intensity, float):
            self.peak_intensity = float(self.peak_intensity)

        if self.raw_x is not None and not isinstance(self.raw_x, float):
            self.raw_x = float(self.raw_x)

        if self.raw_y is not None and not isinstance(self.raw_y, float):
            self.raw_y = float(self.raw_y)

        if self.raw_z is not None and not isinstance(self.raw_z, float):
            self.raw_z = float(self.raw_z)

        if self.x_loc_error is not None and not isinstance(self.x_loc_error, float):
            self.x_loc_error = float(self.x_loc_error)

        if self.y_loc_error is not None and not isinstance(self.y_loc_error, float):
            self.y_loc_error = float(self.y_loc_error)

        if self.z_loc_error is not None and not isinstance(self.z_loc_error, float):
            self.z_loc_error = float(self.z_loc_error)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SMLocalizationQualityTable(YAMLRoot):
    """
    The SM Localization Quality table of a FOF-vol-CT dataset (namespace: FOF-CT_vol_quality, no 4dn_ prefix).
    Requirement level: optional (recommended). Only vol_core (table 13) is mandatory for FOF-vol-CT submissions; this
    table provides localization quality metrics indexed by Loc_ID when submitted.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["SMLocalizationQualityTable"]
    class_class_curie: ClassVar[str] = "fof_ct:SMLocalizationQualityTable"
    class_name: ClassVar[str] = "SMLocalizationQualityTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.SMLocalizationQualityTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    sm_localization_quality_records: Union[dict[Union[int, SMLocalizationQualityRecordLocId], Union[dict, SMLocalizationQualityRecord]], list[Union[dict, SMLocalizationQualityRecord]]] = empty_dict()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.sm_localization_quality_records):
            self.MissingRequiredField("sm_localization_quality_records")
        self._normalize_inlined_as_list(slot_name="sm_localization_quality_records", slot_type=SMLocalizationQualityRecord, key_name="loc_id", keyed=True)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UndecodedLocalization(YAMLRoot):
    """
    A single raw, undecoded SM localization event in a FOF-vol-CT dataset. Each instance corresponds to one row in the
    TSV data section of the Undecoded SM Localization Data table. This class uses LocalizationMixin for the shared
    loc_id, x, y, z slots. The 8 mandatory columns, in order, are: Loc_ID, Hyb_ID, Image_Frame_ID, X, Y, Z, Channel,
    Fluor. TheZ (the_z) is a reserved, conditionally-required column for the focal Z-plane identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["UndecodedLocalization"]
    class_class_curie: ClassVar[str] = "fof_ct:UndecodedLocalization"
    class_name: ClassVar[str] = "UndecodedLocalization"
    class_model_uri: ClassVar[URIRef] = FOF_CT.UndecodedLocalization

    loc_id: Union[int, UndecodedLocalizationLocId] = None
    hyb_id: int = None
    image_frame_id: int = None
    channel_name: str = None
    fluorophore_name: str = None
    x: float = None
    y: float = None
    z: float = None
    the_z: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.loc_id):
            self.MissingRequiredField("loc_id")
        if not isinstance(self.loc_id, UndecodedLocalizationLocId):
            self.loc_id = UndecodedLocalizationLocId(self.loc_id)

        if self._is_empty(self.hyb_id):
            self.MissingRequiredField("hyb_id")
        if not isinstance(self.hyb_id, int):
            self.hyb_id = int(self.hyb_id)

        if self._is_empty(self.image_frame_id):
            self.MissingRequiredField("image_frame_id")
        if not isinstance(self.image_frame_id, int):
            self.image_frame_id = int(self.image_frame_id)

        if self._is_empty(self.channel_name):
            self.MissingRequiredField("channel_name")
        if not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self._is_empty(self.fluorophore_name):
            self.MissingRequiredField("fluorophore_name")
        if not isinstance(self.fluorophore_name, str):
            self.fluorophore_name = str(self.fluorophore_name)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        if self.the_z is not None and not isinstance(self.the_z, int):
            self.the_z = int(self.the_z)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UndecodedLocalizationTable(YAMLRoot):
    """
    The Undecoded SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_undecoded, no 4dn_ prefix).
    This table is optional but recommended. It records raw localization detections prior to any decoding or assignment
    step. Submission is recommended when the raw detections are available and reproducibility of the decoding pipeline
    is desired.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOF_CT["UndecodedLocalizationTable"]
    class_class_curie: ClassVar[str] = "fof_ct:UndecodedLocalizationTable"
    class_name: ClassVar[str] = "UndecodedLocalizationTable"
    class_model_uri: ClassVar[URIRef] = FOF_CT.UndecodedLocalizationTable

    fof_ct_version: str = None
    table_namespace: str = None
    lab_name: str = None
    experimenter_name: str = None
    experimenter_contact: str = None
    description: str = None
    softwares: Union[Union[dict, Software], list[Union[dict, Software]]] = None
    additional_tables: Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]] = None
    xyz_unit: Union[str, "XYZUnitEnum"] = None
    undecoded_localizations: Union[dict[Union[int, UndecodedLocalizationLocId], Union[dict, UndecodedLocalization]], list[Union[dict, UndecodedLocalization]]] = empty_dict()
    time_unit: Optional[Union[str, "TimeUnitEnum"]] = None
    intensity_unit: Optional[str] = None
    intensity_measurement_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fof_ct_version):
            self.MissingRequiredField("fof_ct_version")
        if not isinstance(self.fof_ct_version, str):
            self.fof_ct_version = str(self.fof_ct_version)

        if self._is_empty(self.table_namespace):
            self.MissingRequiredField("table_namespace")
        if not isinstance(self.table_namespace, str):
            self.table_namespace = str(self.table_namespace)

        if self._is_empty(self.lab_name):
            self.MissingRequiredField("lab_name")
        if not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self._is_empty(self.experimenter_name):
            self.MissingRequiredField("experimenter_name")
        if not isinstance(self.experimenter_name, str):
            self.experimenter_name = str(self.experimenter_name)

        if self._is_empty(self.experimenter_contact):
            self.MissingRequiredField("experimenter_contact")
        if not isinstance(self.experimenter_contact, str):
            self.experimenter_contact = str(self.experimenter_contact)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.softwares):
            self.MissingRequiredField("softwares")
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="software_title", keyed=False)

        if self._is_empty(self.additional_tables):
            self.MissingRequiredField("additional_tables")
        if not isinstance(self.additional_tables, list):
            self.additional_tables = [self.additional_tables] if self.additional_tables is not None else []
        self.additional_tables = [v if isinstance(v, TableNamespaceEnum) else TableNamespaceEnum(v) for v in self.additional_tables]

        if self._is_empty(self.xyz_unit):
            self.MissingRequiredField("xyz_unit")
        if not isinstance(self.xyz_unit, XYZUnitEnum):
            self.xyz_unit = XYZUnitEnum(self.xyz_unit)

        if self._is_empty(self.undecoded_localizations):
            self.MissingRequiredField("undecoded_localizations")
        self._normalize_inlined_as_list(slot_name="undecoded_localizations", slot_type=UndecodedLocalization, key_name="loc_id", keyed=True)

        if self.time_unit is not None and not isinstance(self.time_unit, TimeUnitEnum):
            self.time_unit = TimeUnitEnum(self.time_unit)

        if self.intensity_unit is not None and not isinstance(self.intensity_unit, str):
            self.intensity_unit = str(self.intensity_unit)

        if self.intensity_measurement_method is not None and not isinstance(self.intensity_measurement_method, str):
            self.intensity_measurement_method = str(self.intensity_measurement_method)

        super().__post_init__(**kwargs)


# Enumerations
class XYZUnitEnum(EnumDefinitionImpl):
    """
    Allowed units for X, Y, Z spatial coordinates or distances.
    """
    nm = PermissibleValue(
        text="nm",
        description="Nanometres")
    micron = PermissibleValue(
        text="micron",
        description="Micrometres. Use 'micron' rather than the Greek symbol μm to avoid encoding issues.")
    mm = PermissibleValue(
        text="mm",
        description="Millimetres")

    _defn = EnumDefinition(
        name="XYZUnitEnum",
        description="Allowed units for X, Y, Z spatial coordinates or distances.",
    )

class TimeUnitEnum(EnumDefinitionImpl):
    """
    Allowed units for time intervals.
    """
    s = PermissibleValue(
        text="s",
        description="Seconds (SI base unit)")
    sec = PermissibleValue(
        text="sec",
        description="Seconds (alternative spelling accepted by FOF-CT)")
    ms = PermissibleValue(
        text="ms",
        description="Milliseconds")
    msec = PermissibleValue(
        text="msec",
        description="Milliseconds (alternative spelling accepted by FOF-CT)")
    min = PermissibleValue(
        text="min",
        description="Minutes")
    hr = PermissibleValue(
        text="hr",
        description="Hours")

    _defn = EnumDefinition(
        name="TimeUnitEnum",
        description="Allowed units for time intervals.",
    )

class SoftwareTypeEnum(EnumDefinitionImpl):
    """
    Allowed functional categories for software tools (per the FOF-CT RTD "Allowable value lists" table for
    Software_Type).
    """
    DriftCorrection = PermissibleValue(
        text="DriftCorrection",
        description="Drift correction software")
    Segmentation = PermissibleValue(
        text="Segmentation",
        description="Image segmentation software")
    SpotLoc = PermissibleValue(
        text="SpotLoc",
        description="Spot localisation software")
    Tracing = PermissibleValue(
        text="Tracing",
        description="Chromatin tracing software")
    Other = PermissibleValue(
        text="Other",
        description="Other software type")

    _defn = EnumDefinition(
        name="SoftwareTypeEnum",
        description="""Allowed functional categories for software tools (per the FOF-CT RTD \"Allowable value lists\" table for Software_Type).""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Distance Calculation",
            PermissibleValue(
                text="Distance Calculation",
                description="Distance calculation software"))
        setattr(cls, "Precision Assessment",
            PermissibleValue(
                text="Precision Assessment",
                description="Localization/tracing precision assessment software"))
        setattr(cls, "Single Molecule Localization",
            PermissibleValue(
                text="Single Molecule Localization",
                description="Single-molecule localization software (FOF-vol-CT)"))
        setattr(cls, "SpotLoc+Tracing",
            PermissibleValue(
                text="SpotLoc+Tracing",
                description="Combined spot localisation and tracing software"))

class TableNamespaceEnum(EnumDefinitionImpl):
    """
    Allowed namespace identifiers for FOF-CT tables that may be listed in the additional_tables field. Note: per the
    FOF-CT RTD, the three FOF-vol-CT-exclusive namespaces (vol_core, vol_quality, undecoded) intentionally omit the
    4dn_ prefix used by the 12 shared tables, to reflect the format's continued stewardship by the broader community
    beyond 4DN.
    """
    _defn = EnumDefinition(
        name="TableNamespaceEnum",
        description="""Allowed namespace identifiers for FOF-CT tables that may be listed in the additional_tables field. Note: per the FOF-CT RTD, the three FOF-vol-CT-exclusive namespaces (vol_core, vol_quality, undecoded) intentionally omit the 4dn_ prefix used by the 12 shared tables, to reflect the format's continued stewardship by the broader community beyond 4DN.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "4dn_FOF-CT_core",
            PermissibleValue(
                text="4dn_FOF-CT_core",
                description="DNA-Spot/Trace Data core table (table 1)"))
        setattr(cls, "4dn_FOF-CT_demultiplexing",
            PermissibleValue(
                text="4dn_FOF-CT_demultiplexing",
                description="Spot Demultiplexing table (table 2)"))
        setattr(cls, "4dn_FOF-CT_trace",
            PermissibleValue(
                text="4dn_FOF-CT_trace",
                description="Trace Data table (table 3)"))
        setattr(cls, "4dn_FOF-CT_rna",
            PermissibleValue(
                text="4dn_FOF-CT_rna",
                description="RNA Spot Data table (table 4)"))
        setattr(cls, "4dn_FOF-CT_quality",
            PermissibleValue(
                text="4dn_FOF-CT_quality",
                description="Spot Quality table (table 5)"))
        setattr(cls, "4dn_FOF-CT_rna_quality",
            PermissibleValue(
                text="4dn_FOF-CT_rna_quality",
                description="RNA Spot Quality table (table 6)"))
        setattr(cls, "4dn_FOF-CT_bio",
            PermissibleValue(
                text="4dn_FOF-CT_bio",
                description="Spot Biological Data table (table 7)"))
        setattr(cls, "4dn_FOF-CT_rna_bio",
            PermissibleValue(
                text="4dn_FOF-CT_rna_bio",
                description="RNA Spot Biological Data table (table 8)"))
        setattr(cls, "4dn_FOF-CT_cell",
            PermissibleValue(
                text="4dn_FOF-CT_cell",
                description="Cell Data table (table 9)"))
        setattr(cls, "4dn_FOF-CT_extracell",
            PermissibleValue(
                text="4dn_FOF-CT_extracell",
                description="Extra-Cell ROI Data table (table 10)"))
        setattr(cls, "4dn_FOF-CT_subcell",
            PermissibleValue(
                text="4dn_FOF-CT_subcell",
                description="Sub-Cell ROI Data table (table 11)"))
        setattr(cls, "4dn_FOF-CT_mapping",
            PermissibleValue(
                text="4dn_FOF-CT_mapping",
                description="Cell/ROI Mapping table (table 12)"))
        setattr(cls, "FOF-CT_vol_core",
            PermissibleValue(
                text="FOF-CT_vol_core",
                description="""SM Localization Data table — FOF-vol-CT (table 13). No 4dn_ prefix (see enum-level note)."""))
        setattr(cls, "FOF-CT_vol_quality",
            PermissibleValue(
                text="FOF-CT_vol_quality",
                description="""SM Localization Quality table — FOF-vol-CT (table 14). No 4dn_ prefix (see enum-level note)."""))
        setattr(cls, "FOF-CT_undecoded",
            PermissibleValue(
                text="FOF-CT_undecoded",
                description="""Undecoded SM Localization Data table — FOF-vol-CT (table 15). No 4dn_ prefix (see enum-level note)."""))

class ROIBoundariesFormatTypeEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI Mapping table (per the FOF-CT RTD
    "Allowable value lists" table). Default value is OME_Polygon.
    """
    OME_Polygon = PermissibleValue(
        text="OME_Polygon",
        description="OME ROI data model, polygon representation (default).")
    OME_Mask = PermissibleValue(
        text="OME_Mask",
        description="OME ROI data model, mask representation.")
    Mesh_OBJ = PermissibleValue(
        text="Mesh_OBJ",
        description="3D mesh boundary described using the Wavefront OBJ format.")
    Mesh_STL = PermissibleValue(
        text="Mesh_STL",
        description="3D mesh boundary described using the STL format.")
    Mesh_PLY = PermissibleValue(
        text="Mesh_PLY",
        description="3D mesh boundary described using the PLY format.")
    GeoJSON = PermissibleValue(
        text="GeoJSON",
        description="Boundary described using the GeoJSON format.")
    WKT = PermissibleValue(
        text="WKT",
        description="Boundary described using Well-Known Text.")
    Label_Mask_Image = PermissibleValue(
        text="Label_Mask_Image",
        description="Boundary described as a labeled mask image.")
    Other = PermissibleValue(
        text="Other",
        description="Any other boundary format. When used, ROI_Boundaries_Format_Description becomes mandatory.")

    _defn = EnumDefinition(
        name="ROIBoundariesFormatTypeEnum",
        description="""Controlled vocabulary for ##ROI_Boundaries_Format_Type= in the Cell/ROI Mapping table (per the FOF-CT RTD \"Allowable value lists\" table). Default value is OME_Polygon.""",
    )

# Slots
class slots:
    pass

slots.fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.fof_ct_version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.table_namespace = Slot(uri=FOF_CT.table_namespace, name="table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.table_namespace, domain=None, range=Optional[str])

slots.lab_name = Slot(uri=FOF_CT.lab_name, name="lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.lab_name, domain=None, range=Optional[str])

slots.experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.experimenter_name, domain=None, range=Optional[str])

slots.experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.experimenter_contact, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.description = Slot(uri=FOF_CT.description, name="description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.description, domain=None, range=Optional[str])

slots.additional_tables = Slot(uri=FOF_CT.additional_tables, name="additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.additional_tables, domain=None, range=Optional[Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]]])

slots.softwares = Slot(uri=FOF_CT.softwares, name="softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.softwares, domain=None, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.xyz_unit, domain=None, range=Union[str, "XYZUnitEnum"])

slots.time_unit = Slot(uri=FOF_CT.time_unit, name="time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.time_unit, domain=None, range=Optional[Union[str, "TimeUnitEnum"]])

slots.intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.intensity_unit, domain=None, range=Optional[str])

slots.intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.intensity_measurement_method, domain=None, range=Optional[str])

slots.x = Slot(uri=FOF_CT.x, name="x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.x, domain=None, range=Optional[float])

slots.y = Slot(uri=FOF_CT.y, name="y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.y, domain=None, range=Optional[float])

slots.z = Slot(uri=FOF_CT.z, name="z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.z, domain=None, range=Optional[float])

slots.loc_id = Slot(uri=FOF_CT.loc_id, name="loc_id", curie=FOF_CT.curie('loc_id'),
                   model_uri=FOF_CT.loc_id, domain=None, range=Optional[int])

slots.spot_id = Slot(uri=FOF_CT.spot_id, name="spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.spot_id, domain=None, range=Optional[Union[int, SpotSpotId]])

slots.trace_id = Slot(uri=FOF_CT.trace_id, name="trace_id", curie=FOF_CT.curie('trace_id'),
                   model_uri=FOF_CT.trace_id, domain=None, range=Optional[Union[int, TraceTraceId]])

slots.sub_cell_roi_id = Slot(uri=FOF_CT.sub_cell_roi_id, name="sub_cell_roi_id", curie=FOF_CT.curie('sub_cell_roi_id'),
                   model_uri=FOF_CT.sub_cell_roi_id, domain=None, range=Optional[Union[int, SubCellROISubCellRoiId]])

slots.cell_id = Slot(uri=FOF_CT.cell_id, name="cell_id", curie=FOF_CT.curie('cell_id'),
                   model_uri=FOF_CT.cell_id, domain=None, range=Optional[Union[int, CellCellId]])

slots.extra_cell_roi_id = Slot(uri=FOF_CT.extra_cell_roi_id, name="extra_cell_roi_id", curie=FOF_CT.curie('extra_cell_roi_id'),
                   model_uri=FOF_CT.extra_cell_roi_id, domain=None, range=Optional[Union[int, ExtraCellROIExtraCellRoiId]])

slots.chrom = Slot(uri=FOF_CT.chrom, name="chrom", curie=FOF_CT.curie('chrom'),
                   model_uri=FOF_CT.chrom, domain=None, range=Optional[str])

slots.chrom_start = Slot(uri=FOF_CT.chrom_start, name="chrom_start", curie=FOF_CT.curie('chrom_start'),
                   model_uri=FOF_CT.chrom_start, domain=None, range=Optional[int])

slots.chrom_end = Slot(uri=FOF_CT.chrom_end, name="chrom_end", curie=FOF_CT.curie('chrom_end'),
                   model_uri=FOF_CT.chrom_end, domain=None, range=Optional[int])

slots.rna_spot_id = Slot(uri=FOF_CT.rna_spot_id, name="rna_spot_id", curie=FOF_CT.curie('rna_spot_id'),
                   model_uri=FOF_CT.rna_spot_id, domain=None, range=Optional[Union[int, RNASpotRnaSpotId]])

slots.channel_name = Slot(uri=FOF_CT.channel_name, name="channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.channel_name, domain=None, range=Optional[str])

slots.fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.fluorophore_name, domain=None, range=Optional[str])

slots.x_precision = Slot(uri=FOF_CT.x_precision, name="x_precision", curie=FOF_CT.curie('x_precision'),
                   model_uri=FOF_CT.x_precision, domain=None, range=Optional[float])

slots.y_precision = Slot(uri=FOF_CT.y_precision, name="y_precision", curie=FOF_CT.curie('y_precision'),
                   model_uri=FOF_CT.y_precision, domain=None, range=Optional[float])

slots.z_precision = Slot(uri=FOF_CT.z_precision, name="z_precision", curie=FOF_CT.curie('z_precision'),
                   model_uri=FOF_CT.z_precision, domain=None, range=Optional[float])

slots.photon_count = Slot(uri=FOF_CT.photon_count, name="photon_count", curie=FOF_CT.curie('photon_count'),
                   model_uri=FOF_CT.photon_count, domain=None, range=Optional[int])

slots.goodness_of_fit = Slot(uri=FOF_CT.goodness_of_fit, name="goodness_of_fit", curie=FOF_CT.curie('goodness_of_fit'),
                   model_uri=FOF_CT.goodness_of_fit, domain=None, range=Optional[float])

slots.centroid_intensity = Slot(uri=FOF_CT.centroid_intensity, name="centroid_intensity", curie=FOF_CT.curie('centroid_intensity'),
                   model_uri=FOF_CT.centroid_intensity, domain=None, range=Optional[float])

slots.peak_intensity = Slot(uri=FOF_CT.peak_intensity, name="peak_intensity", curie=FOF_CT.curie('peak_intensity'),
                   model_uri=FOF_CT.peak_intensity, domain=None, range=Optional[float])

slots.raw_x = Slot(uri=FOF_CT.raw_x, name="raw_x", curie=FOF_CT.curie('raw_x'),
                   model_uri=FOF_CT.raw_x, domain=None, range=Optional[float])

slots.raw_y = Slot(uri=FOF_CT.raw_y, name="raw_y", curie=FOF_CT.curie('raw_y'),
                   model_uri=FOF_CT.raw_y, domain=None, range=Optional[float])

slots.raw_z = Slot(uri=FOF_CT.raw_z, name="raw_z", curie=FOF_CT.curie('raw_z'),
                   model_uri=FOF_CT.raw_z, domain=None, range=Optional[float])

slots.x_drift = Slot(uri=FOF_CT.x_drift, name="x_drift", curie=FOF_CT.curie('x_drift'),
                   model_uri=FOF_CT.x_drift, domain=None, range=Optional[float])

slots.y_drift = Slot(uri=FOF_CT.y_drift, name="y_drift", curie=FOF_CT.curie('y_drift'),
                   model_uri=FOF_CT.y_drift, domain=None, range=Optional[float])

slots.z_drift = Slot(uri=FOF_CT.z_drift, name="z_drift", curie=FOF_CT.curie('z_drift'),
                   model_uri=FOF_CT.z_drift, domain=None, range=Optional[float])

slots.x_chromatic_shift = Slot(uri=FOF_CT.x_chromatic_shift, name="x_chromatic_shift", curie=FOF_CT.curie('x_chromatic_shift'),
                   model_uri=FOF_CT.x_chromatic_shift, domain=None, range=Optional[float])

slots.y_chromatic_shift = Slot(uri=FOF_CT.y_chromatic_shift, name="y_chromatic_shift", curie=FOF_CT.curie('y_chromatic_shift'),
                   model_uri=FOF_CT.y_chromatic_shift, domain=None, range=Optional[float])

slots.z_chromatic_shift = Slot(uri=FOF_CT.z_chromatic_shift, name="z_chromatic_shift", curie=FOF_CT.curie('z_chromatic_shift'),
                   model_uri=FOF_CT.z_chromatic_shift, domain=None, range=Optional[float])

slots.x_loc_error = Slot(uri=FOF_CT.x_loc_error, name="x_loc_error", curie=FOF_CT.curie('x_loc_error'),
                   model_uri=FOF_CT.x_loc_error, domain=None, range=Optional[float])

slots.y_loc_error = Slot(uri=FOF_CT.y_loc_error, name="y_loc_error", curie=FOF_CT.curie('y_loc_error'),
                   model_uri=FOF_CT.y_loc_error, domain=None, range=Optional[float])

slots.z_loc_error = Slot(uri=FOF_CT.z_loc_error, name="z_loc_error", curie=FOF_CT.curie('z_loc_error'),
                   model_uri=FOF_CT.z_loc_error, domain=None, range=Optional[float])

slots.image_frame_id = Slot(uri=FOF_CT.image_frame_id, name="image_frame_id", curie=FOF_CT.curie('image_frame_id'),
                   model_uri=FOF_CT.image_frame_id, domain=None, range=Optional[int])

slots.hyb_id = Slot(uri=FOF_CT.hyb_id, name="hyb_id", curie=FOF_CT.curie('hyb_id'),
                   model_uri=FOF_CT.hyb_id, domain=None, range=Optional[int])

slots.the_z = Slot(uri=FOF_CT.the_z, name="the_z", curie=FOF_CT.curie('the_z'),
                   model_uri=FOF_CT.the_z, domain=None, range=Optional[int])

slots.genome_assembly = Slot(uri=FOF_CT.genome_assembly, name="genome_assembly", curie=FOF_CT.curie('genome_assembly'),
                   model_uri=FOF_CT.genome_assembly, domain=None, range=Optional[str])

slots.modification = Slot(uri=FOF_CT.modification, name="modification", curie=FOF_CT.curie('modification'),
                   model_uri=FOF_CT.modification, domain=None, range=Optional[str])

slots.vcf_file_name = Slot(uri=FOF_CT.vcf_file_name, name="vcf_file_name", curie=FOF_CT.curie('vcf_file_name'),
                   model_uri=FOF_CT.vcf_file_name, domain=None, range=Optional[str])

slots.vcf_version = Slot(uri=FOF_CT.vcf_version, name="vcf_version", curie=FOF_CT.curie('vcf_version'),
                   model_uri=FOF_CT.vcf_version, domain=None, range=Optional[str])

slots.cell_type = Slot(uri=FOF_CT.cell_type, name="cell_type", curie=FOF_CT.curie('cell_type'),
                   model_uri=FOF_CT.cell_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.extra_cell_roi_type = Slot(uri=FOF_CT.extra_cell_roi_type, name="extra_cell_roi_type", curie=FOF_CT.curie('extra_cell_roi_type'),
                   model_uri=FOF_CT.extra_cell_roi_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.sub_cell_roi_type = Slot(uri=FOF_CT.sub_cell_roi_type, name="sub_cell_roi_type", curie=FOF_CT.curie('sub_cell_roi_type'),
                   model_uri=FOF_CT.sub_cell_roi_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.software_title = Slot(uri=FOF_CT.software_title, name="software_title", curie=FOF_CT.curie('software_title'),
                   model_uri=FOF_CT.software_title, domain=None, range=str)

slots.software_type = Slot(uri=FOF_CT.software_type, name="software_type", curie=FOF_CT.curie('software_type'),
                   model_uri=FOF_CT.software_type, domain=None, range=Union[str, "SoftwareTypeEnum"])

slots.software_authors = Slot(uri=FOF_CT.software_authors, name="software_authors", curie=FOF_CT.curie('software_authors'),
                   model_uri=FOF_CT.software_authors, domain=None, range=str)

slots.software_description = Slot(uri=FOF_CT.software_description, name="software_description", curie=FOF_CT.curie('software_description'),
                   model_uri=FOF_CT.software_description, domain=None, range=str)

slots.software_parameters = Slot(uri=FOF_CT.software_parameters, name="software_parameters", curie=FOF_CT.curie('software_parameters'),
                   model_uri=FOF_CT.software_parameters, domain=None, range=str)

slots.software_repository = Slot(uri=FOF_CT.software_repository, name="software_repository", curie=FOF_CT.curie('software_repository'),
                   model_uri=FOF_CT.software_repository, domain=None, range=Union[str, URI])

slots.software_preferred_citation_id = Slot(uri=FOF_CT.software_preferred_citation_id, name="software_preferred_citation_id", curie=FOF_CT.curie('software_preferred_citation_id'),
                   model_uri=FOF_CT.software_preferred_citation_id, domain=None, range=Union[str, URI])

slots.spots = Slot(uri=FOF_CT.spots, name="spots", curie=FOF_CT.curie('spots'),
                   model_uri=FOF_CT.spots, domain=SpotTable, range=Optional[Union[dict[Union[int, SpotSpotId], Union[dict, Spot]], list[Union[dict, Spot]]]])

slots.localizations = Slot(uri=FOF_CT.localizations, name="localizations", curie=FOF_CT.curie('localizations'),
                   model_uri=FOF_CT.localizations, domain=DemultiplexingTable, range=Optional[Union[dict[Union[int, LocalizationLocId], Union[dict, Localization]], list[Union[dict, Localization]]]])

slots.traces = Slot(uri=FOF_CT.traces, name="traces", curie=FOF_CT.curie('traces'),
                   model_uri=FOF_CT.traces, domain=TraceTable, range=Optional[Union[list[Union[int, TraceTraceId]], dict[Union[int, TraceTraceId], Union[dict, Trace]]]])

slots.gene_id_type = Slot(uri=FOF_CT.gene_id_type, name="gene_id_type", curie=FOF_CT.curie('gene_id_type'),
                   model_uri=FOF_CT.gene_id_type, domain=RNASpotTable, range=Optional[str])

slots.transcript_id_type = Slot(uri=FOF_CT.transcript_id_type, name="transcript_id_type", curie=FOF_CT.curie('transcript_id_type'),
                   model_uri=FOF_CT.transcript_id_type, domain=RNASpotTable, range=Optional[str])

slots.rna_name = Slot(uri=FOF_CT.rna_name, name="rna_name", curie=FOF_CT.curie('rna_name'),
                   model_uri=FOF_CT.rna_name, domain=RNASpot, range=Optional[str])

slots.gene_id = Slot(uri=FOF_CT.gene_id, name="gene_id", curie=FOF_CT.curie('gene_id'),
                   model_uri=FOF_CT.gene_id, domain=RNASpot, range=Optional[str])

slots.transcript_id = Slot(uri=FOF_CT.transcript_id, name="transcript_id", curie=FOF_CT.curie('transcript_id'),
                   model_uri=FOF_CT.transcript_id, domain=RNASpot, range=Optional[str])

slots.rna_spots = Slot(uri=FOF_CT.rna_spots, name="rna_spots", curie=FOF_CT.curie('rna_spots'),
                   model_uri=FOF_CT.rna_spots, domain=RNASpotTable, range=Optional[Union[dict[Union[int, RNASpotRnaSpotId], Union[dict, RNASpot]], list[Union[dict, RNASpot]]]])

slots.spot_quality_records = Slot(uri=FOF_CT.spot_quality_records, name="spot_quality_records", curie=FOF_CT.curie('spot_quality_records'),
                   model_uri=FOF_CT.spot_quality_records, domain=SpotQualityTable, range=Optional[Union[dict[Union[int, SpotQualityRecordSpotId], Union[dict, SpotQualityRecord]], list[Union[dict, SpotQualityRecord]]]])

slots.rna_spot_quality_records = Slot(uri=FOF_CT.rna_spot_quality_records, name="rna_spot_quality_records", curie=FOF_CT.curie('rna_spot_quality_records'),
                   model_uri=FOF_CT.rna_spot_quality_records, domain=RNASpotQualityTable, range=Optional[Union[dict[Union[int, RNASpotQualityRecordRnaSpotId], Union[dict, RNASpotQualityRecord]], list[Union[dict, RNASpotQualityRecord]]]])

slots.spot_biological_records = Slot(uri=FOF_CT.spot_biological_records, name="spot_biological_records", curie=FOF_CT.curie('spot_biological_records'),
                   model_uri=FOF_CT.spot_biological_records, domain=SpotBiologicalTable, range=Optional[Union[list[Union[int, SpotBiologicalRecordSpotId]], dict[Union[int, SpotBiologicalRecordSpotId], Union[dict, SpotBiologicalRecord]]]])

slots.rna_spot_biological_records = Slot(uri=FOF_CT.rna_spot_biological_records, name="rna_spot_biological_records", curie=FOF_CT.curie('rna_spot_biological_records'),
                   model_uri=FOF_CT.rna_spot_biological_records, domain=RNASpotBiologicalTable, range=Optional[Union[list[Union[int, RNASpotBiologicalRecordRnaSpotId]], dict[Union[int, RNASpotBiologicalRecordRnaSpotId], Union[dict, RNASpotBiologicalRecord]]]])

slots.cells = Slot(uri=FOF_CT.cells, name="cells", curie=FOF_CT.curie('cells'),
                   model_uri=FOF_CT.cells, domain=CellTable, range=Optional[Union[dict[Union[int, CellCellId], Union[dict, Cell]], list[Union[dict, Cell]]]])

slots.extra_cell_rois = Slot(uri=FOF_CT.extra_cell_rois, name="extra_cell_rois", curie=FOF_CT.curie('extra_cell_rois'),
                   model_uri=FOF_CT.extra_cell_rois, domain=ExtraCellROITable, range=Optional[Union[list[Union[int, ExtraCellROIExtraCellRoiId]], dict[Union[int, ExtraCellROIExtraCellRoiId], Union[dict, ExtraCellROI]]]])

slots.sub_cell_rois = Slot(uri=FOF_CT.sub_cell_rois, name="sub_cell_rois", curie=FOF_CT.curie('sub_cell_rois'),
                   model_uri=FOF_CT.sub_cell_rois, domain=SubCellROITable, range=Optional[Union[dict[Union[int, SubCellROISubCellRoiId], Union[dict, SubCellROI]], list[Union[dict, SubCellROI]]]])

slots.roi_boundaries_format_type = Slot(uri=FOF_CT.roi_boundaries_format_type, name="roi_boundaries_format_type", curie=FOF_CT.curie('roi_boundaries_format_type'),
                   model_uri=FOF_CT.roi_boundaries_format_type, domain=ROIMappingTable, range=Optional[Union[str, "ROIBoundariesFormatTypeEnum"]])

slots.roi_boundaries_format_description = Slot(uri=FOF_CT.roi_boundaries_format_description, name="roi_boundaries_format_description", curie=FOF_CT.curie('roi_boundaries_format_description'),
                   model_uri=FOF_CT.roi_boundaries_format_description, domain=ROIMappingTable, range=Optional[str])

slots.roi_boundaries = Slot(uri=FOF_CT.roi_boundaries, name="roi_boundaries", curie=FOF_CT.curie('roi_boundaries'),
                   model_uri=FOF_CT.roi_boundaries, domain=ROIMapping, range=Optional[str])

slots.roi_mappings = Slot(uri=FOF_CT.roi_mappings, name="roi_mappings", curie=FOF_CT.curie('roi_mappings'),
                   model_uri=FOF_CT.roi_mappings, domain=ROIMappingTable, range=Optional[Union[Union[dict, ROIMapping], list[Union[dict, ROIMapping]]]])

slots.sm_localizations = Slot(uri=FOF_CT.sm_localizations, name="sm_localizations", curie=FOF_CT.curie('sm_localizations'),
                   model_uri=FOF_CT.sm_localizations, domain=SMLocalizationTable, range=Optional[Union[dict[Union[int, SMLocalizationLocId], Union[dict, SMLocalization]], list[Union[dict, SMLocalization]]]])

slots.sm_localization_quality_records = Slot(uri=FOF_CT.sm_localization_quality_records, name="sm_localization_quality_records", curie=FOF_CT.curie('sm_localization_quality_records'),
                   model_uri=FOF_CT.sm_localization_quality_records, domain=SMLocalizationQualityTable, range=Optional[Union[dict[Union[int, SMLocalizationQualityRecordLocId], Union[dict, SMLocalizationQualityRecord]], list[Union[dict, SMLocalizationQualityRecord]]]])

slots.undecoded_localizations = Slot(uri=FOF_CT.undecoded_localizations, name="undecoded_localizations", curie=FOF_CT.curie('undecoded_localizations'),
                   model_uri=FOF_CT.undecoded_localizations, domain=UndecodedLocalizationTable, range=Optional[Union[dict[Union[int, UndecodedLocalizationLocId], Union[dict, UndecodedLocalization]], list[Union[dict, UndecodedLocalization]]]])

slots.Spot_spot_id = Slot(uri=FOF_CT.spot_id, name="Spot_spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.Spot_spot_id, domain=Spot, range=Union[int, SpotSpotId])

slots.Spot_trace_id = Slot(uri=FOF_CT.trace_id, name="Spot_trace_id", curie=FOF_CT.curie('trace_id'),
                   model_uri=FOF_CT.Spot_trace_id, domain=Spot, range=Union[int, TraceTraceId])

slots.Spot_x = Slot(uri=FOF_CT.x, name="Spot_x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.Spot_x, domain=Spot, range=float)

slots.Spot_y = Slot(uri=FOF_CT.y, name="Spot_y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.Spot_y, domain=Spot, range=float)

slots.Spot_z = Slot(uri=FOF_CT.z, name="Spot_z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.Spot_z, domain=Spot, range=float)

slots.Spot_chrom = Slot(uri=FOF_CT.chrom, name="Spot_chrom", curie=FOF_CT.curie('chrom'),
                   model_uri=FOF_CT.Spot_chrom, domain=Spot, range=str)

slots.Spot_chrom_start = Slot(uri=FOF_CT.chrom_start, name="Spot_chrom_start", curie=FOF_CT.curie('chrom_start'),
                   model_uri=FOF_CT.Spot_chrom_start, domain=Spot, range=int)

slots.Spot_chrom_end = Slot(uri=FOF_CT.chrom_end, name="Spot_chrom_end", curie=FOF_CT.curie('chrom_end'),
                   model_uri=FOF_CT.Spot_chrom_end, domain=Spot, range=int)

slots.SpotTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SpotTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SpotTable_fof_ct_version, domain=SpotTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SpotTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SpotTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SpotTable_table_namespace, domain=SpotTable, range=str)

slots.SpotTable_genome_assembly = Slot(uri=FOF_CT.genome_assembly, name="SpotTable_genome_assembly", curie=FOF_CT.curie('genome_assembly'),
                   model_uri=FOF_CT.SpotTable_genome_assembly, domain=SpotTable, range=str)

slots.SpotTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SpotTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SpotTable_xyz_unit, domain=SpotTable, range=Union[str, "XYZUnitEnum"])

slots.SpotTable_lab_name = Slot(uri=FOF_CT.lab_name, name="SpotTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SpotTable_lab_name, domain=SpotTable, range=str)

slots.SpotTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SpotTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SpotTable_experimenter_name, domain=SpotTable, range=str)

slots.SpotTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SpotTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SpotTable_experimenter_contact, domain=SpotTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SpotTable_description = Slot(uri=FOF_CT.description, name="SpotTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SpotTable_description, domain=SpotTable, range=str)

slots.SpotTable_softwares = Slot(uri=FOF_CT.softwares, name="SpotTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SpotTable_softwares, domain=SpotTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.SpotTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SpotTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SpotTable_additional_tables, domain=SpotTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SpotTable_spots = Slot(uri=FOF_CT.spots, name="SpotTable_spots", curie=FOF_CT.curie('spots'),
                   model_uri=FOF_CT.SpotTable_spots, domain=SpotTable, range=Union[dict[Union[int, SpotSpotId], Union[dict, Spot]], list[Union[dict, Spot]]])

slots.Localization_loc_id = Slot(uri=FOF_CT.loc_id, name="Localization_loc_id", curie=FOF_CT.curie('loc_id'),
                   model_uri=FOF_CT.Localization_loc_id, domain=Localization, range=Union[int, LocalizationLocId])

slots.Localization_spot_id = Slot(uri=FOF_CT.spot_id, name="Localization_spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.Localization_spot_id, domain=Localization, range=Union[int, SpotSpotId])

slots.Localization_x = Slot(uri=FOF_CT.x, name="Localization_x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.Localization_x, domain=Localization, range=float)

slots.Localization_y = Slot(uri=FOF_CT.y, name="Localization_y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.Localization_y, domain=Localization, range=float)

slots.Localization_z = Slot(uri=FOF_CT.z, name="Localization_z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.Localization_z, domain=Localization, range=float)

slots.Localization_channel_name = Slot(uri=FOF_CT.channel_name, name="Localization_channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.Localization_channel_name, domain=Localization, range=str)

slots.Localization_fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="Localization_fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.Localization_fluorophore_name, domain=Localization, range=str)

slots.DemultiplexingTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="DemultiplexingTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.DemultiplexingTable_fof_ct_version, domain=DemultiplexingTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.DemultiplexingTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="DemultiplexingTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.DemultiplexingTable_table_namespace, domain=DemultiplexingTable, range=str)

slots.DemultiplexingTable_lab_name = Slot(uri=FOF_CT.lab_name, name="DemultiplexingTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.DemultiplexingTable_lab_name, domain=DemultiplexingTable, range=str)

slots.DemultiplexingTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="DemultiplexingTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.DemultiplexingTable_experimenter_name, domain=DemultiplexingTable, range=str)

slots.DemultiplexingTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="DemultiplexingTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.DemultiplexingTable_experimenter_contact, domain=DemultiplexingTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.DemultiplexingTable_description = Slot(uri=FOF_CT.description, name="DemultiplexingTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.DemultiplexingTable_description, domain=DemultiplexingTable, range=str)

slots.DemultiplexingTable_softwares = Slot(uri=FOF_CT.softwares, name="DemultiplexingTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.DemultiplexingTable_softwares, domain=DemultiplexingTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.DemultiplexingTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="DemultiplexingTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.DemultiplexingTable_additional_tables, domain=DemultiplexingTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.DemultiplexingTable_localizations = Slot(uri=FOF_CT.localizations, name="DemultiplexingTable_localizations", curie=FOF_CT.curie('localizations'),
                   model_uri=FOF_CT.DemultiplexingTable_localizations, domain=DemultiplexingTable, range=Union[dict[Union[int, LocalizationLocId], Union[dict, Localization]], list[Union[dict, Localization]]])

slots.Trace_trace_id = Slot(uri=FOF_CT.trace_id, name="Trace_trace_id", curie=FOF_CT.curie('trace_id'),
                   model_uri=FOF_CT.Trace_trace_id, domain=Trace, range=Union[int, TraceTraceId])

slots.TraceTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="TraceTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.TraceTable_fof_ct_version, domain=TraceTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.TraceTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="TraceTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.TraceTable_table_namespace, domain=TraceTable, range=str)

slots.TraceTable_lab_name = Slot(uri=FOF_CT.lab_name, name="TraceTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.TraceTable_lab_name, domain=TraceTable, range=str)

slots.TraceTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="TraceTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.TraceTable_experimenter_name, domain=TraceTable, range=str)

slots.TraceTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="TraceTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.TraceTable_experimenter_contact, domain=TraceTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.TraceTable_description = Slot(uri=FOF_CT.description, name="TraceTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.TraceTable_description, domain=TraceTable, range=str)

slots.TraceTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="TraceTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.TraceTable_additional_tables, domain=TraceTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.TraceTable_traces = Slot(uri=FOF_CT.traces, name="TraceTable_traces", curie=FOF_CT.curie('traces'),
                   model_uri=FOF_CT.TraceTable_traces, domain=TraceTable, range=Union[list[Union[int, TraceTraceId]], dict[Union[int, TraceTraceId], Union[dict, Trace]]])

slots.RNASpot_rna_spot_id = Slot(uri=FOF_CT.rna_spot_id, name="RNASpot_rna_spot_id", curie=FOF_CT.curie('rna_spot_id'),
                   model_uri=FOF_CT.RNASpot_rna_spot_id, domain=RNASpot, range=Union[int, RNASpotRnaSpotId])

slots.RNASpot_x = Slot(uri=FOF_CT.x, name="RNASpot_x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.RNASpot_x, domain=RNASpot, range=float)

slots.RNASpot_y = Slot(uri=FOF_CT.y, name="RNASpot_y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.RNASpot_y, domain=RNASpot, range=float)

slots.RNASpot_z = Slot(uri=FOF_CT.z, name="RNASpot_z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.RNASpot_z, domain=RNASpot, range=float)

slots.RNASpot_rna_name = Slot(uri=FOF_CT.rna_name, name="RNASpot_rna_name", curie=FOF_CT.curie('rna_name'),
                   model_uri=FOF_CT.RNASpot_rna_name, domain=RNASpot, range=str)

slots.RNASpot_gene_id = Slot(uri=FOF_CT.gene_id, name="RNASpot_gene_id", curie=FOF_CT.curie('gene_id'),
                   model_uri=FOF_CT.RNASpot_gene_id, domain=RNASpot, range=str)

slots.RNASpot_trace_id = Slot(uri=FOF_CT.trace_id, name="RNASpot_trace_id", curie=FOF_CT.curie('trace_id'),
                   model_uri=FOF_CT.RNASpot_trace_id, domain=RNASpot, range=Union[int, TraceTraceId])

slots.RNASpotTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="RNASpotTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.RNASpotTable_fof_ct_version, domain=RNASpotTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.RNASpotTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="RNASpotTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.RNASpotTable_table_namespace, domain=RNASpotTable, range=str)

slots.RNASpotTable_genome_assembly = Slot(uri=FOF_CT.genome_assembly, name="RNASpotTable_genome_assembly", curie=FOF_CT.curie('genome_assembly'),
                   model_uri=FOF_CT.RNASpotTable_genome_assembly, domain=RNASpotTable, range=str)

slots.RNASpotTable_gene_id_type = Slot(uri=FOF_CT.gene_id_type, name="RNASpotTable_gene_id_type", curie=FOF_CT.curie('gene_id_type'),
                   model_uri=FOF_CT.RNASpotTable_gene_id_type, domain=RNASpotTable, range=str)

slots.RNASpotTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="RNASpotTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.RNASpotTable_xyz_unit, domain=RNASpotTable, range=Union[str, "XYZUnitEnum"])

slots.RNASpotTable_lab_name = Slot(uri=FOF_CT.lab_name, name="RNASpotTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.RNASpotTable_lab_name, domain=RNASpotTable, range=str)

slots.RNASpotTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="RNASpotTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.RNASpotTable_experimenter_name, domain=RNASpotTable, range=str)

slots.RNASpotTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="RNASpotTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.RNASpotTable_experimenter_contact, domain=RNASpotTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.RNASpotTable_description = Slot(uri=FOF_CT.description, name="RNASpotTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.RNASpotTable_description, domain=RNASpotTable, range=str)

slots.RNASpotTable_softwares = Slot(uri=FOF_CT.softwares, name="RNASpotTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.RNASpotTable_softwares, domain=RNASpotTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.RNASpotTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="RNASpotTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.RNASpotTable_additional_tables, domain=RNASpotTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.RNASpotTable_rna_spots = Slot(uri=FOF_CT.rna_spots, name="RNASpotTable_rna_spots", curie=FOF_CT.curie('rna_spots'),
                   model_uri=FOF_CT.RNASpotTable_rna_spots, domain=RNASpotTable, range=Union[dict[Union[int, RNASpotRnaSpotId], Union[dict, RNASpot]], list[Union[dict, RNASpot]]])

slots.SpotQualityRecord_spot_id = Slot(uri=FOF_CT.spot_id, name="SpotQualityRecord_spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.SpotQualityRecord_spot_id, domain=SpotQualityRecord, range=Union[int, SpotQualityRecordSpotId])

slots.SpotQualityRecord_channel_name = Slot(uri=FOF_CT.channel_name, name="SpotQualityRecord_channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.SpotQualityRecord_channel_name, domain=SpotQualityRecord, range=str)

slots.SpotQualityRecord_fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="SpotQualityRecord_fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.SpotQualityRecord_fluorophore_name, domain=SpotQualityRecord, range=str)

slots.SpotQualityRecord_x_precision = Slot(uri=FOF_CT.x_precision, name="SpotQualityRecord_x_precision", curie=FOF_CT.curie('x_precision'),
                   model_uri=FOF_CT.SpotQualityRecord_x_precision, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_y_precision = Slot(uri=FOF_CT.y_precision, name="SpotQualityRecord_y_precision", curie=FOF_CT.curie('y_precision'),
                   model_uri=FOF_CT.SpotQualityRecord_y_precision, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_z_precision = Slot(uri=FOF_CT.z_precision, name="SpotQualityRecord_z_precision", curie=FOF_CT.curie('z_precision'),
                   model_uri=FOF_CT.SpotQualityRecord_z_precision, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_photon_count = Slot(uri=FOF_CT.photon_count, name="SpotQualityRecord_photon_count", curie=FOF_CT.curie('photon_count'),
                   model_uri=FOF_CT.SpotQualityRecord_photon_count, domain=SpotQualityRecord, range=Optional[int])

slots.SpotQualityRecord_goodness_of_fit = Slot(uri=FOF_CT.goodness_of_fit, name="SpotQualityRecord_goodness_of_fit", curie=FOF_CT.curie('goodness_of_fit'),
                   model_uri=FOF_CT.SpotQualityRecord_goodness_of_fit, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_centroid_intensity = Slot(uri=FOF_CT.centroid_intensity, name="SpotQualityRecord_centroid_intensity", curie=FOF_CT.curie('centroid_intensity'),
                   model_uri=FOF_CT.SpotQualityRecord_centroid_intensity, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_peak_intensity = Slot(uri=FOF_CT.peak_intensity, name="SpotQualityRecord_peak_intensity", curie=FOF_CT.curie('peak_intensity'),
                   model_uri=FOF_CT.SpotQualityRecord_peak_intensity, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_raw_x = Slot(uri=FOF_CT.raw_x, name="SpotQualityRecord_raw_x", curie=FOF_CT.curie('raw_x'),
                   model_uri=FOF_CT.SpotQualityRecord_raw_x, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_raw_y = Slot(uri=FOF_CT.raw_y, name="SpotQualityRecord_raw_y", curie=FOF_CT.curie('raw_y'),
                   model_uri=FOF_CT.SpotQualityRecord_raw_y, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_raw_z = Slot(uri=FOF_CT.raw_z, name="SpotQualityRecord_raw_z", curie=FOF_CT.curie('raw_z'),
                   model_uri=FOF_CT.SpotQualityRecord_raw_z, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_x_drift = Slot(uri=FOF_CT.x_drift, name="SpotQualityRecord_x_drift", curie=FOF_CT.curie('x_drift'),
                   model_uri=FOF_CT.SpotQualityRecord_x_drift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_y_drift = Slot(uri=FOF_CT.y_drift, name="SpotQualityRecord_y_drift", curie=FOF_CT.curie('y_drift'),
                   model_uri=FOF_CT.SpotQualityRecord_y_drift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_z_drift = Slot(uri=FOF_CT.z_drift, name="SpotQualityRecord_z_drift", curie=FOF_CT.curie('z_drift'),
                   model_uri=FOF_CT.SpotQualityRecord_z_drift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_x_chromatic_shift = Slot(uri=FOF_CT.x_chromatic_shift, name="SpotQualityRecord_x_chromatic_shift", curie=FOF_CT.curie('x_chromatic_shift'),
                   model_uri=FOF_CT.SpotQualityRecord_x_chromatic_shift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_y_chromatic_shift = Slot(uri=FOF_CT.y_chromatic_shift, name="SpotQualityRecord_y_chromatic_shift", curie=FOF_CT.curie('y_chromatic_shift'),
                   model_uri=FOF_CT.SpotQualityRecord_y_chromatic_shift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_z_chromatic_shift = Slot(uri=FOF_CT.z_chromatic_shift, name="SpotQualityRecord_z_chromatic_shift", curie=FOF_CT.curie('z_chromatic_shift'),
                   model_uri=FOF_CT.SpotQualityRecord_z_chromatic_shift, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_x_loc_error = Slot(uri=FOF_CT.x_loc_error, name="SpotQualityRecord_x_loc_error", curie=FOF_CT.curie('x_loc_error'),
                   model_uri=FOF_CT.SpotQualityRecord_x_loc_error, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_y_loc_error = Slot(uri=FOF_CT.y_loc_error, name="SpotQualityRecord_y_loc_error", curie=FOF_CT.curie('y_loc_error'),
                   model_uri=FOF_CT.SpotQualityRecord_y_loc_error, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityRecord_z_loc_error = Slot(uri=FOF_CT.z_loc_error, name="SpotQualityRecord_z_loc_error", curie=FOF_CT.curie('z_loc_error'),
                   model_uri=FOF_CT.SpotQualityRecord_z_loc_error, domain=SpotQualityRecord, range=Optional[float])

slots.SpotQualityTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SpotQualityTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SpotQualityTable_fof_ct_version, domain=SpotQualityTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SpotQualityTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SpotQualityTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SpotQualityTable_table_namespace, domain=SpotQualityTable, range=str)

slots.SpotQualityTable_lab_name = Slot(uri=FOF_CT.lab_name, name="SpotQualityTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SpotQualityTable_lab_name, domain=SpotQualityTable, range=str)

slots.SpotQualityTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SpotQualityTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SpotQualityTable_experimenter_name, domain=SpotQualityTable, range=str)

slots.SpotQualityTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SpotQualityTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SpotQualityTable_experimenter_contact, domain=SpotQualityTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SpotQualityTable_description = Slot(uri=FOF_CT.description, name="SpotQualityTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SpotQualityTable_description, domain=SpotQualityTable, range=str)

slots.SpotQualityTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SpotQualityTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SpotQualityTable_additional_tables, domain=SpotQualityTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SpotQualityTable_softwares = Slot(uri=FOF_CT.softwares, name="SpotQualityTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SpotQualityTable_softwares, domain=SpotQualityTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.SpotQualityTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SpotQualityTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SpotQualityTable_xyz_unit, domain=SpotQualityTable, range=Union[str, "XYZUnitEnum"])

slots.SpotQualityTable_time_unit = Slot(uri=FOF_CT.time_unit, name="SpotQualityTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.SpotQualityTable_time_unit, domain=SpotQualityTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.SpotQualityTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="SpotQualityTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.SpotQualityTable_intensity_unit, domain=SpotQualityTable, range=Optional[str])

slots.SpotQualityTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="SpotQualityTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.SpotQualityTable_intensity_measurement_method, domain=SpotQualityTable, range=Optional[str])

slots.SpotQualityTable_spot_quality_records = Slot(uri=FOF_CT.spot_quality_records, name="SpotQualityTable_spot_quality_records", curie=FOF_CT.curie('spot_quality_records'),
                   model_uri=FOF_CT.SpotQualityTable_spot_quality_records, domain=SpotQualityTable, range=Union[dict[Union[int, SpotQualityRecordSpotId], Union[dict, SpotQualityRecord]], list[Union[dict, SpotQualityRecord]]])

slots.RNASpotQualityRecord_rna_spot_id = Slot(uri=FOF_CT.rna_spot_id, name="RNASpotQualityRecord_rna_spot_id", curie=FOF_CT.curie('rna_spot_id'),
                   model_uri=FOF_CT.RNASpotQualityRecord_rna_spot_id, domain=RNASpotQualityRecord, range=Union[int, RNASpotQualityRecordRnaSpotId])

slots.RNASpotQualityRecord_channel_name = Slot(uri=FOF_CT.channel_name, name="RNASpotQualityRecord_channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.RNASpotQualityRecord_channel_name, domain=RNASpotQualityRecord, range=str)

slots.RNASpotQualityRecord_fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="RNASpotQualityRecord_fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.RNASpotQualityRecord_fluorophore_name, domain=RNASpotQualityRecord, range=str)

slots.RNASpotQualityRecord_x_precision = Slot(uri=FOF_CT.x_precision, name="RNASpotQualityRecord_x_precision", curie=FOF_CT.curie('x_precision'),
                   model_uri=FOF_CT.RNASpotQualityRecord_x_precision, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_y_precision = Slot(uri=FOF_CT.y_precision, name="RNASpotQualityRecord_y_precision", curie=FOF_CT.curie('y_precision'),
                   model_uri=FOF_CT.RNASpotQualityRecord_y_precision, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_z_precision = Slot(uri=FOF_CT.z_precision, name="RNASpotQualityRecord_z_precision", curie=FOF_CT.curie('z_precision'),
                   model_uri=FOF_CT.RNASpotQualityRecord_z_precision, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_photon_count = Slot(uri=FOF_CT.photon_count, name="RNASpotQualityRecord_photon_count", curie=FOF_CT.curie('photon_count'),
                   model_uri=FOF_CT.RNASpotQualityRecord_photon_count, domain=RNASpotQualityRecord, range=Optional[int])

slots.RNASpotQualityRecord_goodness_of_fit = Slot(uri=FOF_CT.goodness_of_fit, name="RNASpotQualityRecord_goodness_of_fit", curie=FOF_CT.curie('goodness_of_fit'),
                   model_uri=FOF_CT.RNASpotQualityRecord_goodness_of_fit, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_centroid_intensity = Slot(uri=FOF_CT.centroid_intensity, name="RNASpotQualityRecord_centroid_intensity", curie=FOF_CT.curie('centroid_intensity'),
                   model_uri=FOF_CT.RNASpotQualityRecord_centroid_intensity, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_peak_intensity = Slot(uri=FOF_CT.peak_intensity, name="RNASpotQualityRecord_peak_intensity", curie=FOF_CT.curie('peak_intensity'),
                   model_uri=FOF_CT.RNASpotQualityRecord_peak_intensity, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_raw_x = Slot(uri=FOF_CT.raw_x, name="RNASpotQualityRecord_raw_x", curie=FOF_CT.curie('raw_x'),
                   model_uri=FOF_CT.RNASpotQualityRecord_raw_x, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_raw_y = Slot(uri=FOF_CT.raw_y, name="RNASpotQualityRecord_raw_y", curie=FOF_CT.curie('raw_y'),
                   model_uri=FOF_CT.RNASpotQualityRecord_raw_y, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_raw_z = Slot(uri=FOF_CT.raw_z, name="RNASpotQualityRecord_raw_z", curie=FOF_CT.curie('raw_z'),
                   model_uri=FOF_CT.RNASpotQualityRecord_raw_z, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_x_drift = Slot(uri=FOF_CT.x_drift, name="RNASpotQualityRecord_x_drift", curie=FOF_CT.curie('x_drift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_x_drift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_y_drift = Slot(uri=FOF_CT.y_drift, name="RNASpotQualityRecord_y_drift", curie=FOF_CT.curie('y_drift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_y_drift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_z_drift = Slot(uri=FOF_CT.z_drift, name="RNASpotQualityRecord_z_drift", curie=FOF_CT.curie('z_drift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_z_drift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_x_chromatic_shift = Slot(uri=FOF_CT.x_chromatic_shift, name="RNASpotQualityRecord_x_chromatic_shift", curie=FOF_CT.curie('x_chromatic_shift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_x_chromatic_shift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_y_chromatic_shift = Slot(uri=FOF_CT.y_chromatic_shift, name="RNASpotQualityRecord_y_chromatic_shift", curie=FOF_CT.curie('y_chromatic_shift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_y_chromatic_shift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_z_chromatic_shift = Slot(uri=FOF_CT.z_chromatic_shift, name="RNASpotQualityRecord_z_chromatic_shift", curie=FOF_CT.curie('z_chromatic_shift'),
                   model_uri=FOF_CT.RNASpotQualityRecord_z_chromatic_shift, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_x_loc_error = Slot(uri=FOF_CT.x_loc_error, name="RNASpotQualityRecord_x_loc_error", curie=FOF_CT.curie('x_loc_error'),
                   model_uri=FOF_CT.RNASpotQualityRecord_x_loc_error, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_y_loc_error = Slot(uri=FOF_CT.y_loc_error, name="RNASpotQualityRecord_y_loc_error", curie=FOF_CT.curie('y_loc_error'),
                   model_uri=FOF_CT.RNASpotQualityRecord_y_loc_error, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityRecord_z_loc_error = Slot(uri=FOF_CT.z_loc_error, name="RNASpotQualityRecord_z_loc_error", curie=FOF_CT.curie('z_loc_error'),
                   model_uri=FOF_CT.RNASpotQualityRecord_z_loc_error, domain=RNASpotQualityRecord, range=Optional[float])

slots.RNASpotQualityTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="RNASpotQualityTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.RNASpotQualityTable_fof_ct_version, domain=RNASpotQualityTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.RNASpotQualityTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="RNASpotQualityTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.RNASpotQualityTable_table_namespace, domain=RNASpotQualityTable, range=str)

slots.RNASpotQualityTable_lab_name = Slot(uri=FOF_CT.lab_name, name="RNASpotQualityTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.RNASpotQualityTable_lab_name, domain=RNASpotQualityTable, range=str)

slots.RNASpotQualityTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="RNASpotQualityTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.RNASpotQualityTable_experimenter_name, domain=RNASpotQualityTable, range=str)

slots.RNASpotQualityTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="RNASpotQualityTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.RNASpotQualityTable_experimenter_contact, domain=RNASpotQualityTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.RNASpotQualityTable_description = Slot(uri=FOF_CT.description, name="RNASpotQualityTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.RNASpotQualityTable_description, domain=RNASpotQualityTable, range=str)

slots.RNASpotQualityTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="RNASpotQualityTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.RNASpotQualityTable_additional_tables, domain=RNASpotQualityTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.RNASpotQualityTable_softwares = Slot(uri=FOF_CT.softwares, name="RNASpotQualityTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.RNASpotQualityTable_softwares, domain=RNASpotQualityTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.RNASpotQualityTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="RNASpotQualityTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.RNASpotQualityTable_xyz_unit, domain=RNASpotQualityTable, range=Union[str, "XYZUnitEnum"])

slots.RNASpotQualityTable_time_unit = Slot(uri=FOF_CT.time_unit, name="RNASpotQualityTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.RNASpotQualityTable_time_unit, domain=RNASpotQualityTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.RNASpotQualityTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="RNASpotQualityTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.RNASpotQualityTable_intensity_unit, domain=RNASpotQualityTable, range=Optional[str])

slots.RNASpotQualityTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="RNASpotQualityTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.RNASpotQualityTable_intensity_measurement_method, domain=RNASpotQualityTable, range=Optional[str])

slots.RNASpotQualityTable_rna_spot_quality_records = Slot(uri=FOF_CT.rna_spot_quality_records, name="RNASpotQualityTable_rna_spot_quality_records", curie=FOF_CT.curie('rna_spot_quality_records'),
                   model_uri=FOF_CT.RNASpotQualityTable_rna_spot_quality_records, domain=RNASpotQualityTable, range=Union[dict[Union[int, RNASpotQualityRecordRnaSpotId], Union[dict, RNASpotQualityRecord]], list[Union[dict, RNASpotQualityRecord]]])

slots.SpotBiologicalRecord_spot_id = Slot(uri=FOF_CT.spot_id, name="SpotBiologicalRecord_spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.SpotBiologicalRecord_spot_id, domain=SpotBiologicalRecord, range=Union[int, SpotBiologicalRecordSpotId])

slots.SpotBiologicalTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SpotBiologicalTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SpotBiologicalTable_fof_ct_version, domain=SpotBiologicalTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SpotBiologicalTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SpotBiologicalTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SpotBiologicalTable_table_namespace, domain=SpotBiologicalTable, range=str)

slots.SpotBiologicalTable_lab_name = Slot(uri=FOF_CT.lab_name, name="SpotBiologicalTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SpotBiologicalTable_lab_name, domain=SpotBiologicalTable, range=str)

slots.SpotBiologicalTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SpotBiologicalTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SpotBiologicalTable_experimenter_name, domain=SpotBiologicalTable, range=str)

slots.SpotBiologicalTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SpotBiologicalTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SpotBiologicalTable_experimenter_contact, domain=SpotBiologicalTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SpotBiologicalTable_description = Slot(uri=FOF_CT.description, name="SpotBiologicalTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SpotBiologicalTable_description, domain=SpotBiologicalTable, range=str)

slots.SpotBiologicalTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SpotBiologicalTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SpotBiologicalTable_additional_tables, domain=SpotBiologicalTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SpotBiologicalTable_softwares = Slot(uri=FOF_CT.softwares, name="SpotBiologicalTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SpotBiologicalTable_softwares, domain=SpotBiologicalTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.SpotBiologicalTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SpotBiologicalTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SpotBiologicalTable_xyz_unit, domain=SpotBiologicalTable, range=Union[str, "XYZUnitEnum"])

slots.SpotBiologicalTable_time_unit = Slot(uri=FOF_CT.time_unit, name="SpotBiologicalTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.SpotBiologicalTable_time_unit, domain=SpotBiologicalTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.SpotBiologicalTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="SpotBiologicalTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.SpotBiologicalTable_intensity_unit, domain=SpotBiologicalTable, range=Optional[str])

slots.SpotBiologicalTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="SpotBiologicalTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.SpotBiologicalTable_intensity_measurement_method, domain=SpotBiologicalTable, range=Optional[str])

slots.SpotBiologicalTable_spot_biological_records = Slot(uri=FOF_CT.spot_biological_records, name="SpotBiologicalTable_spot_biological_records", curie=FOF_CT.curie('spot_biological_records'),
                   model_uri=FOF_CT.SpotBiologicalTable_spot_biological_records, domain=SpotBiologicalTable, range=Union[list[Union[int, SpotBiologicalRecordSpotId]], dict[Union[int, SpotBiologicalRecordSpotId], Union[dict, SpotBiologicalRecord]]])

slots.RNASpotBiologicalRecord_rna_spot_id = Slot(uri=FOF_CT.rna_spot_id, name="RNASpotBiologicalRecord_rna_spot_id", curie=FOF_CT.curie('rna_spot_id'),
                   model_uri=FOF_CT.RNASpotBiologicalRecord_rna_spot_id, domain=RNASpotBiologicalRecord, range=Union[int, RNASpotBiologicalRecordRnaSpotId])

slots.RNASpotBiologicalTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="RNASpotBiologicalTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_fof_ct_version, domain=RNASpotBiologicalTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.RNASpotBiologicalTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="RNASpotBiologicalTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_table_namespace, domain=RNASpotBiologicalTable, range=str)

slots.RNASpotBiologicalTable_lab_name = Slot(uri=FOF_CT.lab_name, name="RNASpotBiologicalTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_lab_name, domain=RNASpotBiologicalTable, range=str)

slots.RNASpotBiologicalTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="RNASpotBiologicalTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_experimenter_name, domain=RNASpotBiologicalTable, range=str)

slots.RNASpotBiologicalTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="RNASpotBiologicalTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_experimenter_contact, domain=RNASpotBiologicalTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.RNASpotBiologicalTable_description = Slot(uri=FOF_CT.description, name="RNASpotBiologicalTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_description, domain=RNASpotBiologicalTable, range=str)

slots.RNASpotBiologicalTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="RNASpotBiologicalTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_additional_tables, domain=RNASpotBiologicalTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.RNASpotBiologicalTable_softwares = Slot(uri=FOF_CT.softwares, name="RNASpotBiologicalTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_softwares, domain=RNASpotBiologicalTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.RNASpotBiologicalTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="RNASpotBiologicalTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_xyz_unit, domain=RNASpotBiologicalTable, range=Union[str, "XYZUnitEnum"])

slots.RNASpotBiologicalTable_time_unit = Slot(uri=FOF_CT.time_unit, name="RNASpotBiologicalTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_time_unit, domain=RNASpotBiologicalTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.RNASpotBiologicalTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="RNASpotBiologicalTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_intensity_unit, domain=RNASpotBiologicalTable, range=Optional[str])

slots.RNASpotBiologicalTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="RNASpotBiologicalTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_intensity_measurement_method, domain=RNASpotBiologicalTable, range=Optional[str])

slots.RNASpotBiologicalTable_rna_spot_biological_records = Slot(uri=FOF_CT.rna_spot_biological_records, name="RNASpotBiologicalTable_rna_spot_biological_records", curie=FOF_CT.curie('rna_spot_biological_records'),
                   model_uri=FOF_CT.RNASpotBiologicalTable_rna_spot_biological_records, domain=RNASpotBiologicalTable, range=Union[list[Union[int, RNASpotBiologicalRecordRnaSpotId]], dict[Union[int, RNASpotBiologicalRecordRnaSpotId], Union[dict, RNASpotBiologicalRecord]]])

slots.Cell_cell_id = Slot(uri=FOF_CT.cell_id, name="Cell_cell_id", curie=FOF_CT.curie('cell_id'),
                   model_uri=FOF_CT.Cell_cell_id, domain=Cell, range=Union[int, CellCellId])

slots.Cell_extra_cell_roi_id = Slot(uri=FOF_CT.extra_cell_roi_id, name="Cell_extra_cell_roi_id", curie=FOF_CT.curie('extra_cell_roi_id'),
                   model_uri=FOF_CT.Cell_extra_cell_roi_id, domain=Cell, range=Optional[Union[int, ExtraCellROIExtraCellRoiId]])

slots.CellTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="CellTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.CellTable_fof_ct_version, domain=CellTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.CellTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="CellTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.CellTable_table_namespace, domain=CellTable, range=str)

slots.CellTable_cell_type = Slot(uri=FOF_CT.cell_type, name="CellTable_cell_type", curie=FOF_CT.curie('cell_type'),
                   model_uri=FOF_CT.CellTable_cell_type, domain=CellTable, range=str,
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.CellTable_lab_name = Slot(uri=FOF_CT.lab_name, name="CellTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.CellTable_lab_name, domain=CellTable, range=str)

slots.CellTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="CellTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.CellTable_experimenter_name, domain=CellTable, range=str)

slots.CellTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="CellTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.CellTable_experimenter_contact, domain=CellTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.CellTable_description = Slot(uri=FOF_CT.description, name="CellTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.CellTable_description, domain=CellTable, range=str)

slots.CellTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="CellTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.CellTable_additional_tables, domain=CellTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.CellTable_extra_cell_roi_type = Slot(uri=FOF_CT.extra_cell_roi_type, name="CellTable_extra_cell_roi_type", curie=FOF_CT.curie('extra_cell_roi_type'),
                   model_uri=FOF_CT.CellTable_extra_cell_roi_type, domain=CellTable, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.CellTable_softwares = Slot(uri=FOF_CT.softwares, name="CellTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.CellTable_softwares, domain=CellTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.CellTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="CellTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.CellTable_xyz_unit, domain=CellTable, range=Union[str, "XYZUnitEnum"])

slots.CellTable_time_unit = Slot(uri=FOF_CT.time_unit, name="CellTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.CellTable_time_unit, domain=CellTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.CellTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="CellTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.CellTable_intensity_unit, domain=CellTable, range=Optional[str])

slots.CellTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="CellTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.CellTable_intensity_measurement_method, domain=CellTable, range=Optional[str])

slots.CellTable_cells = Slot(uri=FOF_CT.cells, name="CellTable_cells", curie=FOF_CT.curie('cells'),
                   model_uri=FOF_CT.CellTable_cells, domain=CellTable, range=Union[dict[Union[int, CellCellId], Union[dict, Cell]], list[Union[dict, Cell]]])

slots.ExtraCellROI_extra_cell_roi_id = Slot(uri=FOF_CT.extra_cell_roi_id, name="ExtraCellROI_extra_cell_roi_id", curie=FOF_CT.curie('extra_cell_roi_id'),
                   model_uri=FOF_CT.ExtraCellROI_extra_cell_roi_id, domain=ExtraCellROI, range=Union[int, ExtraCellROIExtraCellRoiId])

slots.ExtraCellROITable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="ExtraCellROITable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.ExtraCellROITable_fof_ct_version, domain=ExtraCellROITable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.ExtraCellROITable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="ExtraCellROITable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.ExtraCellROITable_table_namespace, domain=ExtraCellROITable, range=str)

slots.ExtraCellROITable_extra_cell_roi_type = Slot(uri=FOF_CT.extra_cell_roi_type, name="ExtraCellROITable_extra_cell_roi_type", curie=FOF_CT.curie('extra_cell_roi_type'),
                   model_uri=FOF_CT.ExtraCellROITable_extra_cell_roi_type, domain=ExtraCellROITable, range=str,
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.ExtraCellROITable_lab_name = Slot(uri=FOF_CT.lab_name, name="ExtraCellROITable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.ExtraCellROITable_lab_name, domain=ExtraCellROITable, range=str)

slots.ExtraCellROITable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="ExtraCellROITable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.ExtraCellROITable_experimenter_name, domain=ExtraCellROITable, range=str)

slots.ExtraCellROITable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="ExtraCellROITable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.ExtraCellROITable_experimenter_contact, domain=ExtraCellROITable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.ExtraCellROITable_description = Slot(uri=FOF_CT.description, name="ExtraCellROITable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.ExtraCellROITable_description, domain=ExtraCellROITable, range=str)

slots.ExtraCellROITable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="ExtraCellROITable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.ExtraCellROITable_additional_tables, domain=ExtraCellROITable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.ExtraCellROITable_softwares = Slot(uri=FOF_CT.softwares, name="ExtraCellROITable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.ExtraCellROITable_softwares, domain=ExtraCellROITable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.ExtraCellROITable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="ExtraCellROITable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.ExtraCellROITable_xyz_unit, domain=ExtraCellROITable, range=Union[str, "XYZUnitEnum"])

slots.ExtraCellROITable_time_unit = Slot(uri=FOF_CT.time_unit, name="ExtraCellROITable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.ExtraCellROITable_time_unit, domain=ExtraCellROITable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.ExtraCellROITable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="ExtraCellROITable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.ExtraCellROITable_intensity_unit, domain=ExtraCellROITable, range=Optional[str])

slots.ExtraCellROITable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="ExtraCellROITable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.ExtraCellROITable_intensity_measurement_method, domain=ExtraCellROITable, range=Optional[str])

slots.ExtraCellROITable_extra_cell_rois = Slot(uri=FOF_CT.extra_cell_rois, name="ExtraCellROITable_extra_cell_rois", curie=FOF_CT.curie('extra_cell_rois'),
                   model_uri=FOF_CT.ExtraCellROITable_extra_cell_rois, domain=ExtraCellROITable, range=Union[list[Union[int, ExtraCellROIExtraCellRoiId]], dict[Union[int, ExtraCellROIExtraCellRoiId], Union[dict, ExtraCellROI]]])

slots.SubCellROI_sub_cell_roi_id = Slot(uri=FOF_CT.sub_cell_roi_id, name="SubCellROI_sub_cell_roi_id", curie=FOF_CT.curie('sub_cell_roi_id'),
                   model_uri=FOF_CT.SubCellROI_sub_cell_roi_id, domain=SubCellROI, range=Union[int, SubCellROISubCellRoiId])

slots.SubCellROI_cell_id = Slot(uri=FOF_CT.cell_id, name="SubCellROI_cell_id", curie=FOF_CT.curie('cell_id'),
                   model_uri=FOF_CT.SubCellROI_cell_id, domain=SubCellROI, range=Optional[Union[int, CellCellId]])

slots.SubCellROITable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SubCellROITable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SubCellROITable_fof_ct_version, domain=SubCellROITable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SubCellROITable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SubCellROITable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SubCellROITable_table_namespace, domain=SubCellROITable, range=str)

slots.SubCellROITable_sub_cell_roi_type = Slot(uri=FOF_CT.sub_cell_roi_type, name="SubCellROITable_sub_cell_roi_type", curie=FOF_CT.curie('sub_cell_roi_type'),
                   model_uri=FOF_CT.SubCellROITable_sub_cell_roi_type, domain=SubCellROITable, range=str,
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.SubCellROITable_lab_name = Slot(uri=FOF_CT.lab_name, name="SubCellROITable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SubCellROITable_lab_name, domain=SubCellROITable, range=str)

slots.SubCellROITable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SubCellROITable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SubCellROITable_experimenter_name, domain=SubCellROITable, range=str)

slots.SubCellROITable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SubCellROITable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SubCellROITable_experimenter_contact, domain=SubCellROITable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SubCellROITable_description = Slot(uri=FOF_CT.description, name="SubCellROITable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SubCellROITable_description, domain=SubCellROITable, range=str)

slots.SubCellROITable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SubCellROITable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SubCellROITable_additional_tables, domain=SubCellROITable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SubCellROITable_cell_type = Slot(uri=FOF_CT.cell_type, name="SubCellROITable_cell_type", curie=FOF_CT.curie('cell_type'),
                   model_uri=FOF_CT.SubCellROITable_cell_type, domain=SubCellROITable, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.SubCellROITable_softwares = Slot(uri=FOF_CT.softwares, name="SubCellROITable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SubCellROITable_softwares, domain=SubCellROITable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.SubCellROITable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SubCellROITable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SubCellROITable_xyz_unit, domain=SubCellROITable, range=Union[str, "XYZUnitEnum"])

slots.SubCellROITable_time_unit = Slot(uri=FOF_CT.time_unit, name="SubCellROITable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.SubCellROITable_time_unit, domain=SubCellROITable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.SubCellROITable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="SubCellROITable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.SubCellROITable_intensity_unit, domain=SubCellROITable, range=Optional[str])

slots.SubCellROITable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="SubCellROITable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.SubCellROITable_intensity_measurement_method, domain=SubCellROITable, range=Optional[str])

slots.SubCellROITable_sub_cell_rois = Slot(uri=FOF_CT.sub_cell_rois, name="SubCellROITable_sub_cell_rois", curie=FOF_CT.curie('sub_cell_rois'),
                   model_uri=FOF_CT.SubCellROITable_sub_cell_rois, domain=SubCellROITable, range=Union[dict[Union[int, SubCellROISubCellRoiId], Union[dict, SubCellROI]], list[Union[dict, SubCellROI]]])

slots.ROIMapping_sub_cell_roi_id = Slot(uri=FOF_CT.sub_cell_roi_id, name="ROIMapping_sub_cell_roi_id", curie=FOF_CT.curie('sub_cell_roi_id'),
                   model_uri=FOF_CT.ROIMapping_sub_cell_roi_id, domain=ROIMapping, range=Optional[Union[int, SubCellROISubCellRoiId]])

slots.ROIMapping_cell_id = Slot(uri=FOF_CT.cell_id, name="ROIMapping_cell_id", curie=FOF_CT.curie('cell_id'),
                   model_uri=FOF_CT.ROIMapping_cell_id, domain=ROIMapping, range=Optional[Union[int, CellCellId]])

slots.ROIMapping_extra_cell_roi_id = Slot(uri=FOF_CT.extra_cell_roi_id, name="ROIMapping_extra_cell_roi_id", curie=FOF_CT.curie('extra_cell_roi_id'),
                   model_uri=FOF_CT.ROIMapping_extra_cell_roi_id, domain=ROIMapping, range=Optional[Union[int, ExtraCellROIExtraCellRoiId]])

slots.ROIMapping_roi_boundaries = Slot(uri=FOF_CT.roi_boundaries, name="ROIMapping_roi_boundaries", curie=FOF_CT.curie('roi_boundaries'),
                   model_uri=FOF_CT.ROIMapping_roi_boundaries, domain=ROIMapping, range=str)

slots.ROIMappingTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="ROIMappingTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.ROIMappingTable_fof_ct_version, domain=ROIMappingTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.ROIMappingTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="ROIMappingTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.ROIMappingTable_table_namespace, domain=ROIMappingTable, range=str)

slots.ROIMappingTable_roi_boundaries_format_type = Slot(uri=FOF_CT.roi_boundaries_format_type, name="ROIMappingTable_roi_boundaries_format_type", curie=FOF_CT.curie('roi_boundaries_format_type'),
                   model_uri=FOF_CT.ROIMappingTable_roi_boundaries_format_type, domain=ROIMappingTable, range=Union[str, "ROIBoundariesFormatTypeEnum"])

slots.ROIMappingTable_roi_boundaries_format_description = Slot(uri=FOF_CT.roi_boundaries_format_description, name="ROIMappingTable_roi_boundaries_format_description", curie=FOF_CT.curie('roi_boundaries_format_description'),
                   model_uri=FOF_CT.ROIMappingTable_roi_boundaries_format_description, domain=ROIMappingTable, range=Optional[str])

slots.ROIMappingTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="ROIMappingTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.ROIMappingTable_xyz_unit, domain=ROIMappingTable, range=Union[str, "XYZUnitEnum"])

slots.ROIMappingTable_lab_name = Slot(uri=FOF_CT.lab_name, name="ROIMappingTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.ROIMappingTable_lab_name, domain=ROIMappingTable, range=str)

slots.ROIMappingTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="ROIMappingTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.ROIMappingTable_experimenter_name, domain=ROIMappingTable, range=str)

slots.ROIMappingTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="ROIMappingTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.ROIMappingTable_experimenter_contact, domain=ROIMappingTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.ROIMappingTable_description = Slot(uri=FOF_CT.description, name="ROIMappingTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.ROIMappingTable_description, domain=ROIMappingTable, range=str)

slots.ROIMappingTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="ROIMappingTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.ROIMappingTable_additional_tables, domain=ROIMappingTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.ROIMappingTable_cell_type = Slot(uri=FOF_CT.cell_type, name="ROIMappingTable_cell_type", curie=FOF_CT.curie('cell_type'),
                   model_uri=FOF_CT.ROIMappingTable_cell_type, domain=ROIMappingTable, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.ROIMappingTable_sub_cell_roi_type = Slot(uri=FOF_CT.sub_cell_roi_type, name="ROIMappingTable_sub_cell_roi_type", curie=FOF_CT.curie('sub_cell_roi_type'),
                   model_uri=FOF_CT.ROIMappingTable_sub_cell_roi_type, domain=ROIMappingTable, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.ROIMappingTable_extra_cell_roi_type = Slot(uri=FOF_CT.extra_cell_roi_type, name="ROIMappingTable_extra_cell_roi_type", curie=FOF_CT.curie('extra_cell_roi_type'),
                   model_uri=FOF_CT.ROIMappingTable_extra_cell_roi_type, domain=ROIMappingTable, range=Optional[str],
                   pattern=re.compile(r'^(Other|[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_]+( \(.+\))?)$'))

slots.ROIMappingTable_softwares = Slot(uri=FOF_CT.softwares, name="ROIMappingTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.ROIMappingTable_softwares, domain=ROIMappingTable, range=Optional[Union[Union[dict, Software], list[Union[dict, Software]]]])

slots.ROIMappingTable_time_unit = Slot(uri=FOF_CT.time_unit, name="ROIMappingTable_time_unit", curie=FOF_CT.curie('time_unit'),
                   model_uri=FOF_CT.ROIMappingTable_time_unit, domain=ROIMappingTable, range=Optional[Union[str, "TimeUnitEnum"]])

slots.ROIMappingTable_intensity_unit = Slot(uri=FOF_CT.intensity_unit, name="ROIMappingTable_intensity_unit", curie=FOF_CT.curie('intensity_unit'),
                   model_uri=FOF_CT.ROIMappingTable_intensity_unit, domain=ROIMappingTable, range=Optional[str])

slots.ROIMappingTable_intensity_measurement_method = Slot(uri=FOF_CT.intensity_measurement_method, name="ROIMappingTable_intensity_measurement_method", curie=FOF_CT.curie('intensity_measurement_method'),
                   model_uri=FOF_CT.ROIMappingTable_intensity_measurement_method, domain=ROIMappingTable, range=Optional[str])

slots.ROIMappingTable_roi_mappings = Slot(uri=FOF_CT.roi_mappings, name="ROIMappingTable_roi_mappings", curie=FOF_CT.curie('roi_mappings'),
                   model_uri=FOF_CT.ROIMappingTable_roi_mappings, domain=ROIMappingTable, range=Union[Union[dict, ROIMapping], list[Union[dict, ROIMapping]]])

slots.SMLocalization_loc_id = Slot(uri=FOF_CT.loc_id, name="SMLocalization_loc_id", curie=FOF_CT.curie('loc_id'),
                   model_uri=FOF_CT.SMLocalization_loc_id, domain=SMLocalization, range=Union[int, SMLocalizationLocId])

slots.SMLocalization_x = Slot(uri=FOF_CT.x, name="SMLocalization_x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.SMLocalization_x, domain=SMLocalization, range=float)

slots.SMLocalization_y = Slot(uri=FOF_CT.y, name="SMLocalization_y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.SMLocalization_y, domain=SMLocalization, range=float)

slots.SMLocalization_z = Slot(uri=FOF_CT.z, name="SMLocalization_z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.SMLocalization_z, domain=SMLocalization, range=float)

slots.SMLocalization_spot_id = Slot(uri=FOF_CT.spot_id, name="SMLocalization_spot_id", curie=FOF_CT.curie('spot_id'),
                   model_uri=FOF_CT.SMLocalization_spot_id, domain=SMLocalization, range=Union[int, SpotSpotId])

slots.SMLocalization_trace_id = Slot(uri=FOF_CT.trace_id, name="SMLocalization_trace_id", curie=FOF_CT.curie('trace_id'),
                   model_uri=FOF_CT.SMLocalization_trace_id, domain=SMLocalization, range=Union[int, TraceTraceId])

slots.SMLocalization_chrom = Slot(uri=FOF_CT.chrom, name="SMLocalization_chrom", curie=FOF_CT.curie('chrom'),
                   model_uri=FOF_CT.SMLocalization_chrom, domain=SMLocalization, range=str)

slots.SMLocalization_chrom_start = Slot(uri=FOF_CT.chrom_start, name="SMLocalization_chrom_start", curie=FOF_CT.curie('chrom_start'),
                   model_uri=FOF_CT.SMLocalization_chrom_start, domain=SMLocalization, range=int)

slots.SMLocalization_chrom_end = Slot(uri=FOF_CT.chrom_end, name="SMLocalization_chrom_end", curie=FOF_CT.curie('chrom_end'),
                   model_uri=FOF_CT.SMLocalization_chrom_end, domain=SMLocalization, range=int)

slots.SMLocalization_sub_cell_roi_id = Slot(uri=FOF_CT.sub_cell_roi_id, name="SMLocalization_sub_cell_roi_id", curie=FOF_CT.curie('sub_cell_roi_id'),
                   model_uri=FOF_CT.SMLocalization_sub_cell_roi_id, domain=SMLocalization, range=Optional[Union[int, SubCellROISubCellRoiId]])

slots.SMLocalization_cell_id = Slot(uri=FOF_CT.cell_id, name="SMLocalization_cell_id", curie=FOF_CT.curie('cell_id'),
                   model_uri=FOF_CT.SMLocalization_cell_id, domain=SMLocalization, range=Optional[Union[int, CellCellId]])

slots.SMLocalization_extra_cell_roi_id = Slot(uri=FOF_CT.extra_cell_roi_id, name="SMLocalization_extra_cell_roi_id", curie=FOF_CT.curie('extra_cell_roi_id'),
                   model_uri=FOF_CT.SMLocalization_extra_cell_roi_id, domain=SMLocalization, range=Optional[Union[int, ExtraCellROIExtraCellRoiId]])

slots.SMLocalizationTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SMLocalizationTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SMLocalizationTable_fof_ct_version, domain=SMLocalizationTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SMLocalizationTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SMLocalizationTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SMLocalizationTable_table_namespace, domain=SMLocalizationTable, range=str)

slots.SMLocalizationTable_lab_name = Slot(uri=FOF_CT.lab_name, name="SMLocalizationTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SMLocalizationTable_lab_name, domain=SMLocalizationTable, range=str)

slots.SMLocalizationTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SMLocalizationTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SMLocalizationTable_experimenter_name, domain=SMLocalizationTable, range=str)

slots.SMLocalizationTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SMLocalizationTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SMLocalizationTable_experimenter_contact, domain=SMLocalizationTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SMLocalizationTable_description = Slot(uri=FOF_CT.description, name="SMLocalizationTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SMLocalizationTable_description, domain=SMLocalizationTable, range=str)

slots.SMLocalizationTable_softwares = Slot(uri=FOF_CT.softwares, name="SMLocalizationTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SMLocalizationTable_softwares, domain=SMLocalizationTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.SMLocalizationTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SMLocalizationTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SMLocalizationTable_additional_tables, domain=SMLocalizationTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SMLocalizationTable_genome_assembly = Slot(uri=FOF_CT.genome_assembly, name="SMLocalizationTable_genome_assembly", curie=FOF_CT.curie('genome_assembly'),
                   model_uri=FOF_CT.SMLocalizationTable_genome_assembly, domain=SMLocalizationTable, range=str)

slots.SMLocalizationTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SMLocalizationTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SMLocalizationTable_xyz_unit, domain=SMLocalizationTable, range=Union[str, "XYZUnitEnum"])

slots.SMLocalizationTable_sm_localizations = Slot(uri=FOF_CT.sm_localizations, name="SMLocalizationTable_sm_localizations", curie=FOF_CT.curie('sm_localizations'),
                   model_uri=FOF_CT.SMLocalizationTable_sm_localizations, domain=SMLocalizationTable, range=Union[dict[Union[int, SMLocalizationLocId], Union[dict, SMLocalization]], list[Union[dict, SMLocalization]]])

slots.SMLocalizationQualityRecord_loc_id = Slot(uri=FOF_CT.loc_id, name="SMLocalizationQualityRecord_loc_id", curie=FOF_CT.curie('loc_id'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_loc_id, domain=SMLocalizationQualityRecord, range=Union[int, SMLocalizationQualityRecordLocId])

slots.SMLocalizationQualityRecord_channel_name = Slot(uri=FOF_CT.channel_name, name="SMLocalizationQualityRecord_channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_channel_name, domain=SMLocalizationQualityRecord, range=str)

slots.SMLocalizationQualityRecord_fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="SMLocalizationQualityRecord_fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_fluorophore_name, domain=SMLocalizationQualityRecord, range=str)

slots.SMLocalizationQualityRecord_x_precision = Slot(uri=FOF_CT.x_precision, name="SMLocalizationQualityRecord_x_precision", curie=FOF_CT.curie('x_precision'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_x_precision, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_y_precision = Slot(uri=FOF_CT.y_precision, name="SMLocalizationQualityRecord_y_precision", curie=FOF_CT.curie('y_precision'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_y_precision, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_z_precision = Slot(uri=FOF_CT.z_precision, name="SMLocalizationQualityRecord_z_precision", curie=FOF_CT.curie('z_precision'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_z_precision, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_photon_count = Slot(uri=FOF_CT.photon_count, name="SMLocalizationQualityRecord_photon_count", curie=FOF_CT.curie('photon_count'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_photon_count, domain=SMLocalizationQualityRecord, range=Optional[int])

slots.SMLocalizationQualityRecord_goodness_of_fit = Slot(uri=FOF_CT.goodness_of_fit, name="SMLocalizationQualityRecord_goodness_of_fit", curie=FOF_CT.curie('goodness_of_fit'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_goodness_of_fit, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_centroid_intensity = Slot(uri=FOF_CT.centroid_intensity, name="SMLocalizationQualityRecord_centroid_intensity", curie=FOF_CT.curie('centroid_intensity'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_centroid_intensity, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_peak_intensity = Slot(uri=FOF_CT.peak_intensity, name="SMLocalizationQualityRecord_peak_intensity", curie=FOF_CT.curie('peak_intensity'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_peak_intensity, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_raw_x = Slot(uri=FOF_CT.raw_x, name="SMLocalizationQualityRecord_raw_x", curie=FOF_CT.curie('raw_x'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_raw_x, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_raw_y = Slot(uri=FOF_CT.raw_y, name="SMLocalizationQualityRecord_raw_y", curie=FOF_CT.curie('raw_y'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_raw_y, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_raw_z = Slot(uri=FOF_CT.raw_z, name="SMLocalizationQualityRecord_raw_z", curie=FOF_CT.curie('raw_z'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_raw_z, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_x_loc_error = Slot(uri=FOF_CT.x_loc_error, name="SMLocalizationQualityRecord_x_loc_error", curie=FOF_CT.curie('x_loc_error'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_x_loc_error, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_y_loc_error = Slot(uri=FOF_CT.y_loc_error, name="SMLocalizationQualityRecord_y_loc_error", curie=FOF_CT.curie('y_loc_error'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_y_loc_error, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityRecord_z_loc_error = Slot(uri=FOF_CT.z_loc_error, name="SMLocalizationQualityRecord_z_loc_error", curie=FOF_CT.curie('z_loc_error'),
                   model_uri=FOF_CT.SMLocalizationQualityRecord_z_loc_error, domain=SMLocalizationQualityRecord, range=Optional[float])

slots.SMLocalizationQualityTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="SMLocalizationQualityTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_fof_ct_version, domain=SMLocalizationQualityTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.SMLocalizationQualityTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="SMLocalizationQualityTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_table_namespace, domain=SMLocalizationQualityTable, range=str)

slots.SMLocalizationQualityTable_lab_name = Slot(uri=FOF_CT.lab_name, name="SMLocalizationQualityTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_lab_name, domain=SMLocalizationQualityTable, range=str)

slots.SMLocalizationQualityTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="SMLocalizationQualityTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_experimenter_name, domain=SMLocalizationQualityTable, range=str)

slots.SMLocalizationQualityTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="SMLocalizationQualityTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_experimenter_contact, domain=SMLocalizationQualityTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.SMLocalizationQualityTable_description = Slot(uri=FOF_CT.description, name="SMLocalizationQualityTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_description, domain=SMLocalizationQualityTable, range=str)

slots.SMLocalizationQualityTable_softwares = Slot(uri=FOF_CT.softwares, name="SMLocalizationQualityTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_softwares, domain=SMLocalizationQualityTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.SMLocalizationQualityTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="SMLocalizationQualityTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_additional_tables, domain=SMLocalizationQualityTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.SMLocalizationQualityTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="SMLocalizationQualityTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_xyz_unit, domain=SMLocalizationQualityTable, range=Union[str, "XYZUnitEnum"])

slots.SMLocalizationQualityTable_sm_localization_quality_records = Slot(uri=FOF_CT.sm_localization_quality_records, name="SMLocalizationQualityTable_sm_localization_quality_records", curie=FOF_CT.curie('sm_localization_quality_records'),
                   model_uri=FOF_CT.SMLocalizationQualityTable_sm_localization_quality_records, domain=SMLocalizationQualityTable, range=Union[dict[Union[int, SMLocalizationQualityRecordLocId], Union[dict, SMLocalizationQualityRecord]], list[Union[dict, SMLocalizationQualityRecord]]])

slots.UndecodedLocalization_loc_id = Slot(uri=FOF_CT.loc_id, name="UndecodedLocalization_loc_id", curie=FOF_CT.curie('loc_id'),
                   model_uri=FOF_CT.UndecodedLocalization_loc_id, domain=UndecodedLocalization, range=Union[int, UndecodedLocalizationLocId])

slots.UndecodedLocalization_x = Slot(uri=FOF_CT.x, name="UndecodedLocalization_x", curie=FOF_CT.curie('x'),
                   model_uri=FOF_CT.UndecodedLocalization_x, domain=UndecodedLocalization, range=float)

slots.UndecodedLocalization_y = Slot(uri=FOF_CT.y, name="UndecodedLocalization_y", curie=FOF_CT.curie('y'),
                   model_uri=FOF_CT.UndecodedLocalization_y, domain=UndecodedLocalization, range=float)

slots.UndecodedLocalization_z = Slot(uri=FOF_CT.z, name="UndecodedLocalization_z", curie=FOF_CT.curie('z'),
                   model_uri=FOF_CT.UndecodedLocalization_z, domain=UndecodedLocalization, range=float)

slots.UndecodedLocalization_hyb_id = Slot(uri=FOF_CT.hyb_id, name="UndecodedLocalization_hyb_id", curie=FOF_CT.curie('hyb_id'),
                   model_uri=FOF_CT.UndecodedLocalization_hyb_id, domain=UndecodedLocalization, range=int)

slots.UndecodedLocalization_image_frame_id = Slot(uri=FOF_CT.image_frame_id, name="UndecodedLocalization_image_frame_id", curie=FOF_CT.curie('image_frame_id'),
                   model_uri=FOF_CT.UndecodedLocalization_image_frame_id, domain=UndecodedLocalization, range=int)

slots.UndecodedLocalization_channel_name = Slot(uri=FOF_CT.channel_name, name="UndecodedLocalization_channel_name", curie=FOF_CT.curie('channel_name'),
                   model_uri=FOF_CT.UndecodedLocalization_channel_name, domain=UndecodedLocalization, range=str)

slots.UndecodedLocalization_fluorophore_name = Slot(uri=FOF_CT.fluorophore_name, name="UndecodedLocalization_fluorophore_name", curie=FOF_CT.curie('fluorophore_name'),
                   model_uri=FOF_CT.UndecodedLocalization_fluorophore_name, domain=UndecodedLocalization, range=str)

slots.UndecodedLocalization_the_z = Slot(uri=FOF_CT.the_z, name="UndecodedLocalization_the_z", curie=FOF_CT.curie('the_z'),
                   model_uri=FOF_CT.UndecodedLocalization_the_z, domain=UndecodedLocalization, range=Optional[int])

slots.UndecodedLocalizationTable_fof_ct_version = Slot(uri=FOF_CT.fof_ct_version, name="UndecodedLocalizationTable_fof_ct_version", curie=FOF_CT.curie('fof_ct_version'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_fof_ct_version, domain=UndecodedLocalizationTable, range=str,
                   pattern=re.compile(r'^v[0-9]+\.[0-9]+'))

slots.UndecodedLocalizationTable_table_namespace = Slot(uri=FOF_CT.table_namespace, name="UndecodedLocalizationTable_table_namespace", curie=FOF_CT.curie('table_namespace'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_table_namespace, domain=UndecodedLocalizationTable, range=str)

slots.UndecodedLocalizationTable_lab_name = Slot(uri=FOF_CT.lab_name, name="UndecodedLocalizationTable_lab_name", curie=FOF_CT.curie('lab_name'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_lab_name, domain=UndecodedLocalizationTable, range=str)

slots.UndecodedLocalizationTable_experimenter_name = Slot(uri=FOF_CT.experimenter_name, name="UndecodedLocalizationTable_experimenter_name", curie=FOF_CT.curie('experimenter_name'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_experimenter_name, domain=UndecodedLocalizationTable, range=str)

slots.UndecodedLocalizationTable_experimenter_contact = Slot(uri=FOF_CT.experimenter_contact, name="UndecodedLocalizationTable_experimenter_contact", curie=FOF_CT.curie('experimenter_contact'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_experimenter_contact, domain=UndecodedLocalizationTable, range=str,
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.UndecodedLocalizationTable_description = Slot(uri=FOF_CT.description, name="UndecodedLocalizationTable_description", curie=FOF_CT.curie('description'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_description, domain=UndecodedLocalizationTable, range=str)

slots.UndecodedLocalizationTable_softwares = Slot(uri=FOF_CT.softwares, name="UndecodedLocalizationTable_softwares", curie=FOF_CT.curie('softwares'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_softwares, domain=UndecodedLocalizationTable, range=Union[Union[dict, Software], list[Union[dict, Software]]])

slots.UndecodedLocalizationTable_additional_tables = Slot(uri=FOF_CT.additional_tables, name="UndecodedLocalizationTable_additional_tables", curie=FOF_CT.curie('additional_tables'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_additional_tables, domain=UndecodedLocalizationTable, range=Union[Union[str, "TableNamespaceEnum"], list[Union[str, "TableNamespaceEnum"]]])

slots.UndecodedLocalizationTable_xyz_unit = Slot(uri=FOF_CT.xyz_unit, name="UndecodedLocalizationTable_xyz_unit", curie=FOF_CT.curie('xyz_unit'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_xyz_unit, domain=UndecodedLocalizationTable, range=Union[str, "XYZUnitEnum"])

slots.UndecodedLocalizationTable_undecoded_localizations = Slot(uri=FOF_CT.undecoded_localizations, name="UndecodedLocalizationTable_undecoded_localizations", curie=FOF_CT.curie('undecoded_localizations'),
                   model_uri=FOF_CT.UndecodedLocalizationTable_undecoded_localizations, domain=UndecodedLocalizationTable, range=Union[dict[Union[int, UndecodedLocalizationLocId], Union[dict, UndecodedLocalization]], list[Union[dict, UndecodedLocalization]]])
