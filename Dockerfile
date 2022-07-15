FROM python:alpine3.16
WORKDIR /app
COPY require.txt .
RUN pip install -r require.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]