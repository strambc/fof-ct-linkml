---
search:
  boost: 5.0
---

# Slot: software_type 


_Functional category of the software tool. Written as #Software_Type:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_type](https://w3id.org/fof-ct/software_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Software](Software.md) | Provenance metadata for a single software tool used to produce or process dat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SoftwareTypeEnum](SoftwareTypeEnum.md) |
| Domain Of | [Software](Software.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| SpotLoc+Tracing |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_type |
| native | fof_ct:software_type |




## LinkML Source

<details>
```yaml
name: software_type
description: 'Functional category of the software tool. Written as #Software_Type:.'
examples:
- value: SpotLoc+Tracing
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- Software
range: SoftwareTypeEnum
required: true

```
</details></div>