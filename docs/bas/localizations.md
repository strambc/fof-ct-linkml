---
search:
  boost: 5.0
---

# Slot: localizations 


_The complete collection of Localization events constituting this dataset. Each Localization corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:localizations](https://w3id.org/fof-ct/localizations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DemultiplexingTable](DemultiplexingTable.md) | The Spot Demultiplexing table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Localization](Localization.md) |
| Domain | [DemultiplexingTable](DemultiplexingTable.md) |
| Domain Of | [DemultiplexingTable](DemultiplexingTable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:localizations |
| native | fof_ct:localizations |




## LinkML Source

<details>
```yaml
name: localizations
description: The complete collection of Localization events constituting this dataset.
  Each Localization corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: DemultiplexingTable
domain_of:
- DemultiplexingTable
range: Localization
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>