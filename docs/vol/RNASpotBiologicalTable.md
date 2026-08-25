---
search:
  boost: 10.0
---

# Class: RNASpotBiologicalTable 


_The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_rna_bio). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of RNASpotBiologicalRecord rows. Submission of this table is optional but highly recommended._



<div data-search-exclude markdown="1">



URI: [fof_ct:RNASpotBiologicalTable](https://w3id.org/fof-ct/RNASpotBiologicalTable)





```mermaid
 classDiagram
    class RNASpotBiologicalTable
    click RNASpotBiologicalTable href "../RNASpotBiologicalTable/"
      RNASpotBiologicalTable : additional_tables
        
          
    
        
        
        RNASpotBiologicalTable --> "1..*" TableNamespaceEnum : additional_tables
        click TableNamespaceEnum href "../TableNamespaceEnum/"
    

        
      RNASpotBiologicalTable : description
        
      RNASpotBiologicalTable : experimenter_contact
        
      RNASpotBiologicalTable : experimenter_name
        
      RNASpotBiologicalTable : fof_ct_version
        
      RNASpotBiologicalTable : intensity_measurement_method
        
      RNASpotBiologicalTable : intensity_unit
        
      RNASpotBiologicalTable : lab_name
        
      RNASpotBiologicalTable : rna_spot_biological_records
        
          
    
        
        
        RNASpotBiologicalTable --> "1..*" RNASpotBiologicalRecord : rna_spot_biological_records
        click RNASpotBiologicalRecord href "../RNASpotBiologicalRecord/"
    

        
      RNASpotBiologicalTable : softwares
        
          
    
        
        
        RNASpotBiologicalTable --> "*" Software : softwares
        click Software href "../Software/"
    

        
      RNASpotBiologicalTable : table_namespace
        
      RNASpotBiologicalTable : time_unit
        
          
    
        
        
        RNASpotBiologicalTable --> "0..1" TimeUnitEnum : time_unit
        click TimeUnitEnum href "../TimeUnitEnum/"
    

        
      RNASpotBiologicalTable : xyz_unit
        
          
    
        
        
        RNASpotBiologicalTable --> "1" XYZUnitEnum : xyz_unit
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
| [lab_name](lab_name.md) | 1 <br/> [String](String.md) | Name of the laboratory where the experiment was performed | direct |
| [experimenter_name](experimenter_name.md) | 1 <br/> [String](String.md) | Full name of the person who performed the experiment | direct |
| [experimenter_contact](experimenter_contact.md) | 1 <br/> [String](String.md) | Email address of the person who performed the experiment | direct |
| [description](description.md) | 1 <br/> [String](String.md) | Free-text description of the experiment and of the data recorded in this tabl... | direct |
| [additional_tables](additional_tables.md) | 1..* <br/> [TableNamespaceEnum](TableNamespaceEnum.md) | List of additional FOF-CT table namespaces being submitted alongside this tab... | direct |
| [softwares](softwares.md) | * <br/> [Software](Software.md) | One or more Software entries documenting every tool used to produce or proces... | direct |
| [xyz_unit](xyz_unit.md) | 1 <br/> [XYZUnitEnum](XYZUnitEnum.md) | Unit used to represent X, Y, Z spatial coordinates or distances in this table | direct |
| [time_unit](time_unit.md) | 0..1 <br/> [TimeUnitEnum](TimeUnitEnum.md) | Unit used for any time metric reported in user-defined columns | direct |
| [intensity_unit](intensity_unit.md) | 0..1 <br/> [String](String.md) | Unit used for any intensity metric reported in user-defined columns | direct |
| [intensity_measurement_method](intensity_measurement_method.md) | 0..1 <br/> [String](String.md) | Method used to perform intensity measurements | direct |
| [rna_spot_biological_records](rna_spot_biological_records.md) | 1..* <br/> [RNASpotBiologicalRecord](RNASpotBiologicalRecord.md) | The complete collection of RNASpotBiologicalRecord rows constituting this dat... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RNASpotBiologicalTable](RNASpotBiologicalTable.md) | [rna_spot_biological_records](rna_spot_biological_records.md) | domain | [RNASpotBiologicalTable](RNASpotBiologicalTable.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:RNASpotBiologicalTable |
| native | fof_ct:RNASpotBiologicalTable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RNASpotBiologicalTable
description: 'The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace:
  4dn_FOF-CT_rna_bio). This class represents the entire file: it holds all dataset-level
  provenance metadata (recorded as header lines in the TSV serialisation) together
  with the full collection of RNASpotBiologicalRecord rows. Submission of this table
  is optional but highly recommended.'
from_schema: https://w3id.org/fof-ct/vol
slots:
- fof_ct_version
- table_namespace
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
- rna_spot_biological_records
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    description: 'Identifier for this table type. Must always be ''4dn_FOF-CT_rna_bio''.
      Written as ##Table_Namespace= in the file header.'
    required: true
    equals_string: 4dn_FOF-CT_rna_bio
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
    description: 'One or more Software entries documenting every tool used to produce
      or process data in this table. Required only when software was used; omit the
      block entirely if no software was applied. Written as repeating #Software_*
      blocks in the file header.'
    required: false
  xyz_unit:
    name: xyz_unit
    required: true
  time_unit:
    name: time_unit
    description: 'Unit used for any time metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Time_Unit=
      in the file header.'
    required: false
  intensity_unit:
    name: intensity_unit
    description: 'Unit used for any intensity metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Intensity_Unit=
      in the file header.'
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    description: 'Method used to perform intensity measurements. Conditionally required
      when any intensity metric is present. Written as #Intensity_Measurement_Method:
      in the file header.'
    required: false
  rna_spot_biological_records:
    name: rna_spot_biological_records
    required: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: RNASpotBiologicalTable
description: 'The RNA Spot Biological Data table of a FOF-bas-CT dataset (namespace:
  4dn_FOF-CT_rna_bio). This class represents the entire file: it holds all dataset-level
  provenance metadata (recorded as header lines in the TSV serialisation) together
  with the full collection of RNASpotBiologicalRecord rows. Submission of this table
  is optional but highly recommended.'
from_schema: https://w3id.org/fof-ct/vol
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    description: 'Identifier for this table type. Must always be ''4dn_FOF-CT_rna_bio''.
      Written as ##Table_Namespace= in the file header.'
    required: true
    equals_string: 4dn_FOF-CT_rna_bio
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
    description: 'One or more Software entries documenting every tool used to produce
      or process data in this table. Required only when software was used; omit the
      block entirely if no software was applied. Written as repeating #Software_*
      blocks in the file header.'
    required: false
  xyz_unit:
    name: xyz_unit
    required: true
  time_unit:
    name: time_unit
    description: 'Unit used for any time metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Time_Unit=
      in the file header.'
    required: false
  intensity_unit:
    name: intensity_unit
    description: 'Unit used for any intensity metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Intensity_Unit=
      in the file header.'
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    description: 'Method used to perform intensity measurements. Conditionally required
      when any intensity metric is present. Written as #Intensity_Measurement_Method:
      in the file header.'
    required: false
  rna_spot_biological_records:
    name: rna_spot_biological_records
    required: true
attributes:
  fof_ct_version:
    name: fof_ct_version
    description: Version of the FOF-CT format used in this file. Always the first
      line of the file header (##FOF-CT_Version=).
    examples:
    - value: v1.0
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
    pattern: ^v[0-9]+\.[0-9]+
  table_namespace:
    name: table_namespace
    description: 'Identifier for this table type. Must always be ''4dn_FOF-CT_rna_bio''.
      Written as ##Table_Namespace= in the file header.'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
    equals_string: 4dn_FOF-CT_rna_bio
  lab_name:
    name: lab_name
    description: 'Name of the laboratory where the experiment was performed. Written
      as #Lab_Name: in the file header.'
    examples:
    - value: Nobel
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
  experimenter_name:
    name: experimenter_name
    description: 'Full name of the person who performed the experiment. Written as
      #Experimenter_Name: in the file header.'
    examples:
    - value: John Doe
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
  experimenter_contact:
    name: experimenter_contact
    description: 'Email address of the person who performed the experiment. Written
      as #Experimenter_Contact: in the file header.'
    examples:
    - value: john.doe@email.com
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
    pattern: ^[^@\s]+@[^@\s]+\.[^@\s]+$
  description:
    name: description
    description: 'Free-text description of the experiment and of the data recorded
      in this table. Should provide sufficient detail for interpretation and reproducibility.
      Written as #Description: in the file header.'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: string
    required: true
  additional_tables:
    name: additional_tables
    description: 'List of additional FOF-CT table namespaces being submitted alongside
      this table, separated by commas in the TSV header. Written as #Additional_Tables:
      in the file header.'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    required: true
    multivalued: true
  softwares:
    name: softwares
    description: 'One or more Software entries documenting every tool used to produce
      or process data in this table. Required only when software was used; omit the
      block entirely if no software was applied. Written as repeating #Software_*
      blocks in the file header.'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    range: XYZUnitEnum
    required: true
  time_unit:
    name: time_unit
    description: 'Unit used for any time metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Time_Unit=
      in the file header.'
    examples:
    - value: sec
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    - SMLocalizationTable
    - SMLocalizationQualityTable
    - UndecodedLocalizationTable
    range: TimeUnitEnum
    required: false
  intensity_unit:
    name: intensity_unit
    description: 'Unit used for any intensity metric reported in user-defined columns.
      Conditionally required when any such metric is present. Written as ##Intensity_Unit=
      in the file header.'
    examples:
    - value: a.u.
    - value: photons
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    - SMLocalizationTable
    - SMLocalizationQualityTable
    - UndecodedLocalizationTable
    range: string
    required: false
  intensity_measurement_method:
    name: intensity_measurement_method
    description: 'Method used to perform intensity measurements. Conditionally required
      when any intensity metric is present. Written as #Intensity_Measurement_Method:
      in the file header.'
    examples:
    - value: Localization centroid intensity
    - value: Mean Fluorescence Intensity
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: RNASpotBiologicalTable
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
    - SMLocalizationTable
    - SMLocalizationQualityTable
    - UndecodedLocalizationTable
    range: string
    required: false
  rna_spot_biological_records:
    name: rna_spot_biological_records
    description: The complete collection of RNASpotBiologicalRecord rows constituting
      this dataset. Each record corresponds to one data row in the TSV serialisation
      and must include at least one user-defined biological property column.
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    domain: RNASpotBiologicalTable
    owner: RNASpotBiologicalTable
    domain_of:
    - RNASpotBiologicalTable
    range: RNASpotBiologicalRecord
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>