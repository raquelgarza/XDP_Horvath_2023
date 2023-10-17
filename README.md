# The KRAB zinc finger protein ZNF91 protects the human genome from the regulatory impact of SVA transposons in human brain development and disease
author: Raquel Garza

date: 2023-10-11

This repository presents analyses for the manuscript
[The KRAB zinc finger protein ZNF91 protects the human genome from the regulatory impact of SVA transposons in human brain development and disease]().

## File tree
- `src` - Directory containing all pipelines and scripts.
- `src/config_files` - Json files required to run Snakefiles.
- `src/r_scripts` - Directory containing helper functions and R markdowns for downstream analyses and visualization for the figures.
- `tables/` - Directory containing tables with differential gene expression analysis and TLDR output.

## Preprocessing pipelines 
- `src` - Directory containing all pipelines and scripts
- [**provider.pl**](./src/provider.pl) - Perl script for SNP analysis
- [**Snakefile_RNAseq**](./src/Snakefile_RNAseq) - Snakemake for preprocessing of bulk RNAseq data.
- [**Snakefile_cutnrun**](./src/Snakefile_cutnrun) - Snakemake for preprocessing of CUT&RUN data.
- [**Snakefile_op_043_hg38**](./src/Snakefile_op_043_hg38) - Snakemake for preprocessing ONT whole genome data and identification of de novo TE insertions.
- [**Snakefile_op_069_hg38**](./src/Snakefile_op_069_hg38) - Same Snakemake as `Snakefile_op_043_hg38` for the preprocessing of ONT WG, but without TLDR step (redundant).
- [**add_polymorphic_insertions_fa.py**](./src/add_polymorphic_insertions_fa.py) - Python script to add sequences of the identified de novo TE insertions to the reference genome. Inputs a tabulated file of chr, start, end, and sequence for each de novo TE insertion, a text file with the list of chromosomes (one per line), and a fasta file per chromosome. The output files of this script were concatenated and used to generate a minimap2 index of the genome (`minimap2 -x map-ont -d denovoTE_hg38.mmi denovoTE_hg38.fa`)
- [**add_polymorphic_insertions.py**](./src/add_polymorphic_insertions.py) - Python script to update coordinates of features in a gtf file with the identified de novo TE insertions. 
- [**Snakefile_op_043_069_poly**](./src/Snakefile_op_043_069_poly) - Snakemake for mapping ONT WG data to the custom genome with the identified de novo TE insertions added to it.
- [**Snakefile_targeted_ont**](./src/Snakefile_targeted_ont) - Snakemake for preprocessing of targeted ONT, mapping and calling methylation status over TAF1.
- [**Snakefile_upreg_genes_nearby_SVAs**](./src/Snakefile_upreg_genes_nearby_SVAs) - Snakemake for calling methylation status over a list of regions using reference hg38 genome.
- [**Snakefile_upreg_genes_nearby_SVAs_poly**](./src/Snakefile_upreg_genes_nearby_SVAs_poly) - Snakemake for calling methylation status over a list of regions using the custom genome (with the de novo TE insertions added to it).

## Statistical and visualization scripts
- `src/r_scripts` - Directory containing R markdowns for downstream analyses and visualization for the figures.
	+ [**SNP_analysis.Rmd**](./src/r_scripts/SNP_analysis.Rmd) - R markdown for the visualization of the SNP analysis.
	+ [**all_experiments_pcas_kds_taf1_clean.Rmd**](./src/r_scripts/all_experiments_pcas_kds_taf1_clean.Rmd) - Gene DEA.
	+ [**TE_DEA_all_experiments.Rmd**](./src/r_scripts/TE_DEA_all_experiments.Rmd) - TE DEA.
	+ [**common_SVAs_iPSC_iPSCNES.Rmd**](./src/r_scripts/common_SVAs_iPSC_iPSCNES.Rmd) - Upregulated SVAs common between ipsc and ipsc --> nes. 

