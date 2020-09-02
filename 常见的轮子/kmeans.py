import warnings
warnings.filterwarnings('ignore')
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df_test_res = feature_extract(df_test_res)       # 特征提取函数
data_feature = df_test_res.iloc[:, 3:]
# 进行标准化
scaler = StandardScaler() 
data_feature_scaled = scaler.fit_transform(data_feature)

kmeans = KMeans(random_state=123)

# Instantiate the KElbowVisualizer with the number of clusters and the metric 
Visualizer = KElbowVisualizer(kmeans, k=(2,7), metric='silhouette', timings=False)
plt.figure(figsize=(5,3))
# Fit the data and visualize
Visualizer.fit(data_feature_scaled)    
Visualizer.poof()
