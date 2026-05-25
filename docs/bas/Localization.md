---
search:
  boost: 10.0
---

# Class: Localization 


_A single individual localisation event contributing to the final position of a bright DNA Spot in a multiplexed FISH experiment (e.g. MERFISH). Each instance of this class corresponds to one row in the CSV data section of the FOF-CT Spot Demultiplexing table. The spot_id field links each Localization to its parent Spot in the core table (or RNA Spot Data table); it may be NA when the localisation could not be assigned to any Spot. This class accepts additional user-defined optional columns (e.g. Hyb, Brightness, Fit_Quality)._



<div data-search-exclude markdown="1">



URI: [fof_ct:Localization](https://w3id.org/fof-ct/Localization)





```mermaid
 classDiagram
    class Localization
    click Localization href "../Localization/"
      LocalizationMixin <|-- Localization
        click LocalizationMixin href "../LocalizationMixin/"
      
      Localization : fluor
        
      Localization : loc_id
        
      Localization : spot_id
        
      Localization : x
        
      Localization : y
        
      Localization : z
        
      
```





## Inheritance
* **Localization** [ [LocalizationMixin](LocalizationMixin.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [spot_id](spot_id.md) | 1 <br/> [Integer](Integer.md) | Unique identifier for a bright DNA Spot | direct |
| [fluor](fluor.md) | 1 <br/> [String](String.md) | Fluorescent channel in which this localization event was detected (e | direct |
| [loc_id](loc_id.md) | 1 <br/> [Integer](Integer.md) | A unique integer identifier for an individual localization event | [LocalizationMixin](LocalizationMixin.md) |
| [x](x.md) | 1 <br/> [Float](Float.md) | Sub-pixel X coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |
| [y](y.md) | 1 <br/> [Float](Float.md) | Sub-pixel Y coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |
| [z](z.md) | 1 <br/> [Float](Float.md) | Sub-pixel Z coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DemultiplexingTable](DemultiplexingTable.md) | [localizations](localizations.md) | range | [Localization](Localization.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:Localization |
| native | fof_ct:Localization |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Localization
description: A single individual localisation event contributing to the final position
  of a bright DNA Spot in a multiplexed FISH experiment (e.g. MERFISH). Each instance
  of this class corresponds to one row in the CSV data section of the FOF-CT Spot
  Demultiplexing table. The spot_id field links each Localization to its parent Spot
  in the core table (or RNA Spot Data table); it may be NA when the localisation could
  not be assigned to any Spot. This class accepts additional user-defined optional
  columns (e.g. Hyb, Brightness, Fit_Quality).
from_schema: https://w3id.org/fof-ct/bas
mixins:
- LocalizationMixin
slots:
- spot_id
- fluor
slot_usage:
  loc_id:
    name: loc_id
    identifier: true
    required: true
  spot_id:
    name: spot_id
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
  fluor:
    name: fluor
    required: true

```
</details>

### Induced

<details>
```yaml
name: Localization
description: A single individual localisation event contributing to the final position
  of a bright DNA Spot in a multiplexed FISH experiment (e.g. MERFISH). Each instance
  of this class corresponds to one row in the CSV data section of the FOF-CT Spot
  Demultiplexing table. The spot_id field links each Localization to its parent Spot
  in the core table (or RNA Spot Data table); it may be NA when the localisation could
  not be assigned to any Spot. This class accepts additional user-defined optional
  columns (e.g. Hyb, Brightness, Fit_Quality).
from_schema: https://w3id.org/fof-ct/bas
mixins:
- LocalizationMixin
slot_usage:
  loc_id:
    name: loc_id
    identifier: true
    required: true
  spot_id:
    name: spot_id
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
  fluor:
    name: fluor
    required: true
attributes:
  spot_id:
    name: spot_id
    description: Unique identifier for a bright DNA Spot. Used as a primary key in
      quality and biological data tables, and as a foreign key linking localization
      events to their parent Spot in the demultiplexing table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Localization
    domain_of:
    - Spot
    - Localization
    - SpotQualityRecord
    - SpotBiologicalRecord
    range: integer
    required: true
  fluor:
    name: fluor
    description: Fluorescent channel in which this localization event was detected
      (e.g. DAPI, GFP, Cy5, Alexa647). Mandatory in both the Spot Demultiplexing and
      Undecoded SM Localization tables.
    examples:
    - value: Cy5
    - value: Alexa647
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    owner: Localization
    domain_of:
    - Localization
    range: string
    required: true
  loc_id:
    name: loc_id
    description: A unique integer identifier for an individual localization event.
      Loc_ID values are unique across the entire dataset. Serves as primary key in
      the Spot Demultiplexing, SM Localization Data, and Undecoded SM Localization
      tables, and as a foreign key in the SM Localization Quality table.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/bas
    rank: 1000
    identifier: true
    owner: Localization
    domain_of:
    - LocalizationMixin
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
    owner: Localization
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
    owner: Localization
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
    owner: Localization
    domain_of:
    - LocalizationMixin
    - Spot
    - RNASpot
    range: float
    required: true

```
</details></div>