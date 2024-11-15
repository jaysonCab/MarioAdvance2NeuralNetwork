import pyautogui
import pygetwindow as gw
from PIL import Image
import time

def get_window_region(title):
    # Get the window object by title
    window = gw.getWindowsWithTitle(title)
    
    if window:
        # Assuming the first matching window is the one we want
        win = window[0]
        
        # Get window position and size
        left, top = win.left, win.top
        width, height = win.width, win.height
        
        return (left, top, width, height)
    else:
        print(f"Window with title '{title}' not found.")
        return None

def display_screen():
  
  window_title = "Super Mario Advanced 2 - Super Mario World (U) [!] - VisualBoyAdvance-M 2.0.1"  # Replace with your window's title
  region = get_window_region(window_title)

  if region:
    while True:
      # Take a screenshot of the specific window region
      screenshot = pyautogui.screenshot(region=region)

      # Convert the screenshot to grayscale
      grayscale_image = screenshot.convert('L')

      # Resize the image (e.g., to 84x84 or smaller)
      resized_image = grayscale_image.resize((84, 84))

      # Optionally display the processed image
      resized_image.show()

      # Small delay between screenshots
      time.sleep(0.1)
  return
