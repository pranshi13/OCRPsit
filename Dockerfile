FROM python:3.7
WORKDIR /app
COPY ./ /app
ENV UVICORN_WORKERS=1

RUN pip install -r requirements.txt

CMD uvicorn Service:app  --host 0.0.0.0 --workers $UVICORN_WORKERS
