import re

def parse_table_rows(lines):
    rows = []
    header_row_found = False

    for line in lines:
        columns = re.split(r'\s{2,}|\t+', line.strip())

        # First non-numeric row with 3+ columns -> header
        if not header_row_found and len(columns) >= 3 and not all(is_number(c) for c in columns):
            rows.append(columns)
            header_row_found = True
        elif header_row_found:
            if len(columns) >= 2:
                rows.append(columns)
            else:
                # Handle broken rows or descriptions
                if rows:
                    rows[-1][-1] += " " + line.strip()
        else:
            continue

    return rows


def is_number(s):
    try:
        float(s.replace(',', ''))
        return True
    except:
        return False
