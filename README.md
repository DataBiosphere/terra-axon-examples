# terra-axon-examples

## Overview

This repository contains example notebooks and documentation for working with [Enterprise Terra](https://verily.com/solutions/terra/).

[Enterprise Terra](https://verily.com/solutions/terra/) is a new platform developed by Verily to connect the multimodal data ecosystem and meet the needs of commercial or industry-led research organizations. Building on Terra’s academic roots, Enterprise Terra is an integrated platform that provides a secure foundation to discover, govern, and unify multimodal data in a collaborative environment to accelerate discoveries.

- Explore: discover multimodal data sets available in Enterprise Terra’s data ecosystem.
- Unify: connect all data types, from both internal and external sources, into a single platform under one governance framework.
- Analyze: unlock insights faster with familiar analysis tools.
- Collaborate: share best practices and publish reproducible research.
- Scale: maximize the power of any cloud with security, compliance, and support from industry standards.


## Getting started

### Setup Github integration in Enterprise Terra

Go to [Enterprise Terra](https://verily.com/solutions/terra/) and:
1. Add your SSH key to GitHub. 
2. Create a personal workspace where you can test out many examples, such as this one. Name it something like *"Personal workspace {your email address} {YYYYMMDD}"*.
3. [Optional] If you want Terra to clone this repo automatically, add it as a reference in your workspace. Otherwise you will need to clone it manually, which is pretty easy.
4. Create a Cloud Environment for yourself. Name it something like *"{your email address}-{YYYYMMDD}"*.
5. Be sure to run notebook [workspace_setup.ipynb](https://github.com/DataBiosphere/terra-axon-examples/blob/main/workspace_setup.ipynb) first before running any other notebook files. It sets up some buckets and a BigQuery dataset that all the other notebooks refer to by reference and expect to exist.
