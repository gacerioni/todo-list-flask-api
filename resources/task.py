from flask import Response, request
from database.models import Task, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, TaskAlreadyExistsError, InternalServerError, UpdatingTaskError, DeletingTaskError, TaskNotExistsError


class TasksApi(Resource):
    def get(self):
        query = Task.objects()
        tasks = Task.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            task = Task(**body, created_by=user)
            task.save()
            user.update(push__tasks=task)
            user.save()
            id = task.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise TaskAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class TaskApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            task = Task.objects.get(id=id, created_by=user_id)
            body = request.get_json()
            Task.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingTaskError
        except Exception:
            raise InternalServerError       
    
    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            task = Task.objects.get(id=id, added_by=user_id)
            task.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingTaskError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            task = Task.objects.get(id=id).to_json()
            return Response(task, mimetype="application/json", status=200)
        except DoesNotExist:
            raise TaskNotExistsError
        except Exception:
            raise InternalServerError
