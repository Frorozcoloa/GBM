from typing import List, Tuple
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np


from feature_engeenier import extract_feature

def create_train_test()-> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Create train and test dataset
    output: Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]-> (X_train, X_test, y_train, y_test)
    """
    df = extract_feature()
    y = df["type_consumer"]
    X = df.drop(["type_consumer"], axis=1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def create_nn(X_train)-> keras.Sequential:
    """
    Create neural network
    output: keras.Sequential -> model
    arquitecture: 64 neurons, 32 neurons, 3 neurons
    """
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(3, activation='softmax')  # 3 neuronas de salida para 3 categorías
    ])
    return model

def train(model, X_train, y_train)-> None:
    """
    Train the model with the train dataset, uses the adam optimizer and sparse_categorical_crossentropy loss
    input:
        model: keras.Sequential
        X_train: np.ndarray
        y_train: np.ndarray
    """
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32)

def evaluate(model, X_test, y_test)-> None:
    """
    Evaluate the model with the test dataset and print the classification report
    input:
        model: keras.Sequential
        X_test: np.ndarray
        y_test: np.ndarray
    """
    y_pred = model.predict(X_test)
    y_pred = np.argmax(y_pred, axis=1)
    print(classification_report(y_test, y_pred))

def main():
    """Main function"""
    X_train, X_test, y_train, y_test = create_train_test()
    model = create_nn(X_train)
    train(model, X_train, y_train)
    evaluate(model, X_test, y_test)
    
if __name__ == "__main__":
    main()
    