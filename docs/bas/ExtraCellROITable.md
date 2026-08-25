---
search:
  boost: 10.0
---

# Class: ExtraCellROITable 


_The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of extracellular ROIs (recorded as data rows). This table is optional but recommended. Analogous to the MappingSet class in SSSOM._



<div data-search-exclude markdown="1">



URI: [fof_ct:ExtraCellROITable](https://w3id.org/fof-ct/ExtraCellROITable)





```mermaid
 classDiagram
    class ExtraCellROITable
    click ExtraCellROITable href "../ExtraCellROITable/"
      ExtraCellROITable : additional_tables
        
          
    
        
        
        ExtraCellROITable --> "1..*" TableNamespaceEnum : additional_tables
        click TableNamespaceEnum href "../TableNamespaceEnum/"
    

        
      ExtraCellROITable : description
        
      ExtraCellROITable : experimenter_contact
        
      ExtraCellROITable : experimenter_name
        
      ExtraCellROITable : extra_cell_roi_type
        
      ExtraCellROITable : extra_cell_rois
        
          
    
        
        
        ExtraCellROITable --> "1..*" ExtraCellROI : extra_cell_rois
        click ExtraCellROI href "../ExtraCellROI/"
    

        
      ExtraCellROITable : fof_ct_version
        
      ExtraCellROITable : intensity_measurement_method
        
      ExtraCellROITable : intensity_unit
        
      ExtraCellROITable : lab_name
        
      ExtraCellROITable : softwares
        
          
    
        
        
        ExtraCellROITable --> "*" Software : softwares
        click Software href "../Software/"
    

        
      ExtraCellROITable : table_namespace
        
      ExtraCellROITable : time_unit
        
          
    
        
        
        ExtraCellROITable --> "0..1" TimeUnitEnum : time_unit
        click TimeUnitEnum href "../TimeUnitEnum/"
    

        
      ExtraCellROITable : xyz_unit
        
          
    
        
        
        ExtraCellROITable --> "1" XYZUnitEnum : xyz_unit
        click XYZUnitEnum href "../XYZUnitEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [fof_ct_version](fof_ct_version.md) | 1 <br/> [String](String.md) | Version of the FOF-CT format used in this file | direct |
| [table_namespace](table_namespace.md) | 1 <br/> [String](String.md) | Identifier for this table type | direct |
| [extra_cell_roi_type](extra_cell_roi_type.md) | 1 <br/> [String](String.md) | The type of extracellular structure ROI within which cells are embedded, expr... | direct |
| [lab_name](lab_name.md) | 1 <br/> [String](String.md) | Name of the laboratory where the experiment was performed | direct |
| [experimenter_name](experimenter_name.md) | 1 <br/> [String](String.md) | Full name of the person who performed the experiment | direct |
| [experimenter_contact](experimenter_contact.md) | 1 <br/> [String](String.md) | Email address of the person who performed the experiment | direct |
| [description](description.md) | 1 <br/> [String](String.md) | Free-text description of the experiment and of the data recorded in this tabl... | direct |
| [additional_tables](additional_tables.md) | 1..* <br/> [TableNamespaceEnum](TableNamespaceEnum.md) | List of additional FOF-CT table namespaces being submitted alongside this tab... | direct |
| [softwares](softwares.md) | * <br/> [Software](Software.md) | One or more Software entries documenting every tool used to produce or proces... | direct |
| [xyz_unit](xyz_unit.md) | 1 <br/> [XYZUnitEnum](XYZUnitEnum.md) | Unit used to represent X, Y, Z spatial coordinates or distances in this table | direct |
| [time_unit](time_unit.md) | 0..1 <br/> [TimeUnitEnum](TimeUnitEnum.md) | Unit used to represent time intervals in this table | direct |
| [intensity_unit](intensity_unit.md) | 0..1 <br/> [String](String.md) | Unit used to represent intensity measurements in this table | direct |
| [intensity_measurement_method](intensity_measurement_method.md) | 0..1 <br/> [String](String.md) | Method used to perform intensity measurements, including how digital signals ... | direct |
| [extra_cell_rois](extra_cell_rois.md) | 1..* <br/> [ExtraCellROI](ExtraCellROI.md) | The complete collection of extracellular ROIs constituting this dataset | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ExtraCellROITable](ExtraCellROITable.md) | [extra_cell_rois](extra_cell_rois.md) | domain | [ExtraCellROITable](ExtraCellROITable.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:ExtraCellROITable |
| native | fof_ct:ExtraCellROITable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExtraCellROITable
description: 'The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell).
  This class represents the entire file: it holds all dataset-level provenance metadata
  (recorded as header lines in the TSV serialisation) together with the full collection
  of extracellular ROIs (recorded as data rows). This table is optional but recommended.
  Analogous to the MappingSet class in SSSOM.'
from_schema: https://w3id.org/fof-ct/bas
slots:
- fof_ct_version
- table_namespace
- extra_cell_roi_type
- lab_name
- experimenter_name
- experimenter_contact
- description
- additional_tables
- softwares
- xyz_unit
- time_unit
- intensity_unit
- intensity_measurement_method
- extra_cell_rois
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    required: true
    equals_string: 4dn_FOF-CT_extracell
  extra_cell_roi_type:
    name: extra_cell_roi_type
    required: true
  lab_name:
    name: lab_name
    required: true
  experimenter_name:
    name: experimenter_name
    required: true
  experimenter_contact:
    name: experimenter_contact
    required: true
  description:
    name: description
    required: true
  additional_tables:
    name: additional_tables
    required: true
  softwares:
    name: softwares
    range: Software
    required: false
    multivalued: true
  xyz_unit:
    name: xyz_unit
    required: true
  time_unit:
    name: time_unit
    required: false
  intensity_unit:
    name: intensity_unit
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    required: false
  extra_cell_rois:
    name: extra_cell_rois
    required: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: ExtraCellROITable
description: 'The Extra-Cell ROI Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_extracell).
  This class represents the entire file: it holds all dataset-level provenance metadata
  (recorded as header lines in the TSV serialisation) together with the full collection
  of extracellular ROIs (recorded as data rows). This table is optional but recommended.
  Analogous to the MappingSet class in SSSOM.'
from_schema: https://w3id.org/fof-ct/bas
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    required: true
    equals_string: 4dn_FOF-CT_extracell
  extra_cell_roi_type:
    name: extra_cell_roi_type
    required: true
  lab_name:
    name: lab_name
    required: true
  experimenter_name:
    name: experimenter_name
    required: true
  experimenter_contact:
    name: experimenter_contact
    required: true
  description:
    name: description
    required: true
  additional_tables:
    name: additional_tables
    required: true
  softwares:
    name: softwares
    range: Software
    required: false
    multivalued: true
  xyz_unit:
    name: xyz_unit
    required: true
  time_unit:
    name: time_unit
    required: false
  intensity_unit:
    name: intensity_unit
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    required: false
  extra_cell_rois:
    name: extra_cell_rois
    required: true
attributes:
  fof_ct_version:
    name: fof_ct_version
    description: Version of the FOF-CT format used in this file. Always the first
      line of the file header (##FOF-CT_Version=).
    examples:
    - value: v1.0
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
    pattern: ^v[0-9]+\.[0-9]+
  table_namespace:
    name: table_namespace
    description: 'Identifier for this table type. The required value is specific to
      each table. Written as ##Table_Namespace= in the file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
    equals_string: 4dn_FOF-CT_extracell
  extra_cell_roi_type:
    name: extra_cell_roi_type
    description: 'The type of extracellular structure ROI within which cells are embedded,
      expressed using an EFO ''organism part'' child term (e.g. Tissue, Organoid).
      Conditionally required when extracellular structure ROIs are identified and
      reported in a dedicated Extra-Cell ROI Data table. Written as #Extra_Cell_ROI_Type:
      in the file header.'
    examples:
    - value: Tissue
    - value: Organoid
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
    domain_of:
    - CellTable
    - ExtraCellROITable
    - ROIMappingTable
    range: string
    required: true
  lab_name:
    name: lab_name
    description: 'Name of the laboratory where the experiment was performed. Written
      as #Lab_Name: in the file header.'
    examples:
    - value: Nobel
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
  experimenter_name:
    name: experimenter_name
    description: 'Full name of the person who performed the experiment. Written as
      #Experimenter_Name: in the file header.'
    examples:
    - value: John Doe
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
  experimenter_contact:
    name: experimenter_contact
    description: 'Email address of the person who performed the experiment. Written
      as #Experimenter_Contact: in the file header.'
    examples:
    - value: john.doe@email.com
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
    pattern: ^[^@\s]+@[^@\s]+\.[^@\s]+$
  description:
    name: description
    description: 'Free-text description of the experiment and of the data recorded
      in this table. Should provide sufficient detail for interpretation and reproducibility.
      Written as #Description: in the file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: true
  additional_tables:
    name: additional_tables
    description: 'List of additional FOF-CT table namespaces being submitted alongside
      this table, separated by commas in the TSV header. Written as #Additional_Tables:
      in the file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: TableNamespaceEnum
    required: true
    multivalued: true
  softwares:
    name: softwares
    description: 'One or more Software entries documenting every tool used to produce
      or process data in this table. Written as repeating #Software_* blocks in the
      file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: Software
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  xyz_unit:
    name: xyz_unit
    description: 'Unit used to represent X, Y, Z spatial coordinates or distances
      in this table. Use ''micron'' to avoid issues with Greek symbols. Values should
      be drawn from SI units of length. Written as ##XYZ_Unit= in the file header.
      Mandatory in every FOF-CT table.'
    examples:
    - value: micron
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: XYZUnitEnum
    required: true
  time_unit:
    name: time_unit
    description: 'Unit used to represent time intervals in this table. Allowed values
      are SI time units plus ''min'' and ''hr''. Written as ##Time_Unit= in the file
      header. Conditionally required (metric- triggered) when any time metric is reported
      in an optional column.'
    examples:
    - value: sec
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    required: false
  intensity_unit:
    name: intensity_unit
    description: 'Unit used to represent intensity measurements in this table. Written
      as ##Intensity_Unit= in the file header. Conditionally required (metric-triggered)
      when any intensity metric is reported in an optional column.'
    examples:
    - value: a.u.
    - value: photons
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    description: 'Method used to perform intensity measurements, including how digital
      signals were converted to photon counts. Written as #Intensity_Measurement_Method:
      in the file header. Conditionally required (metric-triggered) when any intensity
      metric is reported.'
    examples:
    - value: Localization centroid intensity
    - value: Mean Fluorescence Intensity
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: ExtraCellROITable
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
    range: string
    required: false
  extra_cell_rois:
    name: extra_cell_rois
    description: The complete collection of extracellular ROIs constituting this dataset.
      Each ExtraCellROI corresponds to one data row in the TSV serialisation. At least
      one user-defined optional column (e.g. ROI_Volume, Cell_Count) MUST be present
      in every submitted Extra-Cell ROI Data table.
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    domain: ExtraCellROITable
    owner: ExtraCellROITable
    domain_of:
    - ExtraCellROITable
    range: ExtraCellROI
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>