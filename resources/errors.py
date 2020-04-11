class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class TaskAlreadyExistsError(Exception):
    pass


class UpdatingTaskError(Exception):
    pass


class DeletingTaskError(Exception):
    pass


class TaskNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class EmailDoesnotExistsError(Exception):
    pass


class BadTokenError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "TaskAlreadyExistsError": {
        "message": "The Task already exists!",
        "status": 400
    },
    "UpdatingTaskError": {
        "message": "Updating a task added by other is forbidden",
        "status": 403
    },
    "DeletingTaskError": {
        "message": "Deleting a task added by other is forbidden",
        "status": 403
    },
    "TaskNotExistsError": {
        "message": "A task with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 403
    }
}
