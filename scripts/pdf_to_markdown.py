#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files (3.2.4 to 3.2.12) to Markdown format
"""

import os
import re
import fitz  # pymupdf

def is_in_range(filename):
    """
    すべてのPDFファイルを許可するように変更
    """
    return filename.endswith('.pdf')

#    """
#    Check if the PDF file is in the range 3.2.1 to 3.2.12
#    Examples: 3.2.1, 3.2.4, 3.2.5, 3.2.10.1, 3.2.11, etc.
#    """
#    # Extract version number from filename (e.g., "3.2.4" or "3.2.10.1")
#    match = re.match(r'^(3\.2\.(\d+)(?:\.\d+)*)\s', filename)
#    if not match:
#        return False

#    # Get the main version number (e.g., 4 from 3.2.4, or 10 from 3.2.10.1)
#    main_version = int(match.group(2))

#    # Check if it's in range 3.2.1 to 3.2.12
#    return 1 <= main_version <= 12


def convert_pdf_to_markdown(pdf_path, md_path):
    """
    Convert a PDF file to Markdown format
    """
    try:
        # Open PDF
        doc = fitz.open(pdf_path)

        # Extract text from all pages
        markdown_content = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()

            # Add page separator
            if page_num > 0:
                markdown_content.append(f"\n---\n\n**Page {page_num + 1}**\n\n")
            else:
                markdown_content.append(f"**Page {page_num + 1}**\n\n")

            markdown_content.append(text)

        doc.close()

        # Write to markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))

        return True

    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        return False

def main():
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create md folder if it doesn't exist
    md_folder = os.path.join(current_dir, 'md')
    os.makedirs(md_folder, exist_ok=True)

    # Get all PDF files in current directory
    pdf_files = [f for f in os.listdir(current_dir) if f.endswith('.pdf')]

    # Filter files in range 3.2.4 to 3.2.12
    target_files = [f for f in pdf_files if is_in_range(f)]

    # Sort files
    target_files.sort()

    print(f"Found {len(target_files)} PDF files to convert:")
    for f in target_files:
        print(f"  - {f}")
    print()

    # Convert each file
    success_count = 0
    for pdf_file in target_files:
        # Create paths
        pdf_path = os.path.join(current_dir, pdf_file)
        md_filename = pdf_file.replace('.pdf', '.md')
        md_path = os.path.join(md_folder, md_filename)

        print(f"Converting: {pdf_file} -> md/{md_filename}")

        if convert_pdf_to_markdown(pdf_path, md_path):
            success_count += 1
            print(f"  [OK] Success")
        else:
            print(f"  [ERROR] Failed")

    print(f"\nConversion complete: {success_count}/{len(target_files)} files successfully converted")

if __name__ == '__main__':
    main()
