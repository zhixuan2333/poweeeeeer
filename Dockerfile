FROM python:3.9-slim

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Set the working directory
WORKDIR /app

COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x poweeeeer.py

WORKDIR /mnt/data

ENTRYPOINT [ "/app/poweeeeer.py" ]
CMD [ "--help" ]
