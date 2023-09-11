# GUI for digit recognition

import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw

class DigitRecognizer(tk.Tk):
    def __init__(self, model):
        super().__init__()

        self.model = model
        self.canvas_width = 280
        self.canvas_height = 280
        self.pen_width = 15
        self.initialize_ui()

    def initialize_ui(self):
        self.canvas = Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(pady=20)

        self.canvas.bind("<B1-Motion>", self.paint)

        clear_button = tk.Button(self, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(pady=20)

        recognize_button = tk.Button(self, text="Recognize Digit", command=self.recognize_digit)
        recognize_button.pack(pady=20)

        self.label = tk.Label(self, text="Draw a digit...", font=("Helvetica", 16))
        self.label.pack(pady=20)

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval((x, y, x + self.pen_width, y + self.pen_width), fill="black", width=0)

    def clear_canvas(self):
        self.canvas.delete("all")

    def recognize_digit(self):
        # Get the canvas content as an image
        canvas_image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        draw = ImageDraw.Draw(canvas_image)
        for item in self.canvas.find_all():
            x0, y0, x1, y1 = self.canvas.coords(item)
            draw.ellipse([x0, y0, x1, y1], fill="black")

        digit, confidence = self.predict_digit(canvas_image)
        self.label.config(text=f"Predicted Digit: {digit} (Confidence: {confidence:.2f}%)")

    def predict_digit(self, img):
        img = img.resize((28, 28))
        img = img.convert('L')
        img = np.array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img / 255.0
        prediction = self.model.predict([img])[0]
        return np.argmax(prediction), max(prediction) * 100

# Running the GUI
app = DigitRecognizer(model)
app.title("Handwritten Digit Recognizer")
app.mainloop()
