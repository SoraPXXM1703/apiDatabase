# app/Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# ติดตั้ง dependencies จาก requirements.txt (ควรตรวจสอบว่าไฟล์นี้มีการระบุ lib ทั้งหมดแล้ว)
RUN pip install --no-cache-dir -r requirements.txt

# ติดตั้ง Flask และ dependencies อื่นๆ ที่จำเป็น
RUN pip install --upgrade Flask==2.0.1 Werkzeug==2.0.2 flask_sqlalchemy uvicorn fastapi

# ตั้งค่า environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production  

# Expose the correct port (ในที่นี้ให้ Flask รันบนพอร์ต 8000)
EXPOSE 8000

# รัน Flask เมื่อ container เริ่มทำงาน
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
