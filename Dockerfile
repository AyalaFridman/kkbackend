FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN python -m pip --version

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
