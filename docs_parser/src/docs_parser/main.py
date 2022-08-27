import os
import json
import shutil
import pdf_parser
from typing import List


REPORT_TITLES = (
    'דספהו חוור תוחוד',
    'יפסכה בצמה לע תוחוד',
    'ללוכה חוורה לע תוחוד'
)

SOURCE_DIR = "docs_parser/pdf_src"
OUTPUT_DIR = "docs_parser/output"


def prepare_output_dir(output_dir):
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)


def get_pdf_files_paths(source_dir: str) -> List[str]:
    pdf_files_paths = []
    files = os.listdir(source_dir)
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(source_dir, file)
            pdf_files_paths.append(file_path)
    return pdf_files_paths


def write_outputs_to_jsons(outputs: List[dict], output_dir: str):
    for parsed_pdf in outputs:
        file_name = parsed_pdf["file_name"]
        json_file_path = os.path.join(output_dir, f"{file_name}.json")
        with open(json_file_path, "w") as fd:
            json.dump(parsed_pdf, fd)
            print(f"{file_name}.json was written")


def main():
    if not os.path.isdir(SOURCE_DIR):
        raise Exception('Directory pdf_src must exist to run this')

    prepare_output_dir(OUTPUT_DIR)
    pdf_files_paths = get_pdf_files_paths(SOURCE_DIR)

    outputs: List[dict] = []
    for file_path in pdf_files_paths:
        parsed_pdf = pdf_parser.parse_pdf(file_path, REPORT_TITLES)
        outputs.append(parsed_pdf)

    write_outputs_to_jsons(outputs, OUTPUT_DIR)


if __name__ == '__main__':
    main()
