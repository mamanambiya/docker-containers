# Picard

A set of Java command line tools for manipulating high-throughput sequencing data (SAM/BAM/VCF files) from the Broad Institute.

## Contents

- **Picard** v3.3.0 - Comprehensive toolkit for SAM/BAM/VCF manipulation
- **OpenJDK 17** - Java runtime (Eclipse Temurin)
- Based on Alpine Linux for minimal footprint

## Usage

```bash
# Run Picard tool
docker run --rm -v /path/to/data:/data ghcr.io/mamanambiya/docker-containers/picard:latest \
    picard MarkDuplicates \
    -I /data/input.bam \
    -O /data/output.bam \
    -M /data/metrics.txt

# Check version
docker run --rm ghcr.io/mamanambiya/docker-containers/picard:latest picard --version

# List available tools
docker run --rm ghcr.io/mamanambiya/docker-containers/picard:latest picard --help
```

## Common Tools

| Tool | Description |
|------|-------------|
| `MarkDuplicates` | Identify and mark duplicate reads |
| `SortSam` | Sort SAM/BAM files by coordinate or queryname |
| `ValidateSamFile` | Validate SAM/BAM file format |
| `CollectAlignmentSummaryMetrics` | Produce alignment metrics |
| `CreateSequenceDictionary` | Create sequence dictionary for reference |
| `MergeSamFiles` | Merge multiple SAM/BAM files |
| `AddOrReplaceReadGroups` | Add or replace read groups |
| `BuildBamIndex` | Create BAM index (.bai) file |

## Links

- [Picard GitHub](https://github.com/broadinstitute/picard)
- [Picard Documentation](https://broadinstitute.github.io/picard/)
