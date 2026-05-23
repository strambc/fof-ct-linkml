RAEADME

FOF-bas-CT LinkML(YAML) 

Produced with Claude by Caterina Strambio De Castillia
5/22/2026

13/13 files pass YAML validation. 

Here's what was produced:
fof_bas_ct_common.yaml — the shared foundation imported by all 11 supporting schemas. 

It defines: 

- the Software class, all header slots that repeat across tables (fof_ct_version, lab_name, experimenter_name, experimenter_contact, description, additional_tables, softwares, the three unit slots, intensity_measurement_method), 
- all cross-table foreign-key slots (spot_id, trace_id, sub_cell_roi_id, cell_id, extra_cell_roi_id), and 
- the shared enums (XYZUnitEnum, TimeUnitEnum, SoftwareTypeEnum, TableNamespaceEnum). 

This is the key difference from the core schema — the core was written self-contained, while the 11 supporting tables all import from common to avoid duplication.

The 11 table schemas — one brief note on each design decision worth knowing:

- Tables 2–4 (demultiplexing, trace, rna): software is mandatory in demultiplexing and rna (data analysis always requires it), but conditional in trace (it may be derived manually). The RNA table adds genome_assembly, gene_id_type, and transcript_id_type as local header slots.

- Tables 5–8 (quality, rna_quality, bio, rna_bio): all four are pure open-ended tables — only the primary key column is fixed, everything else is user-defined. Modelled with additional_properties: true on the row class and software as conditional.
Tables 9–11 (cell, extracell, subcell): each introduces a domain-specific mandatory header field (cell_type, extra_cell_roi_type, sub_cell_roi_type) recommending use of EFO ontology terms.

- Table 12 (mapping): the most unusual — the primary key column is itself conditional (one of cell_id, sub_cell_roi_id, or extra_cell_roi_id per submission), and roi_boundaries_format is a new mandatory header slot describing which coordinate format is used.

One follow-up to consider: the fof_bas_ct_core.yaml currently re-defines enums and slots that are now also in fof_bas_ct_common.yaml. 

When you're ready, it would be worth refactoring core to import common as well, so all 12 table schemas share a single source of truth.