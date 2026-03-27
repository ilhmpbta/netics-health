# Gunakan base image python yang ringan
FROM python:3.9-slim
WORKDIR /app
COPY app/ .
RUN pip install --no-cache-dir flask
EXPOSE 6767
CMD ["python", "app.py"]