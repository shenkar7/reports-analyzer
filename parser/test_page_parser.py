import pytest
import page_parser


# def test_remove_spaces_at_start():
#     result = page_parser._remove_spaces_at_start('  abc')
#     assert result == 'abc'
#
#     result = page_parser._remove_spaces_at_start('abc')
#     assert result == 'abc'


@pytest.mark.parametrize("line,expected", [(" ", True), ("     ", True), ("  f ", False), ("  f", False)])
def test_is_space_string(line, expected):
    page_parser._is_space_string(line) == expected


def test_remove_commas():
    lines = [" sdf fsdf  34,5", " sdf ds,f", "sdfs df,ds ", "sdfsd fs,df sdfs,dfsd"]
    result = page_parser._remove_commas(lines)
    assert result == [" sdf fsdf  345", " sdf dsf", "sdfs dfds ", "sdfsd fsdf sdfsdfsd"]


def test_remove_start_and_end_spaces():
    lines = [" sdf fsdf ", " sdf dsf", "sdfs dfds ", "sdfsd fsdf sdfsdfsd"]
    result = page_parser._remove_start_and_end_spaces(lines)
    assert result == ["sdf fsdf", "sdf dsf", "sdfs dfds", "sdfsd fsdf sdfsdfsd"]
