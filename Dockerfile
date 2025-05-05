FROM python:3.11-slim

# Install build tools and OpenMP
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend/ ./backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Build C extension
RUN cd backend && python -m setup build_ext --inplace

# Copy frontend files
COPY frontend/ ./frontend/

# Expose port
EXPOSE 5000

# Run Flask server
CMD ["python", "backend/server.py"]