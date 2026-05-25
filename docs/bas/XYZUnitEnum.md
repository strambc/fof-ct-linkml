---
search:
  boost: 2.0
---


# Enum: XYZUnitEnum 




_Allowed units for X, Y, Z spatial coordinates or distances._



<div data-search-exclude markdown="1">

URI: [fof_ct:XYZUnitEnum](https://w3id.org/fof-ct/XYZUnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| nm | None | Nanometres |
| micron | None | Micrometres |
| mm | None | Millimetres |




## Slots

| Name | Description |
| ---  | --- |
| [xyz_unit](xyz_unit.md) | Unit used to represent X, Y, Z spatial coordinates or distances in this table |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas






## LinkML Source

<details>
```yaml
name: XYZUnitEnum
description: Allowed units for X, Y, Z spatial coordinates or distances.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
permissible_values:
  nm:
    text: nm
    description: Nanometres
  micron:
    text: micron
    description: Micrometres. Use 'micron' rather than the Greek symbol μm to avoid
      encoding issues.
  mm:
    text: mm
    description: Millimetres

```
</details>

</div>