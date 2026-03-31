import pytest

@pytest.fixture
def sample_trade():
    return {'stock': 'ABC', 'price': 100.0, 'timestamp': '2026-03-15T09:30:00'}
