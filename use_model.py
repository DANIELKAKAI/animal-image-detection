import pickle
from skimage.io import imread
from skimage.transform import resize

labels = ['Bull', 'Cattle', 'Goat', 'Sheep']


def get_animal(image_url):
    model = pickle.load(open('models/model.p', 'rb'))

    img = imread(image_url, plugin='imageio')

    img_resize = resize(img, (150, 150, 3))

    l = [img_resize.flatten()]

    probability = model.predict_proba(l)

    result = []
    for i, v in enumerate(labels):
        result.append(f"{v}: {int(probability[0][i] * 100)}%\n")

    return result
