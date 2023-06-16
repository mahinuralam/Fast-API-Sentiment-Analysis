FROM python:3.9

WORKDIR /Fast-API-Sentiment-Analysis

COPY ./requirements.txt /Fast-API-Sentiment-Analysis

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /Fast-API-Sentiment-Analysis

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
