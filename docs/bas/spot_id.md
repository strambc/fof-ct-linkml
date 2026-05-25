---
search:
  boost: 5.0
---

# Slot: spot_id 


_Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table._



<div data-search-exclude markdown="1">



URI: [fof_ct:spot_id](https://w3id.org/fof-ct/spot_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spot](Spot.md) | A single DNA-FISH bright Spot detected in a ball-and-stick Chromatin Tracing ... |  yes  |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |
| [SpotBiologicalRecord](SpotBiologicalRecord.md) | A single row in the Spot Biological Data table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [Localization](Localization.md), [SpotQualityRecord](SpotQualityRecord.md), [SpotBiologicalRecord](SpotBiologicalRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:spot_id |
| native | fof_ct:spot_id |




## LinkML Source

<details>
```yaml
name: spot_id
description: Unique identifier for a bright DNA Spot. Used as a primary key in quality
  and biological data tables, and as a foreign key linking localization events to
  their parent Spot in the demultiplexing table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Spot
- Localization
- SpotQualityRecord
- SpotBiologicalRecord
range: integer

```
</details></div>