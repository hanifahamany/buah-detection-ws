# buah-detection-ws
Detail

Dataset: [Fruits by YOLO Detection Dataset](https://www.kaggle.com/datasets/kapturovalexander/fruits-by-yolo-fruits-detection).

buah-detection-ws/

├── dataset-buah/                 # dataset (Train, Valid, Test)
│       test/
│       images/              
├── runs/
│       detect/
│           buah_model/           # output training model YOLO
│               weights/
│                   best.pt       # model terbaik hasil training
├── .gitignore                    
├── inference-1.py                # Script Inference untuk path gambar manual
├── inference-2.py                # Script Inference dengan pengambilan gambar acak
├── README.md                     
├── requirements.txt              
└── train.py                      # Script Training Model

OS: Windows 11 64-bit | CPU: AMD Ryzen 5 5500U | RAM:16 GB | Storage: 256 GB | GPU: Radeon Graphics 2.1 GHz

Google Colab Link: https://colab.research.google.com/drive/1tztRwT92JvGTtVOg8jdAoXMJ4t9fHmzp?usp=sharing