from python:3.10-bullseye

RUN pip install requests

WORKDIR /app

COPY py .

ENV SERVER=0.0.0.0
ENV PORT=8080

CMD ["python", "client.py"]
