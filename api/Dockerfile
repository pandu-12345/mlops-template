
FROM python:3.12 AS builder


WORKDIR /app

COPY ./api/requirements-api.txt .


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements-api.txt --target=/install


FROM python:3.12-slim

# Set the working directory.
WORKDIR /app

COPY --from=builder /install /usr/local/lib/python3.12/site-packages/
COPY --from=builder /install/bin /usr/local/bin/

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
