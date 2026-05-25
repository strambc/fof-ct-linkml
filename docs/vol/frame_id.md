---
search:
  boost: 5.0
---

# Slot: frame_id 


_Unique integer identifier for the imaging frame in which this undecoded localization event was detected. Used in the Undecoded SM Localization table._



<div data-search-exclude markdown="1">



URI: [fof_ct:frame_id](https://w3id.org/fof-ct/frame_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UndecodedLocalization](UndecodedLocalization.md) | A single raw, undecoded SM localization event in a FOF-vol-CT dataset |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [UndecodedLocalization](UndecodedLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 42 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:frame_id |
| native | fof_ct:frame_id |




## LinkML Source

<details>
```yaml
name: frame_id
description: Unique integer identifier for the imaging frame in which this undecoded
  localization event was detected. Used in the Undecoded SM Localization table.
examples:
- value: '42'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- UndecodedLocalization
range: integer

```
</details></div>