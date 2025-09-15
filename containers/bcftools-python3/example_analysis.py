#!/usr/bin/env python3
"""
Example analysis script demonstrating BCFtools + Python integration
This script shows how to combine BCFtools VCF processing with Python data analysis
"""

import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pysam
import os
from pathlib import Path

def run_bcftools_command(command, input_file=None, output_file=None):
    """Run a BCFtools command and return the result"""
    if input_file and output_file:
        full_command = f"bcftools {command} {input_file} > {output_file}"
    elif input_file:
        full_command = f"bcftools {command} {input_file}"
    else:
        full_command = f"bcftools {command}"
    
    print(f"Running: {full_command}")
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout

def analyze_vcf_with_bcftools_and_python(vcf_file):
    """
    Complete VCF analysis pipeline combining BCFtools and Python
    """
    print("🧬 Starting VCF Analysis Pipeline")
    print("=" * 50)
    
    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 1. Basic VCF statistics with BCFtools
    print("\n📊 Step 1: Basic VCF Statistics")
    stats_output = run_bcftools_command(f"stats {vcf_file}")
    if stats_output:
        with open(output_dir / "vcf_stats.txt", "w") as f:
            f.write(stats_output)
        print("✅ VCF statistics saved to output/vcf_stats.txt")
    
    # 2. Extract variant information for Python analysis
    print("\n🐍 Step 2: Extract Data for Python Analysis")
    query_cmd = "query -f '%CHROM\\t%POS\\t%QUAL\\t%INFO/AF\\t%INFO/DP\\n'"
    variants_data = run_bcftools_command(query_cmd, vcf_file)
    
    if variants_data:
        # Save to file
        with open(output_dir / "variants.tsv", "w") as f:
            f.write("CHROM\tPOS\tQUAL\tAF\tDP\n")
            f.write(variants_data)
        
        # Load into pandas
        df = pd.read_csv(output_dir / "variants.tsv", sep="\t")
        print(f"✅ Loaded {len(df)} variants into pandas DataFrame")
        
        # 3. Python-based analysis and visualization
        print("\n📈 Step 3: Python Data Analysis & Visualization")
        
        # Basic statistics
        print("\nVariant Quality Statistics:")
        print(df['QUAL'].describe())
        
        # Create visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('VCF Analysis Results', fontsize=16)
        
        # Quality distribution
        axes[0, 0].hist(df['QUAL'].dropna(), bins=50, alpha=0.7, color='skyblue')
        axes[0, 0].set_xlabel('Quality Score')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].set_title('Variant Quality Distribution')
        
        # Allele frequency distribution
        af_data = pd.to_numeric(df['AF'], errors='coerce').dropna()
        if len(af_data) > 0:
            axes[0, 1].hist(af_data, bins=50, alpha=0.7, color='lightgreen')
            axes[0, 1].set_xlabel('Allele Frequency')
            axes[0, 1].set_ylabel('Frequency')
            axes[0, 1].set_title('Allele Frequency Distribution')
        
        # Quality vs Depth scatter plot
        qual_data = pd.to_numeric(df['QUAL'], errors='coerce')
        dp_data = pd.to_numeric(df['DP'], errors='coerce')
        valid_data = pd.DataFrame({'QUAL': qual_data, 'DP': dp_data}).dropna()
        
        if len(valid_data) > 0:
            axes[1, 0].scatter(valid_data['DP'], valid_data['QUAL'], alpha=0.5, s=1)
            axes[1, 0].set_xlabel('Depth (DP)')
            axes[1, 0].set_ylabel('Quality Score')
            axes[1, 0].set_title('Quality vs Depth')
        
        # Variants per chromosome
        chrom_counts = df['CHROM'].value_counts().head(10)
        axes[1, 1].bar(range(len(chrom_counts)), chrom_counts.values)
        axes[1, 1].set_xlabel('Chromosome')
        axes[1, 1].set_ylabel('Number of Variants')
        axes[1, 1].set_title('Variants per Chromosome (Top 10)')
        axes[1, 1].set_xticks(range(len(chrom_counts)))
        axes[1, 1].set_xticklabels(chrom_counts.index, rotation=45)
        
        plt.tight_layout()
        plt.savefig(output_dir / "vcf_analysis_plots.png", dpi=300, bbox_inches='tight')
        print("✅ Analysis plots saved to output/vcf_analysis_plots.png")
        
        # 4. Advanced analysis with seaborn
        print("\n🎨 Step 4: Advanced Visualization with Seaborn")
        
        if len(valid_data) > 100:  # Only if we have enough data
            plt.figure(figsize=(12, 8))
            
            # Create a correlation heatmap
            plt.subplot(2, 2, 1)
            correlation_data = valid_data.corr()
            sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0)
            plt.title('Quality Metrics Correlation')
            
            # Quality distribution by chromosome
            plt.subplot(2, 2, 2)
            top_chroms = df['CHROM'].value_counts().head(5).index
            chrom_qual_data = df[df['CHROM'].isin(top_chroms)]
            sns.boxplot(data=chrom_qual_data, x='CHROM', y='QUAL')
            plt.title('Quality Distribution by Chromosome')
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.savefig(output_dir / "advanced_analysis.png", dpi=300, bbox_inches='tight')
            print("✅ Advanced analysis plots saved to output/advanced_analysis.png")
    
    # 5. Generate summary report
    print("\n📋 Step 5: Generate Summary Report")
    
    with open(output_dir / "analysis_summary.txt", "w") as f:
        f.write("VCF Analysis Summary Report\n")
        f.write("=" * 30 + "\n\n")
        f.write(f"Input file: {vcf_file}\n")
        f.write(f"Total variants analyzed: {len(df) if 'df' in locals() else 'N/A'}\n")
        
        if 'df' in locals():
            f.write(f"Quality score range: {df['QUAL'].min():.2f} - {df['QUAL'].max():.2f}\n")
            f.write(f"Mean quality score: {df['QUAL'].mean():.2f}\n")
            f.write(f"Chromosomes represented: {df['CHROM'].nunique()}\n")
        
        f.write("\nFiles generated:\n")
        f.write("- vcf_stats.txt: BCFtools statistics\n")
        f.write("- variants.tsv: Extracted variant data\n")
        f.write("- vcf_analysis_plots.png: Basic analysis plots\n")
        f.write("- advanced_analysis.png: Advanced visualizations\n")
        f.write("- analysis_summary.txt: This summary report\n")
    
    print("✅ Summary report saved to output/analysis_summary.txt")
    print("\n🎉 Analysis complete! Check the output/ directory for results.")

def main():
    """Main function to run the analysis"""
    print("BCFtools + Python3 Scientific Stack Demo")
    print("=" * 40)
    
    # Check if a VCF file is provided
    import sys
    if len(sys.argv) > 1:
        vcf_file = sys.argv[1]
        if os.path.exists(vcf_file):
            analyze_vcf_with_bcftools_and_python(vcf_file)
        else:
            print(f"Error: VCF file '{vcf_file}' not found!")
    else:
        print("Usage: python example_analysis.py <vcf_file>")
        print("\nThis script demonstrates the integration of:")
        print("🧬 BCFtools for VCF processing")
        print("🐍 Python for data analysis")
        print("📊 Matplotlib/Seaborn for visualization")
        print("📋 Pandas for data manipulation")
        print("\nExample:")
        print("python example_analysis.py input/sample.vcf.gz")

if __name__ == "__main__":
    main()
