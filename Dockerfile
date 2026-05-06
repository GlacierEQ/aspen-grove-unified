FROM python:3.11-slim

WORKDIR /app

COPY aspen_setup.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "aspen_setup.py"]