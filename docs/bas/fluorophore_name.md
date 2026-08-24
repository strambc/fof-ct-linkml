---
search:
  boost: 5.0
---

# Slot: fluorophore_name 


_The name of the fluorophore whose emission was used to detect this Spot / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Fluor column._



<div data-search-exclude markdown="1">



URI: [fof_ct:fluorophore_name](https://w3id.org/fof-ct/fluorophore_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |
| [RNASpotQualityRecord](RNASpotQualityRecord.md) | A single row in the RNA Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Localization](Localization.md), [SpotQualityRecord](SpotQualityRecord.md), [RNASpotQualityRecord](RNASpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| AlexaFluor_488 |
| Cy5 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:fluorophore_name |
| native | fof_ct:fluorophore_name |




## LinkML Source

<details>
```yaml
name: fluorophore_name
description: The name of the fluorophore whose emission was used to detect this Spot
  / RNA Spot / localization event (e.g. AlexaFluor_488, Cy5). Mandatory in the Spot
  Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded
  SM Localization tables. Written as the Fluor column.
examples:
- value: AlexaFluor_488
- value: Cy5
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Localization
- SpotQualityRecord
- RNASpotQualityRecord
range: string

```
</details></div>