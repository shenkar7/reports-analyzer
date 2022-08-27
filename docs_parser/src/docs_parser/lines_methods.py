from typing import List
import pdfplumber.page


def get_pdf_page_lines(pdf_page: pdfplumber.page.Page) -> List[str]:
    text = pdf_page.extract_text()
    lines = text.split('\n')
    lines = [line for line in lines if not is_only_spaces_string(line)]
    lines = remove_commas(lines)
    lines = remove_start_and_end_spaces(lines)
    # years_line_index = _detect_years_line_num(lines)
    # lines = lines[years_line_num + 1:]
    return lines


def is_only_spaces_string(text: str) -> bool:
    if len(text) == 0:
        return False
    for char in text:
        if char != ' ':
            return False
    return True


def remove_commas(lines: List[str]) -> List[str]:
    edited_lines = []
    for line in lines:
        line = line.replace(",", "")
        edited_lines.append(line)
    return edited_lines


def remove_start_and_end_spaces(lines: List[str]) -> List[str]:
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
