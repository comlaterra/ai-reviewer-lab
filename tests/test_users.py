"""
Basic tests for user endpoints.

Run with: python -m pytest tests/ -v
"""

import unittest

from src.app import create_app


class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_register_success(self):
        response = self.client.post("/user", json={
            "username": "newuser",
            "email": "new@example.com",
            "password": "securePass123!",
        })
        self.assertEqual(response.status_code, 201)

    def test_register_missing_username(self):
        response = self.client.post("/user", json={
            "email": "test@example.com",
            "password": "pass123",
        })
        self.assertEqual(response.status_code, 400)

    def test_register_missing_email(self):
        response = self.client.post("/user", json={
            "username": "testuser",
            "password": "pass123",
        })
        self.assertEqual(response.status_code, 400)

    def test_register_invalid_email(self):
        response = self.client.post("/user", json={
            "username": "testuser",
            "email": "not-an-email",
            "password": "pass123",
        })
        self.assertEqual(response.status_code, 400)

    def test_register_invalid_username(self):
        response = self.client.post("/user", json={
            "username": "ab",
            "email": "valid@example.com",
            "password": "pass123",
        })
        self.assertEqual(response.status_code, 400)

    def test_register_empty_body(self):
        response = self.client.post("/user", content_type="application/json")
        self.assertEqual(response.status_code, 400)


class TestUserLookup(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_get_user_requires_auth(self):
        response = self.client.get("/user/1")
        self.assertEqual(response.status_code, 401)

    def test_get_user_invalid_token(self):
        response = self.client.get(
            "/user/1",
            headers={"Authorization": "Bearer invalidtoken"},
        )
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
