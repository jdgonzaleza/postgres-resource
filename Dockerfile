FROM python:3.9.5-buster

RUN RUN pip install psycopg2-binary

COPY assets/check.py /opt/resource/check
COPY assets/in.py /opt/resource/in
COPY assets/out.py /opt/resource/out
COPY assets/common.py /opt/resource/common.py