# Dataproc + Hail on Verily Workbench

This directory contains examples of using the Dataproc cloud environment in [Verily Workbench (VWB)](https://workbench.verily.com/).

To run these notebooks, first create a Dataproc cluster environment in the VWB web UI,  **with
[Hail](https://hail.is/) installed**, as described
[here](https://docs.google.com/document/d/1OVd--z7p-fW76QsMG0pihuTNA-XPriWDZe7rkcqmMsk/edit#heading=h.gaxudskpflrb).
<!-- TODO: move from gdoc when ready -->

Once the cluster is up and running, click its link to bring up the JupyterLab server running on the
cluster’s “main” node.

If you’re running the examples via a VWB workspace that has [added this repo as a GitHub resource](https://support.workbench.verily.com/docs/how_to_guides/add_repo_to_ws/), then on the JupyterLab server, you can find the example notebook files under the `/home/dataproc/repos/terra-axon-examples/dataproc` directory.
Otherwise, you can directly clone the repo in the notebook server yourself (e.g., from the Terminal window), via:
```sh
git clone https://github.com/DataBiosphere/terra-axon-examples.git
```
You can also upload the notebook files directly to the JupyterLab server.

The [annotate_significant_gwas_results_with_gnomad.ipynb](./annotate_significant_gwas_results_with_gnomad.ipynb) notebook uses [Hail](https://hail.is/) to annotate the significant GWAS results with [gnomAD](https://gnomad.broadinstitute.org/).
This notebook is intended to be run from the on-cluster JupyterLab server, and requires that Hail is installed on cluster creation.

The [batch_job_submit.ipynb](./batch_job_submit.ipynb) notebook shows an example of submitting a batch job to the Dataproc cluster.  It uses the  [annotate_significant_gwas_results_with_gnomad.ipynb](./annotate_significant_gwas_results_with_gnomad.ipynb) notebook file as a basis for its example batch script, but other scripts can be submitted in the same manner.
This notebook requires a running Dataproc cluster, but can itself be run from either the on-cluster JupyerLab server, or from a  [notebook cloud environment](https://support.workbench.verily.com/docs/how_to_guides/using_cloud_environments/).