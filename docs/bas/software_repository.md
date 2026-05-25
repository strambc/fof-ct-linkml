---
search:
  boost: 5.0
---

# Slot: software_repository 


_URL of the repository where the software release can be obtained. Written as #Software_Repository:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_repository](https://w3id.org/fof-ct/software_repository)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Software](Software.md) | Provenance metadata for a single software tool used to produce or process dat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Software](Software.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| https://github.com/BoettigerLab/ORCA-public |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_repository |
| native | fof_ct:software_repository |




## LinkML Source

<details>
```yaml
name: software_repository
description: 'URL of the repository where the software release can be obtained. Written
  as #Software_Repository:.'
examples:
- value: https://github.com/BoettigerLab/ORCA-public
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Software
range: uri
required: true

```
</details></div>