import pytest
from docs_parser import lines_methods


def test_get_pdf_page_lines():
    pass


@pytest.mark.parametrize("line,expected", [("", False), (" ", True), ("     ", True), ("  f ", False), ("  f", False)])
def test_is_only_spaces_string(line, expected):
    assert lines_methods.is_only_spaces_string(line) == expected


def test_remove_commas():
    lines = [" sdf fsdf  34,5", " sdf ds,f", "sdfs df,ds ", "sdfsd fs,df sdfs,dfsd"]
    result = lines_methods.remove_commas(lines)
    assert result == [" sdf fsdf  345", " sdf dsf", "sdfs dfds ", "sdfsd fsdf sdfsdfsd"]


def test_remove_start_and_end_spaces():
    lines = [" sdf fsdf ", " sdf dsf", "sdfs dfds ", "sdfsd fsdf sdfsdfsd"]
    result = lines_methods.remove_start_and_end_spaces(lines)
    assert result == ["sdf fsdf", "sdf dsf", "sdfs dfds", "sdfsd fsdf sdfsdfsd"]


def test_remove_lines_without_numbers():
    lines = [
        'some words in the sentence',
        'another 12 in the text',
        '1 with more and more text',
        'and45more'
    ]

    expected = lines[1:]
    result = lines_methods.remove_lines_without_numbers(lines)
    assert result == expected

# def test_remove_spaces_at_start():
#     result = page_parser._remove_spaces_at_start('  abc')
#     assert result == 'abc'
#
#     result = page_parser._remove_spaces_at_start('abc')
#     assert result == 'abc'


# def test_detect_years_line_num():
#     lines = [
#         "first line 5928 985432 and more",
#         "line with years 2016 2017 2018 and more",
#         "some-other-line 2342"
#     ]
#     years_line_num = lines_methods.detect_years_line_num(lines)
#     assert years_line_num == 1


# def test_get_years():
#     lines = [
#         "first line",
#         "line with years 2016 2017 2018 and more",
#         "some-other-line"
#     ]
#     years_line_num = 1
#     years = lines_methods.get_years(lines, years_line_num)
#     assert years == [2016, 2017, 2018]
