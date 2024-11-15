from pynput.keyboard import Key, Controller
import time

def keyboard_initialize():

  # Create a keyboard controller instance
  keyboard = Controller()

   # Instructions to start
  print("Starting script. Ensure the emulator window is in focus.")
  time.sleep(5)  # Gives you time to focus on the emulator window

  try:
      while True:
          
        keyboard.press(Key.right)
        keyboard.press('z')
        time.sleep(10) 
        keyboard.release(Key.right)
        keyboard.release('z')

        # Small delay before repeating
        time.sleep(1)

  except KeyboardInterrupt:
      print("Script stopped.")

  return