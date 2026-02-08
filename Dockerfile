FROM bitnami/python:3.13.5

WORKDIR /api_grafic

COPY . /api_grafic

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
