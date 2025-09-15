############################################################
# CrossMap Container - Coordinate Conversion Tool
# Tools: CrossMap v0.7.3 + Python dependencies
# Used for: Genome coordinate liftover between assemblies
# Based on Python Alpine for better package support
############################################################

FROM python:3.11-alpine3.19

LABEL maintainer="AfriGen-D Consortium"
LABEL version="0.7.3"
LABEL org.opencontainers.image.description="CrossMap v0.7.3 coordinate conversion tool for genomics. Alpine Linux based container for lifting over genomic coordinates between assemblies (hg19/GRCh37 to hg38/GRCh38, etc.)."

# Install minimal system dependencies
RUN apk add --no-cache \
    bash \
    wget \
    curl \
    ca-certificates \
    build-base \
    zlib-dev \
    bzip2-dev

# Upgrade pip first
RUN pip install --upgrade pip

# Install CrossMap directly (it will pull in its dependencies)
RUN pip install --no-cache-dir CrossMap==0.7.3

# Create working directory
WORKDIR /data

# Create symlink for easier access
RUN ln -sf /usr/local/bin/CrossMap.py /usr/local/bin/crossmap

# Test installation
RUN CrossMap.py --help

# Set default command
CMD ["CrossMap.py", "--help"]
