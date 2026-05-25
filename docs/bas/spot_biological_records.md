---
search:
  boost: 5.0
---

# Slot: spot_biological_records 


_The complete collection of SpotBiologicalRecord rows constituting this dataset. Each record corresponds to one data row in the TSV serialisation and must include at least one user-defined biological property column._



<div data-search-exclude markdown="1">



URI: [fof_ct:spot_biological_records](https://w3id.org/fof-ct/spot_biological_records)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotBiologicalTable](SpotBiologicalTable.md) | The Spot Biological Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpotBiologicalRecord](SpotBiologicalRecord.md) |
| Domain | [SpotBiologicalTable](SpotBiologicalTable.md) |
| Domain Of | [SpotBiologicalTable](SpotBiologicalTable.md) |

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
| self | fof_ct:spot_biological_records |
| native | fof_ct:spot_biological_records |




## LinkML Source

<details>
```yaml
name: spot_biological_records
description: The complete collection of SpotBiologicalRecord rows constituting this
  dataset. Each record corresponds to one data row in the TSV serialisation and must
  include at least one user-defined biological property column.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain: SpotBiologicalTable
domain_of:
- SpotBiologicalTable
range: SpotBiologicalRecord
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>