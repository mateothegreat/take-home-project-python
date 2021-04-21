from python:3.8-alpine

WORKDIR /app

RUN pip install fastapi uvicorn

EXPOSE 80

COPY /src /app

CMD ["uvicorn", "app:app", "--reload" , "--host", "0.0.0.0", "--port", "80"]