FROM python:3.7
RUN mkdir /streaming-collector
WORKDIR /streaming-collector
COPY ./source .
RUN pip install -r /streaming-collector/requirements.txt
CMD ["python", "-u", "streaming-collector.py"]