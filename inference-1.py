# INFERENCE MANUAL PATH IMAGE

from pathlib import Path
import cv2
from ultralytics import YOLO


MODEL_PATH = Path("runs/detect/buah_model/weights/best.pt")
IMAGE_PATH = Path("dataset-buah/test/images/images-2023-02-07T160626-599_jpeg.rf.c770d565a5436a9bf520265abac00e25.jpg")


def main():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"model isn't found: {MODEL_PATH}")

    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(f"image isn't found: {IMAGE_PATH}")

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise ValueError(f"image couldn't be read: {IMAGE_PATH}")

    model = YOLO(str(MODEL_PATH))
    print("detecting...")
    results = model.predict(source=image, conf=0.5, verbose=False)
    annotated_image = results[0].plot()

    cv2.imshow("Detected Fruit", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()