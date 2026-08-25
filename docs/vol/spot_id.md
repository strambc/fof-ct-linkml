---
search:
  boost: 5.0
---

# Slot: spot_id 


_Unique identifier for a bright DNA Spot. Used as a primary key in quality and biological data tables, and as a foreign key linking localization events to their parent Spot in the demultiplexing table. In FOF-vol-CT (table 13, SM Localization Data), this same Spot_ID concept is derived by clustering Single-Molecule (SM) Localization events rather than by direct optical detection, and every SM Localization event MUST report its associated Spot_ID._



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
| [SMLocalization](SMLocalization.md) | A single individual single-molecule (SM) localization event in a FOF-vol-CT d... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Spot](Spot.md), [Localization](Localization.md), [SpotQualityRecord](SpotQualityRecord.md), [SpotBiologicalRecord](SpotBiologicalRecord.md), [SMLocalization](SMLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




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
  their parent Spot in the demultiplexing table. In FOF-vol-CT (table 13, SM Localization
  Data), this same Spot_ID concept is derived by clustering Single-Molecule (SM) Localization
  events rather than by direct optical detection, and every SM Localization event
  MUST report its associated Spot_ID.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- Spot
- Localization
- SpotQualityRecord
- SpotBiologicalRecord
- SMLocalization
range: integer

```
</details></div>