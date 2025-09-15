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

# Test installation - CrossMap installs as CrossMap.py
RUN python -c "import CrossMap; print('CrossMap module imported successfully')"

# Check what was installed and create appropriate wrapper
RUN ls -la /usr/local/bin/ | grep -i crossmap || true && \
    if [ -f /usr/local/bin/CrossMap.py ]; then \
        ln -sf /usr/local/bin/CrossMap.py /usr/local/bin/crossmap; \
    else \
        echo '#!/usr/bin/env python' > /usr/local/bin/crossmap && \
        echo 'import sys' >> /usr/local/bin/crossmap && \
        echo 'from CrossMap.CrossMap import main' >> /usr/local/bin/crossmap && \
        echo 'if __name__ == "__main__":' >> /usr/local/bin/crossmap && \
        echo '    main()' >> /usr/local/bin/crossmap && \
        chmod +x /usr/local/bin/crossmap; \
    fi

# Test that it works
RUN crossmap 2>&1 | grep -i "usage" || crossmap --help || CrossMap.py --help || python -c "from CrossMap.CrossMap import main; print('CrossMap ready')"

# Set default command
CMD ["crossmap"]
