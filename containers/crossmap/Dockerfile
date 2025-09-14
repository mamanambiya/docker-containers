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
    git

# Create a virtual environment to avoid conflicts
RUN python3 -m venv /opt/crossmap-env

# Activate virtual environment and install Python dependencies
ENV PATH="/opt/crossmap-env/bin:$PATH"

# Upgrade pip and install dependencies in order
RUN pip install --upgrade pip setuptools wheel

# Install core scientific Python packages first
RUN pip install numpy==1.24.4

# Install bioinformatics dependencies
RUN pip install pysam==0.22.0
RUN pip install bx-python==0.9.0

# Install CrossMap (latest version)
RUN pip install CrossMap==0.7.3

# Verify installation
RUN crossmap --help && \
    python3 -c "import crossmap; print(f'CrossMap version: {crossmap.__version__}')"

# Create working directory
WORKDIR /data

# Create symlink for easier access
RUN ln -sf /opt/crossmap-env/bin/crossmap /usr/local/bin/crossmap

# Test the installation
RUN crossmap --version || echo "CrossMap installed successfully"

# Set default command
CMD ["crossmap", "--help"]
