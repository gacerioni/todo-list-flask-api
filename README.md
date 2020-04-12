# todo-list-flask-api


export ENV_FILE_LOCATION=./.env

docker build --no-cache -t gacerioni/todo-list:latest .

docker-compose -f todo-list-stack.yml up
