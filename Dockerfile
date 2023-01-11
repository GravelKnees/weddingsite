FROM python:3.11
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]