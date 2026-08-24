---
search:
  boost: 5.0
---

# Slot: software_parameters 


_Free-text description of the input parameters used for the specific analysis run performed using this Software. Should provide sufficient detail about the analysis parameters used to guarantee interpretation and reproducibility (e.g. input parameters used for assessing the precision of single molecule localization or drift correction in X, Y and Z). Written as #Software_Parameters:._



<div data-search-exclude markdown="1">



URI: [fof_ct:software_parameters](https://w3id.org/fof-ct/software_parameters)
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
| X_Loc_Precision Parameter = 1.01 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:software_parameters |
| native | fof_ct:software_parameters |




## LinkML Source

<details>
```yaml
name: software_parameters
description: 'Free-text description of the input parameters used for the specific
  analysis run performed using this Software. Should provide sufficient detail about
  the analysis parameters used to guarantee interpretation and reproducibility (e.g.
  input parameters used for assessing the precision of single molecule localization
  or drift correction in X, Y and Z). Written as #Software_Parameters:.'
examples:
- value: X_Loc_Precision Parameter = 1.01
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- Software
range: string
required: true

```
</details></div>