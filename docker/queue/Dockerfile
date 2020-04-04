FROM python:3.7-alpine
RUN mkdir /queue
WORKDIR /queue
COPY requirements.txt .
RUN pip install -r /queue/requirements.txt
COPY source .
EXPOSE 5000
CMD ["python", "tweet-queue.py"]