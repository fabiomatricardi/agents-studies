import argparse
import pymupdf4llm
from pathlib import Path
import sys

def convert_pdf_to_md():
    # 1. Setup Argparse
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to Markdown using PyMuPDF4LLM."
    )
    
    # Positional argument for the input file
    parser.add_argument(
        "filename", 
        help="Path to the source PDF file."
    )
    
    # Optional argument for the output directory
    parser.add_argument(
        "-o", "--output-dir", 
        help="Directory to save the markdown file. Defaults to the same directory as the PDF.",
        default=None
    )

    args = parser.parse_args()

    # 2. Handle File Paths
    input_path = Path(args.filename)
    
    if not input_path.exists():
        print(f"Error: The file '{args.filename}' does not exist.")
        sys.exit(1)

    # Determine output directory
    out_dir = Path(args.output_dir) if args.output_dir else input_path.parent
    
    # Ensure output directory exists
    out_dir.mkdir(parents=True, exist_ok=True)

    # Create output filename (same name, .md extension)
    output_path = out_dir / f"{input_path.stem}.md"

    # 3. Extraction Logic
    try:
        print(f"Converting '{input_path.name}'...")
        
        md_text = pymupdf4llm.to_markdown(
            str(input_path), 
            header=False, 
            footer=False, 
            use_ocr=False
        )

        # 4. Save the Result
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_text)
        
        print(f"Success! Markdown saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    convert_pdf_to_md()