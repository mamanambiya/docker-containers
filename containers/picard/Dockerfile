############################################################
# Picard Container
# Tools: Picard (SAM/BAM/VCF manipulation)
# Used in: MarkDuplicates, SortSam, ValidateSamFile, etc.
# Based on Eclipse Temurin OpenJDK 17 Alpine
############################################################

FROM eclipse-temurin:17-jre-alpine

LABEL maintainer="AfriGen-D Consortium"
LABEL version="1.0"
LABEL org.opencontainers.image.description="Picard v3.3.0 - A set of Java command line tools for manipulating high-throughput sequencing data (SAM/BAM/VCF). Based on Alpine Linux with OpenJDK 17."

# Picard version
ENV PICARD_VERSION=3.3.0

# Install dependencies
RUN apk add --no-cache \
    bash \
    wget \
    ca-certificates

# Create directories
RUN mkdir -p /opt/picard /data /input /output

WORKDIR /opt/picard

# Download Picard JAR
RUN wget -q https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar && \
    chmod 644 picard.jar

# Create wrapper script for easy invocation
RUN echo '#!/bin/bash' > /usr/local/bin/picard && \
    echo 'java -jar /opt/picard/picard.jar "$@"' >> /usr/local/bin/picard && \
    chmod +x /usr/local/bin/picard

# Create info script
RUN echo '#!/bin/bash' > /usr/local/bin/picard_info && \
    echo 'echo "=== Picard Tools ==="' >> /usr/local/bin/picard_info && \
    echo 'echo "Picard version: ${PICARD_VERSION}"' >> /usr/local/bin/picard_info && \
    echo 'echo "Java: $(java --version 2>&1 | head -1)"' >> /usr/local/bin/picard_info && \
    echo 'echo ""' >> /usr/local/bin/picard_info && \
    echo 'echo "Usage: picard <tool> [options]"' >> /usr/local/bin/picard_info && \
    echo 'echo "Example: picard MarkDuplicates -I input.bam -O output.bam -M metrics.txt"' >> /usr/local/bin/picard_info && \
    echo 'echo ""' >> /usr/local/bin/picard_info && \
    echo 'echo "Common tools:"' >> /usr/local/bin/picard_info && \
    echo 'echo "  MarkDuplicates      - Mark duplicate reads"' >> /usr/local/bin/picard_info && \
    echo 'echo "  SortSam             - Sort SAM/BAM files"' >> /usr/local/bin/picard_info && \
    echo 'echo "  ValidateSamFile     - Validate SAM/BAM files"' >> /usr/local/bin/picard_info && \
    echo 'echo "  CollectAlignmentSummaryMetrics - Alignment metrics"' >> /usr/local/bin/picard_info && \
    echo 'echo "  CreateSequenceDictionary - Create .dict file"' >> /usr/local/bin/picard_info && \
    chmod +x /usr/local/bin/picard_info

WORKDIR /data

# Verify installation (check jar is valid by listing tools)
RUN java -jar /opt/picard/picard.jar 2>&1 | grep -q "Available Programs" && echo "Picard verified successfully"

CMD ["picard_info"]
