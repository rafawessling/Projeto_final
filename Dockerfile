FROM python:3.10.5-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "source.main:app", "--host", "0.0.0.0", "--port", "$PORT"]