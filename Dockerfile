FROM python:3.11
WORKDIR /app
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]