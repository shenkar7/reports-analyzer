import pdfplumber
from pdfplumber.pdf import PDF
import parsed_page
from pathlib import Path
from typing import Dict, List, Tuple, Union


def _create_empty_parsed_reports_dict(relevant_report_titles: Tuple[str]):
    parsed_reports = {}
    for title in relevant_report_titles:
        parsed_reports[title] = []
    return parsed_reports


def _build_parsed_reports(pdf: PDF, relevant_report_titles: Tuple[str]) -> Dict[str, List[str]]:
    parsed_reports = _create_empty_parsed_reports_dict(relevant_report_titles)

    print(f"detecting relevant pages")
    for page_index, pdf_page in enumerate(pdf.pages):
        page = parsed_page.ParsedPage(pdf_page, relevant_report_titles)
        if not page.is_relevant():
            continue

        page_report_title = page.get_report_title()
        # create and use here a function that will append to parsed_reports[page_report_title] the parsed content of the page
        page_num_in_pdf = page_index + 1
        print(f"detected page {page_num_in_pdf} for report {page_report_title}")

    return parsed_reports


def _print_parsed_report_summary(parsed_reports: dict):
    for report_title, content_lines in parsed_reports.items():
        print(f"detected {len(content_lines)} content lines for report {report_title}")


def parse_pdf(file_path: str, relevant_report_titles: Tuple[str]) -> dict:
    file_name = Path(file_path).name
    print(f"Parsing {file_name}")
    with pdfplumber.open(file_path) as pdf:
        parsed_reports = _build_parsed_reports(pdf, relevant_report_titles)
        _print_parsed_report_summary(parsed_reports)

    parsed_pdf = {
        # "title": "some-title",  # get the title
        # "date": "some-date",  # get the date
        "file_name": file_name,
        "reports": parsed_reports
    }
    #
    # for page_lines in pages:
    #     page_lines = page_parser.remove_lines_without_numbers(page_lines)
    #     print(page_lines)
    print(f"Finished parsing {file_name}")
    return parsed_pdf
