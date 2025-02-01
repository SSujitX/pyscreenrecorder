# pyscreenrecorder

Python screen recorder `pyscreenrecorder` is a powerful Python package for screen recording with an **optional mouse cursor overlay**.  
It allows **high-performance screen capturing**, **custom resolution**, and **real-time mouse tracking**.

## ✨ Features

- 🎥 **Record screen** with smooth frame rates (30 FPS default).
- 🖱 **Mouse overlay customization** (color, size, thickness).
- 📺 **Multi-monitor support** – Choose which monitor to record.
- 🔄 **Set custom resolution** (e.g., 1280x720, 1920x1080).
- ⚡ **Optimized performance** with `mss` for fast screen capture.
- 🎨 **Flexible output formats** – Supports `.mp4`, `.avi`, and `.mkv`.
- 🔍 **Monitor detection** – List available monitors and their specs.

---

## 📦 Installation

Install `pyscreenrecorder` using pip:

```sh
pip install pyscreenrecorder
```

Upgrade `pyscreenrecorder` using pip:

```sh
pip install pyscreenrecorder -U
```

## 🚀 Usage

### Basic Screen Recording

```python
from pyscreenrecorder import ScreenRecorder

ScreenRecorder(
    filename="screen_record.mp4",
    duration=10,
    fps=30,
    monitor_number=1,
    mouse=True,
)
```

## 📺 Listing Available Monitors

```python
from pyscreenrecorder import pyScreenRecorder

monitors = pyScreenRecorder.list_monitors()
print("Available Monitors:", monitors)
```

Example Output:

```json
[
  { "monitor": 0, "width": 1920, "height": 1080 },
  { "monitor": 1, "width": 2560, "height": 1440 }
]
```

## 🎥 Recording with Custom Settings

```python
from pyscreenrecorder import ScreenRecorder

ScreenRecorder(
    filename="custom_record.mp4",
    duration=15,
    fps=60,
    monitor_number=2,
    resolution=(1280, 720),  # Set custom resolution
    mouse=True,
    mouse_color=(255, 0, 0),  # Red cursor
    mouse_size=10,
    mouse_thickness=3,
)
```

🔹 60 FPS Recording  
🔹 Custom 1280x720 resolution  
🔹 Red-colored mouse cursor with increased size

## 🛠 Advanced Example

```python
from pyscreenrecorder import pyScreenRecorder

if __name__ == "__main__":
    # Display available monitors
    monitors = pyScreenRecorder.list_monitors()
    print("Available Monitors:", monitors)

    # Start recording with advanced settings
    pyRec = pyScreenRecorder(
        filename="high_quality_record.mp4",
        duration=30,
        fps=60,
        monitor_number=1,
        resolution=(1920, 1080),  # Full HD recording
        mouse=True,
        mouse_color=(0, 255, 0),  # Green cursor
        mouse_size=6,
        mouse_thickness=2,
    )
    pyRec.screenRecorder()
```

---

## ⚙ Supported File Formats

`pyscreenrecorder` supports the following video formats:

| Format  | Description          |
| ------- | -------------------- |
| **MP4** | High compatibility   |
| **AVI** | Uncompressed quality |
| **MKV** | Modern, flexible     |

Set the format by using the appropriate file extension in `filename`.  
Example:

```python
ScreenRecorder(filename="recording.mkv")
```

---

## 🎯 Dependencies

`pyscreenrecorder` relies on:

- `opencv-python`
- `numpy`
- `mss`
- `pyautogui`
- `MouseInfo`
- `PyGetWindow`
- `PyMsgBox`
- `pyperclip`
- `PyRect`
- `PyScreeze`
- `pytweening`

No additional configuration is required.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 📚 More Information

📌 **GitHub Repository:**  
🔗 [https://github.com/SSujitX/pyscreenrecorder](https://github.com/SSujitX/pyscreenrecorder)

📌 **Issue Tracker:**  
🐛 [Report a Bug](https://github.com/SSujitX/pyscreenrecorder/issues)

---

## 🏁 Conclusion

`pyscreenrecorder` is an **efficient**, **easy-to-use**, and **customizable** screen recording tool in Python. Whether you need **basic screen capturing** or **advanced mouse-tracked recordings**, this package provides all the features.

🚀 **Try it today!** 🚀
