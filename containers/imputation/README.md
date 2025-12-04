# Imputation Container

Comprehensive Alpine Linux-based container for genotype imputation workflows combining Minimac4 with VCF processing tools.

## Tools Included

- **Minimac4 v4.1.6** - Primary genotype imputation engine
- **BCFtools v1.20** - VCF pre/post-processing
- **VCFtools v0.1.16** - VCF analysis and filtering
- **HTSlib v1.20** - High-throughput sequencing data handling (includes tabix)

## Used In

This container is used in the following workflow processes:
- `impute_minimac4` - Main imputation process
- `impute_minimac4_1` - Single chromosome imputation
- `combineImpute` - Combine imputation results

## Purpose

This all-in-one container provides everything needed for genotype imputation:
1. Pre-processing VCF files before imputation
2. Running Minimac4 imputation
3. Post-processing and filtering imputation results

## Usage

### Check installed tools

```bash
docker run --rm imputation
```

### Run Minimac4 imputation

```bash
docker run --rm -v /path/to/data:/data imputation \
  minimac4 \
  --refHaps reference.m3vcf.gz \
  --haps target.vcf.gz \
  --prefix output \
  --format GT,DS,GP
```

### Pre-process with BCFtools

```bash
docker run --rm -v /path/to/data:/data imputation \
  bcftools view -Oz -o output.vcf.gz input.vcf
```

### Filter with VCFtools

```bash
docker run --rm -v /path/to/data:/data imputation \
  vcftools --gzvcf input.vcf.gz --max-missing 0.1 --recode --out filtered
```

## Minimac4 Key Options

- `--refHaps` - Reference panel in M3VCF format
- `--haps` - Target genotypes to impute (phased VCF)
- `--prefix` - Output file prefix
- `--format` - Output format (GT=genotypes, DS=dosages, GP=probabilities)
- `--cpus` - Number of threads to use
- `--chr` - Chromosome to impute
- `--start` / `--end` - Genomic region to impute

## Reference Panels

Minimac4 requires reference panels in M3VCF format:
- TOPMed: https://imputationserver.sph.umich.edu/
- 1000 Genomes: https://www.internationalgenome.org/
- HRC: http://www.haplotype-reference-consortium.org/

Reference panels must be converted to M3VCF format using Minimac3 or Minimac4.

## Working Directories

- `/data` - Default working directory
- `/input` - For input files
- `/output` - For output files

## Workflow Integration

Typical imputation workflow using this container:
1. Phase genotypes (use `phasing` or `eagle-phasing` container)
2. Run imputation with Minimac4
3. Filter results by imputation quality (R² or INFO score)
4. Combine chromosome results

## Version

v2.0 - Based on Alpine Linux 3.18
