import pytest
from reports.average_rating import AverageRatingReport


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
        {"name": "iphone 14", "brand": "apple", "price": "799", "rating": "4.7"},
    ]

def test_average_rating_report(sample_data):
    report = AverageRatingReport(sample_data)
    result = report.generate()

    assert result[0][0] == "apple"
    assert result[0][1] == pytest.approx(4.8, rel=1e-2)
    assert len(result) == 3

def test_empty_data():
    report = AverageRatingReport([])
    result = report.generate()
    assert result == []
