FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
