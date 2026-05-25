---
search:
  boost: 5.0
---

# Slot: transcript_id 


_Official transcript identifier for the specific transcript targeted by the FISH probe. Conditionally required when multiple transcripts share the same gene_id and the FISH probe can distinguish among them. The type of identifier used must be declared in the transcript_id_type header field._



<div data-search-exclude markdown="1">



URI: [fof_ct:transcript_id](https://w3id.org/fof-ct/transcript_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RNASpot](RNASpot.md) | A single detected RNA bright Spot corresponding to one RNA transcript locatio... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [RNASpot](RNASpot.md) |
| Domain Of | [RNASpot](RNASpot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ENST00000331789 |
| NM_001101.5 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fof_ct:transcript_id |
| native | fof_ct:transcript_id |




## LinkML Source

<details>
```yaml
name: transcript_id
description: Official transcript identifier for the specific transcript targeted by
  the FISH probe. Conditionally required when multiple transcripts share the same
  gene_id and the FISH probe can distinguish among them. The type of identifier used
  must be declared in the transcript_id_type header field.
examples:
- value: ENST00000331789
- value: NM_001101.5
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
domain: RNASpot
domain_of:
- RNASpot
range: string

```
</details></div>