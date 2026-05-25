---
search:
  boost: 5.0
---

# Slot: roi_mappings 


_The complete collection of ROI boundary records constituting this dataset. Each ROIMapping corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:roi_mappings](https://w3id.org/fof-ct/roi_mappings)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ROIMappingTable](ROIMappingTable.md) | The Cell/ROI Mapping table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_map... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ROIMapping](ROIMapping.md) |
| Domain | [ROIMappingTable](ROIMappingTable.md) |
| Domain Of | [ROIMappingTable](ROIMappingTable.md) |

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
| self | fof_ct:roi_mappings |
| native | fof_ct:roi_mappings |




## LinkML Source

<details>
```yaml
name: roi_mappings
description: The complete collection of ROI boundary records constituting this dataset.
  Each ROIMapping corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: ROIMappingTable
domain_of:
- ROIMappingTable
range: ROIMapping
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>