---
search:
  boost: 2.0
---


# Enum: SoftwareTypeEnum 




_Allowed functional categories for software tools._



<div data-search-exclude markdown="1">

URI: [fof_ct:SoftwareTypeEnum](https://w3id.org/fof-ct/SoftwareTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SpotLoc | None | Spot localisation software |
| Tracing | None | Chromatin tracing software |
| SpotLoc+Tracing | None | Combined spot localisation and tracing software |
| Segmentation | None | Image segmentation software |
| QC | None | Quality control software |
| Distance | None | Distance calculation software |
| Other | None | Other software type |




## Slots

| Name | Description |
| ---  | --- |
| [software_type](software_type.md) | Functional category of the software tool |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas






## LinkML Source

<details>
```yaml
name: SoftwareTypeEnum
description: Allowed functional categories for software tools.
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
permissible_values:
  SpotLoc:
    text: SpotLoc
    description: Spot localisation software
  Tracing:
    text: Tracing
    description: Chromatin tracing software
  SpotLoc+Tracing:
    text: SpotLoc+Tracing
    description: Combined spot localisation and tracing software
  Segmentation:
    text: Segmentation
    description: Image segmentation software
  QC:
    text: QC
    description: Quality control software
  Distance:
    text: Distance
    description: Distance calculation software
  Other:
    text: Other
    description: Other software type

```
</details>

</div>