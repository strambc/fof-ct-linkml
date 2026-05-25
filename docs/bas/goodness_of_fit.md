---
search:
  boost: 5.0
---

# Slot: goodness_of_fit 


_Metric quantifying how well the fitted model matches the observed signal (e.g. chi-squared, R-squared). Optional (but standardised name) in the Spot Quality table; recommended in the SM Localization Quality table._



<div data-search-exclude markdown="1">



URI: [fof_ct:goodness_of_fit](https://w3id.org/fof-ct/goodness_of_fit)
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
| 0.95 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:goodness_of_fit |
| native | fof_ct:goodness_of_fit |




## LinkML Source

<details>
```yaml
name: goodness_of_fit
description: Metric quantifying how well the fitted model matches the observed signal
  (e.g. chi-squared, R-squared). Optional (but standardised name) in the Spot Quality
  table; recommended in the SM Localization Quality table.
examples:
- value: '0.95'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
domain_of:
- SpotQualityRecord
range: float

```
</details></div>