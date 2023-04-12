import os
import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# prepare data
# 412 images

input_dir = 'data'

data = []
labels = []

for dirname, _, filenames in os.walk(input_dir):
    for filename in filenames:
        label = dirname.split('/')[-1]
        if label == 'Label':
            continue
        file_path = os.path.join(dirname, filename)
        img = imread(file_path)
        img = resize(img, (150, 150, 3))
        data.append(img.flatten())
        labels.append(label)

data = np.asarray(data, dtype=object)
labels = np.asarray(labels)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42, stratify=labels)

# train classifier
classifier = SVC(probability=True)

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_

y_prediction = best_estimator.predict(x_test)

score = accuracy_score(y_prediction, y_test)

print('{}% of samples were correctly classified'.format(str(score * 100)))

pickle.dump(best_estimator, open('models/model.p', 'wb'))
