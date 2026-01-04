FROM python:3.11-slim

# نحددو الدوسي داخل الكونتينر
WORKDIR /app

# ننسخو المتطلبات
COPY requirements.txt .

# نثبّتو الليبري
RUN pip install --no-cache-dir -r requirements.txt

# ننسخو الكود
COPY . .

# نحلّو البورت
EXPOSE 8000

# نشغّلو السيرفر
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
