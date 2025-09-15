# Minimal CrossMap container - just get it working
FROM python:3.11-slim

LABEL maintainer="AfriGen-D Consortium"
LABEL version="0.7.3"
LABEL org.opencontainers.image.description="CrossMap v0.7.3 coordinate conversion tool for genomics."

# Install CrossMap
RUN pip install --no-cache-dir CrossMap==0.7.3

# Create working directory
WORKDIR /data

# Test that it works
RUN python -c "import CrossMap; print('CrossMap ready')"

# Set default command - use python module directly
CMD ["python", "-m", "CrossMap", "--help"]
