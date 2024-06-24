import pytest

@pytest.fixture
def visa_platinum_card():
    return 'Visa Platinum 7000 7922 8960 6361'

@pytest.fixture
def maestro_card():
    return 'Maestro 1596 8378 6870 5199'

@pytest.fixture
def master_card():
    return 'MasterCard 7158 3007 3472 6758'

@pytest.fixture
def visa_classic_card():
    return 'Visa Classic 6831 9824 7673 7658'

@pytest.fixture
def mask_visa_classic_card():
    return 'Visa Classic 6831 98** **** 7658'