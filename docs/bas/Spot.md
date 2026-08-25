---
search:
  boost: 10.0
---

# Class: Spot 


_A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing experiment. Each instance of this class corresponds to one row in the TSV data section of the FOF-CT core table and represents a specific genomic target sequence localised in 3D space and assigned to a chromatin Trace._



<div data-search-exclude markdown="1">



URI: [fof_ct:Spot](https://w3id.org/fof-ct/Spot)





```mermaid
 classDiagram
    class Spot
    click Spot href "../Spot/"
      Spot : cell_id
        
      Spot : chrom
        
      Spot : chrom_end
        
      Spot : chrom_start
        
      Spot : extra_cell_roi_id
        
      Spot : spot_id
        
      Spot : sub_cell_roi_id
        
      Spot : trace_id
        
      Spot : x
        
      Spot : y
        
      Spot : z
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [spot_id](spot_id.md) | 1 <br/> [Integer](Integer.md) | Unique identifier for a bright DNA Spot | direct |
| [trace_id](trace_id.md) | 1 <br/> [Integer](Integer.md) | Unique identifier for a chromatin Trace | direct |
| [x](x.md) | 1 <br/> [Float](Float.md) | Sub-pixel X coordinate of this detected event (Spot or localisation) in the u... | direct |
| [y](y.md) | 1 <br/> [Float](Float.md) | Sub-pixel Y coordinate of this detected event (Spot or localisation) in the u... | direct |
| [z](z.md) | 1 <br/> [Float](Float.md) | Sub-pixel Z coordinate of this detected event (Spot or localisation) in the u... | direct |
| [chrom](chrom.md) | 1 <br/> [String](String.md) | Chromosome name/identifier using BED (Browser Extensible Data) convention (e | direct |
| [chrom_start](chrom_start.md) | 1 <br/> [Integer](Integer.md) | 0-based start coordinate on the chromosome for the genomic target sequence, f... | direct |
| [chrom_end](chrom_end.md) | 1 <br/> [Integer](Integer.md) | Non-inclusive end coordinate on the chromosome for the genomic target sequenc... | direct |
| [sub_cell_roi_id](sub_cell_roi_id.md) | 0..1 <br/> [Integer](Integer.md) | Unique identifier for a sub-cellular structure ROI (e | direct |
| [cell_id](cell_id.md) | 0..1 <br/> [Integer](Integer.md) | Unique identifier for a Cell | direct |
| [extra_cell_roi_id](extra_cell_roi_id.md) | 0..1 <br/> [Integer](Integer.md) | Unique identifier for an extracellular structure ROI (e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SpotTable](SpotTable.md) | [spots](spots.md) | range | [Spot](Spot.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:Spot |
| native | fof_ct:Spot |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Spot
description: A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin
  Tracing experiment. Each instance of this class corresponds to one row in the TSV
  data section of the FOF-CT core table and represents a specific genomic target sequence
  localised in 3D space and assigned to a chromatin Trace.
from_schema: https://w3id.org/fof-ct/bas
slots:
- spot_id
- trace_id
- x
- y
- z
- chrom
- chrom_start
- chrom_end
- sub_cell_roi_id
- cell_id
- extra_cell_roi_id
slot_usage:
  spot_id:
    name: spot_id
    identifier: true
    required: true
  trace_id:
    name: trace_id
    required: true
  x:
    name: x
    required: true
  y:
    name: y
    required: true
  z:
    name: z
    required: true
  chrom:
    name: chrom
    required: true
  chrom_start:
    name: chrom_start
    required: true
  chrom_end:
    name: chrom_end
    required: true

```
</details>

### Induced

<details>
```yaml
name: Spot
description: A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin
  Tracing experiment. Each instance of this class corresponds to one row in the TSV
  data section of the FOF-CT core table and represents a specific genomic target sequence
  localised in 3D space and assigned to a chromatin Trace.
from_schema: https://w3id.org/fof-ct/bas
slot_usage:
  spot_id:
    name: spot_id
    identifier: true
    required: true
  trace_id:
    name: trace_id
    required: true
  x:
    name: x
    required: true
  y:
    name: y
    required: true
  z:
    name: z
    required: true
  chrom:
    name: chrom
    required: true
  chrom_start:
    name: chrom_start
    required: true
  chrom_end:
    name: chrom_end
    required: true
attributes:
  spot_id:
    name: spot_id
    description: Unique identifier for a bright DNA Spot. Used as a primary key in
      quality and biological data tables, and as a foreign key linking localization
      events to their parent Spot in the demultiplexing table. In FOF-vol-CT (table
      13, SM Localization Data), this same Spot_ID concept is derived by clustering
      Single-Molecule (SM) Localization events rather than by direct optical detection,
      and every SM Localization event MUST report its associated Spot_ID.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    identifier: true
    owner: Spot
    domain_of:
    - Spot
    - Localization
    - SpotQualityRecord
    - SpotBiologicalRecord
    range: integer
    required: true
  trace_id:
    name: trace_id
    description: Unique identifier for a chromatin Trace. Used as a primary key in
      the Trace Data table and as a foreign key in the RNA Spot Data table and (mandatorily)
      in the FOF-vol-CT SM Localization Data table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    - Trace
    - RNASpot
    range: integer
    required: true
  x:
    name: x
    description: Sub-pixel X coordinate of this detected event (Spot or localisation)
      in the unit specified by xyz_unit. The reported value is the final position
      after all post-processing corrections (drift correction, chromatic correction,
      etc.).
    examples:
    - value: '14.43'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - LocalizationMixin
    - Spot
    - RNASpot
    range: float
    required: true
  y:
    name: y
    description: Sub-pixel Y coordinate of this detected event (Spot or localisation)
      in the unit specified by xyz_unit. The reported value is the final position
      after all post-processing corrections.
    examples:
    - value: '41.43'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - LocalizationMixin
    - Spot
    - RNASpot
    range: float
    required: true
  z:
    name: z
    description: Sub-pixel Z coordinate of this detected event (Spot or localisation)
      in the unit specified by xyz_unit. The reported value is the final position
      after all post-processing corrections.
    examples:
    - value: '1.23'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - LocalizationMixin
    - Spot
    - RNASpot
    range: float
    required: true
  chrom:
    name: chrom
    description: Chromosome name/identifier using BED (Browser Extensible Data) convention
      (e.g., chr3, chrY, chr2_random). Used by both the core (Spot) and vol_core (SMLocalization)
      tables.
    examples:
    - value: chr3
    - value: chrY
    - value: chr2_random
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    range: string
    required: true
  chrom_start:
    name: chrom_start
    description: 0-based start coordinate on the chromosome for the genomic target
      sequence, following BED convention. Used by both the core (Spot) and vol_core
      (SMLocalization) tables.
    examples:
    - value: '0'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    range: integer
    required: true
    minimum_value: 0
  chrom_end:
    name: chrom_end
    description: Non-inclusive end coordinate on the chromosome for the genomic target
      sequence, following BED convention. Used by both the core (Spot) and vol_core
      (SMLocalization) tables.
    examples:
    - value: '1000'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    range: integer
    required: true
    minimum_value: 0
  sub_cell_roi_id:
    name: sub_cell_roi_id
    description: Unique identifier for a sub-cellular structure ROI (e.g., nucleus,
      nucleolus). Links to the Sub-Cell ROI Data table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    - RNASpot
    - SubCellROI
    - ROIMapping
    range: integer
  cell_id:
    name: cell_id
    description: Unique identifier for a Cell. Links to the Cell Data table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    - RNASpot
    - Cell
    - SubCellROI
    - ROIMapping
    range: integer
  extra_cell_roi_id:
    name: extra_cell_roi_id
    description: Unique identifier for an extracellular structure ROI (e.g., tissue,
      organoid). Links to the Extra-Cell ROI Data table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Spot
    domain_of:
    - Spot
    - RNASpot
    - Cell
    - ExtraCellROI
    - ROIMapping
    range: integer

```
</details></div>