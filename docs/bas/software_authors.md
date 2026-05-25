---
search:
  boost: 5.0
---

# Slot: software_authors 


_Author name(s) in 'Surname, Firstname' format, multiple authors separated by semicolons. Written as #Software_Authors:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_authors](https://w3id.org/fof-ct/software_authors)
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
| Mateo, LJ; Sinnott-Armstrong, N; Boettiger, AN |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_authors |
| native | fof_ct:software_authors |




## LinkML Source

<details>
```yaml
name: software_authors
description: 'Author name(s) in ''Surname, Firstname'' format, multiple authors separated
  by semicolons. Written as #Software_Authors:.'
examples:
- value: Mateo, LJ; Sinnott-Armstrong, N; Boettiger, AN
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Software
range: string
required: true

```
</details></div>