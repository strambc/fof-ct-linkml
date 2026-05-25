---
search:
  boost: 5.0
---

# Slot: x_precision 


_Metric quantifying the precision of the X-axis localization estimate. Typically the Cramer-Rao lower bound or Thompson method estimate. Recommended in the Spot Quality table; mandatory in the SM Localization Quality table. Must be accompanied by a description in the file header._



<div data-search-exclude markdown="1">



URI: [fof_ct:x_precision](https://w3id.org/fof-ct/x_precision)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpotQualityRecord](SpotQualityRecord.md) | A single row in the Spot Quality table |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [SpotQualityRecord](SpotQualityRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.01 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:x_precision |
| native | fof_ct:x_precision |




## LinkML Source

<details>
```yaml
name: x_precision
description: Metric quantifying the precision of the X-axis localization estimate.
  Typically the Cramer-Rao lower bound or Thompson method estimate. Recommended in
  the Spot Quality table; mandatory in the SM Localization Quality table. Must be
  accompanied by a description in the file header.
examples:
- value: '0.01'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>