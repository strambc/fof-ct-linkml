---
search:
  boost: 5.0
---

# Slot: sm_localizations 


_The complete collection of SMLocalization events constituting this dataset. Each entry corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:sm_localizations](https://w3id.org/fof-ct/sm_localizations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SMLocalizationTable](SMLocalizationTable.md) | The SM Localization Data table of a FOF-vol-CT dataset (namespace: 4dn_FOF-CT... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SMLocalization](SMLocalization.md) |
| Domain | [SMLocalizationTable](SMLocalizationTable.md) |
| Domain Of | [SMLocalizationTable](SMLocalizationTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:sm_localizations |
| native | fof_ct:sm_localizations |




## LinkML Source

<details>
```yaml
name: sm_localizations
description: The complete collection of SMLocalization events constituting this dataset.
  Each entry corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: SMLocalizationTable
domain_of:
- SMLocalizationTable
range: SMLocalization
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>