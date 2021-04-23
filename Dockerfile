from python:3.8

WORKDIR /app
RUN pip install fastapi uvicorn
RUN pip install sqlalchemy psycopg2
RUN pip install pytest-asyncio httpx requests
RUN pip3 freeze >> requirements.txt

EXPOSE 80

COPY /src /app

CMD ["uvicorn", "app:app", "--reload" , "--host", "0.0.0.0", "--port", "2602"]