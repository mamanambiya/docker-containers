# BCFtools + Python3 Scientific Stack Container

A comprehensive Docker container that combines BCFtools genomics tools with a complete Python 3.11 scientific computing environment.

## 🧬 **Genomics Tools Included**

- **BCFtools v1.20** - VCF/BCF manipulation and analysis
- **SAMtools v1.20** - Sequence alignment/map manipulation  
- **HTSlib v1.20** - High-throughput sequencing data processing
- **tabix** - Generic indexer for TAB-delimited genome position files

## 🐍 **Python Scientific Stack**

### Core Scientific Computing
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **SciPy** - Scientific computing algorithms

### Data Visualization
- **Matplotlib** - Static plotting
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive plotting

### Machine Learning
- **Scikit-learn** - Machine learning algorithms

### Bioinformatics
- **Pysam** - Python interface to SAM/BAM files
- **bx-python** - Tools for manipulating biological data

### Interactive Analysis
- **Jupyter** - Interactive notebooks
- **IPython** - Enhanced interactive Python shell

### Data I/O
- **openpyxl** - Excel file reading/writing
- **xlsxwriter** - Excel file creation

## 🚀 **Usage**

### Pull from Docker Hub
```bash
docker pull mamana/bcftools-python3:1.0.0
```

### Basic Usage
```bash
# Show available tools
docker run --rm mamana/bcftools-python3:1.0.0

# Interactive Python session
docker run -it --rm mamana/bcftools-python3:1.0.0 python

# Run BCFtools
docker run --rm -v $(pwd):/data mamana/bcftools-python3:1.0.0 bcftools --help

# Start Jupyter notebook
docker run -p 8888:8888 -v $(pwd):/data mamana/bcftools-python3:1.0.0 jupyter notebook --ip=0.0.0.0 --allow-root
```

### With Docker Compose
```yaml
services:
  bcftools-python3:
    image: mamana/bcftools-python3:1.0.0
    volumes:
      - ./data:/data
      - ./scripts:/scripts
    working_dir: /data
```

## 📁 **Directory Structure**

- `/data` - Main working directory (mount your data here)
- `/input` - Input files directory
- `/output` - Output files directory  
- `/scripts` - Scripts directory

## 🔧 **Example Workflows**

### VCF Analysis with Python
```python
import pysam
import pandas as pd
import matplotlib.pyplot as plt

# Read VCF file
vcf = pysam.VariantFile("input.vcf.gz")

# Process variants
variants = []
for record in vcf:
    variants.append({
        'chrom': record.chrom,
        'pos': record.pos,
        'qual': record.qual
    })

# Create DataFrame and plot
df = pd.DataFrame(variants)
plt.figure(figsize=(10, 6))
plt.hist(df['qual'], bins=50)
plt.xlabel('Quality Score')
plt.ylabel('Frequency')
plt.title('Variant Quality Distribution')
plt.savefig('output/quality_distribution.png')
```

### BCFtools + Python Pipeline
```bash
# Filter VCF with BCFtools
bcftools view -f PASS input.vcf.gz > filtered.vcf

# Convert to pandas-friendly format
bcftools query -f '%CHROM\t%POS\t%QUAL\t%INFO/AF\n' filtered.vcf > variants.tsv

# Analyze with Python
python -c "
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('variants.tsv', sep='\t', names=['CHROM', 'POS', 'QUAL', 'AF'])
print(df.describe())

plt.scatter(df['AF'], df['QUAL'])
plt.xlabel('Allele Frequency')
plt.ylabel('Quality Score')
plt.savefig('output/af_vs_qual.png')
"
```

## 🏷️ **Container Specifications**

- **Base Image**: python:3.11-slim
- **Size**: ~800MB (optimized for functionality)
- **Architecture**: linux/amd64
- **Maintainer**: AfriGen-D Consortium

## 🔗 **Integration**

This container is designed to work seamlessly with other containers in the genotype imputation pipeline:

- Use with `mamana/vcf-processing` for additional VCF tools
- Combine with `mamana/r-analysis` for R-based statistical analysis
- Integrate with `mamana/crossmap` for coordinate conversion

## 📊 **Performance**

Optimized for:
- Large VCF/BCF file processing
- Scientific computing workflows
- Interactive data analysis
- Batch processing pipelines

## 🛠️ **Building Locally**

```bash
cd containers/bcftools-python3
docker build -t bcftools-python3:1.0.0 .
```
