---
search:
  boost: 5.0
---

# Slot: spots 


_The complete collection of Spots constituting this dataset. Each Spot corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:spots](https://w3id.org/fof-ct/spots)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotTable](SpotTable.md) | The DNA-Spot/Trace Data core table of a FOF-bas-CT dataset (namespace: 4dn_FO... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spot](Spot.md) |
| Domain | [SpotTable](SpotTable.md) |
| Domain Of | [SpotTable](SpotTable.md) |

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
| self | fof_ct:spots |
| native | fof_ct:spots |




## LinkML Source

<details>
```yaml
name: spots
description: The complete collection of Spots constituting this dataset. Each Spot
  corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: SpotTable
domain_of:
- SpotTable
range: Spot
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>