import argparse
import cv2
import pytesseract
from pytesseract import Output


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image", required=True)
    args = p.parse_args()

    img = cv2.imread(args.image)
    if img is None:
        raise SystemExit(f"Could not read {args.image}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    data = pytesseract.image_to_data(gray, output_type=Output.DICT)
    words = []
    for i, word in enumerate(data["text"]):
        if word.strip() and float(data["conf"][i]) > 50:
            x, y, w, h = (data[k][i] for k in ("left", "top", "width", "height"))
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            words.append(word)
    print("Extracted text:\n" + " ".join(words))
    cv2.imshow("Text Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
