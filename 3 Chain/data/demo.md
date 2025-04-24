<h1 >YOLOv8</h1>

一、环境安装
- anaconda安装
- GPU版本的pytorch安装
- ultralytics（YOLOv8）安装
  - 这里建议使用pip源码安装：
    1. 下载github上ultralytics的源码
    2. 在ultralytics目录下，输入**pip install -e .**

二、数据集构建
- 准备视频，切割为图片
- 使用数据集标注网站（https://www.makesense.ai/）
  - 标注完成后，可导出为xml格式和yolo格式
  - 其中，xml用于下一次接着标注，yolo格式用于训练
  - 最后，在ultralytics项目内添加datasets文件夹，存放train和val的图片及其标签

- 文件夹格式
- ultralytics-main
  - datasets
    - images
      - train
      - val
    - labels
      - train
      - val


三、模型训练
- 创建yaml文件
```python
path: bvn
train: images//train # 以datasets为根目录
val: images//val
test: # 暂时不需要

names:
  0: "dujiaoshou"
  1: "zhangyu"
  2: "mutou"
  3: "shu"
```
- 开始训练
```python
from ultralytics import YOLO

model = YOLO('first_best.pt')

model.train(data='bvn.yaml', workers=0, batch=16, epochs=50, device='0')
```

四、模型预测
```python
from ultralytics import YOLO

model = YOLO('data\\best.pt', task='detect') # best.pt为训练好的模型
results = model(source='data\\demo1.mp4', show=True) # source可为视频、图片
```
