# Use Alpine Linux for smaller, more secure container
FROM alpine:3.19

# Set metadata
LABEL maintainer="AfriGen-D Consortium"
LABEL description="Python container for genotype imputation QC plotting and analysis"
LABEL version="1.3.0"
LABEL org.opencontainers.image.description="Python 3.11 data visualization and analysis container with matplotlib, seaborn, pandas, numpy, scipy, and plotly for genomics workflows."

# Set working directory
WORKDIR /app

# Install system dependencies required for scientific Python packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    bash \
    gcc \
    g++ \
    gfortran \
    musl-dev \
    linux-headers \
    openblas-dev \
    lapack-dev \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    zlib-dev \
    ca-certificates \
    curl \
    git

# Create virtual environment for better dependency management
RUN python3 -m venv /opt/plotting-env

# Activate virtual environment
ENV PATH="/opt/plotting-env/bin:$PATH"

# Upgrade pip and install core packages
RUN pip install --upgrade pip setuptools wheel

# Install core scientific packages first (in order to avoid conflicts)
RUN pip install numpy==1.24.4
RUN pip install pandas==2.0.3
RUN pip install scipy==1.11.2

# Install plotting libraries
RUN pip install matplotlib==3.7.2
RUN pip install seaborn==0.12.2
RUN pip install plotly==5.17.0

# Install additional scientific packages
RUN pip install scikit-learn==1.3.0
RUN pip install statsmodels==0.14.0

# Install utility packages
RUN pip install tqdm==4.66.1
RUN pip install joblib==1.3.2

# Install bioinformatics-specific packages
RUN pip install pysam==0.22.0
RUN pip install bx-python==0.9.0

# Set environment variables for matplotlib
ENV MPLBACKEND=Agg
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Create directories for input/output
RUN mkdir -p /data /output

# Create working directory
WORKDIR /data

# Test installation
RUN python3 -c "import numpy, pandas, matplotlib, seaborn, plotly, scipy, sklearn; print('All packages imported successfully')"

# Set default command
CMD ["python3", "--version"]