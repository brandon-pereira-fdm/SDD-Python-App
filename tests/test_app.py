from app import app 
 
 
def test_home_page_returns_success(): 
    client = app.test_client() 
    response = client.get("/") 
 
    assert response.status_code == 200 
 
 
def test_home_page_contains_sdd_content(): 
    client = app.test_client() 
    response = client.get("/") 
    page_text = response.data.decode("utf-8") 
 
    assert "Spec-Driven Development" in page_text 
    assert "Clear Requirements" in page_text 
    assert "Less Rework" in page_text 
    assert "Better Testing" in page_text 
    assert "Traceable Delivery" in page_text 