import pdfplumber
from typing import List
from datetime import datetime


def parse_to_lines(page: pdfplumber.page.Page) -> List[str]:
    text = page.extract_text()
    lines = _get_lines(text)
    lines = _remove_start_and_end_spaces(lines)
    years_line_num = _detect_years_line_num(lines)
    years = _get_years(lines, years_line_num)
    lines = lines[years_line_num + 1:]
    return lines


def _detect_years_line_num(lines: List[str]) -> int:
    upper_year = datetime.today().year
    lower_year = 2010
    for line_num, line in enumerate(lines):
        line_numbers = [int(c) for c in line.split() if c.isdigit()]
        if len(line_numbers) < 2:
            continue
        if all([lower_year <= num <= upper_year for num in line_numbers]):
            return line_num
    raise Exception("couldn't detect years")


def _get_years(lines: List[str], years_line_num: int) -> List[int]:
    years_line = lines[years_line_num]
    years = [int(c) for c in years_line.split() if c.isdigit()]
    years.sort()
    return years


def _get_lines(text: str) -> List[str]:
    lines = text.split('\n')
    lines = [line for line in lines if not _is_only_spaces_string(line)]
    lines = _remove_commas(lines)
    return lines


def _is_only_spaces_string(text: str) -> bool:
    for char in text:
        if char != ' ':
            return False
    return True


def _remove_commas(lines: List[str]) -> List[str]:
    edited_lines = []
    for line in lines:
        line = line.replace(",", "")
        edited_lines.append(line)
    return edited_lines


def _remove_start_and_end_spaces(lines: List[str]) -> List[str]:
    edited_lines = []
    for line in lines:
        if line[0] == " ":
            while line[0] == " ":
                line = line[1:]
        if line[-1] == " ":
            while line[-1] == " ":
                line = line[:-1]
        edited_lines.append(line)
    return edited_lines


def remove_lines_without_numbers(lines: str) -> list:
    edited_lines = []
    for line in lines:
        if any(char.isdigit() for char in line):
            edited_lines.append(line)
    return edited_lines
