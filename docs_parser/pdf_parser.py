import pdfplumber
from pdfplumber.pdf import PDF
import page_parser
from pathlib import Path
from typing import Dict, List, Tuple, Union


def _get_page_title_if_is_relevant_report(relevant_report_titles: Tuple[str], page_content_lines: List[str]) -> Union[str, None]:
    page_first_line = page_content_lines[1]
    for report_title in relevant_report_titles:
        if page_first_line.endswith(report_title):
            return report_title
    return None


def _detect_and_parse_relevant_pages(pdf: PDF, relevant_report_titles: Tuple[str], parsed_reports: dict):
    print(f"detecting relevant pages")
    for page_num, page in enumerate(pdf.pages):
        page_content_lines = page_parser.parse_to_lines(page)
        report_title = _get_page_title_if_is_relevant_report(relevant_report_titles, page_content_lines)

        if report_title is not None:
            parsed_reports[report_title].extend(page_content_lines)
            print(f"detected page {page_num + 1} for report {report_title}")


def _build_parsed_reports(pdf: PDF, relevant_report_titles: Tuple[str]) -> Dict[str, List[str]]:
    parsed_reports = {}
    for title in relevant_report_titles:
        parsed_reports[title] = []

    _detect_and_parse_relevant_pages(pdf, relevant_report_titles, parsed_reports)

    for report_title, content_lines in parsed_reports.items():
        print(f"detected {len(content_lines)} content lines for report {report_title}")

    return parsed_reports


def parse_pdf(file_path: str, relevant_report_titles: Tuple[str]) -> dict:
    file_name = Path(file_path).name
    print(f"Parsing {file_name}")
    with pdfplumber.open(file_path) as pdf:
        parsed_reports = _build_parsed_reports(pdf, relevant_report_titles)

        report = {
            "title": "some-title",  # get the title
            "date": "some-date"  # get the date
        }
        for page_lines in pages:
            page_lines = page_parser.remove_lines_without_numbers(page_lines)
            print(page_lines)
    print(f"Finished parsing {file_name}")
