import pdfplumber

def extract_lines_from_pdf(pdf_path):
    lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                lines.extend(text.split("\n"))
            else:
                # Fallback to character-level extraction
                chars = page.chars
                chars.sort(key=lambda c: (round(c["top"]), c["x0"]))
                line_dict = {}
                for c in chars:
                    top = round(c["top"])
                    if top not in line_dict:
                        line_dict[top] = []
                    line_dict[top].append((c["x0"], c["text"]))

                for top in sorted(line_dict.keys()):
                    line = "".join([ch for _, ch in sorted(line_dict[top])])
                    lines.append(line)

    return lines
