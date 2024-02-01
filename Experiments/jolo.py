from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model = YOLO('yolov8s.pt')

    for i in range(3):
        results = model.train(
            data='data_custom.yaml',
            imgsz=640,
            epochs=10,
            batch=2,
            name='yolov8n_custom'
        )
    model.eval()
    res = model('C:\\internship\\Experiments\\val\\images\\93-im-03-31-23.jpg')[0]
    res = Image.fromarray(res.plot()[:, :, ::-1])
    plt.imshow(res)
    plt.show()

