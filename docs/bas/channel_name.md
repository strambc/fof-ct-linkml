---
search:
  boost: 5.0
---

# Slot: channel_name 


_The name of the imaging channel used for this Spot (e.g. 510/25). Mandatory in the Spot Quality table._



<div data-search-exclude markdown="1">



URI: [fof_ct:channel_name](https://w3id.org/fof-ct/channel_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 510/25 |
| 647/50 |



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
description: The name of the imaging channel used for this Spot (e.g. 510/25). Mandatory
  in the Spot Quality table.
examples:
- value: 510/25
- value: 647/50
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: string

```
</details></div>