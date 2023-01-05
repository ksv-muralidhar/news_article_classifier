FROM python:3.7-slim
WORKDIR /webapp
COPY . .
RUN rm -r ./docker
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "gunicorn", "app:app"]
EXPOSE 5002