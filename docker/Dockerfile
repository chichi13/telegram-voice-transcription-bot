FROM python:3.11.9-slim-bullseye
LABEL maintainer="chichi13"

RUN apt-get update -y && apt-get upgrade -y && apt install ffmpeg -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

# Copy only requirements/ for caching purpose
WORKDIR /app

COPY requirements/ requirements/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements/dev.txt

COPY . .

CMD ["python3", "main.py"]
