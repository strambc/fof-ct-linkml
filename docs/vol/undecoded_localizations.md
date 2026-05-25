---
search:
  boost: 5.0
---

# Slot: undecoded_localizations 


_The complete collection of UndecodedLocalization events constituting this dataset. Each entry corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:undecoded_localizations](https://w3id.org/fof-ct/undecoded_localizations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UndecodedLocalizationTable](UndecodedLocalizationTable.md) | The Undecoded SM Localization Data table of a FOF-vol-CT dataset (namespace: ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [UndecodedLocalization](UndecodedLocalization.md) |
| Domain | [UndecodedLocalizationTable](UndecodedLocalizationTable.md) |
| Domain Of | [UndecodedLocalizationTable](UndecodedLocalizationTable.md) |

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
| self | fof_ct:undecoded_localizations |
| native | fof_ct:undecoded_localizations |




## LinkML Source

<details>
```yaml
name: undecoded_localizations
description: The complete collection of UndecodedLocalization events constituting
  this dataset. Each entry corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: UndecodedLocalizationTable
domain_of:
- UndecodedLocalizationTable
range: UndecodedLocalization
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>