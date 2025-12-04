# gwaslab Container

GWAS data analysis and visualization toolkit for processing and visualizing genome-wide association study results.

## Tools Included

- **gwaslab** - Python package for GWAS summary statistics QC, harmonization, and visualization
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scipy** - Scientific computing
- **matplotlib** - Data visualization

## Purpose

This container provides a complete environment for:
- GWAS summary statistics quality control
- Data harmonization and formatting
- Manhattan plots and QQ plots
- Regional association plots
- Lead variant annotation

## Usage

### Basic Usage

```bash
# Run Python interactively
docker run --rm -it -v $(pwd):/data mamana/gwaslab:3.6.13 python3

# Run a Python script
docker run --rm -v $(pwd):/data mamana/gwaslab:3.6.13 python3 /data/analysis.py
```

### Example: Load GWAS Summary Statistics

```bash
docker run --rm -v $(pwd):/data mamana/gwaslab:3.6.13 python3 -c "
import gwaslab as gl
import pandas as pd

# Load summary statistics
mysumstats = gl.Sumstats('/data/sumstats.txt',
    snpid='SNP',
    chrom='CHR',
    pos='BP',
    ea='A1',
    nea='A2',
    beta='BETA',
    se='SE',
    p='P')

# Basic QC
mysumstats.basic_check()

# Save harmonized data
mysumstats.data.to_csv('/data/harmonized_sumstats.csv', index=False)
"
```

### Example: Create Manhattan Plot

```bash
docker run --rm -v $(pwd):/data mamana/gwaslab:3.6.13 python3 -c "
import gwaslab as gl

mysumstats = gl.Sumstats('/data/sumstats.txt',
    snpid='SNP', chrom='CHR', pos='BP',
    ea='A1', nea='A2', beta='BETA', se='SE', p='P')

# Generate Manhattan plot
mysumstats.plot_mqq(save='/data/manhattan_qq.png')
"
```

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `/data` | Main working directory (mount your data here) |
| `/input` | Input files directory |
| `/output` | Output files directory |
| `/scripts` | Custom scripts directory |

## Container Specifications

- **Base Image**: python:3.10-slim
- **Architecture**: linux/amd64
- **Working Directory**: /data

## Building Locally

```bash
# Build
docker build -t test-gwaslab:local ./containers/gwaslab

# Test
docker run --rm test-gwaslab:local python -c "import gwaslab; print(gwaslab.__version__)"

# Interactive shell
docker run --rm -it test-gwaslab:local /bin/bash
```
