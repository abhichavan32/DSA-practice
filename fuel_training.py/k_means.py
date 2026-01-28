import os
import numpy as np
from sklearn.cluster import KMeans

os.environ["LOKY_MAX_CPU_COUNT"] = "4"

# data = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])
# model = KMeans(n_clusters=2)
# model.fit(data)
# print(model.labels_)

# data=np.array([[18],[13],[16],[21],[20],[12]])
# model=KMeans(n_clusters=3)
# model.fit(data)
# print(model.labels_)
# print(model.cluster_centers_)

# data=np.array([[12,10],[1,9],[4,8],[2,10],[6,2],[23,5]])
# model=KMeans(n_clusters=2)
# model.fit(data)
# print(model.predict([[56,3]]))
# print(model.labels_)
# print(model.inertia_)
# print(model.cluster_centers_)

data=np.array([[98],[64],[23],[56],[82],[96],[53],[75],[45],[12]])
model=KMeans(n_clusters=3)
model.fit(data)
labels=model.labels_
print(model.predict([[25]]))

cluster_name={
    0:"meadium",
    1:"topper",
    2:"lower"
}
names=[cluster_name[i] for i in labels]
print(names)
