
FROM python:3.9-slim
RUN pip install prometheus-flask-exporter
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]