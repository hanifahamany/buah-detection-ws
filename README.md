# AI Training: Fruit Detection

## 📊 Dataset
Dataset yang digunakan berasal dari proyek **Fruits by YOLO**:
* [Roboflow Universe - Fruits by YOLO Dataset](https://universe.roboflow.com/fruitsdetection/fruits-by-yolo/dataset/1)
* [Kaggle - Fruits by YOLO Detection Dataset](https://www.kaggle.com/datasets/kapturovalexander/fruits-by-yolo-fruits-detection)

## 🛠️ Tech Stack
* **Bahasa pemrograman:** Python
* **Framework object detection:** Ultralytics YOLOv8
* **Deep learning framework:** PyTorch
* **Computer vision library:** OpenCV (`cv2`)
* **GUI/window library:** OpenCV HighGUI (`cv2.imshow`, `cv2.waitKey`, `cv2.destroyAllWindows`)
* **Training environment:** Google Colab dengan GPU Tesla T4

## 💻 Environment & Spesifikasi Perangkat
* **OS:** Windows 11 64-bit
* **Processor:** AMD Ryzen 5 5500U
* **RAM:** 16 GB
* **Storage:** 256 GB
* **GPU:** Radeon Graphics 2.1 GHz *(Training model dilakukan menggunakan Google Colab GPU Tesla T4)*

## 🚀 Google Colab Training
Script dan proses training model dapat diakses melalui [Google Colab](https://colab.research.google.com/drive/1tztRwT92JvGTtVOg8jdAoXMJ4t9fHmzp?usp=sharing)

## 📁 Struktur Direktori Proyek

```text
buah-detection-ws/
├── dataset-buah/                 # Direktori dataset (Train, Valid, Test)
│   └── test/
│       └── images/               # Kumpulan gambar untuk pengujian inference
├── runs/
│   └── detect/
│       └── buah_model/           # Hasil output training model YOLO
│           └── weights/
│               └── best.pt       # Bobot model terbaik hasil training
├── .gitignore                    
├── inference-1.py                # Script Inference untuk path gambar manual
├── inference-2.py                # Script Inference dengan pengambilan gambar acak
├── README.md                     # Dokumentasi proyek
├── requirements.txt              # Daftar dependensi library Python
└── train.py                      # Script Training Model