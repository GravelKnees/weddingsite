FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python3 create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]