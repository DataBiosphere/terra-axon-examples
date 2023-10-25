
# 1000 Genomes examples


## R Single Chromosome PCA Example: Reading variant data into an R sparse matrix

Adapted from:
http://bwlewis.github.io/1000_genomes_examples/PCA.html  \
https://github.com/bwlewis/1000_genomes_examples

This example walks through the computation of principal components (PCA) of genomic variant data across one chromosome from 2,504 people from the [1000 genomes project](https://www.internationalgenome.org/1000-genomes-summary/). The example projects all of the variant data for one chromosome into a three-dimensional subspace, and then plots the result.

The example uses:

- a very simple C parsing program to efficiently read variant data into an R sparse matrix,
- the `irlba` package to efficiently compute principal components,
- the `threejs` package to visualize the result.

This example is intended to be run in a Verily Workbench notebook cloud environment ('Jupyterlab Vertex AI Workbench instance'), using the R environment image.  You can take the defaults when creating the notebook environment, though some compute-heavy aspects of the analysis will run more quickly with additional cores.