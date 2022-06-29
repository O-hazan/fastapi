FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./app /app

CMD ["./start.sh"]


# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
