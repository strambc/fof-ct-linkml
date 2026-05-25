---
search:
  boost: 5.0
---

# Slot: loc_id 


_A unique integer identifier for an individual localization event. Loc_ID values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing, SM Localization Data, and Undecoded SM Localization tables, and as a foreign key in the SM Localization Quality table._



<div data-search-exclude markdown="1">



URI: [fof_ct:loc_id](https://w3id.org/fof-ct/loc_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocalizationMixin](LocalizationMixin.md) | Mixin capturing the shared concept of a single localization event across FOF-... |  no  |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [LocalizationMixin](LocalizationMixin.md) |

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
| self | fof_ct:loc_id |
| native | fof_ct:loc_id |




## LinkML Source

<details>
```yaml
name: loc_id
description: A unique integer identifier for an individual localization event. Loc_ID
  values are unique across the entire dataset. Serves as primary key in the Spot Demultiplexing,
  SM Localization Data, and Undecoded SM Localization tables, and as a foreign key
  in the SM Localization Quality table.
examples:
- value: '1'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- LocalizationMixin
range: integer

```
</details></div>