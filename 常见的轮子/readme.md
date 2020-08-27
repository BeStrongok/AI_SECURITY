## 对抗性恶意代码分析
### 特征提取
- 灰度图  
   读取恶意代码的字节序列并将其转为灰度图像，使用卷积神经网络进行训练，这是一个基本的方式，其核心代码在[灰度图.py](https://github.com/cjx1016/AI_SECURITY/blob/master/%E5%B8%B8%E8%A7%81%E7%9A%84%E8%BD%AE%E5%AD%90/%E7%81%B0%E5%BA%A6%E5%9B%BE.py)中。
