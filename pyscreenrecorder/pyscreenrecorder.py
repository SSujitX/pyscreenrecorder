import cv2
import numpy as np
import mss
import time
import pyautogui


class pyScreenRecorder:
    """
    A Python-based screen recording tool with mouse overlay and resolution settings.

    Features:
    - Record screen at a specified FPS and duration.
    - Customize mouse cursor appearance (size, color, thickness).
    - List available monitors.
    - Set custom resolution for recorded video.

    Attributes:
        filename (str): Output video filename.
        duration (int): Recording duration in seconds.
        fps (int): Frames per second.
        monitor_number (int): Monitor index to capture (0 for all monitors).
        mouse (bool): Enable/disable mouse overlay.
        mouse_color (tuple): Color of the mouse circle (B, G, R).
        mouse_size (int): Radius of the mouse circle.
        mouse_thickness (int): Thickness of the mouse circle.
        resolution (tuple): Custom resolution (width, height). Defaults to original screen resolution.
    """

    def __init__(
        self,
        filename: str = "output.mp4",
        duration: int = 5,
        fps: int = 30,
        monitor_number: int = 1,
        resolution: tuple = None,  # If None, use full monitor resolution
        mouse: bool = True,
        mouse_color: tuple = (0, 255, 0),  # Green color (BGR format)
        mouse_size: int = 5,
        mouse_thickness: int = 2,
    ):
        """
        Initialize the screen recorder with customizable options.

        Args:
            filename (str): The output video filename.
            duration (int): The recording duration in seconds.
            fps (int): Frames per second for recording.
            monitor_number (int): The monitor index to capture (0 for all).
            resolution (tuple): Custom resolution (width, height) for recording.
            mouse (bool): Whether to overlay the mouse cursor.
            mouse_color (tuple): RGB color for mouse overlay (B, G, R).
            mouse_size (int): Radius of mouse cursor overlay.
            mouse_thickness (int): Thickness of mouse circle.
        """
        self.filename = filename
        self.duration = duration
        self.fps = fps
        self.monitor_number = monitor_number
        self.mouse = mouse
        self.mouse_color = mouse_color
        self.mouse_size = mouse_size
        self.mouse_thickness = mouse_thickness
        self.resolution = resolution

    @staticmethod
    def list_monitors():
        """
        List available monitors and their dimensions.

        Returns:
            list: A list of available monitors with their dimensions.
        """
        with mss.mss() as sct:
            monitors = sct.monitors
        return [
            {"monitor": idx, "width": mon["width"], "height": mon["height"]}
            for idx, mon in enumerate(monitors)
        ]

    def screenRecorder(self):
        """
        Start screen recording with the configured settings.

        Raises:
            ValueError: If an unsupported file format is provided or if monitor_number is invalid.
        """
        valid_formats = ["avi", "mp4", "mkv"]
        file_extension = self.filename.split(".")[-1].lower()
        if file_extension not in valid_formats:
            raise ValueError(
                f"Unsupported file format: {file_extension}. Supported formats: {valid_formats}"
            )

        with mss.mss() as sct:
            monitors = sct.monitors
            if self.monitor_number < 0 or self.monitor_number >= len(monitors):
                raise ValueError(
                    f"Invalid monitor_number {self.monitor_number}. Must be between 0 and {len(monitors)-1}."
                )
            monitor = monitors[self.monitor_number]
            screen_width, screen_height = monitor["width"], monitor["height"]

        if self.resolution:
            output_width, output_height = self.resolution
        else:
            output_width, output_height = screen_width, screen_height

        # Scaling factor for mouse position
        scale_x = output_width / screen_width
        scale_y = output_height / screen_height

        fourcc = (
            cv2.VideoWriter_fourcc(*"mp4v")
            if file_extension == "mp4"
            else cv2.VideoWriter_fourcc(*"XVID")
        )
        out = cv2.VideoWriter(
            self.filename, fourcc, self.fps, (output_width, output_height)
        )

        start_time = time.time()
        target_frame_count = self.fps * self.duration

        with mss.mss() as sct:
            for i in range(target_frame_count):
                target_time = start_time + (i / self.fps)
                now = time.time()
                if target_time > now:
                    time.sleep(target_time - now)

                frame = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                if self.resolution and (output_width, output_height) != (
                    screen_width,
                    screen_height,
                ):
                    frame = cv2.resize(frame, (output_width, output_height))

                if self.mouse:
                    mouse_x, mouse_y = pyautogui.position()
                    scaled_mouse_x = int(mouse_x * scale_x)
                    scaled_mouse_y = int(mouse_y * scale_y)

                    cv2.circle(
                        frame,
                        (scaled_mouse_x, scaled_mouse_y),
                        self.mouse_size,
                        self.mouse_color,
                        self.mouse_thickness,
                    )

                out.write(frame)

        out.release()


# if __name__ == "__main__":
#     # Display available monitors
#     monitors = pyScreenRecorder.list_monitors()
#     print("Available Monitors:", monitors)

#     # Example usage with customized settings
#     pyRec = pyScreenRecorder(
#         filename="custom_record.mp4",
#         duration=22,
#         fps=30,
#         monitor_number=3,
#         resolution=(1920, 1080),  # Custom resolution
#         mouse=True,
#         mouse_color=(0, 0, 255),  # Red color
#         mouse_size=3,
#         mouse_thickness=2,
#     )
#     pyRec.screenRecorder()
