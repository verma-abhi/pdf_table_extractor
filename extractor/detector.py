import re

def detect_table_blocks(lines):
    blocks = []
    current_block = []

    for line in lines:
        if is_potential_table_line(line):
            current_block.append(line)
        elif current_block:
            if len(current_block) >= 2:  # discard accidental short blocks
                blocks.append(current_block)
            current_block = []

    if current_block and len(current_block) >= 2:
        blocks.append(current_block)

    return blocks


def is_potential_table_line(line):
    return bool(re.search(r'\d', line)) and len(line.strip().split()) >= 3
