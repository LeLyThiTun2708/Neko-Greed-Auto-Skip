#pip install Pillow
#pip install pyautogui
import time
import pyautogui
from PIL import Image

def find_and_click(image_path, confidence=0.8, timeout=10):
    start_time = time.time()

    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        
        if location is not None:
            # Tính toán tọa độ trung tâm của hình ảnh
            center_x = location.left + location.width / 2
            center_y = location.top + location.height / 2
            # Di chuyển chuột và click vào tọa độ đó
            pyautogui.click(center_x, center_y)
            return True
        else:
            # Chờ 0.1 giây trước khi kiểm tra lại
            time.sleep(0.2)

    # Hết thời gian chờ, không tìm thấy hình ảnh
    return False

# Thực hiện các hành động theo trình tự
actions = ["Roll", "Upgrade", "Play", "Skip"]

number = int(input("Number of click: "))

for i in range(number):
    for action in actions:
        if i == number - 1 and action == "Skip":
            break
        else:
            image_path = f"{action}.png"
            success = find_and_click(image_path)

            if success:
                print(f"{action} thành công!")
                time.sleep(0.8)  # Đợi 2 giây trước khi thực hiện hành động tiếp theo
            else:
                print(f"{action} không thành công. Hình ảnh không được tìm thấy trong khoảng thời gian chờ.")

    

# # Kết thúc chương trình
import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Skip", "Done!")

