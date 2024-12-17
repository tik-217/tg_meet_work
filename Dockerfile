FROM python:3.9.6

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "view/main.py"]