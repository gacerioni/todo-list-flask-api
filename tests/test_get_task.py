import unittest
import json

from tests.BaseCase import BaseCase


class TestGetMovies(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/movies')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_movie_response(self):
        # Given
        email = "gacerioni@gmail.com"
        password = "mycoolpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        task_payload = {
            "title": "Give Bart the Shiba a bath",
            "tags": ["Personal", "Bart", "Hygiene"],
            "status": "IN PROGRESS"
        }
        response = self.app.post('/api/todo-list',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(task_payload))

        # When
        response = self.app.get('/api/todo-list')
        added_task = response.json[0]

        # Then
        self.assertEqual(task_payload['title'], added_task['title'])
        self.assertEqual(task_payload['tags'], added_task['tags'])
        self.assertEqual(task_payload['status'], added_task['status'])
        self.assertEqual(user_id, added_task['created_by']['$oid'])
        self.assertEqual(200, response.status_code)
