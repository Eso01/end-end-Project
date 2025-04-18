FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY src/main.py .

EXPOSE 5000

# Production command (using Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
