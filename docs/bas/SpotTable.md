---
search:
  boost: 10.0
---

# Class: SpotTable 


_The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_core). This class represents the entire file: it holds all dataset-level provenance metadata (recorded as header lines in the TSV serialisation) together with the full collection of Spots (recorded as data rows). Analogous to the MappingSet class in SSSOM._



<div data-search-exclude markdown="1">



URI: [fof_ct:SpotTable](https://w3id.org/fof-ct/SpotTable)





```mermaid
 classDiagram
    class SpotTable
    click SpotTable href "../SpotTable/"
      SpotTable : additional_tables
        
          
    
        
        
        SpotTable --> "*" TableNamespaceEnum : additional_tables
        click TableNamespaceEnum href "../TableNamespaceEnum/"
    

        
      SpotTable : description
        
      SpotTable : experimenter_contact
        
      SpotTable : experimenter_name
        
      SpotTable : fof_ct_version
        
      SpotTable : genome_assembly
        
      SpotTable : lab_name
        
      SpotTable : modification
        
      SpotTable : softwares
        
          
    
        
        
        SpotTable --> "1..*" Software : softwares
        click Software href "../Software/"
    

        
      SpotTable : spots
        
          
    
        
        
        SpotTable --> "1..*" Spot : spots
        click Spot href "../Spot/"
    

        
      SpotTable : table_namespace
        
      SpotTable : vcf_file_name
        
      SpotTable : vcf_version
        
      SpotTable : xyz_unit
        
          
    
        
        
        SpotTable --> "1" XYZUnitEnum : xyz_unit
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
| [genome_assembly](genome_assembly.md) | 1 <br/> [String](String.md) | Genome build used for Chrom, Chrom_Start and Chrom_End coordinates | direct |
| [xyz_unit](xyz_unit.md) | 1 <br/> [XYZUnitEnum](XYZUnitEnum.md) | Unit used to represent X, Y, Z spatial coordinates or distances in this table | direct |
| [lab_name](lab_name.md) | 1 <br/> [String](String.md) | Name of the laboratory where the experiment was performed | direct |
| [experimenter_name](experimenter_name.md) | 1 <br/> [String](String.md) | Full name of the person who performed the experiment | direct |
| [experimenter_contact](experimenter_contact.md) | 1 <br/> [String](String.md) | Email address of the person who performed the experiment | direct |
| [description](description.md) | 1 <br/> [String](String.md) | Free-text description of the experiment and of the data recorded in this tabl... | direct |
| [softwares](softwares.md) | 1..* <br/> [Software](Software.md) | One or more Software entries documenting every tool used to produce or proces... | direct |
| [additional_tables](additional_tables.md) | * <br/> [TableNamespaceEnum](TableNamespaceEnum.md) | List of additional FOF-CT table namespaces being submitted alongside this tab... | direct |
| [spots](spots.md) | 1..* <br/> [Spot](Spot.md) | The complete collection of Spots constituting this dataset | direct |
| [modification](modification.md) | 0..1 <br/> [String](String.md) | Description of the nature and genomic position of a DNA insertion or deletion... | direct |
| [vcf_file_name](vcf_file_name.md) | 0..1 <br/> [String](String.md) | Name of the Variant Call Format (VCF) file that must be submitted alongside t... | direct |
| [vcf_version](vcf_version.md) | 0..1 <br/> [String](String.md) | Version of the VCF format used for the accompanying VCF file | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SpotTable](SpotTable.md) | [spots](spots.md) | domain | [SpotTable](SpotTable.md) |
| [SpotTable](SpotTable.md) | [modification](modification.md) | domain | [SpotTable](SpotTable.md) |
| [SpotTable](SpotTable.md) | [vcf_file_name](vcf_file_name.md) | domain | [SpotTable](SpotTable.md) |
| [SpotTable](SpotTable.md) | [vcf_version](vcf_version.md) | domain | [SpotTable](SpotTable.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:SpotTable |
| native | fof_ct:SpotTable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpotTable
description: 'The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace:
  4dn_FOF-CT_core). This class represents the entire file: it holds all dataset-level
  provenance metadata (recorded as header lines in the TSV serialisation) together
  with the full collection of Spots (recorded as data rows). Analogous to the MappingSet
  class in SSSOM.'
from_schema: https://w3id.org/fof-ct/bas
slots:
- fof_ct_version
- table_namespace
- genome_assembly
- xyz_unit
- lab_name
- experimenter_name
- experimenter_contact
- description
- softwares
- additional_tables
- spots
- modification
- vcf_file_name
- vcf_version
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    required: true
    equals_string: 4dn_FOF-CT_core
  genome_assembly:
    name: genome_assembly
    required: true
  xyz_unit:
    name: xyz_unit
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
  softwares:
    name: softwares
    required: true
  spots:
    name: spots
    required: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: SpotTable
description: 'The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace:
  4dn_FOF-CT_core). This class represents the entire file: it holds all dataset-level
  provenance metadata (recorded as header lines in the TSV serialisation) together
  with the full collection of Spots (recorded as data rows). Analogous to the MappingSet
  class in SSSOM.'
from_schema: https://w3id.org/fof-ct/bas
slot_usage:
  fof_ct_version:
    name: fof_ct_version
    required: true
  table_namespace:
    name: table_namespace
    required: true
    equals_string: 4dn_FOF-CT_core
  genome_assembly:
    name: genome_assembly
    required: true
  xyz_unit:
    name: xyz_unit
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
  softwares:
    name: softwares
    required: true
  spots:
    name: spots
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
    owner: SpotTable
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
    owner: SpotTable
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
    equals_string: 4dn_FOF-CT_core
  genome_assembly:
    name: genome_assembly
    description: 'Genome build used for Chrom, Chrom_Start and Chrom_End coordinates.
      The 4DN Data Portal accepts GRCh38 (human) and GRCm38 (mouse). When the genome
      under study contains an INSERTION or DELETION the value must use the mandatory
      ''custom-build:'' prefix followed by a descriptive name (e.g., custom-build:GRCm38+pJT039(insertion)).
      Written as ##Genome_Assembly= in the file header.'
    examples:
    - value: GRCh38
    - value: custom-build:GRCm38+pJT039(insertion)
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: SpotTable
    domain_of:
    - SpotTable
    - RNASpotTable
    range: string
    required: true
  xyz_unit:
    name: xyz_unit
    description: 'Unit used to represent X, Y, Z spatial coordinates or distances
      in this table. Use ''micron'' to avoid issues with Greek symbols. Values should
      be drawn from SI units of length. Written as ##XYZ_Unit= in the file header.
      Conditionally required when any location or distance metric is reported.'
    examples:
    - value: micron
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: SpotTable
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
  lab_name:
    name: lab_name
    description: 'Name of the laboratory where the experiment was performed. Written
      as #Lab_Name: in the file header.'
    examples:
    - value: Nobel
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: SpotTable
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
    owner: SpotTable
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
    owner: SpotTable
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
    owner: SpotTable
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
  softwares:
    name: softwares
    description: 'One or more Software entries documenting every tool used to produce
      or process data in this table. Written as repeating #Software_* blocks in the
      file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: SpotTable
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
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  additional_tables:
    name: additional_tables
    description: 'List of additional FOF-CT table namespaces being submitted alongside
      this table, separated by commas in the TSV header. Written as #Additional_Tables:
      in the file header.'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: SpotTable
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
    multivalued: true
  spots:
    name: spots
    description: The complete collection of Spots constituting this dataset. Each
      Spot corresponds to one data row in the TSV serialisation.
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    domain: SpotTable
    owner: SpotTable
    domain_of:
    - SpotTable
    range: Spot
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  modification:
    name: modification
    description: 'Description of the nature and genomic position of a DNA insertion
      or deletion in the genome under study. Conditionally required when genome_assembly
      uses the ''custom-build:'' prefix. Written as ##Modification= in the file header.'
    examples:
    - value: pJT039:chr3(insertion 0001-2500)
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    domain: SpotTable
    owner: SpotTable
    domain_of:
    - SpotTable
    range: string
  vcf_file_name:
    name: vcf_file_name
    description: 'Name of the Variant Call Format (VCF) file that must be submitted
      alongside the dataset to describe the genome insertion or deletion. Conditionally
      required when genome_assembly uses the ''custom-build:'' prefix. Written as
      ##VCF_File_Name= in the file header.'
    examples:
    - value: pJT039:chr3.vcf
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    domain: SpotTable
    owner: SpotTable
    domain_of:
    - SpotTable
    range: string
  vcf_version:
    name: vcf_version
    description: 'Version of the VCF format used for the accompanying VCF file. Conditionally
      required when genome_assembly uses the ''custom-build:'' prefix. Written as
      ##VCF_Version= in the file header.'
    examples:
    - value: v4.2
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    domain: SpotTable
    owner: SpotTable
    domain_of:
    - SpotTable
    range: string
tree_root: true

```
</details></div>