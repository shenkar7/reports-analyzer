import os
import pdfplumber
import page_parser

PDF_SOURCE_DIR = 'pdf_src'
REPORT_TITLES = ('דספהו חוור תוחוד', 'יפסכה בצמה לע תוחוד', 'ללוכה חוורה לע תוחוד')


def get_pdf_files_names():
    pdf_files = []
    files = os.listdir(PDF_SOURCE_DIR)
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(PDF_SOURCE_DIR, file)
            pdf_files.append(file_path)
    return pdf_files


def detect_reports_pages(pdf):
    print(f"detecting relevant pages")
    report_pages = []
    for index, page in enumerate(pdf.pages):
        page_lines = page_parser.parse_to_lines(page)
        if any(page_lines[1].endswith(title) for title in REPORT_TITLES):
            report_pages.append(page_lines)
            print(f"page {index + 1} was added")
    print(f"total of {len(report_pages)} pages were detected")
    return report_pages


def main():
    if not os.path.isdir(PDF_SOURCE_DIR):
        raise Exception('Directory pdf_src must exist to run this')

    pdf_files_paths = get_pdf_files_names()

    for file_path in pdf_files_paths:
        with pdfplumber.open(file_path) as pdf:
            pages = detect_reports_pages(pdf)
            report = {
                "title": "some-title", # get the title
                "date": "some-date" # get the date
            }
            for page_lines in pages:
                page_lines = page_parser.remove_lines_without_numbers(page_lines)
                breakpoint()
                # print(parsed_text)


        # load file

        # detect relevant pages and save them only

        # create a report class with name, years and fields. Each field has a value for each year and "beur".
        #     the class can also export a dict with the data.

        # create a parser that fills the class data (a report can be multiple pages in the PDF)

        # export a json list of reports

        # return a list of reports

if __name__ == '__main__':
    main()
