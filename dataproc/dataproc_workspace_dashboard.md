# Overview

This workspace shows how to start a [Dataproc](https://cloud.google.com/dataproc) (managed Spark) cluster, with Hail installed, on Verily Workbench, and how to submit batch jobs to the cluster as well as how to run an interactive notebook on the Hail cluster.

It uses an example that annotates significant GWAS results with gnomAD using [Hail](https://hail.is/).

The example specifically annotates GWAS results from the paper [*Whole genome sequence analysis of blood lipid levels in >66,000 individuals. Selvaraj et al 2021*](https://www.biorxiv.org/content/10.1101/2021.10.11.463514v1.supplementary-material). There are only 338 significant LDL results to annotate, so it might be faster to annotate using a tool other than Hail, but this workspace is meant to be illustrative and run on publicly available data.

# How do I get started?

## Step 0: Set up your github SSH key (optional) and _Duplicate_ this workspace

- (Optional) In the Verily Workbench UI, click on your profile icon, then click on "My Profile". Copy the public SSH key listed there.
  Then, [add that key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to your GitHub account. This is not necessary to run the Dataproc example notebooks, but will allow you to clone private repos from your workspace cloud environments.
  [This page](https://terra-docs.api.verily.com/docs/how_to_guides/terra_ssh_key_guide/) has more detail on the process.

- Then, *Duplicate* this workspace. You can do that via the 'three-dot' menu in the upper right of the workspace.


<!-- ## Step 1: Preview prior runs of the relevant notebooks.

On the 'Resources' page, navigate to the Enterprise Terra folder "Notebook snapshots" and preview the notebooks you see there in this order to get a deeper understanding of what setup and analysis this demonstration workspace enables:
1. `workspace_setup.ipynb`
2. `cloud_env_setup.ipynb`
3. `create_hail_cluster.ipynb`
4. `annotate_significant_gwas_results_with_gnomad_brief.ipynb`, which was run on a small region of the genome
5. `annotate_significant_gwas_results_with_gnomad_at_scale.ipynb`, which was run on all autosomes -->

## Step 1.1 (optional): Create an autoscaling policy

Create a Dataproc autoscaling policy for your workspace project, as described
[here](https://docs.google.com/document/d/1OVd--z7p-fW76QsMG0pihuTNA-XPriWDZe7rkcqmMsk/edit#heading=h.89g8dezaw1r4).


## Step 1.2: Create your own Dataproc + Hail cluster

Create a Dataproc cluster cloud environment in the Verily Workbench web UI,  **with
[Hail](https://hail.is/) installed**, as described
[here](https://docs.google.com/document/d/1OVd--z7p-fW76QsMG0pihuTNA-XPriWDZe7rkcqmMsk/edit).

If you like, configure the cluster to use the autoscaling policy that you created.

When the cluster is up and running, click on its link to open its on-node JupyterLab server.


## Step 2: Use the Hail cluster to run a brief interactive analysis.

From JupyterLab, navigate to the `repos/terra-axon-examples/dataproc` subdirectory.
Click to open the [`annotate_significant_gwas_results_with_gnomad.ipynb`](./annotate_significant_gwas_results_with_gnomad.ipynb) notebook.

> **If you do not see the `terra-axon-examples` subdirectory**, first open a Terminal window on the notebook server (under the **File** menu) and run:

  ```sh
  cd ~/repos
  git clone https://github.com/DataBiosphere/terra-axon-examples.git
  ```

## Step 3: Submit a batch job

In JupyterLab, navigate to the `repos/terra-axon-examples/dataproc` subdirectory.
Run the [`batch_job_submit.ipynb`](./batch_job_submit.ipynb) notebook.  It will walk you through the process of creating a batch script and submitting it to the cluster.

You can run this notebook from the on-cluster JupyterLab server, or from a VWB notebook cloud environment. (You can also run it from your local machine).


## Step 4: Use the Hail cluster to run the analysis at scale!

With notebook `annotate_significant_gwas_results_with_gnomad.ipynb`, you can also control how much data it uses as input, so that it either completes briefly (e.g. 5 minutes) or runs longer (e.g. 30 minutes). Edit variable `INTERVALS_TO_EXAMINE` to have value `['chr1-chr22']` in either the script or notebook version of the analysis so that you can observe autoscaling and cluster metrics as it runs.
