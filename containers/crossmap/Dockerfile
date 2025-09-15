# CrossMap container with proper dependencies
FROM python:3.11-slim

LABEL maintainer="AfriGen-D Consortium"
LABEL version="0.7.3"
LABEL org.opencontainers.image.description="CrossMap v0.7.3 coordinate conversion tool for genomics."

# Install system dependencies needed for CrossMap and its Python dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install CrossMap and ensure dependencies are installed
RUN pip install --no-cache-dir \
    CrossMap==0.7.3 \
    pysam \
    bx-python

# Create working directory
WORKDIR /data

# Test that CrossMap is properly installed
RUN python -c "import CrossMap; print('CrossMap module ready')" && \
    python -c "from CrossMap import CrossMap; print('CrossMap main module accessible')"

# Create a wrapper script since CrossMap.py might not be in PATH
RUN echo '#!/usr/bin/env python3' > /usr/local/bin/crossmap && \
    echo 'import sys' >> /usr/local/bin/crossmap && \
    echo 'from CrossMap import CrossMap' >> /usr/local/bin/crossmap && \
    echo 'if __name__ == "__main__":' >> /usr/local/bin/crossmap && \
    echo '    CrossMap.main()' >> /usr/local/bin/crossmap && \
    chmod +x /usr/local/bin/crossmap

# Set default command
CMD ["crossmap"]
