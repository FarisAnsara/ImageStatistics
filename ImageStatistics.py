from PIL import Image
import math


class ImageStatistics:
    
    def __init__(self, image_path):
        image = Image.open(image_path).convert('L')
        self.pixels = list(image.getdata())
        self.pixel_count = len(self.pixels)
        self.pixel_sum = sum(self.pixels)

    def calculate_mean(self):
        return self.pixel_sum / self.pixel_count

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
        return {
            'Mean': self.calculate_mean(),
            'Variance': self.calculate_variance(),
            'Standard Deviation': self.calculate_std(),
            'Min Pixel Value': self.get_min_pixel_value(),
            'Max Pixel Value': self.get_max_pixel_value()
        }

image = r'DataSets\FacesDataSet\faces\images\train\00006c07d2b033d1.jpg'
image_statistics = ImageStatistics(image)
print(image_statistics.get_all_statistics())