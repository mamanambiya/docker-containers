# Use Python Alpine for better package support
FROM python:3.11-alpine3.19

# Set metadata
LABEL maintainer="AfriGen-D Consortium"
LABEL description="Python container for genotype imputation QC plotting and analysis"
LABEL version="1.3.0"
LABEL org.opencontainers.image.description="Python 3.11 data visualization and analysis container with matplotlib, seaborn, pandas, numpy, scipy, and plotly for genomics workflows."

# Install system dependencies required for scientific Python packages
RUN apk add --no-cache \
    bash \
    gcc \
    g++ \
    gfortran \
    musl-dev \
    openblas-dev \
    lapack-dev \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    zlib-dev \
    ca-certificates \
    curl

# Upgrade pip first
RUN pip install --upgrade pip

# Install core scientific packages (let pip handle dependencies)
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