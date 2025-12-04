# Minimac4 Container

Lightweight Alpine Linux-based container with Minimac4 genotype imputation software only.

## Tools Included

- **Minimac4 v4.1.6** - Genotype imputation software

## Purpose

This is a minimal container containing only Minimac4 for users who need just the imputation tool without additional VCF processing utilities. For a full-featured imputation container that includes BCFtools and VCFtools, see the `imputation` container.

## Usage

### Check Minimac4 version

```bash
docker run --rm minimac4
```

### Run imputation

```bash
docker run --rm -v /path/to/data:/data minimac4 \
  minimac4 \
  --refHaps reference.m3vcf.gz \
  --haps target.vcf.gz \
  --prefix output \
  --format GT,DS,GP
```

### Run with multiple CPUs

```bash
docker run --rm -v /path/to/data:/data minimac4 \
  minimac4 \
  --refHaps reference.m3vcf.gz \
  --haps target.vcf.gz \
  --prefix output \
  --cpus 8
```

### Impute specific region

```bash
docker run --rm -v /path/to/data:/data minimac4 \
  minimac4 \
  --refHaps reference.m3vcf.gz \
  --haps target.vcf.gz \
  --prefix output \
  --chr 22 \
  --start 20000000 \
  --end 21000000
```

## Key Parameters

### Required
- `--refHaps` - Reference panel in M3VCF format
- `--haps` - Target genotypes to impute (phased VCF)
- `--prefix` - Output file prefix

### Optional
- `--format` - Output format: GT (genotypes), DS (dosages), GP (probabilities)
- `--cpus` - Number of threads (default: 1)
- `--chr` - Chromosome to impute
- `--start` / `--end` - Genomic region boundaries
- `--window` - Buffer size around region (default: 500000)
- `--minRatio` - Minimum imputation quality ratio (default: 0.00001)

## Input Requirements

1. **Reference Panel**: M3VCF format (`.m3vcf.gz`)
   - Pre-processed reference haplotypes
   - Can be created using Minimac3 or Minimac4

2. **Target Genotypes**: Phased VCF (`.vcf.gz`)
   - Must be phased (use Eagle or SHAPEIT first)
   - Should be quality-controlled
   - Must be indexed with tabix if using regions

## Output Files

- `.dose.vcf.gz` - Imputed genotypes in VCF format
- `.info` - Imputation quality metrics per variant
- `.log` - Detailed logging information

## Reference Panels

Available reference panels (must be in M3VCF format):
- **TOPMed** - High-coverage whole genome sequences
- **1000 Genomes Phase 3** - Diverse population panel
- **HRC** - Haplotype Reference Consortium

Download from: https://imputationserver.sph.umich.edu/

## Working Directory

- `/data` - Default working directory (mount your data here)

## Performance Tips

1. Use multiple CPUs for large datasets (`--cpus`)
2. Split by chromosome for parallel processing
3. Pre-filter reference and target for common region
4. Ensure sufficient memory for large reference panels

## Comparison with `imputation` Container

| Feature | minimac4 | imputation |
|---------|----------|------------|
| Minimac4 | ✓ | ✓ |
| BCFtools | ✗ | ✓ |
| VCFtools | ✗ | ✓ |
| HTSlib/tabix | ✗ | ✓ |
| Image Size | Smaller | Larger |
| Use Case | Imputation only | Full workflow |

## Version

v4.1.6 - Based on Alpine Linux 3.18
