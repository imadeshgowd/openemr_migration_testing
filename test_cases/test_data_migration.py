import pytest
from utils.data_utils import validate_data_migration

def test_data_migration():
    assert validate_data_migration() is True