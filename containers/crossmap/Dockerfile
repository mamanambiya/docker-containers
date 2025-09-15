# CrossMap container - working version
FROM python:3.11-slim

LABEL maintainer="AfriGen-D Consortium"
LABEL version="0.7.3"
LABEL org.opencontainers.image.description="CrossMap v0.7.3 coordinate conversion tool for genomics."

# Install system dependencies required for pysam and pyBigWig
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install CrossMap (it will install pysam, bx-python, pyBigWig automatically)
RUN pip install --no-cache-dir CrossMap==0.7.3

# Create working directory
WORKDIR /data

# Test that CrossMap is installed and working
# CrossMap installs an executable script that imports from cmmodule
RUN python -c "from cmmodule import crossmap; print('CrossMap module ready')" && \
    CrossMap --help | head -1

# Set default command - CrossMap is installed as an executable
CMD ["CrossMap", "--help"]
