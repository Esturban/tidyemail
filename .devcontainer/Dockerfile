# Stage 1: Builder
FROM python:3.13-alpine AS builder

# Install build dependencies
RUN apk add --no-cache git build-base

# Set the working directory
WORKDIR /workspace


# Install Python dependencies (if any)
COPY . .

# Stage 2: Final
FROM python:3.13-alpine

# Install runtime dependencies
RUN apk add --no-cache git

# Set the working directory
WORKDIR /workspace
RUN pip install --no-cache-dir python-dotenv
# Copy only the necessary files from the builder stage
COPY --from=builder /workspace /workspace
EXPOSE $PORT
# Ensure the entrypoint is set to bash for interactive use
ENTRYPOINT ["/bin/sh"]