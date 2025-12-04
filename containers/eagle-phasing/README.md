# Eagle Phasing Container

Lightweight Alpine Linux-based container for haplotype phasing using Eagle software.

## Tools Included

- **Eagle v2.4.1** - Fast haplotype phasing software

## Purpose

Eagle performs haplotype phasing of genotype data, which is a critical preprocessing step before genotype imputation. Phasing determines which alleles are inherited together on the same chromosome.

## Features

- Ultra-fast phasing algorithm
- Can phase with or without a reference panel
- Supports VCF input/output
- Multi-threaded processing

## Usage

### Check Eagle version

```bash
docker run --rm eagle-phasing
```

### Basic phasing (no reference panel)

```bash
docker run --rm -v /path/to/data:/data eagle-phasing \
  eagle \
  --vcf input.vcf.gz \
  --geneticMapFile genetic_map.txt \
  --outPrefix output \
  --numThreads 4
```

### Phasing with reference panel

```bash
docker run --rm -v /path/to/data:/data eagle-phasing \
  eagle \
  --vcf target.vcf.gz \
  --vcfRef reference.vcf.gz \
  --geneticMapFile genetic_map.txt \
  --outPrefix output \
  --numThreads 4
```

## Required Files

1. **Input VCF** - Target genotypes to be phased
2. **Genetic Map** - Recombination rate map (available from Eagle documentation)
3. **Reference Panel** (optional) - Phased reference haplotypes for improved accuracy

## Genetic Maps

Genetic map files for different populations are available from:
- Eagle documentation: https://alkesgroup.broadinstitute.org/Eagle/
- 1000 Genomes: https://bochet.gcc.biostat.washington.edu/beagle/genetic_maps/

## Working Directory

- `/data` - Default working directory (mount your data here)

## Performance

Eagle is designed for speed and can phase large cohorts efficiently. For best performance:
- Use multiple threads (`--numThreads`)
- Ensure input VCF files are indexed
- Provide appropriate genetic map for your population

## Version

v2.4.1 - Based on Alpine Linux 3.19
