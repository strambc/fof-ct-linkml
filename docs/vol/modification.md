---
search:
  boost: 5.0
---

# Slot: modification 


_Description of the nature and genomic position of a DNA insertion or deletion in the genome under study. Conditionally required (content- triggered) when genome_assembly uses the 'custom-build:' prefix. Applies to both the core (bas) and vol_core (vol) tables. Written as ##Modification= in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:modification](https://w3id.org/fof-ct/modification)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  no  |
| [SMLocalizationTable](SMLocalizationTable.md) | The SM Localization Data table of a FOF-vol-CT dataset (namespace: FOF-CT_vol... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SpotTable](SpotTable.md), [SMLocalizationTable](SMLocalizationTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| pJT039:chr3(insertion 0001-2500) |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:modification |
| native | fof_ct:modification |




## LinkML Source

<details>
```yaml
name: modification
description: 'Description of the nature and genomic position of a DNA insertion or
  deletion in the genome under study. Conditionally required (content- triggered)
  when genome_assembly uses the ''custom-build:'' prefix. Applies to both the core
  (bas) and vol_core (vol) tables. Written as ##Modification= in the file header.'
examples:
- value: pJT039:chr3(insertion 0001-2500)
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain_of:
- SpotTable
- SMLocalizationTable
range: string

```
</details></div>