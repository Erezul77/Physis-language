# Use Python 3.10 as base
FROM python:3.10

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run the app
CMD ["python", "app.py"]
