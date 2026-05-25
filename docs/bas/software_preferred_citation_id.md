---
search:
  boost: 5.0
---

# Slot: software_preferred_citation_id 


_Unique identifier (DOI, PMCID, ArXiv ID, etc.) for the primary publication describing this software. Written as #Software_PreferredCitationID:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_preferred_citation_id](https://w3id.org/fof-ct/software_preferred_citation_id)
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
| https://doi.org/10.1038/s41596-020-00478-x |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_preferred_citation_id |
| native | fof_ct:software_preferred_citation_id |




## LinkML Source

<details>
```yaml
name: software_preferred_citation_id
description: 'Unique identifier (DOI, PMCID, ArXiv ID, etc.) for the primary publication
  describing this software. Written as #Software_PreferredCitationID:.'
examples:
- value: https://doi.org/10.1038/s41596-020-00478-x
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- Software
range: uri
required: true

```
</details></div>