# Phasing Container

Comprehensive Alpine Linux-based container for haplotype phasing combining Eagle with HTSlib tools.

## Tools Included

- **Eagle v2.4.1** - Fast haplotype phasing software
- **HTSlib v1.20** - High-throughput sequencing data handling (includes tabix)

## Used In

This container is used in the following workflow processes:
- `minimac4_phasing_eagle` - Phasing before Minimac4 imputation
- `impute5_phasing_eagle` - Phasing before IMPUTE5 imputation
- `phasing_vcf_no_ref_chunk` - Phasing without reference panel

## Purpose

This container provides everything needed for haplotype phasing workflows:
1. Phase genotypes using Eagle
2. Index VCF files with tabix
3. Validate and process phased VCF files

## Usage

### Check installed tools

```bash
docker run --rm phasing
```

### Phase with Eagle

```bash
docker run --rm -v /path/to/data:/data phasing \
  eagle \
  --vcf input.vcf.gz \
  --geneticMapFile genetic_map.txt \
  --outPrefix output \
  --numThreads 4
```

### Phase with reference panel

```bash
docker run --rm -v /path/to/data:/data phasing \
  eagle \
  --vcf target.vcf.gz \
  --vcfRef reference.vcf.gz \
  --geneticMapFile genetic_map.txt \
  --outPrefix output \
  --numThreads 4
```

### Index with tabix

```bash
docker run --rm -v /path/to/data:/data phasing \
  tabix -p vcf phased.vcf.gz
```

### Validate VCF with htsfile

```bash
docker run --rm -v /path/to/data:/data phasing \
  htsfile input.vcf.gz
```

## Eagle Key Options

### Required
- `--vcf` - Input VCF file with genotypes
- `--geneticMapFile` - Recombination rate map
- `--outPrefix` - Output file prefix

### Optional
- `--vcfRef` - Reference panel for improved phasing
- `--numThreads` - Number of CPU threads (default: 1)
- `--chrom` - Chromosome to phase
- `--bpStart` / `--bpEnd` - Genomic region boundaries
- `--maxMissingPerSnp` - Maximum missing rate per SNP
- `--maxMissingPerIndiv` - Maximum missing rate per individual

## Required Files

1. **Input VCF** - Target genotypes to be phased (can be unphased)
2. **Genetic Map** - Recombination rate map for the population
3. **Reference Panel** (optional) - Pre-phased haplotypes for improved accuracy

## Genetic Maps

Genetic map files are available from:
- Eagle downloads: https://alkesgroup.broadinstitute.org/Eagle/
- 1000 Genomes maps: https://bochet.gcc.biostat.washington.edu/beagle/genetic_maps/

Common maps:
- `genetic_map_hg19_withX.txt.gz` - Human GRCh37/hg19
- `genetic_map_hg38_withX.txt.gz` - Human GRCh38/hg38

## Output Files

- `.vcf.gz` - Phased genotypes in VCF format
- `.log` - Detailed phasing log with quality metrics

## Phasing Quality Metrics

Eagle reports:
- Phasing rate - Percentage of heterozygous genotypes phased
- Switch error rate - Estimated phasing accuracy
- Runtime statistics

## Working Directories

- `/data` - Default working directory
- `/input` - For input files
- `/output` - For output files

## Workflow Integration

Typical phasing workflow using this container:

1. **Pre-QC** (use `vcf-processing` container)
   - Filter low quality variants
   - Remove high missingness samples

2. **Phase** (this container)
   - Run Eagle with appropriate genetic map
   - Optionally use reference panel

3. **Post-QC** (use `vcf-processing` container)
   - Index phased VCF with tabix
   - Validate output

4. **Impute** (use `imputation` or `minimac4` container)
   - Use phased genotypes for imputation

## Performance Tips

1. Use multiple threads (`--numThreads`) for large datasets
2. Process chromosomes in parallel
3. Use reference panel when available for better accuracy
4. Ensure VCF files are compressed and indexed

## Comparison with `eagle-phasing` Container

| Feature | phasing | eagle-phasing |
|---------|---------|---------------|
| Eagle v2.4.1 | ✓ | ✓ |
| HTSlib/tabix | ✓ | ✗ |
| htsfile | ✓ | ✗ |
| Image Size | Slightly larger | Smaller |
| Use Case | Full phasing workflow | Eagle only |

## Version

v2.0 - Based on Alpine Linux 3.18
