---
search:
  boost: 2.0
---


# Enum: TableNamespaceEnum 




_Allowed namespace identifiers for FOF-CT tables that may be listed in the additional_tables field. Note: per the FOF-CT RTD, the three FOF-vol-CT-exclusive namespaces (vol_core, vol_quality, undecoded) intentionally omit the 4dn_ prefix used by the 12 shared tables, to reflect the format's continued stewardship by the broader community beyond 4DN._



<div data-search-exclude markdown="1">

URI: [fof_ct:TableNamespaceEnum](https://w3id.org/fof-ct/TableNamespaceEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| 4dn_FOF-CT_core | None | DNA-Spot/Trace Data core table (table 1) |
| 4dn_FOF-CT_demultiplexing | None | Spot Demultiplexing table (table 2) |
| 4dn_FOF-CT_trace | None | Trace Data table (table 3) |
| 4dn_FOF-CT_rna | None | RNA Spot Data table (table 4) |
| 4dn_FOF-CT_quality | None | Spot Quality table (table 5) |
| 4dn_FOF-CT_rna_quality | None | RNA Spot Quality table (table 6) |
| 4dn_FOF-CT_bio | None | Spot Biological Data table (table 7) |
| 4dn_FOF-CT_rna_bio | None | RNA Spot Biological Data table (table 8) |
| 4dn_FOF-CT_cell | None | Cell Data table (table 9) |
| 4dn_FOF-CT_extracell | None | Extra-Cell ROI Data table (table 10) |
| 4dn_FOF-CT_subcell | None | Sub-Cell ROI Data table (table 11) |
| 4dn_FOF-CT_mapping | None | Cell/ROI Mapping table (table 12) |
| FOF-CT_vol_core | None | SM Localization Data table — FOF-vol-CT (table 13) |
| FOF-CT_vol_quality | None | SM Localization Quality table — FOF-vol-CT (table 14) |
| FOF-CT_undecoded | None | Undecoded SM Localization Data table — FOF-vol-CT (table 15) |




## Slots

| Name | Description |
| ---  | --- |
| [additional_tables](additional_tables.md) | List of additional FOF-CT table namespaces being submitted alongside this tab... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fof-ct/bas






## LinkML Source

<details>
```yaml
name: TableNamespaceEnum
description: 'Allowed namespace identifiers for FOF-CT tables that may be listed in
  the additional_tables field. Note: per the FOF-CT RTD, the three FOF-vol-CT-exclusive
  namespaces (vol_core, vol_quality, undecoded) intentionally omit the 4dn_ prefix
  used by the 12 shared tables, to reflect the format''s continued stewardship by
  the broader community beyond 4DN.'
from_schema: https://w3id.org/fof-ct/bas
rank: 1000
permissible_values:
  4dn_FOF-CT_core:
    text: 4dn_FOF-CT_core
    description: DNA-Spot/Trace Data core table (table 1)
  4dn_FOF-CT_demultiplexing:
    text: 4dn_FOF-CT_demultiplexing
    description: Spot Demultiplexing table (table 2)
  4dn_FOF-CT_trace:
    text: 4dn_FOF-CT_trace
    description: Trace Data table (table 3)
  4dn_FOF-CT_rna:
    text: 4dn_FOF-CT_rna
    description: RNA Spot Data table (table 4)
  4dn_FOF-CT_quality:
    text: 4dn_FOF-CT_quality
    description: Spot Quality table (table 5)
  4dn_FOF-CT_rna_quality:
    text: 4dn_FOF-CT_rna_quality
    description: RNA Spot Quality table (table 6)
  4dn_FOF-CT_bio:
    text: 4dn_FOF-CT_bio
    description: Spot Biological Data table (table 7)
  4dn_FOF-CT_rna_bio:
    text: 4dn_FOF-CT_rna_bio
    description: RNA Spot Biological Data table (table 8)
  4dn_FOF-CT_cell:
    text: 4dn_FOF-CT_cell
    description: Cell Data table (table 9)
  4dn_FOF-CT_extracell:
    text: 4dn_FOF-CT_extracell
    description: Extra-Cell ROI Data table (table 10)
  4dn_FOF-CT_subcell:
    text: 4dn_FOF-CT_subcell
    description: Sub-Cell ROI Data table (table 11)
  4dn_FOF-CT_mapping:
    text: 4dn_FOF-CT_mapping
    description: Cell/ROI Mapping table (table 12)
  FOF-CT_vol_core:
    text: FOF-CT_vol_core
    description: SM Localization Data table — FOF-vol-CT (table 13). No 4dn_ prefix
      (see enum-level note).
  FOF-CT_vol_quality:
    text: FOF-CT_vol_quality
    description: SM Localization Quality table — FOF-vol-CT (table 14). No 4dn_ prefix
      (see enum-level note).
  FOF-CT_undecoded:
    text: FOF-CT_undecoded
    description: Undecoded SM Localization Data table — FOF-vol-CT (table 15). No
      4dn_ prefix (see enum-level note).

```
</details>

</div>