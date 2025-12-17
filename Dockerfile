# Use a lightweight alpine version of python 3.12.
FROM python:3.12-alpine

# The app will be at /app inside the container.
WORKDIR /app

# Copy source code and requirements.
COPY src src
COPY requirements.txt requirements.txt

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8123 that the app will use.
# This doesn't do anything really, it just serves as documentation.
EXPOSE 8123

# We need to bind to 0.0.0.0 to be accessible from outside the container.
# CMD will be the default command when the container starts.
CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8123"]
