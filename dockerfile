from python:3.11-slim

WORKDIR /GLADOS-TTS-MAIN
COPY  ./requirements.txt /GLADOS-TTS-MAIN/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /GLADOS-TTS-MAIN/requirements.txt
COPY . /GLADOS-TTS-MAIN
