def test_get_all_garments_no_records(client):
    # Act
    response = client.get("/garments")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_garment(client, two_saved_garments):
    # Act
    response = client.get("/garments/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Arabella Gown",
        "brand": "BHLDN",
        "size": 8,
        "color": "ivory",
        "condition": "Excellent used condition",
        "price": "800",
        "description": "A beautiful, flowy blush gown",
        "is_available": True
    }

def test_create_one_garment(client):
    # Act
    response = client.post("/garments", json={
        "title": "Solaine Gown",
        "brand": "Leanne Marshall",
        "size": 18,
        "color": "ivory",
        "condition": "Good used condition",
        "price": "600",
        "description": "A watercolor-inspired gown"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["title"] == "Solaine Gown"

def test_toggle_garment_availability(client, two_saved_garments):
    # Act
    response = client.patch("/garments/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200