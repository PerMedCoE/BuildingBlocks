# COVID-19 Pilot Workflow Assets

This folder contains the assets for the COVID-19 Building Blocks.

## Assets

There are five folders, one for each building block required.

```bash
.
├── MaBoSS
├── personalize_patient
├── PhysiBoSS
├── single_cell
└── meta_analysis
```

Each folder contains the code that is executed within the given singularity
container.

## Scripts

In addition, there is a set o scripts to ease the Building Blocks testing:

```bash
.
├── 1_run_maboss_bb.sh
├── 2_run_single_cell_bb.sh
├── 3_run_personalize_patient_bb.sh
├── 4_run_physiboss_bb.sh
└── 5_meta_analysis.sh
```

These scripts can be executed one after the other.

**WARNING:** Please, update the ``PERMEDCOE_IMAGES`` and ``PERMEDCOE_ASSETS``
environment variables exported within each script to the appropriate
singularity container folder and assets folder accordingly.

Finally, there is a ``clean.sh`` script aimed at cleaning the results of the
building blocks execution.
