# przykład powiększenia obrazu zoomu
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
# wgrywanie obrazu
img = load_img("/content/00028.jpg")
# przekonwertuj na tablicę numpy
data = img_to_array(img)
# rozszerzenie wymiaru do jednej próbki
samples = expand_dims(data, 0)
# tworzenie generatora rozszerzenia danych obrazu
datagen=ImageDataGenerator(rotation_range=40,
              width_shift_range=0.2,
              height_shift_range=0.2,
              shear_range=0.2,
              zoom_range=0.2,
              horizontal_flip=True,
              brightness_range=[0.2,1.0],
              fill_mode='nearest')
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generowanie przykladow oraz wykresow
for i in range(9):
 pyplot.subplot(330 + 1 + i)
 batch = it.next()
 image = batch[0].astype("uint8")
 pyplot.imshow(image)
# przedstaw wykres
pyplot.show()
