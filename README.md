🧥 Invisible Cloak using Python & OpenCV

✨ Overview
This project creates a real-time invisibility effect using computer vision. By detecting a red-colored cloak in the webcam feed and replacing it with a static background image, the cloak appears to vanish—just like magic!

📸 Demo
Include a GIF or screenshot showing the cloak effect in action.

🛠️ Technologies Used
- Python
- OpenCV
- NumPy

🚀 How It Works
1. Background Capture** (`background.py`):  
   Captures a static background image from the webcam when you press `q`. This image is saved as `background.jpg` and used later for the invisibility effect.

2. Invisible Cloak Effect** (`invisible_cloak.py`):  
   Detects red-colored cloak in the live video feed and replaces it with the saved background image using HSV masking and bitwise operations.

📦 Installation
```bash
pip install opencv-python numpy
```

▶️ Usage
1. Run `background.py` and press `q` to save your background.
2. Place a red cloth in front of your webcam.
3. Run `invisible_cloak.py` to activate the cloak effect.
4. Press `q` to quit.

📁 Files
- `background.py`: Captures and saves the background image.
- `invisible_cloak.py`: Main script for the invisibility effect.
- `background.jpg`: Static background image used for cloaking.

📌 Notes
- Works best with a solid red cloth and consistent lighting.
- You can tweak HSV values to detect other colors.
