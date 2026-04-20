from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Helper function to create a sample test result for testing
def create_sample():
    return client.post("/test-results", json={
        "test_name": "login_test",
        "status": "PASS",
        "execution_time": 1.2,
        "environment": "staging"
    })

# Test Cases for API Endpoints
def test_create_result():
    response = create_sample()
    assert response.status_code == 200
    assert response.json()["status"] == "PASS"

# Note: The following tests assume that the database is in a clean state before each test run.
def test_get_all_results():
    response = client.get("/test-results")
    assert response.status_code == 200

# Assuming at least one result exists from previous test
def test_get_by_id():
    create = create_sample()
    test_id = create.json()["id"]

    response = client.get(f"/test-results/{test_id}")
    assert response.status_code == 200
    assert response.json()["id"] == test_id

# Update the status of the created test result
def test_update_result():
    create = create_sample()
    test_id = create.json()["id"]

    response = client.put(f"/test-results/{test_id}", json={
        "status": "FAIL"
    })

    assert response.status_code == 200
    assert response.json()["status"] == "FAIL"

# Delete the created test result
def test_delete_result():
    create = create_sample()
    test_id = create.json()["id"]

    response = client.delete(f"/test-results/{test_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/test-results/{test_id}")
    assert response.status_code == 404