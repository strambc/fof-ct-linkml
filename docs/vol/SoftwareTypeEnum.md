---
search:
  boost: 2.0
---


# Enum: SoftwareTypeEnum 




_Allowed functional categories for software tools (per the FOF-CT RTD "Allowable value lists" table for Software_Type)._



<div data-search-exclude markdown="1">

URI: [fof_ct:SoftwareTypeEnum](https://w3id.org/fof-ct/SoftwareTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Distance Calculation | None | Distance calculation software |
| DriftCorrection | None | Drift correction software |
| Precision Assessment | None | Localization/tracing precision assessment software |
| Segmentation | None | Image segmentation software |
| Single Molecule Localization | None | Single-molecule localization software (FOF-vol-CT) |
| SpotLoc | None | Spot localisation software |
| SpotLoc+Tracing | None | Combined spot localisation and tracing software |
| Tracing | None | Chromatin tracing software |
| Other | None | Other software type |




## Slots

| Name | Description |
| ---  | --- |
| [software_type](software_type.md) | Functional category of the software tool |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/vol






## LinkML Source

<details>
```yaml
name: SoftwareTypeEnum
description: Allowed functional categories for software tools (per the FOF-CT RTD
  "Allowable value lists" table for Software_Type).
from_schema: https://w3id.org/fof-ct/vol
rank: 1000
permissible_values:
  Distance Calculation:
    text: Distance Calculation
    description: Distance calculation software
  DriftCorrection:
    text: DriftCorrection
    description: Drift correction software
  Precision Assessment:
    text: Precision Assessment
    description: Localization/tracing precision assessment software
  Segmentation:
    text: Segmentation
    description: Image segmentation software
  Single Molecule Localization:
    text: Single Molecule Localization
    description: Single-molecule localization software (FOF-vol-CT)
  SpotLoc:
    text: SpotLoc
    description: Spot localisation software
  SpotLoc+Tracing:
    text: SpotLoc+Tracing
    description: Combined spot localisation and tracing software
  Tracing:
    text: Tracing
    description: Chromatin tracing software
  Other:
    text: Other
    description: Other software type

```
</details>

</div>