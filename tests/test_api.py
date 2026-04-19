from api.api_client import get_users, create_user

def test_get_users():
    response = get_users()

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_create_user():
    response = create_user("Srishti", "Engineer")

    # JSONPlaceholder returns 201 but doesn’t actually create
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Srishti"