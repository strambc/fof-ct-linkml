---
search:
  boost: 5.0
---

# Slot: software_title 


_Name of the software tool. Written as #Software_Title:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_title](https://w3id.org/fof-ct/software_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Software](Software.md) | Provenance metadata for a single software tool used to produce or process dat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Software](Software.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| ChrTracer3 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_title |
| native | fof_ct:software_title |




## LinkML Source

<details>
```yaml
name: software_title
description: 'Name of the software tool. Written as #Software_Title:.'
examples:
- value: ChrTracer3
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Software
range: string
required: true

```
</details></div>