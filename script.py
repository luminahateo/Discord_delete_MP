#Python
## Run on AutoKey

for c in range(10000): #nombre de ligne à effacer
    keyboard.send_keys("<up>")
    time.sleep(0.25)
    keyboard.send_keys("<ctrl>+a")
    time.sleep(0.25)
    keyboard.send_keys("<backspace>")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("<page_up>")
    time.sleep(0.25)

keyboard.send_keys("<tab>")
keyboard.send.keys("terminé")
