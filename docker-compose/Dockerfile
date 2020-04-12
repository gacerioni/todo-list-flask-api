FROM python:3.7
RUN mkdir /app
RUN git clone https://github.com/gacerioni/todo-list-flask-api.git /app
WORKDIR /app
ENV ENV_FILE_LOCATION=./.env
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
