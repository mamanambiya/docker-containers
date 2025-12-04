# Development Guidelines for Claude

## Testing Docker Containers Locally

**IMPORTANT**: Always build and test Docker containers locally before pushing changes to GitHub.

### Why Build Locally First?

1. **Catch errors early** - Identify build failures before triggering GitHub Actions
2. **Save CI/CD resources** - Avoid unnecessary GitHub Actions runs
3. **Faster iteration** - Local builds are faster than waiting for GitHub Actions
4. **Test functionality** - Verify the container works as expected before deployment

### How to Build Locally

#### Single Container

From the project root directory:

```bash
# Build a specific container
docker build -t test-<container-name>:local ./containers/<container-name>

# Example: Build the vcf-processing container
docker build -t test-vcf-processing:local ./containers/vcf-processing
```

#### Test the Built Container

```bash
# Run the container to verify it works
docker run --rm test-vcf-processing:local

# For interactive testing
docker run --rm -it test-vcf-processing:local /bin/bash

# Test specific tools inside the container
docker run --rm test-vcf-processing:local bcftools --version
docker run --rm test-vcf-processing:local python3 --version
```

#### Common Build Issues to Check

1. **Syntax errors** in Dockerfile
2. **Download failures** for external dependencies
3. **Version conflicts** between packages
4. **Missing dependencies** for build or runtime
5. **Path issues** in installation steps
6. **Permission problems** with executables

### Workflow

1. **Make changes** to the Dockerfile
2. **Build locally** using the commands above
3. **Test the container** to verify functionality
4. **Fix any issues** that arise during build or testing
5. **Commit changes** only after successful local build
6. **Push to GitHub** to trigger automated builds and deployment

### Quick Reference

```bash
# Build
docker build -t test-<name>:local ./containers/<name>

# Test run
docker run --rm test-<name>:local

# Interactive shell
docker run --rm -it test-<name>:local /bin/bash

# Clean up test images
docker rmi test-<name>:local
```

## Git Push (Authenticated)

Use this command to push changes using GitHub CLI authentication:

```bash
TOKEN=$(gh auth token) && git push https://mamanambiya:${TOKEN}@github.com/mamanambiya/docker-containers.git main
```

## Additional Notes

- GitHub Actions will automatically build and push containers when changes are pushed to `main`
- Container tags follow the pattern: `ghcr.io/mamanambiya/docker-containers/<name>:latest`
- Always verify the GitHub Actions workflow succeeds after pushing changes
