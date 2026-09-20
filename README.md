# Text Detection & Extraction (OCR)

Preprocesses an image, extracts text with Tesseract and draws a box around every detected word.

Part of a series of beginner-friendly OpenCV projects.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
brew install tesseract
python main.py --image document.png
```

Press `q` to quit any live window.

## License

MIT
