FROM ubuntu:20.04
RUN apt update -y && apt upgrade -y
RUN apt install python3 -y
RUN apt install pip -y
COPY requirements.txt requirements.txt
COPY app.py app.py
CMD ["python3","app.py"]

