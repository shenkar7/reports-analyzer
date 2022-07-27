import pdfplumber
from typing import List


def parse_to_lines(page: pdfplumber.page.Page) -> List[str]:
    text = page.extract_text()
    lines = _get_lines(text)
    lines = _remove_start_and_end_spaces(lines)
    return lines


def _get_lines(text: str) -> List[str]:
    lines = text.split('\n')
    lines = [line for line in lines if not _is_space_string(line)]
    lines = _remove_commas(lines)
    return lines


def _is_space_string(text: str) -> bool:
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
