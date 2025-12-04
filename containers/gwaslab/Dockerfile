FROM python:3.10-slim

LABEL maintainer="AfriGen-D Consortium"
LABEL version="3.6.13"
LABEL org.opencontainers.image.description="gwaslab - GWAS data analysis and visualization toolkit"

# Install system dependencies for scientific Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip wheel setuptools

# Install Python packages
RUN pip install --no-cache-dir \
    gwaslab \
    pandas \
    numpy \
    matplotlib \
    scipy

# Create standard directories
RUN mkdir -p /data /input /output /scripts

WORKDIR /data

# Environment variables for headless operation
ENV PYTHONUNBUFFERED=1
ENV MPLBACKEND=Agg

# Test installation
RUN python -c "import gwaslab; print('gwaslab installed successfully')"

CMD ["python3", "--version"]
