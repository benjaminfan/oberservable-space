FROM python:3.9.1-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN ["chmod", "+x", "./run_service.sh"]
ENTRYPOINT ["./run_service.sh"]