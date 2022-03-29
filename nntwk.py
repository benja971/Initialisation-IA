import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


# Et on normalise les 2 bases
datas = pd.read_csv("./data/whites.csv", sep=";")

y = datas.quality
x = datas.drop(['quality'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)

scaler = preprocessing.StandardScaler().fit(x_train)

x_train_norm = scaler.transform(x_train)
x_test_norm = scaler.transform(x_test)

model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(11), name='input'),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1, name='output')
])

loss_fn = tf.keras.losses.MeanSquaredError()

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

model.summary()

BATCH_SIZE = 100


# La base de validation
dataset = tf.data.Dataset.from_tensor_slices((x_train_norm, y_train))
dataset = dataset.shuffle(x_train_norm.shape[0])
dataset = dataset.batch(BATCH_SIZE)

history = model.fit(dataset, validation_data=x_test_norm, epochs=1000)
results = model.evaluate(x_test_norm)


# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for accuracy
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Fonction de perte (entropie croisee)')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
