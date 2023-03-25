import pytest
from ask_the_light import ask_light

@pytest.fixture
def topic_string():
    return "hate"

# Define a test function for the ask_light() function
def test_ask_light(topic_string):
    # Test case 1: check that the function returns a string
    result = ask_light(topic_string)
    assert isinstance(result, str)

    # Test case 2: check that the function does not return an empty string
    result = ask_light(topic_string)
    assert len(result) > 0

    # Test case 3: check that the function does not contain any newline characters
    result = ask_light(topic_string)
    assert '\n' not in result
