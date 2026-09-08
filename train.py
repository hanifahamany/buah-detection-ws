from pathlib import Path

from ultralytics import YOLO

def main():
    # trained YOLOv8 nano model
    model = YOLO("yolov8n.pt")

    yaml_path = Path(__file__).resolve().parent / "data.yaml"
    if not yaml_path.is_file():
        raise FileNotFoundError(f"data.yaml is not found: {yaml_path}")

    print("start training...")

    model.train(
        data=str(yaml_path),
        epochs=25,
        imgsz=640,
        project="runs/detect",
        name="buah_model",
        exist_ok=True,
    )

    print("finished")
    print("model tersimpan di runs/detect/buah_model/weights/best.pt")

if __name__ == '__main__':
    main()