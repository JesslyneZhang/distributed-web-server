# Menggunakan Python 3.12 yang mendukung ARM64 dan AMD64
FROM python:3.12-slim

# Mengatur direktori kerja
WORKDIR /app

# Mengatur environment Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Menyalin dan menginstal dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh kode backend
COPY . .

# Port aplikasi Flask
EXPOSE 5000

# Menjalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]