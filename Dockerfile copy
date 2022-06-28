FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# RUN pip install python-multipart

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./app /app

CMD ["./start.sh"]





# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
