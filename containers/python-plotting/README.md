# Python Plotting Container

Python 3.11 container with scientific computing and data visualization libraries for genomics QC and analysis.

## Tools Included

- **Python 3.11** - Latest stable Python
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Static plotting
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive plotting
- **SciPy** - Scientific computing
- **scikit-learn** - Machine learning

## Purpose

This container provides a complete Python environment for:
- Quality control visualization in imputation workflows
- Statistical analysis of genomic data
- Creating publication-quality plots
- Interactive data exploration
- Post-imputation analysis and reporting

## Usage

### Check Python version

```bash
docker run --rm python-plotting
```

### Run Python script

```bash
docker run --rm -v /path/to/data:/data python-plotting \
  python3 script.py
```

### Interactive Python session

```bash
docker run --rm -it -v /path/to/data:/data python-plotting python3
```

### Run with mounted code and data

```bash
docker run --rm \
  -v /path/to/scripts:/scripts \
  -v /path/to/data:/data \
  -v /path/to/output:/output \
  python-plotting \
  python3 /scripts/plot_qc_metrics.py
```

## Example Scripts

### Basic plotting example

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read data
df = pd.read_csv('/data/qc_metrics.csv')

# Create plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='missing_rate', y='het_rate')
plt.savefig('/output/qc_plot.png', dpi=300, bbox_inches='tight')
```

### Imputation quality visualization

```python
import pandas as pd
import plotly.express as px

# Read imputation info
info = pd.read_csv('/data/imputation.info', sep='\t')

# Interactive R² plot
fig = px.scatter(info, x='MAF', y='Rsq',
                 color='Rsq',
                 title='Imputation Quality by MAF')
fig.write_html('/output/rsq_plot.html')
```

## Common Use Cases

### 1. QC Metrics Visualization
- Sample missingness rates
- Variant call rates
- Hardy-Weinberg equilibrium plots
- Heterozygosity distributions
- PCA plots

### 2. Imputation Quality Assessment
- R² (imputation quality) distributions
- INFO score plots
- MAF stratified quality metrics
- Per-chromosome quality summaries

### 3. Statistical Analysis
- Association test results
- Manhattan plots
- QQ plots
- Effect size distributions

### 4. Data Processing
- VCF summary statistics
- Dosage file manipulation
- Results formatting and filtering
- Report generation

## Environment Variables

- `MPLBACKEND=Agg` - Non-interactive matplotlib backend (for server use)
- `PYTHONUNBUFFERED=1` - Unbuffered output for better logging

## Working Directory

- `/data` - Default working directory (mount your data here)

## Tips

### Save plots without display

```python
import matplotlib
matplotlib.use('Agg')  # Already set by default
import matplotlib.pyplot as plt

# Your plotting code
plt.savefig('/output/plot.png')
```

### Memory-efficient data loading

```python
import pandas as pd

# Read large files in chunks
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process_chunk(chunk)
```

### Create multiple plot formats

```python
# Save as PNG for presentations
plt.savefig('/output/plot.png', dpi=300)

# Save as PDF for publications
plt.savefig('/output/plot.pdf')

# Save as SVG for editing
plt.savefig('/output/plot.svg')
```

## Integration with Workflows

This container is typically used for:
1. Pre-imputation QC visualization
2. Post-imputation quality assessment
3. Final results visualization and reporting

## Volume Mounts

Recommended directory structure:
```bash
docker run --rm \
  -v /local/scripts:/scripts \    # Your Python scripts
  -v /local/data:/data \           # Input data
  -v /local/output:/output \       # Output plots/results
  python-plotting \
  python3 /scripts/analysis.py
```

## Package Versions

Uses latest compatible versions from PyPI:
- Python: 3.11
- All scientific packages: Latest stable releases

To check installed versions:
```bash
docker run --rm python-plotting pip list
```

## Version

v1.3.0 - Based on Python 3.11 slim (Debian)
