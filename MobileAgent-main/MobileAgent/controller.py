import time
import subprocess
from PIL import Image
import io
import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_size(adb_path):
    try:
        command = adb_path + " shell wm size"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout.strip()
        print("Command output:", output)  # Debugging print

        if "Physical size" in output:
            resolution_line = output.split(": ")[1]
            width, height = map(int, resolution_line.split('x'))
            return width, height
        else:
            raise ValueError("Unexpected output format")

    except Exception as e:
        print("Error getting screen size:", e)
        return None, None


def get_screenshot(adb_path):
    command = adb_path + " shell rm /sdcard/screenshot.png"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(0.5)
    command = adb_path + " shell screencap -p /sdcard/screenshot.png"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(0.5)
    command = adb_path + " pull /sdcard/screenshot.png ./screenshot"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    image_path = "./screenshot/screenshot.png"
    save_path = "./screenshot/screenshot.jpg"
    image = Image.open(image_path)
    original_width, original_height = image.size
    new_width = int(original_width * 0.5)
    new_height = int(original_height * 0.5)
    resized_image = image.resize((new_width, new_height))
    resized_image.convert("RGB").save(save_path, "JPEG")
    time.sleep(1)


def tap(adb_path, x, y, px, py):
    if x is None or y is None:
        raise ValueError("x or y is None, ensure they are properly initialized")
    w = px
    h = py
    if w is None:
        raise ValueError("w is None, ensure it is properly initialized")
    ax = int(x*w)
    ay = int(y*h)
    command = adb_path + f" shell input tap {ax} {ay}"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(1)


def type(adb_path, text):
    text = text.replace("\\n", "_").replace("\n", "_")
    for char in text:
        if char == ' ':
            command = adb_path + f" shell input text %s"
            subprocess.run(command, capture_output=True, text=True, shell=True)
        elif char == '_':
            command = adb_path + f" shell input keyevent 66"
            subprocess.run(command, capture_output=True, text=True, shell=True)
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char.isdigit():
            command = adb_path + f" shell input text {char}"
            subprocess.run(command, capture_output=True, text=True, shell=True)
        elif char in '-.,!?@\'°/:;()':
            command = adb_path + f" shell input text \"{char}\""
            subprocess.run(command, capture_output=True, text=True, shell=True)
        else:
            command = adb_path + f" shell am broadcast -a ADB_INPUT_TEXT --es msg \"{char}\""
            subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(1)


def slide(adb_path, action, x, y):
    if "down" in action:
        command = adb_path + f" shell input swipe {int(x/2)} {int(y/2)} {int(x/2)} {int(y/4)} 500"
        subprocess.run(command, capture_output=True, text=True, shell=True)
    elif "up" in action:
        command = adb_path + f" shell input swipe {int(x/2)} {int(y/2)} {int(x/2)} {int(3*y/4)} 500"
        subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(1)


def back(adb_path):
    command = adb_path + f" shell input keyevent 4"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(1)
    
    
def back_to_desktop(adb_path):
    command = adb_path + f" shell am start -a android.intent.action.MAIN -c android.intent.category.HOME"
    subprocess.run(command, capture_output=True, text=True, shell=True)
    time.sleep(1)