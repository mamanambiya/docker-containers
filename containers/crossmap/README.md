# CrossMap Container

Python-based container for genomic coordinate conversion between different genome assemblies.

## Tools Included

- **CrossMap v0.7.3** - Coordinate conversion tool for genomics
- **Python 3.11** - Runtime environment
- **pysam** - SAM/BAM file manipulation (installed as CrossMap dependency)
- **bx-python** - Python library for biological data analysis
- **pyBigWig** - BigWig file reading and writing

## Purpose

CrossMap is used to convert genomic coordinates and annotation files between different reference genome assemblies (e.g., hg19 to hg38, GRCh37 to GRCh38).

## Supported File Formats

- BAM/SAM - Sequence alignment files
- BED - Genomic intervals
- BigWig - Continuous-valued data
- GFF/GTF - Gene annotations
- VCF - Variant Call Format
- WIG - Wiggle format

## Usage

### Check CrossMap version

```bash
docker run --rm crossmap
```

### Convert BED file

```bash
docker run --rm -v /path/to/data:/data crossmap \
  CrossMap bed chain_file.chain input.bed output.bed
```

### Convert VCF file

```bash
docker run --rm -v /path/to/data:/data crossmap \
  CrossMap vcf chain_file.chain input.vcf reference.fa output.vcf
```

### Convert BAM file

```bash
docker run --rm -v /path/to/data:/data crossmap \
  CrossMap bam chain_file.chain input.bam output.bam
```

## Chain Files

CrossMap requires chain files that define the coordinate mapping between genome assemblies. These can be downloaded from:
- UCSC Genome Browser: http://hgdownload.cse.ucsc.edu/downloads.html
- Ensembl: https://www.ensembl.org/info/data/ftp/index.html

## Working Directory

- `/data` - Default working directory (mount your data here)

## Version

v0.7.3 - Based on Python 3.11 slim
