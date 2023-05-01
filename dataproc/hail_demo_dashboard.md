# Overview

This workspace shows how to start a [Dataproc](https://cloud.google.com/dataproc) (managed Spark) cluster, with Hail installed, on Enterprise Terra, and how to submit batch jobs to the cluster as well as how to run an interactive notebook on the Hail cluster.

It uses an example that annotates significant GWAS results with gnomAD using [Hail](https://hail.is/).

The example specifically annotates GWAS results from the paper [*Whole genome sequence analysis of blood lipid levels in >66,000 individuals. Selvaraj et al 2021*](https://www.biorxiv.org/content/10.1101/2021.10.11.463514v1.supplementary-material). There are only 338 significant LDL results to annotate, so it might be faster to annotate using a tool other than Hail, but this workspace is meant to be illustrative and run on publicly available data.

# How do I get started?

## Step 0: Set up your github SSH key and _Duplicate_ this workspace

- In the Enterprise Terra UI, click on your profile icon, then click on "My Profile". Copy the public SSH key listed there.
  Then, [add that key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to your GitHub account.
  [This page](https://terra-docs.api.verily.com/docs/how_to_guides/terra_ssh_key_guide/) has more detail.

  This setup allows the `terra-axon-examples` example repo, which you can see listed as a Git repository for the workflow, to be automatically cloned when you create a Cloud Environment.
  > **Note**: if you do not have a GitHub account, then you can clone the repo manually after you've created the Cloud Environment.

- Then, *Duplicate* this workspace. You can do that via the 'three-dot' menu in the upper right of the workspace.



## Step 1: Preview prior runs of the relevant notebooks.

On the 'Resources' page, navigate to the Enterprise Terra folder "Notebook snapshots" and preview the notebooks you see there in this order to get a deeper understanding of what setup and analysis this demonstration workspace enables:
1. `workspace_setup.ipynb`
2. `cloud_env_setup.ipynb`
3. `create_hail_cluster.ipynb`
4. `annotate_significant_gwas_results_with_gnomad_brief.ipynb`, which was run on a small region of the genome
5. `annotate_significant_gwas_results_with_gnomad_at_scale.ipynb`, which was run on all autosomes


## Step 2: Create an Enterprise Terra Cloud Environment and run setup notebooks.

Create an Enterprise Terra Cloud environment, by navigating to the "Environments" tab of the workspace. You can use the configuration defaults.

Launch the environment once it's running, and then run the notebooks [workspace_setup.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/workspace_setup.ipynb) and [cloud_env_setup.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/cloud_env_setup.ipynb). You only need to run `workspace_setup.ipynb` once per workspace (it's fine to run it multiple times).  Run `cloud_env_setup.ipynb` for each cloud environment.

The example repo, `terra-axon-examples`, which is defined as a workspace Git repository, should be automatically cloned to your Enterprise Terra Cloud Environments, and you should be able to navigate to the notebook in the JupyterLab file browser. Look for the `terra-axon-examples` subdirectory.

> **If you have not set up your ssh key, and do not see the `terra-axon-examples` subdirectory**, first open a Terminal window on the notebook server (under the **File** menu) and run:

  ```sh
  git clone https://github.com/DataBiosphere/terra-axon-examples.git
  ```

## Step 3: Create your own Hail cluster.

Run the notebook `create_hail_cluster.ipynb` to create your Hail cluster. You will find this notebook in [https://github.com/DataBiosphere/terra-axon-examples/tree/main/dataproc](https://github.com/https://github.com/DataBiosphere/terra-axon-examples/tree/main/dataproc).  As mentioned above, its repo, `terra-axon-examples`, will be automatically cloned to your Enterprise Terra Cloud Environment, and you should be able to navigate to the notebook in the JupyterLab file browser.

## Step 4: Use the Hail cluster to run a brief analysis.

Notebook `create_hail_cluster.ipynb` provides instructions on how to run `annotate_significant_gwas_results_with_gnomad.ipynb`, which resides in the same directory, as either a batch script or as an interactive Jupyter notebook on the Hail cluster.

## Step 5: Use the Hail cluster to run the analysis at scale!

With notebook `annotate_significant_gwas_results_with_gnomad.ipynb`, you can also control how much data it uses as input so that it either completes briefly (e.g. 5 minutes) or runs longer (e.g. 30 minutes). Edit variable `INTERVALS_TO_EXAMINE` to have value `['chr1-chr22']` in either the script or notebook version of the analysis so that you can observe autoscaling and cluster metrics as it runs.
