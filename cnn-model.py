from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

n_channels = X.shape[1]
n_samples = X.shape[2]
n_classes = y.shape[1]

model = Sequential([
    Conv2D(16, (1, 5), activation='relu', input_shape=(n_channels, n_samples, 1)),
    MaxPooling2D((1, 2)),
    Conv2D(32, (1, 5), activation='relu'),
    MaxPooling2D((1, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(n_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))
