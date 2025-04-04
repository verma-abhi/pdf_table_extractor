import re

def clean_line(line):
    return re.sub(r'\s+', ' ', line).strip()

def is_table_row(line):
    # Heuristic: A row starts with a date (dd/mm/yyyy or dd-mm-yyyy)
    return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}', line))
