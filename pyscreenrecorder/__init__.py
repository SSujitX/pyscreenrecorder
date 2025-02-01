from .pyscreenrecorder import pyScreenRecorder
from .__version__ import __version__


def ScreenRecorder(
    filename="custom_record.mp4",
    duration=10,
    fps=30,
    monitor_number=1,
    resolution=None,  # Default to full resolution
    mouse=True,
    mouse_color=(0, 0, 255),  # Red color
    mouse_size=8,
    mouse_thickness=2,
):
    """
    A simple function wrapper to initialize and start screen recording.

    This function allows quick usage of the pyScreenRecorder class without
    explicitly creating an instance.

    Parameters:
        filename (str): The output video filename (default: 'custom_record.mp4').
        duration (int): Recording duration in seconds (default: 10).
        fps (int): Frames per second (default: 30).
        monitor_number (int): The monitor index to capture (default: 1).
        resolution (tuple, optional): Custom resolution (width, height). Defaults to full resolution.
        mouse (bool): If True, overlays the mouse cursor (default: True).
        mouse_color (tuple): Mouse cursor color in BGR format (default: Red `(0, 0, 255)`).
        mouse_size (int): Radius of the mouse overlay circle (default: 8).
        mouse_thickness (int): Thickness of the mouse overlay circle (default: 2).

    Returns:
        None: Starts screen recording.
    """
    pyRec = pyScreenRecorder(
        filename=filename,
        duration=duration,
        fps=fps,
        monitor_number=monitor_number,
        resolution=resolution,
        mouse=mouse,
        mouse_color=mouse_color,
        mouse_size=mouse_size,
        mouse_thickness=mouse_thickness,
    )
    pyRec.screenRecorder()


__all__ = [
    "ScreenRecorder",
    "pyScreenRecorder",
    "__version__",
]
