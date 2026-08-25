---
search:
  boost: 2.0
---


# Enum: TimeUnitEnum 




_Allowed units for time intervals._



<div data-search-exclude markdown="1">

URI: [fof_ct:TimeUnitEnum](https://w3id.org/fof-ct/TimeUnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| s | None | Seconds (SI base unit) |
| sec | None | Seconds (alternative spelling accepted by FOF-CT) |
| ms | None | Milliseconds |
| msec | None | Milliseconds (alternative spelling accepted by FOF-CT) |
| min | None | Minutes |
| hr | None | Hours |




## Slots

| Name | Description |
| ---  | --- |
| [time_unit](time_unit.md) | Unit used to represent time intervals in this table |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol






## LinkML Source

<details>
```yaml
name: TimeUnitEnum
description: Allowed units for time intervals.
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
permissible_values:
  s:
    text: s
    description: Seconds (SI base unit)
  sec:
    text: sec
    description: Seconds (alternative spelling accepted by FOF-CT)
  ms:
    text: ms
    description: Milliseconds
  msec:
    text: msec
    description: Milliseconds (alternative spelling accepted by FOF-CT)
  min:
    text: min
    description: Minutes
  hr:
    text: hr
    description: Hours

```
</details>

</div>