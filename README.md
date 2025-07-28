# Adobe Hackathon - Round 1A

## Approach
We use PyMuPDF to extract text blocks and font sizes, assuming larger fonts represent headings.

## Requirements
- PyMuPDF
- pdfminer.six

## Run Docker
```bash
docker build --platform linux/amd64 -t adobe-round1a .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe-round1a
```
