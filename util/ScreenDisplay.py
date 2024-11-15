import mss
import pygetwindow as gw
from PIL import Image, ImageEnhance
import time

def get_window_region(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        win = windows[0]
        return {"top": win.top, "left": win.left, "width": win.width, "height": win.height}
    else:
        print(f"Window with title '{title}' not found.")
        return None

def display_screen():
  
  window_title = "Super Mario Advance 2 - Super Mario World (U) [!] - VisualBoyAdvance-M 2.1.11"  # Replace with your window's title
  region = get_window_region(window_title)

  if region:
    with mss.mss() as sct:
      while True:
        # Capture the window
        screenshot = sct.grab(region)

        # Convert to grayscale and resize
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        grayscale_image = image.convert("L")
        resized_image = grayscale_image.resize((512, 405), Image.Resampling.LANCZOS)

        # Show the processed image
        enhancer = ImageEnhance.Sharpness(resized_image)
        sharpend_image = enhancer.enhance(2.0)
      
        sharpend_image.show()

        # Delay to control frequency
        time.sleep(0.1)
  else:
      print("Could not locate the specified window.")

  return
