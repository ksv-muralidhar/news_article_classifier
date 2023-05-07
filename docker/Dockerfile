FROM python:3.7-slim
WORKDIR /webapp
COPY . .
RUN rm -r ./docker
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "gunicorn", "app:app",  "--timeout", "120", "--workers=3", "--threads=3", "--worker-connections=1000"]
EXPOSE 5002
