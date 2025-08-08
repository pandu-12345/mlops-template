FROM python:3.10

WORKDIR /app

COPY home.py .

RUN pip install streamlit mlflow requests pillow


EXPOSE 8501

CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
