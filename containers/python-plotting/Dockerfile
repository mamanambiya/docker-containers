# Use Python slim for better compatibility with scientific packages
FROM python:3.11-slim

# Set metadata
LABEL maintainer="AfriGen-D Consortium"
LABEL description="Python container for genotype imputation QC plotting and analysis"
LABEL version="1.3.0"
LABEL org.opencontainers.image.description="Python 3.11 data visualization and analysis container with matplotlib, seaborn, pandas, numpy, scipy, and plotly for genomics workflows."

# Install system dependencies required for scientific Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    gfortran \
    libc6-dev \
    libopenblas-dev \
    liblapack-dev \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    zlib1g-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel for binary packages
RUN pip install --upgrade pip wheel setuptools

# Install core scientific packages - use latest compatible versions
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    plotly \
    scipy \
    scikit-learn

# Set environment variables for matplotlib
ENV MPLBACKEND=Agg
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /data

# Test installation
RUN python3 -c "import numpy, pandas, matplotlib, seaborn, plotly, scipy, sklearn; print('All packages imported successfully')"

# Set default command
CMD ["python3", "--version"]