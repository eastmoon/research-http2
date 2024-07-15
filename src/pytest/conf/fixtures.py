# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def second_entry():
    return 2

# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]
