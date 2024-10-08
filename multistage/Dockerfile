# Stage 1: Builder
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

EXPOSE 5000

# Stage 2: Final image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy only the necessary parts from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

# Set the entrypoint for the application
ENTRYPOINT ["python", "app.py"]

