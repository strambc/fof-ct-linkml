---
search:
  boost: 5.0
---

# Slot: fluor 


_Fluorescent channel in which this localization event was detected (e.g. DAPI, GFP, Cy5, Alexa647). Mandatory in both the Spot Demultiplexing and Undecoded SM Localization tables._



<div data-search-exclude markdown="1">



URI: [fof_ct:fluor](https://w3id.org/fof-ct/fluor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Localization](Localization.md) | A single individual localisation event contributing to the final position of ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Localization](Localization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Cy5 |
| Alexa647 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:fluor |
| native | fof_ct:fluor |




## LinkML Source

<details>
```yaml
name: fluor
description: Fluorescent channel in which this localization event was detected (e.g.
  DAPI, GFP, Cy5, Alexa647). Mandatory in both the Spot Demultiplexing and Undecoded
  SM Localization tables.
examples:
- value: Cy5
- value: Alexa647
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Localization
range: string

```
</details></div>