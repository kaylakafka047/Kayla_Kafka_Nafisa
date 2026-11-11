import pytest
from employee import Employee


@pytest.fixture
def employee():
    """Create an employee for use in the tests."""
    return Employee("John", "Doe", 50000)


def test_give_default_raise(employee):
    """Test that the default raise is added correctly."""

    employee.give_raise()

    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """Test that a custom raise is added correctly."""

    employee.give_raise(10000)

    assert employee.annual_salary == 60000