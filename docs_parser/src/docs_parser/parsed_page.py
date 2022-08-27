from .lines_methods import *
import pdfplumber.page
from datetime import datetime
from typing import Dict, List, Tuple, Union


LOWEST_RECOGNIZABLE_YEAR = 2010


class ParsedPage:
    def __init__(self, pdf_page: pdfplumber.page.Page, relevant_report_titles: Tuple[str]):

        self._lines = get_pdf_page_lines(pdf_page)
        self._report_title = self._find_report_title(relevant_report_titles)
        self._page_is_relevant = self._report_title is not None
        if self._page_is_relevant:
            self._years = self._get_years()
            self._parse()

    def is_relevant(self):
        return self._page_is_relevant

    def get_report_title(self):
        return self._report_title

    def get_parsed_page(self):
        pass

    def _parse(self):
        pass

    def _find_report_title(self, relevant_report_titles) -> Union[str, None]:
        first_line = self._lines[1]
        for report_title in relevant_report_titles:
            if first_line.endswith(report_title):
                return report_title
        return None

    def _find_years_line_index(self) -> int:
        current_year = datetime.today().year
        for line_index, line in enumerate(self._lines):
            numbers_in_line = [int(char) for char in line.split() if char.isdigit()]
            if len(numbers_in_line) < 2:
                continue
            all_numbers_are_years = all([LOWEST_RECOGNIZABLE_YEAR <= num <= current_year for num in numbers_in_line])
            if all_numbers_are_years:
                return line_index
        raise Exception("couldn't find years line index")

    def _get_years(self) -> List[int]:
        years_line_index = self._find_years_line_index()
        years_line = self._lines[years_line_index]
        years_in_line = [int(char) for char in years_line.split() if char.isdigit()]
        years_in_line.sort()
        return years_in_line
