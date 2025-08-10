
FROM python:3.12 AS builder


WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt --target=/install


FROM python:3.12-slim


WORKDIR /app


COPY --from=builder /install /usr/local/lib/python3.12/site-packages/


COPY ./api/ .

EXPOSE 8000

CMD ["python", "app.py"]