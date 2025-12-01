FROM python:3.9-slim

WORKDIR /app
COPY libs.txt .
RUN pip install --no-cache-dir -r libs.txt
COPY . .

CMD ["python", "app.py"]