FROM python:alpine3.16
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY required.txt .
RUN pip install -r required.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]