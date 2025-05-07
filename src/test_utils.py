import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize("number, expected", [    (0, "0b0"),(1, "0b1"),(2, "0b10"),(100, "0b1100100")])
def test_convert_to_binary(number, expected):
    assert utils.convert_to_binary(number) == expected

@pytest.mark.parametrize("number", [-1, 101, 1000])
def test_convert_to_binary_out_of_range(number):
    with pytest.raises(ValueError, match="Number must be between 0 and 100."):
        utils.convert_to_binary(number)

    
@pytest.mark.parametrize("number", [1.5, 0.1, 99.9])
def test_convert_to_binary_not_integer(number):
    with pytest.raises(TypeError, match="Number must be an integer."):
        utils.convert_to_binary(number)