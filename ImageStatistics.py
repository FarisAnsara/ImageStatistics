import os
import math

class ImageStatistics:
    def __init__(self, image_path, width, height):
        """
        Initialize ImageStatistics for a .raw grayscale image.
        :param image_path: Path to the .raw image file.
        :param width: Width of the image.
        :param height: Height of the image.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The file '{image_path}' does not exist.")

        if not image_path.lower().endswith('.raw'):
            raise ValueError("Only .raw grayscale images are supported.")

        self.width = width
        self.height = height
        self.pixel_count = width * height
        self.pixels = self.load_raw(image_path)

    def load_raw(self, image_path):
        """
        Load and process a .raw image file.
        Trims extra bytes if present and validates file size.
        """
        with open(image_path, "rb") as f:
            pixel_data = list(f.read())

        if len(pixel_data) > self.pixel_count:
            print(f"Warning: Trimming {len(pixel_data) - self.pixel_count} extra bytes.")
            pixel_data = pixel_data[:self.pixel_count]

        elif len(pixel_data) < self.pixel_count:
            raise ValueError(f"File size too small ({len(pixel_data)} bytes) for expected dimensions ({self.width}x{self.height}).")

        return pixel_data

    def calculate_mean(self):
        return sum(self.pixels) / self.pixel_count

    def calculate_variance(self):
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.pixels) / self.pixel_count

    def calculate_std(self):
        return math.sqrt(self.calculate_variance())

    def get_min_pixel_value(self):
        return min(self.pixels)

    def get_max_pixel_value(self):
        return max(self.pixels)

    def get_all_statistics(self):
        """
        Return all calculated statistics for the image.
        """
        return {
            'Mean': self.calculate_mean(),
            'Variance': self.calculate_variance(),
            'Standard Deviation': self.calculate_std(),
            'Min Pixel Value': self.get_min_pixel_value(),
            'Max Pixel Value': self.get_max_pixel_value()
        }
