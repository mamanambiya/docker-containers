FROM alpine:3.18

# Minimac4 v4.1.6 for genotype imputation
LABEL maintainer="AfriGen-D <info@afrigen.org>"
LABEL version="4.1.6"
LABEL org.opencontainers.image.description="Minimac4 v4.1.6 genotype imputation software. Alpine Linux based container with Minimac4 imputation tool."

# Install runtime dependencies and build tools (in case we need to compile)
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
    git

# Download and install prebuilt Minimac4 binary with fallback to source build
RUN cd /tmp && \
    echo "Attempting to download prebuilt Minimac4 v4.1.6..." && \
    if wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 3 \
        https://github.com/statgen/Minimac4/releases/download/v4.1.6/minimac4-4.1.6-Linux-x86_64.sh; then \
        echo "Downloaded prebuilt binary, installing..." && \
        chmod +x minimac4-4.1.6-Linux-x86_64.sh && \
        ./minimac4-4.1.6-Linux-x86_64.sh --skip-license --prefix=/usr/local && \
        rm minimac4-4.1.6-Linux-x86_64.sh; \
    else \
        echo "Prebuilt binary download failed, building from source..." && \
        git clone --depth 1 --branch v4.1.6 https://github.com/statgen/Minimac4.git && \
        cd Minimac4 && \
        mkdir build && cd build && \
        cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local && \
        make -j$(nproc) && \
        make install && \
        cd /tmp && rm -rf Minimac4; \
    fi

# Create working directory
WORKDIR /data

# Test the installation
RUN echo "Testing Minimac4 installation..." && \
    minimac4 --help && \
    echo "Minimac4 v4.1.6 installed successfully"

# Set default command
CMD ["minimac4", "--help"] 