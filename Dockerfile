FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "library_system.py"]