# Overview

This workspace shows how to start a [Dataproc](https://cloud.google.com/dataproc) (managed Spark) cluster, with Hail installed, on Enterprise Terra, and how to submit batch jobs to the cluster as well as how to run an interactive notebook on the Hail cluster.

It uses an example that annotates significant GWAS results with gnomAD using [Hail](https://hail.is/).

The example specifically annotates GWAS results from the paper [*Whole genome sequence analysis of blood lipid levels in >66,000 individuals. Selvaraj et al 2021*](https://www.biorxiv.org/content/10.1101/2021.10.11.463514v1.supplementary-material). There are only 338 significant LDL results to annotate, so it might be faster to annotate using a tool other than Hail, but this workspace is meant to be illustrative and run on publicly available data.

# How do I get started?

*Duplicate* this workspace. You can do that via the 'three-dot' menu in the upper right of the workspace.


## Step 1: Preview prior runs of the relevant notebooks.

On the 'Resources' page, navigate to the Enterprise Terra folder "Notebook snapshots" and preview the notebooks you see there in this order to get a deeper understanding of what setup and analysis this demonstration workspace enables:
1. `workspace_setup.ipynb` (This notebook was run as part of the "Hail Demo" workspace creation, and you do not need to run it again in your duplicated workspace).
2. `create_hail_cluster.ipynb`
3. `annotate_significant_gwas_results_with_gnomad_brief.ipynb`, which was run on a small region of the genome
4. `annotate_significant_gwas_results_with_gnomad_at_scale.ipynb`, which was run on all autosomes


## Step 2: Create your own Hail cluster.

Create an Enterprise Terra Cloud environment, by navigating to the "Environments" tab of the workspace. You can use the configuration defaults.

Launch the environment once it's running, and then run the notebook `create_hail_cluster.ipynb` to create your Hail cluster. You will find this notebook in [https://github.com/DataBiosphere/terra-axon-examples/tree/main/dataproc](https://github.com/https://github.com/DataBiosphere/terra-axon-examples/tree/main/dataproc).  This repo, which is defined as a workspace Git repository, will be automatically cloned to your Enterprise Terra Cloud Environment, and you should be able to navigate to the notebook in the JupyterLab file browser.

## Step 3: Use the Hail cluster to run a brief analysis.

Notebook `create_hail_cluster.ipynb` provides instructions on how to run `annotate_significant_gwas_results_with_gnomad.ipynb`, which resides in the same directory, as either a batch script or as an interactive Jupyter notebook on the Hail cluster.

## Step 4: Use the Hail cluster to run the analysis at scale!

With notebook `annotate_significant_gwas_results_with_gnomad.ipynb`, you can also control how much data it uses as input so that it either completes briefly (e.g. 5 minutes) or runs longer (e.g. 30 minutes). Edit variable `INTERVALS_TO_EXAMINE` to have value `['chr1-chr22']` in either the script or notebook version of the analysis so that you can observe autoscaling and cluster metrics as it runs.
