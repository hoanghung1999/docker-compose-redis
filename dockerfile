FROM python:3.4-alpine
ADD . /codeserver
WORKDIR /codeserver
RUN pip install -r requirements.txt
CMD ["python", "server.py"]