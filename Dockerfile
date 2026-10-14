FROM python:3.12-slim

WORKDIR /app

COPY app/ ./app/

RUN python -m compileall -q app

EXPOSE 8080

CMD ["python", "-u", "app/main.py"]
