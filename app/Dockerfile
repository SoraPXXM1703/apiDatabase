# app/Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

#ENV LANG th_TH.UTF-8
#ENV LC_ALL th_TH.UTF-8

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask_sqlalchemy
RUN pip install --upgrade Werkzeug==2.0.2 Flask==2.0.1

# Make port 80 available to the world outside this container
EXPOSE 80


# Run app.py when the container launches
CMD ["python", "app.py"]