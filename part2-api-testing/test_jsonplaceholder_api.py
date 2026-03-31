"""
Part 2: API Testing - JSONPlaceholder API Tests

Automated tests for the JSONPlaceholder REST API (https://jsonplaceholder.typicode.com/)
demonstrating basic QA automation skills including GET requests, POST requests,
and error handling for non-existent resources.

Test Framework: pytest
HTTP Client: requests
"""

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJSONPlaceholderAPI:
      """Test suite for JSONPlaceholder REST API."""

    # ---------- Test 1: GET request - Fetch a user ----------
      def test_fetch_user_successfully(self):
                """
                        Validates that GET /users/1 returns a 200 status code
                                and the response contains the required fields: id, name, email.
                                        """
                response = requests.get(f"{BASE_URL}/users/1")

          # Validate status code is 200 OK
                assert response.status_code == 200, (
                    f"Expected status 200, got {response.status_code}"
                )

          user = response.json()

        # Validate required fields exist in the response
        assert "id" in user, "Response missing 'id' field"
        assert "name" in user, "Response missing 'name' field"
        assert "email" in user, "Response missing 'email' field"

        # Validate the correct user was returned
        assert user["id"] == 1, f"Expected user id 1, got {user['id']}"

        # Validate field types
        assert isinstance(user["id"], int), "Field 'id' should be an integer"
        assert isinstance(user["name"], str), "Field 'name' should be a string"
        assert isinstance(user["email"], str), "Field 'email' should be a string"

        # Validate fields are not empty
        assert len(user["name"]) > 0, "Field 'name' should not be empty"
        assert len(user["email"]) > 0, "Field 'email' should not be empty"

    # ---------- Test 2: POST request - Create a new post ----------
    def test_create_new_post(self):
              """
                      Validates that POST /posts correctly creates a new post.
                              Sends JSON data and verifies the response matches the submitted data.
                                      """
              new_post = {
                  "title": "QA Automation Test Post",
                  "body": "This is a test post created during the API testing assessment.",
                  "userId": 1
              }

        response = requests.post(
                      f"{BASE_URL}/posts",
                      json=new_post,
                      headers={"Content-Type": "application/json"}
        )

        # Validate status code is 201 Created
        assert response.status_code == 201, (
                      f"Expected status 201, got {response.status_code}"
        )

        created_post = response.json()

        # Validate the response contains an id (assigned by the server)
        assert "id" in created_post, "Response missing 'id' field"

        # Validate the submitted data is reflected in the response
        assert created_post["title"] == new_post["title"], (
                      "Response 'title' does not match submitted data"
        )
        assert created_post["body"] == new_post["body"], (
                      "Response 'body' does not match submitted data"
        )
        assert created_post["userId"] == new_post["userId"], (
                      "Response 'userId' does not match submitted data"
        )

    # ---------- Test 3: Error handling - Non-existent resource ----------
    def test_handle_nonexistent_user(self):
              """
                      Validates that GET /users/999 returns a 404 status code
                              for a non-existent resource and returns an appropriate response.
                                      """
              response = requests.get(f"{BASE_URL}/users/999")

        # Validate status code is 404 Not Found
              assert response.status_code == 404, (
                  f"Expected status 404, got {response.status_code}"
              )

        # Validate the response body is an empty object (JSONPlaceholder returns {})
              response_body = response.json()
        assert response_body == {}, (
                      f"Expected empty object for non-existent user, got {response_body}"
        )
