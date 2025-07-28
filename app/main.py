import os
import json
import fitz  # PyMuPDF

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = doc.metadata.get("title", "Untitled Document")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join(span["text"] for span in line["spans"])
                    size = line["spans"][0]["size"]

                    if size > 20:
                        outline.append({"level": "H1", "text": text, "page": page_num + 1})
                    elif size > 16:
                        outline.append({"level": "H2", "text": text, "page": page_num + 1})
                    elif size > 14:
                        outline.append({"level": "H3", "text": text, "page": page_num + 1})

    return {"title": title, "outline": outline}

if __name__ == "__main__":
    input_folder = "/app/input"
    output_folder = "/app/output"

    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file)
            result = extract_outline(pdf_path)

            output_path = os.path.join(output_folder, file.replace(".pdf", ".json"))
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)
