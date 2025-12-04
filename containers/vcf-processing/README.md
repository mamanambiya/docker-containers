# VCF Processing Container

Alpine Linux-based container for VCF file processing in genotype imputation workflows.

## Tools Included

- **BCFtools v1.20** - Primary VCF manipulation tool
- **VCFtools v0.1.16** - VCF analysis and filtering
- **HTSlib v1.20** - High-throughput sequencing data handling (includes tabix)
- **Python 3.x** - Scripting support

## Used In

This container is used in the following workflow processes:
- `qc_dupl` - Duplicate site quality control
- `split_multi_allelic` - Split multi-allelic variants
- `fill_tags_vcf` - Add/update VCF tags
- `filter_min_ac` - Filter by minimum allele count
- `sites_only` - Extract sites-only VCF
- `combine_vcfs` - Merge multiple VCF files

## Usage

### Check installed tools

```bash
docker run --rm vcf-processing
```

### Run BCFtools

```bash
docker run --rm -v /path/to/data:/data vcf-processing bcftools view input.vcf.gz
```

### Run VCFtools

```bash
docker run --rm -v /path/to/data:/data vcf-processing vcftools --vcf input.vcf
```

### Run tabix

```bash
docker run --rm -v /path/to/data:/data vcf-processing tabix -p vcf input.vcf.gz
```

## Working Directories

- `/data` - Default working directory
- `/input` - For input files
- `/output` - For output files

## Version

v2.0 - Based on Alpine Linux 3.18
