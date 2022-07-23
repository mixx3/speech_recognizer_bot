FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
CMD ["python3", "main.py"]



