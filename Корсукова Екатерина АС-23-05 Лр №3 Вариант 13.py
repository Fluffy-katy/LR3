import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import numpy as np

def calculate_Y():
    try:
        # Получаем исходный массив X из текстового поля
        X_str = text_X.get(1.0, tk.END)
        X = [float(x) for x in X_str.split()]

        # Проверяем наличие четных индексов и вычисляем p
        even_indices = X[1::2]
        if not even_indices:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Искомых элементов нет")
            return
        p = np.prod(even_indices)

        # Фильтруем массив X по условию X >= p
        Y = [x for x in X if x >= p]

        # Выводим результат в текстовое поле
        result_text.delete(1.0, tk.END)
        for y in Y:
            result_text.insert(tk.END, f"{y}\n")

    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Ошибка ввода. Пожалуйста, введите числа.")

# Создаем главное окно
root = tk.Tk()
root.title("Лабораторная работа номер 3 Корсукова Екатерина АС-23-05")

# Создаем текстовое поле для массива X
text_X = scrolledtext.ScrolledText(root, width=20, height=10, wrap=tk.WORD, bg = "#d2caff")
text_X.insert(tk.END, "2.95 7.34 -4.2 0.5 -4.9 0.22 0.35 1 10.1 12")
text_X.pack()

# Кнопка для вычисления массива Y
calculate_button = tk.Button(root, text="Вычислить массив Y", command=calculate_Y)
calculate_button.pack()

# Текстовое поле для вывода массива Y
result_text = scrolledtext.ScrolledText(root, width=20, height=10, wrap=tk.WORD, bg = "#d2caff")
result_text.pack()

# Вставляем изображение Exercise
image_path = "Exercise.png"
exercise_image = Image.open(image_path)
exercise_image = exercise_image.resize((560, 120))
photo = ImageTk.PhotoImage(exercise_image)
image_label = tk.Label(root, image=photo, bg="#d2caff")
image_label.image = photo
image_label.pack()

# Запускаем главный цикл программы
root.mainloop()
