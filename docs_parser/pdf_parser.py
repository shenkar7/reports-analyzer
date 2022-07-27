import pdfplumber
from pdfplumber.pdf import PDF
import page_parser
from pathlib import Path
from typing import Dict, List


def _get_reports_pages(pdf: PDF, relevant_report_titles: List[str]) -> Dict[str, List[list]]:
    print(f"detecting relevant pages")
    reports_lines = {}

    for page_num, page in enumerate(pdf.pages):
        page_lines = page_parser.parse_to_lines(page)
        page_first_line = page_lines[1]

        for report_title in relevant_report_titles:
            if page_first_line.endswith(report_title):
                reports_lines[report_title] = page_lines
                print(f"detected page {page_num + 1} for report {report_title}")

    for report_title, pages in reports_lines.items():
        print(f"detected {len(pages)} pages for report {report_title}")
    return reports_lines


def parse_pdf(file_path: str, relevant_report_titles: List[str]) -> dict:
    file_name = Path(file_path).name
    print(f"Parsing {file_name}")
    with pdfplumber.open(file_path) as pdf:
        reports_pages = _get_reports_pages(pdf, relevant_report_titles)
        report = {
            "title": "some-title",  # get the title
            "date": "some-date"  # get the date
        }
        for page_lines in pages:
            page_lines = page_parser.remove_lines_without_numbers(page_lines)
            print(page_lines)
    print(f"Finished parsing {file_name}")
