FROM apache/airflow:2.9.0-python3.9

USER root
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
USER airflow

COPY requirements.txt .

ARG AIRFLOW_VERSION=2.9.0
ARG PYTHON_VERSION=3.9
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

RUN pip install --no-cache-dir -r requirements.txt -c "${CONSTRAINT_URL}"

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/src"
