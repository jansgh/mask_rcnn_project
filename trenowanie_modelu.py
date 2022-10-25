model = keras.models.Sequential ([ keras.layers.Conv20 (64, 7, activation "relu",
                input shape=[28, 28, 3)
                padding="same",
keras.layers.MaxPooling20(2),
keras.layers.Conv2D(128, 3, activation "relu", padding="same"),
keras.layers.Conv20 (128, 3, activation="relu", padding same"),
keras. Tayers.MaxPooling20(2), keras.layers.Conv20 (256, 3, activation-"relu", padding="same"),
keras.layers.Conv20 (256, 3, activation="relu", padding="same"),
keras.Tayers.MaxPooling20(2),
keras.layers. Flatten(),
keras.layers.Dense (128, activation="relu"),
keras.layers.Dropout (0.5),
keras.layers.Dense (64, activation="relu"),
keras.layers.Dropout (0.5),
keras.layers.Dense (10, activation="softmax")
})
