# Cromwell Setup

## Overview

The notebooks in this directory are intended to provide examples setting up [Cromwell](https://cromwell.readthedocs.io/en/stable/) and running workflows with it. 

## Getting started

Start by running the [cromwell_examples.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/cromwell_setup/cromwell_examples.ipynb). This notebook is intended to demonstrate how you can use the Cromwell engine on Terra to execute and manage workflows. Setup instructions are provided, along with examples of commands to submit workflows, check a job's status, list jobs, and examine output. This notebook also includes an example of submitting to a locally running Cromwell server if you have one running.

To start a locally running Cromwell server, run the [cromwell_server_management.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/cromwell_setup/cromwell_server_management.ipynb) notebook. This notebook walks you through starting a server, monitoring its status, and examples for submitting and stopping.

This directory also contains a [cromwell_gvs_setup_inputs.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/cromwell_setup/cromwell_gvs_setup_inputs.ipynb) notebook demonstrating how to run the [GVS workflow](https://github.com/DataBiosphere/terra-axon-examples/tree/main/cromwell_setup/gvs_wdls) on your locally running Cromwell server. This notebook guides you through setting up your inputs, submitting the job, and monitoring it as it runs. 