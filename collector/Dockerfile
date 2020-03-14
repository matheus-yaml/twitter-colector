FROM python:3.7
RUN mkdir /collector
WORKDIR /collector
COPY ./source .
RUN pip install -r /collector/requirements.txt
CMD ["python", "simple-collector.py"]