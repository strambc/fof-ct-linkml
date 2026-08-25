---
search:
  boost: 5.0
---

# Slot: channel_name 


_The wavelength characteristics of the emission channel used to image this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality, and Undecoded SM Localization tables. Written as the Channel column._



<div data-search-exclude markdown="1">



URI: [fof_ct:channel_name](https://w3id.org/fof-ct/channel_name)
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
| 510/25 |
| 695/81 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:channel_name |
| native | fof_ct:channel_name |




## LinkML Source

<details>
```yaml
name: channel_name
description: The wavelength characteristics of the emission channel used to image
  this Spot / RNA Spot / localization event (e.g. '510/25', '695/81'). Mandatory in
  the Spot Demultiplexing, Spot Quality, RNA Spot Quality, SM Localization Quality,
  and Undecoded SM Localization tables. Written as the Channel column.
examples:
- value: 510/25
- value: 695/81
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Localization
- SpotQualityRecord
- RNASpotQualityRecord
range: string

```
</details></div>