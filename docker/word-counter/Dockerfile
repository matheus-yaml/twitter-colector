FROM python:3.7
RUN mkdir /counter
WORKDIR /counter
COPY requirements.txt .
RUN pip install -r /counter/requirements.txt
COPY source .
EXPOSE 8080
CMD ["python", "counter.py"]