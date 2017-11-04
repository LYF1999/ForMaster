FROM python:2.7
ENV PYTHONUNBUFFERED 1
VOLUME /ForMaster
WORKDIR /ForMaster
RUN pip install -r requirements.txt