from conftest import get_user_token


def test_user_login(client, db):
    response = client.post(
        "/api/v1/token",
        data={"username": "testuser", "password": "password123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_user_login_invalid_credentials(client, db):
    response = client.post(
        "/api/v1/token",
        data={"username": "wronguser", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

def test_access_protected_route_without_token(client, db):
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"



def test_create_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/v1/expenses/",
        json={"description": "Test Expense", "amount": 100.0, "date": "2024-01-01"},
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()["description"] == "Test Expense"
    assert response.json()["amount"] == 100.0

def test_create_expense_missing_fields(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/v1/expenses/",
        json={"amount": 100.0},
        headers=headers
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "description" in response.json()["detail"][0]["loc"]

def test_get_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    # Assuming there is an expense with ID 1
    response = client.get("/api/v1/expenses/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_nonexistent_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/v1/expenses/9999", headers=headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found"

def test_update_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.put(
        "/api/v1/expenses/1",
        json={"description": "Updated Expense", "amount": 200.0},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Expense"

def test_delete_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.delete("/api/v1/expenses/1", headers=headers)
    assert response.status_code == 204  # No Content

    # Verify that the expense no longer exists
    response = client.get("/api/v1/expenses/1", headers=headers)
    assert response.status_code == 404


def test_create_expense_invalid_amount(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/v1/expenses/",
        json={"description": "Invalid Amount", "amount": -50.0, "date": "2024-01-01"},
        headers=headers
    )
    assert response.status_code == 422  # Unprocessable Entity

def test_update_other_user_expense(client, db):
    token = get_user_token(client, "testuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    response = client.put(
        "/api/v1/expenses/2",
        json={"description": "Unauthorized Update", "amount": 500.0},
        headers=headers
    )
    assert response.status_code == 403  # Forbidden
    assert response.json()["detail"] == "Not enough permissions"

