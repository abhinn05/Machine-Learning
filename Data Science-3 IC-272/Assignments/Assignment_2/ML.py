import pandas as pd
import numpy as np 
from numpy.linalg import eig
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

data = pd.read_csv('iris.csv');

x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = data['Species'].values

def replace_outliers_with_median(x):
    median = np.median(x,axis=0)
    for i in range (x.shape[1]):
        col = x[:,1]
        z_scores = np.abs((col-np.mean(col)) / np.std(col))
        outliers = z_scores > 3
        x[outliers,i] = median[i]
    return x

x_corrected = replace_outliers_with_median(x)


x_meaned = x_corrected - np.mean(x_corrected, axis=0)

cov_matrix = np.cov(x_meaned, rowvar=False)

eigenvalues, eigenvectors = eig(cov_matrix)

sorted_idx = np.argsort(eigenvalues)[::-1]
sorted_eigenvectors = eigenvectors[:, sorted_idx]

k = 2
x_reduced = x_meaned.dot(sorted_eigenvectors[:, :k])


plt.scatter(x_reduced[:, 0], x_reduced[:, 1])
plt.title('PCA - Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

for i in range(k):
    plt.quiver(0, 0, sorted_eigenvectors[0, i], sorted_eigenvectors[1, i], scale=5, color='r')

plt.show()

x_reconstructed = x_reduced.dot(sorted_eigenvectors[:, :k].T) + np.mean(x_corrected, axis=0)

rmse = np.sqrt(mean_squared_error(x_corrected, x_reconstructed))
print(f"RMSE: {rmse}")


rmse = np.sqrt(mean_squared_error(x_corrected, x_reconstructed, multioutput='raw_values'))

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].scatter(x_corrected[:, 0], x_reconstructed[:, 0], color='blue', alpha=0.5)
axes[0, 0].plot([min(x_corrected[:, 0]), max(x_corrected[:, 0])], [min(x_corrected[:, 0]), max(x_corrected[:, 0])], 'r--')
axes[0, 0].set_title(f"Sepal Length: RMSE = {rmse[0]:.4f}")
axes[0, 0].set_xlabel("Original")
axes[0, 0].set_ylabel("Reconstructed")

axes[0, 1].scatter(x_corrected[:, 1], x_reconstructed[:, 1], color='green', alpha=0.5)
axes[0, 1].plot([min(x_corrected[:, 1]), max(x_corrected[:, 1])], [min(x_corrected[:, 1]), max(x_corrected[:, 1])], 'r--')
axes[0, 1].set_title(f"Sepal Width: RMSE = {rmse[1]:.4f}")
axes[0, 1].set_xlabel("Original")
axes[0, 1].set_ylabel("Reconstructed")

axes[1, 0].scatter(x_corrected[:, 2], x_reconstructed[:, 2], color='purple', alpha=0.5)
axes[1, 0].plot([min(x_corrected[:, 2]), max(x_corrected[:, 2])], [min(x_corrected[:, 2]), max(x_corrected[:, 2])], 'r--')
axes[1, 0].set_title(f"Petal Length: RMSE = {rmse[2]:.4f}")
axes[1, 0].set_xlabel("Original")
axes[1, 0].set_ylabel("Reconstructed")

axes[1, 1].scatter(x_corrected[:, 3], x_reconstructed[:, 3], color='orange', alpha=0.5)
axes[1, 1].plot([min(x_corrected[:, 3]), max(x_corrected[:, 3])], [min(x_corrected[:, 3]), max(x_corrected[:, 3])], 'r--')
axes[1, 1].set_title(f"Petal Width: RMSE = {rmse[3]:.4f}")
axes[1, 1].set_xlabel("Original")
axes[1, 1].set_ylabel("Reconstructed")

plt.tight_layout()
plt.show()



###################################################Q-2###################################################################

x_train, x_test, y_train, y_test = train_test_split(x_reduced, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()
