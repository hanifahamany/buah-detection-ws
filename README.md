# AI Training: Fruit Detection

Sistem Object Detection berbasis Artificial Intelligence menggunakan **YOLO (Ultralytics)** untuk mendeteksi dan mengklasifikasikan berbagai jenis buah.

## 📊 Dataset
Dataset yang digunakan dalam proyek ini bersumber dari [Fruits by YOLO Detection Dataset di Kaggle](https://www.kaggle.com/datasets/kapturovalexander/fruits-by-yolo-fruits-detection).

## 💻 Environment & Spesifikasi Perangkat
* **OS:** Windows 11 64-bit
* **Processor:** AMD Ryzen 5 5500U
* **RAM:** 16 GB
* **Storage:** 256 GB
* **GPU:** Radeon Graphics 2.1 GHz *(Training dilakukan menggunakan Google Colab GPU Tesla T4)*

## 🚀 Google Colab Training
Script dan proses training model dilakukan secara cloud melalui Google Colab:
* [Google Colab Notebook Link](https://colab.research.google.com/drive/1tztRwT92JvGTtVOg8jdAoXMJ4t9fHmzp?usp=sharing)

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