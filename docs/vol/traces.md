---
search:
  boost: 5.0
---

# Slot: traces 


_The complete collection of Traces constituting this dataset. Each Trace corresponds to one data row in the TSV serialisation._



<div data-search-exclude markdown="1">



URI: [fof_ct:traces](https://w3id.org/fof-ct/traces)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TraceTable](TraceTable.md) | The Trace Data table of a FOF-bas-CT dataset (namespace: 4dn_FOF-CT_trace) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Trace](Trace.md) |
| Domain | [TraceTable](TraceTable.md) |
| Domain Of | [TraceTable](TraceTable.md) |

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
| self | fof_ct:traces |
| native | fof_ct:traces |




## LinkML Source

<details>
```yaml
name: traces
description: The complete collection of Traces constituting this dataset. Each Trace
  corresponds to one data row in the TSV serialisation.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: TraceTable
domain_of:
- TraceTable
range: Trace
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>