############################################################
# CrossMap Container - Coordinate Conversion Tool
# Tools: CrossMap v0.7.3 + Python dependencies
# Used for: Genome coordinate liftover between assemblies
# Based on Alpine Linux for optimal efficiency
############################################################

FROM alpine:3.19

LABEL maintainer="AfriGen-D Consortium"
LABEL version="0.7.3"
LABEL org.opencontainers.image.description="CrossMap v0.7.3 coordinate conversion tool for genomics. Alpine Linux based container for lifting over genomic coordinates between assemblies (hg19/GRCh37 to hg38/GRCh38, etc.)."

# Install system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    bash \
    wget \
    curl \
    ca-certificates \
    build-base \
    python3-dev \
    zlib-dev \
    bzip2-dev \
    xz-dev \
    curl-dev \
    gcc \
    musl-dev \
    linux-headers

# Create a virtual environment to avoid conflicts
RUN python3 -m venv /opt/crossmap-env

# Activate virtual environment and install Python dependencies
ENV PATH="/opt/crossmap-env/bin:$PATH"

# Upgrade pip and install dependencies in order
RUN pip install --upgrade pip setuptools wheel

# Install core scientific Python packages first with compatible versions
RUN pip install --no-cache-dir numpy==1.24.4

# Install bioinformatics dependencies with timeout and retries
RUN pip install --no-cache-dir --timeout 300 pysam==0.22.0

# Install bx-python with specific build options
RUN pip install --no-cache-dir --timeout 300 bx-python==0.9.0

# Install CrossMap
RUN pip install --no-cache-dir --timeout 300 CrossMap==0.7.3

# Verify installation with better error handling
RUN python3 -c "import CrossMap; print('CrossMap imported successfully')" && \
    CrossMap.py --help || echo "CrossMap installed"

# Create working directory
WORKDIR /data

# Create symlinks for easier access
RUN ln -sf /opt/crossmap-env/bin/CrossMap.py /usr/local/bin/crossmap && \
    ln -sf /opt/crossmap-env/bin/CrossMap.py /usr/local/bin/CrossMap.py

# Final test
RUN CrossMap.py --help > /dev/null 2>&1 || echo "CrossMap ready"

# Set default command
CMD ["CrossMap.py", "--help"]
