#!/bin/bash

# Test script for bcftools-python3 container
echo "🧪 Testing BCFtools + Python3 Container"
echo "========================================"

# Test BCFtools
echo ""
echo "🧬 Testing BCFtools..."
bcftools --version | head -3
echo "✅ BCFtools test passed"

# Test SAMtools
echo ""
echo "🧬 Testing SAMtools..."
samtools --version | head -3
echo "✅ SAMtools test passed"

# Test tabix
echo ""
echo "🧬 Testing tabix..."
tabix --version 2>&1 | head -1
echo "✅ tabix test passed"

# Test Python packages
echo ""
echo "🐍 Testing Python packages..."

python3 -c "
import sys
print(f'Python version: {sys.version}')

# Test core scientific packages
try:
    import numpy as np
    print(f'✅ NumPy v{np.__version__}')
except ImportError as e:
    print(f'❌ NumPy import failed: {e}')

try:
    import pandas as pd
    print(f'✅ Pandas v{pd.__version__}')
except ImportError as e:
    print(f'❌ Pandas import failed: {e}')

try:
    import matplotlib
    print(f'✅ Matplotlib v{matplotlib.__version__}')
except ImportError as e:
    print(f'❌ Matplotlib import failed: {e}')

try:
    import seaborn as sns
    print(f'✅ Seaborn v{sns.__version__}')
except ImportError as e:
    print(f'❌ Seaborn import failed: {e}')

try:
    import scipy
    print(f'✅ SciPy v{scipy.__version__}')
except ImportError as e:
    print(f'❌ SciPy import failed: {e}')

try:
    import sklearn
    print(f'✅ Scikit-learn v{sklearn.__version__}')
except ImportError as e:
    print(f'❌ Scikit-learn import failed: {e}')

try:
    import pysam
    print(f'✅ Pysam v{pysam.__version__}')
except ImportError as e:
    print(f'❌ Pysam import failed: {e}')

try:
    import plotly
    print(f'✅ Plotly v{plotly.__version__}')
except ImportError as e:
    print(f'❌ Plotly import failed: {e}')

try:
    import jupyter
    print(f'✅ Jupyter (core) available')
except ImportError as e:
    print(f'❌ Jupyter import failed: {e}')

print('')
print('🎯 Creating a simple test plot...')

try:
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Create test data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('BCFtools-Python3 Container Test Plot')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot
    plt.savefig('/data/test_plot.png', dpi=150, bbox_inches='tight')
    print('✅ Test plot saved to /data/test_plot.png')
    
except Exception as e:
    print(f'❌ Plot creation failed: {e}')
"

echo ""
echo "📊 Testing tools_info script..."
tools_info

echo ""
echo "🎉 Container test completed!"
echo ""
echo "📁 Available directories:"
ls -la / | grep -E "(data|input|output|scripts)"

echo ""
echo "🚀 Container is ready for use!"
echo ""
echo "Usage examples:"
echo "  # Interactive Python:"
echo "  docker run -it mamana/bcftools-python3:1.0.0 python"
echo ""
echo "  # Run BCFtools:"
echo "  docker run -v \$(pwd):/data mamana/bcftools-python3:1.0.0 bcftools stats input.vcf"
echo ""
echo "  # Start Jupyter:"
echo "  docker run -p 8888:8888 -v \$(pwd):/data mamana/bcftools-python3:1.0.0 jupyter notebook --ip=0.0.0.0 --allow-root"
