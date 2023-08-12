# Digit Recognizer GUI

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Training the Model](#training-the-model)
- [Acknowledgments](#acknowledgments)

## Description
**Digit Recognizer GUI** is an interactive application that allows users to draw handwritten digits and get real-time predictions on what the digit is. Utilizing the power of convolutional neural networks (CNN) trained on the MNIST dataset, this application provides a seamless experience for users to test and visualize the capabilities of deep learning models in recognizing handwritten digits.

The project consists of two main components:
1. **Training Notebook (`main.ipynb`)**: This Jupyter notebook walks through the process of loading the MNIST dataset, preprocessing the data, defining the CNN model architecture, training the model, and evaluating its performance.
2. **GUI Application (`gui_digit_recognizer.py`)**: A user-friendly interface where users can draw digits on a canvas. Once drawn, the application uses the trained model to predict and display the recognized digit.

## Features
- **Interactive Drawing Canvas**: Users can draw digits using their mouse or touchscreen.
- **Real-time Prediction**: As soon as a digit is drawn, the application predicts the digit and displays the result.
- **Clear Canvas**: A clear button allows users to erase their drawing and start fresh.
- **Model Insights**: The application provides confidence scores for predictions, giving users insights into the model's certainty.

## Technologies Used
- **Keras & TensorFlow**: For defining, training, and evaluating the CNN model.
- **Tkinter**: Used to create the interactive GUI.
- **Pillow**: For image processing tasks before feeding the drawn digit to the model.

## Getting Started
1. **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-github-username/digit-recognizer-gui.git](https://github.com/ayushpatel2002/Handwriting-Recognition)
    cd digit-recognizer-gui
    ```

2. **Install Dependencies**:
    ```bash
    pip install numpy, tensorflow, keras, pillow
    ```

3. **Run the Application**:
    ```bash
    python gui_digit_recognizer.py
    ```

## Training the Model
If you're interested in understanding the training process or wish to retrain the model, refer to the `main.ipynb` notebook. This notebook provides a step-by-step guide, starting from data loading to model evaluation. It's a great resource for both beginners and experienced practitioners looking to delve into the world of deep learning.

## Acknowledgments
- The MNIST dataset provided by the Keras library served as the foundation for training the model.
