import os
from pathlib import Path

from docling.document_converter import DocumentConverter

INPUT_DIR = Path("12 Docling pdf parsing/input_pdfs")
OUTPUT_DIR = Path("12 Docling pdf parsing/parsed_output")


def parse_pdfs():
    print("Starting PDF parsing...")
    converter = DocumentConverter()
    print("Docling converter created successfully")
    print(converter)

    OUTPUT_DIR.mkdir(exist_ok=True)
    print("Output directory created successfully")

    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    print(pdf_files)
    if not pdf_files:
        print("No PDF files found in input_pdfs/")
        return

    for pdf_path in pdf_files:
        print(f"Parsing: {pdf_path.name}")
        try:
            result = converter.convert(str(pdf_path))
            doc = result.document

            # Export to markdown (most common, readable choice)
            markdown_content = doc.export_to_markdown()

            output_path = OUTPUT_DIR / f"{pdf_path.stem}.md"
            output_path.write_text(markdown_content, encoding="utf-8")

            print(f"  -> Saved: {output_path}")

        except Exception as e:
            print(f"  !! Failed to parse {pdf_path.name}: {e}")


if __name__ == "__main__":
    parse_pdfs()
