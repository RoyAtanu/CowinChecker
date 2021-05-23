FROM python:3.8-slim

COPY ./*.py ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-u", "./runcowinchecker.py" ]