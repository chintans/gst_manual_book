import os

# Use absolute paths or relative to the cwd of the command
source_path = r"e:\Github\chintans\gst_manual_book\chapters\chapter_1_content.md"
dest_path = r"e:\Github\chintans\gst_manual_book\src\content\docs\gst-manual\chapter-1.md"

frontmatter = """---
title: "Chapter 1: Genesis and Evolution of GST in India"
slug: gst-manual/genesis-and-evolution-of-gst-in-india
---

"""

print(f"Reading from: {source_path}")
with open(source_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
skip_next = False

for i, line in enumerate(lines):
    # Simple logic to filter out the AI commentary lines
    if "I'll now write" in line:
        # Also presumably the line before was '---' and maybe blank lines
        continue
    
    # We might want to remove the '---' that precedes the commentary to avoid double separators?
    # Checking context:
    # 333: ---
    # 335: I'll now write...
    # 337: ## Header
    
    # If I keep '---', it's just a horizontal rule. It's fine.
    
    output_lines.append(line)

print(f"Writing to: {dest_path}")
# Ensure directory exists
os.makedirs(os.path.dirname(dest_path), exist_ok=True)

with open(dest_path, "w", encoding="utf-8") as f:
    f.write(frontmatter)
    f.writelines(output_lines)

print(f"Successfully processed {len(lines)} source lines into {len(output_lines)} output lines.")
