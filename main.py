import sys
from extractor.reader import extract_lines_from_pdf
from extractor.detector import detect_table_blocks
from extractor.parser import parse_table_rows
from extractor.writer import write_to_excel

def main(pdf_path, output_excel_path):
    lines = extract_lines_from_pdf(pdf_path)

    table_blocks = detect_table_blocks(lines)

    if not table_blocks:
        print("No table blocks found.")
        return

    for idx, block in enumerate(table_blocks):
        print(f"\nTable {idx + 1} Detected:")
        for line in block:
            print(line)

    for i, block in enumerate(table_blocks):
        rows = parse_table_rows(block)
        write_to_excel(rows, output_excel_path, sheet_name=f"Table_{i+1}")

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python main.py <input_pdf_path> <output_excel_path>")
    #     sys.exit(1)
    main("sample.pdf", "output.xlsx")
