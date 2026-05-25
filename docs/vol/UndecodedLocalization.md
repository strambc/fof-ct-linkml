---
search:
  boost: 10.0
---

# Class: UndecodedLocalization 


_A single raw, undecoded SM localization event in a FOF-vol-CT dataset. Each instance corresponds to one row in the TSV data section of the Undecoded SM Localization Data table. This class uses LocalizationMixin for the shared loc_id, x, y, z slots. The frame_id column identifies the source imaging frame; fluor identifies the detection channel._



<div data-search-exclude markdown="1">



URI: [fof_ct:UndecodedLocalization](https://w3id.org/fof-ct/UndecodedLocalization)





```mermaid
 classDiagram
    class UndecodedLocalization
    click UndecodedLocalization href "../UndecodedLocalization/"
      LocalizationMixin <|-- UndecodedLocalization
        click LocalizationMixin href "../LocalizationMixin/"
      
      UndecodedLocalization : fluor
        
      UndecodedLocalization : frame_id
        
      UndecodedLocalization : loc_id
        
      UndecodedLocalization : x
        
      UndecodedLocalization : y
        
      UndecodedLocalization : z
        
      
```





## Inheritance
* **UndecodedLocalization** [ [LocalizationMixin](LocalizationMixin.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [frame_id](frame_id.md) | 1 <br/> [Integer](Integer.md) | Unique integer identifier for the imaging frame in which this undecoded local... | direct |
| [fluor](fluor.md) | 1 <br/> [String](String.md) | Fluorescent channel in which this localization event was detected (e | direct |
| [loc_id](loc_id.md) | 1 <br/> [Integer](Integer.md) | Unique integer identifier for this undecoded localization event | [LocalizationMixin](LocalizationMixin.md) |
| [x](x.md) | 1 <br/> [Float](Float.md) | Sub-pixel X coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |
| [y](y.md) | 1 <br/> [Float](Float.md) | Sub-pixel Y coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |
| [z](z.md) | 1 <br/> [Float](Float.md) | Sub-pixel Z coordinate of this detected event (Spot or localisation) in the u... | [LocalizationMixin](LocalizationMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [UndecodedLocalizationTable](UndecodedLocalizationTable.md) | [undecoded_localizations](undecoded_localizations.md) | range | [UndecodedLocalization](UndecodedLocalization.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:UndecodedLocalization |
| native | fof_ct:UndecodedLocalization |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UndecodedLocalization
description: A single raw, undecoded SM localization event in a FOF-vol-CT dataset.
  Each instance corresponds to one row in the TSV data section of the Undecoded SM
  Localization Data table. This class uses LocalizationMixin for the shared loc_id,
  x, y, z slots. The frame_id column identifies the source imaging frame; fluor identifies
  the detection channel.
from_schema: https://w3id.org/fof-ct/vol
mixins:
- LocalizationMixin
slots:
- frame_id
- fluor
slot_usage:
  loc_id:
    name: loc_id
    description: Unique integer identifier for this undecoded localization event.
      Loc_ID values are unique across the entire dataset.
    identifier: true
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
  frame_id:
    name: frame_id
    required: true
  fluor:
    name: fluor
    required: true

```
</details>

### Induced

<details>
```yaml
name: UndecodedLocalization
description: A single raw, undecoded SM localization event in a FOF-vol-CT dataset.
  Each instance corresponds to one row in the TSV data section of the Undecoded SM
  Localization Data table. This class uses LocalizationMixin for the shared loc_id,
  x, y, z slots. The frame_id column identifies the source imaging frame; fluor identifies
  the detection channel.
from_schema: https://w3id.org/fof-ct/vol
mixins:
- LocalizationMixin
slot_usage:
  loc_id:
    name: loc_id
    description: Unique integer identifier for this undecoded localization event.
      Loc_ID values are unique across the entire dataset.
    identifier: true
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
  frame_id:
    name: frame_id
    required: true
  fluor:
    name: fluor
    required: true
attributes:
  frame_id:
    name: frame_id
    description: Unique integer identifier for the imaging frame in which this undecoded
      localization event was detected. Used in the Undecoded SM Localization table.
    examples:
    - value: '42'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: UndecodedLocalization
    domain_of:
    - UndecodedLocalization
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
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: UndecodedLocalization
    domain_of:
    - Localization
    - UndecodedLocalization
    range: string
    required: true
  loc_id:
    name: loc_id
    description: Unique integer identifier for this undecoded localization event.
      Loc_ID values are unique across the entire dataset.
    examples:
    - value: '1'
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    identifier: true
    owner: UndecodedLocalization
    domain_of:
    - LocalizationMixin
    - SMLocalizationQualityRecord
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
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: UndecodedLocalization
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
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: UndecodedLocalization
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
    from_schema: https://w3id.org/fof-ct/vol
    rank: 1000
    owner: UndecodedLocalization
    domain_of:
    - LocalizationMixin
    - Spot
    - RNASpot
    range: float
    required: true

```
</details></div>