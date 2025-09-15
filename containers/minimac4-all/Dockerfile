FROM alpine:3.18

# Minimac4-all: Azure-compatible container (same as minimac4 + Azure features)
LABEL maintainer="AfriGen-D <info@afrigen.org>"
LABEL version="4.1.6-azure"
LABEL description="Minimac4 v4.1.6 with Azure compatibility features"

# Set timezone for Azure
ENV TZ=UTC

# Install runtime dependencies (same as basic minimac4 + Azure tools + build tools)
RUN apk add --no-cache \
    bash \
    ca-certificates \
    wget \
    curl \
    libgomp \
    zlib \
    zlib-dev \
    bzip2 \
    bzip2-dev \
    xz \
    xz-dev \
    libstdc++ \
    build-base \
    cmake \
    git \
    # Azure tools
    python3 \
    py3-pip

# Install minimal Python packages for Azure
RUN pip3 install --no-cache-dir --break-system-packages \
    numpy \
    pandas

# Download and install prebuilt Minimac4 binary with fallback to source build
ENV MINIMAC4_VERSION=4.1.6
RUN cd /tmp && \
    echo "Attempting to download prebuilt Minimac4 v${MINIMAC4_VERSION}..." && \
    if wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 3 \
        https://github.com/statgen/Minimac4/releases/download/v${MINIMAC4_VERSION}/minimac4-${MINIMAC4_VERSION}-Linux-x86_64.sh; then \
        echo "Downloaded prebuilt binary, installing..." && \
        chmod +x minimac4-${MINIMAC4_VERSION}-Linux-x86_64.sh && \
        ./minimac4-${MINIMAC4_VERSION}-Linux-x86_64.sh --skip-license --prefix=/usr/local && \
        rm minimac4-${MINIMAC4_VERSION}-Linux-x86_64.sh; \
    else \
        echo "Prebuilt binary download failed, building from source..." && \
        git clone --depth 1 --branch v${MINIMAC4_VERSION} https://github.com/statgen/Minimac4.git || \
        git clone --depth 1 https://github.com/statgen/Minimac4.git && \
        cd Minimac4 && \
        mkdir build && cd build && \
        cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local && \
        make -j$(nproc) && \
        make install && \
        cd /tmp && rm -rf Minimac4; \
    fi

# Create Azure-compatible directories
RUN mkdir -p /data/{input,output,reference,temp} && \
    mkdir -p /scripts && \
    mkdir -p /logs

# Create non-root user for Azure security compliance
RUN adduser -D -s /bin/bash impuser && \
    chown -R impuser:impuser /data /scripts /logs

# Set environment variables
ENV PATH="/usr/local/bin:${PATH}"

# Test the installation
RUN minimac4 --help > /dev/null 2>&1 && echo "✅ Minimac4 installation verified"

# Create Azure test script  
RUN echo '#!/bin/bash' > /usr/local/bin/test-azure-tools && \
    echo 'echo "=== Minimac4-All Azure Test ==="' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "🏠 Container: $(hostname)"' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "👤 User: $(whoami)"' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "📁 Working directory: $(pwd)"' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "🧬 Minimac4: $(minimac4 --version 2>&1 | head -1)"' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "🐍 Python: $(python3 --version)"' >> /usr/local/bin/test-azure-tools && \
    echo 'echo "✅ Azure-compatible Minimac4 ready!"' >> /usr/local/bin/test-azure-tools && \
    chmod +x /usr/local/bin/test-azure-tools

# Set Azure-compatible defaults
WORKDIR /data
USER impuser

# Set default command
CMD ["/bin/bash", "-l"] 