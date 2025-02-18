import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import matplotlib.pyplot as plt


# Название папки с датасетом
dataset = 'data/Dataset_categories'


# Загрузка данных
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset, validation_split=0.2, subset="training",
    seed=123, image_size=(224, 224), batch_size=32
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset, validation_split=0.2, subset="validation",
    seed=123, image_size=(224, 224), batch_size=32
)

class_names = train_ds.class_names
print("Обнаруженные классы:", class_names)

# Оптимизация загрузки
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Аугментация
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])

# Создание модели
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3), include_top=False, weights="imagenet"
)
base_model.trainable = False
'''for layer in base_model.layers[:-40]:
    layer.trainable = False'''

model = tf.keras.Sequential([
    data_augmentation,
    tf.keras.layers.Rescaling(1./255),
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(len(class_names), activation='softmax')
])
model.build(input_shape=(None, 224, 224, 3))


model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)
model.summary()

history = model.fit(train_ds, validation_data=val_ds, epochs=5)

# Построение графиков точности и потерь
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Точность на обучении')
plt.plot(epochs, val_acc, 'r', label='Точность на тестах')
plt.title('Точность обучения и тестов')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'b', label='Потери на обучении')
plt.plot(epochs, val_loss, 'r', label='Потери на тестах')
plt.title('Потери обучения и тестов')
plt.legend()

plt.show()

# Сохранение
model.save("trashnet_classifier.h5")
print("✅ Модель сохранена!")

model.compile()
