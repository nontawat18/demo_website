
FROM python:3.7.7-slim
WORKDIR /app

COPY . /app


RUN pip freeze > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install  uvicorn==0.22.0 fastapi==0.103.2 SQLAlchemy==2.0.23 fastapi-login==1.8.2


EXPOSE 80

ENV NAME World

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
