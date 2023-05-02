# Overview

This notebook shows how to get started with [Nextflow](https://www.nextflow.io) on Enterprise Terra.

# How do I get started?

## Step 0: _Duplicate_ this workspace

- *Duplicate* this workspace. You can do that via the 'three-dot' menu in the upper right of the workspace. Duplicating this workspace ensures three Git repositories required for these examples will be automatically cloned when you create a Cloud Environment.

   The required repositories which will be cloned include:
  1. (`terra-axon-examples` example repo)[https://github.com/DataBiosphere/terra-axon-examples]: Contains JupyterLab notebook `nextflow_examples.ipynb` which demonstrates how to configure and run Nextflow workflows in Enterprise Terra.
  2. (`rnaseq-nf` repo)[https://github.com/nextflow-io/rnaseq-nf]: Contains a Nextflow RNASeq workflow specification and associated human genomic input data.
  3. (`test-datasets` repo)[https://github.com/nf-core/test-datasets]: For each workflow in the `nf-core` collection, this repo has a branch with appropriate, workflow-specific test data.
  > **Note**: If you do not have a GitHub account, then you can clone each repo manually after you've created the Cloud Environment.


## Step 1: Preview prior runs of the relevant notebooks.

Previews of this notebook, including outputs, are provided in the "Notebook snapshots" folder found by navigating to this workspace's Resources tab. Click the links listed below to view notebook previews in order to gain a better understanding of the setup and analysis included in this demonstration workspace:

1. [Workspace setup](https://terra-preprod-ui-terra.api.verily.com/workspaces/getting-started-with-workflows-workspace/resources/97ce452a-dd3c-4045-97d3-bc70db429f83/notebook_snapshots/workspace_setup.html)
2. [Example 1: Run a Nextflow workflow](https://terra-preprod-ui-terra.api.verily.com/workspaces/getting-started-with-workflows-workspace/resources/21ffa484-75b9-46ff-b70d-6ebeb2962eb2/notebook_snapshots/nextflow_examples_first_exercise_fully_executed.html)
3. [Example 2: Run an `nf-core` workflow](https://terra-preprod-ui-terra.api.verily.com/workspaces/getting-started-with-workflows-workspace/resources/eebc2df6-fc9d-491e-874c-b87dbd3a68e1/notebook_snapshots/nextflow_examples_second_exercise_fully_executed.html)


## Step 2: Create an Enterprise Terra Cloud Environment and run a setup notebook.

Create an Enterprise Terra Cloud environment, by navigating to the "Environments" tab of the workspace. You can use the configuration defaults.

Launch the environment once it's running, and then run the notebook [workspace_setup.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/workspace_setup.ipynb). Its repo, `terra-axon-examples`, which is defined as a workspace Git repository, should be automatically cloned to your Enterprise Terra Cloud Environments, and you should be able to navigate to the notebook in the JupyterLab file browser. Look for the `terra-axon-examples` subdirectory.

> **If you have not set up your ssh key, and do not see the `terra-axon-examples` subdirectory**, first open a Terminal window on the notebook server (under the **File** menu) and run:

  ```sh
  git clone https://github.com/DataBiosphere/terra-axon-examples.git
  ```

## Step 3: Run the Nextflow examples.

Two examples are provided in `nextflow_examples.ipynb`. You will find this notebook in [https://github.com/DataBiosphere/terra-axon-examples/tree/main/nextflow](https://github.com/https://github.com/DataBiosphere/terra-axon-examples/tree/main/nextflow).  As mentioned above, its repo, `terra-axon-examples`, will be automatically cloned to your Enterprise Terra Cloud Environment, and you should be able to navigate to the notebook in the JupyterLab file browser. Before running either example, you'll need to run the Setup section.

- The first example demonstrates running a Nextflow RNASeq workflow on human gut data.
- The second example demonstrates running the (`nf-core`)[https://nf-co.re/]RNASeq pipeline on yeast genome data.

The examples provided are independent of one another (meaning you can run only the second example if desired, without having to execute the first example).

## Step 4: View MultiQC reports produced.

Running either or both examples will result in the creation of a MultiQC report. To preview what reports can be expected to look like, navigate to the workspace resource folder "Report previews" and click to view:
1. [Example 1 MultiQC report preview](https://terra-preprod-ui-terra.api.verily.com/workspaces/getting-started-with-workflows-workspace/resources/6cce61b8-4dff-4342-934b-243134d91cac/example_results/multiqc_report.html)
2. [Example 2 MultiQC report preview](https://terra-preprod-ui-terra.api.verily.com/workspaces/getting-started-with-workflows-workspace/resources/27737b7b-4285-4c11-8848-e8ec3ae8f6d0/example_results/nf_core_multiqc_report.html)
Please note that a warning about Javascript being disabled is expected; instructions in the notebook are provided to address this for the actual reports you produce.