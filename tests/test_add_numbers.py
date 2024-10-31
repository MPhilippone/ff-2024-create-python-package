"""Test that our add numbers module behaves as expected"""
from src.MPTestPackage.add_number import add_num  

def test_add_number():  # Need a colon at the end
    """Test that the output of the add number function is correct"""
    result = add_num(1, 2)  # Call the function you want to test
    assert result == 3, f"Expected 3, but got {result}"  # Check if the result is as expected
