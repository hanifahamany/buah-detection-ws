# INFERENCE RANDOM PICK IMAGE 

import random
from pathlib import Path
import cv2
from ultralytics import YOLO


MODEL_PATH = Path("runs/detect/buah_model/weights/best.pt")
IMAGE_FOLDER = Path("dataset-buah/test/images")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def main():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"model isn't found: {MODEL_PATH}")

    if not IMAGE_FOLDER.is_dir():
        raise FileNotFoundError(f"image's folder isn't found: {IMAGE_FOLDER}")

    image_files = [
        path
        for path in IMAGE_FOLDER.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    ]
    if not image_files:
        raise FileNotFoundError(f"no image files found in: {IMAGE_FOLDER}")

    print("detecting...")
    image_path = random.choice(image_files)
    print(f"testing image: {image_path}")

    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"image couldn't be read: {image_path}")

    model = YOLO(str(MODEL_PATH))
    results = model.predict(source=image, conf=0.5, verbose=False)
    annotated_image = results[0].plot()

    cv2.imshow("Detected Fruit", annotated_image)
    cv2.waitKey(0)         
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()