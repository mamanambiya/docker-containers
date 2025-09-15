# BCFtools + Python3 Scientific Stack Container
FROM python:3.11-slim

LABEL maintainer="AfriGen-D Consortium"
LABEL version="1.0.0"
LABEL org.opencontainers.image.description="BCFtools 1.20 with Python 3.11 scientific stack for genomics analysis and visualization"

# Install system dependencies for BCFtools and Python scientific packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Build tools
    build-essential \
    autoconf \
    automake \
    libtool \
    pkg-config \
    # BCFtools dependencies
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libncurses5-dev \
    # Python scientific package dependencies
    gcc \
    g++ \
    gfortran \
    libc6-dev \
    libopenblas-dev \
    liblapack-dev \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    # Download tools
    wget \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory for builds
WORKDIR /opt/tools

# Install HTSlib 1.20 (required for BCFtools)
RUN wget https://github.com/samtools/htslib/releases/download/1.20/htslib-1.20.tar.bz2 && \
    tar -xjf htslib-1.20.tar.bz2 && \
    cd htslib-1.20 && \
    ./configure --prefix=/usr/local --enable-libcurl --enable-gcs --enable-s3 && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf htslib-1.20*

# Install BCFtools 1.20 (latest stable)
RUN wget https://github.com/samtools/bcftools/releases/download/1.20/bcftools-1.20.tar.bz2 && \
    tar -xjf bcftools-1.20.tar.bz2 && \
    cd bcftools-1.20 && \
    ./configure --prefix=/usr/local && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf bcftools-1.20*

# Install SAMtools 1.20 (companion tool)
RUN wget https://github.com/samtools/samtools/releases/download/1.20/samtools-1.20.tar.bz2 && \
    tar -xjf samtools-1.20.tar.bz2 && \
    cd samtools-1.20 && \
    ./configure --prefix=/usr/local && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf samtools-1.20*

# Upgrade pip and install wheel for binary packages
RUN pip install --upgrade pip wheel setuptools

# Install core scientific Python packages
RUN pip install --no-cache-dir \
    # Core scientific computing
    numpy \
    pandas \
    scipy \
    # Data visualization
    matplotlib \
    seaborn \
    plotly \
    # Machine learning
    scikit-learn \
    # Bioinformatics packages
    pysam \
    bx-python \
    # Jupyter for interactive analysis
    jupyter \
    ipython \
    # Data manipulation
    openpyxl \
    xlsxwriter

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MPLBACKEND=Agg
ENV PATH="/usr/local/bin:${PATH}"

# Create working directories
RUN mkdir -p /data /input /output /scripts
WORKDIR /data

# Create info script to show available tools
RUN echo '#!/bin/bash' > /usr/local/bin/tools_info && \
    echo 'echo "=== BCFtools + Python3 Scientific Stack ==="' >> /usr/local/bin/tools_info && \
    echo 'echo "BCFtools: $(bcftools --version | head -1)"' >> /usr/local/bin/tools_info && \
    echo 'echo "SAMtools: $(samtools --version | head -1)"' >> /usr/local/bin/tools_info && \
    echo 'echo "HTSlib: $(htsfile --version-only 2>/dev/null || echo "Available")"' >> /usr/local/bin/tools_info && \
    echo 'echo "tabix: $(tabix --version 2>&1 | head -1)"' >> /usr/local/bin/tools_info && \
    echo 'echo "Python: $(python --version)"' >> /usr/local/bin/tools_info && \
    echo 'echo "NumPy: $(python -c \"import numpy; print(f\"v{numpy.__version__}\")")"' >> /usr/local/bin/tools_info && \
    echo 'echo "Pandas: $(python -c \"import pandas; print(f\"v{pandas.__version__}\")")"' >> /usr/local/bin/tools_info && \
    echo 'echo "Matplotlib: $(python -c \"import matplotlib; print(f\"v{matplotlib.__version__}\")")"' >> /usr/local/bin/tools_info && \
    echo 'echo "Pysam: $(python -c \"import pysam; print(f\"v{pysam.__version__}\")")"' >> /usr/local/bin/tools_info && \
    chmod +x /usr/local/bin/tools_info

# Test installations
RUN bcftools --version >/dev/null && \
    samtools --version >/dev/null && \
    tabix --version >/dev/null 2>&1 && \
    python -c "import numpy, pandas, matplotlib, seaborn, plotly, scipy, sklearn, pysam; print('All Python packages imported successfully')"

# Set default command
CMD ["tools_info"]
