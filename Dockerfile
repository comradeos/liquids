FROM python:alpine3.16
WORKDIR /app
COPY required.txt .
RUN pip install -r required.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]