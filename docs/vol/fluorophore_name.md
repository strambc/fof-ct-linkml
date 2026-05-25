---
search:
  boost: 5.0
---

# Slot: fluorophore_name 


_The name of the fluorophore used for this Spot (e.g. AlexaFluor_488). Mandatory in the Spot Quality table._



<div data-search-exclude markdown="1">



URI: [fof_ct:fluorophore_name](https://w3id.org/fof-ct/fluorophore_name)
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
| AlexaFluor_488 |
| Cy5 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:fluorophore_name |
| native | fof_ct:fluorophore_name |




## LinkML Source

<details>
```yaml
name: fluorophore_name
description: The name of the fluorophore used for this Spot (e.g. AlexaFluor_488).
  Mandatory in the Spot Quality table.
examples:
- value: AlexaFluor_488
- value: Cy5
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotQualityRecord
range: string

```
</details></div>