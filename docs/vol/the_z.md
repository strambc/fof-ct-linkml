---
search:
  boost: 5.0
---

# Slot: the_z 


_Identifier of the focal Z-plane in which this localization event was detected. Reserved, conditionally-required column name (TheZ) in the Undecoded SM Localization table: optional to use, but if the focal Z-plane is reported this exact reserved column name MUST be used._



<div data-search-exclude markdown="1">



URI: [fof_ct:the_z](https://w3id.org/fof-ct/the_z)
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
| 10 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:the_z |
| native | fof_ct:the_z |




## LinkML Source

<details>
```yaml
name: the_z
description: 'Identifier of the focal Z-plane in which this localization event was
  detected. Reserved, conditionally-required column name (TheZ) in the Undecoded SM
  Localization table: optional to use, but if the focal Z-plane is reported this exact
  reserved column name MUST be used.'
examples:
- value: '10'
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- UndecodedLocalization
range: integer

```
</details></div>