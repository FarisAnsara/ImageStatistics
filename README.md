# Image Statistics

## Overview
This project calculates statistical properties of 8-bit grayscale images stored in `.raw` format. It provides key metrics such as mean, standard deviation, variance, and the minimum and maximum pixel values. The program processes `.raw` files efficiently and ensures proper handling of image dimensions and pixel data.

---

## Requirements
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

**Dependencies:**
- Python == 3.11.3

---

## Cloning the Repository
To clone this repository onto your local machine:
1. Use the following command:
```bash
git clone https://github.com/FarisAnsara/ImageStatistics.git
```
2. Navigate to the project directory:
```bash
cd ImageStatistics
```

---

## How to Run

### 1. **Running the Script**
You can calculate the statistics for a `.raw` image using the command line:
```bash
python main.py --input_image_path <path_to_raw_image> --width <image_width> --height <image_height>
```

**Arguments:**
- `--input_image_path` (required): Path to the input `.raw` image file.
- `--width` (required): The width of the image in pixels.
- `--height` (required): The height of the image in pixels.

**Example:**
```bash
python main.py --input_image_path barbara_gray.raw --width 512 --height 512
```

This will output the following statistics:
- Mean
- Variance
- Standard Deviation
- Minimum Pixel Value
- Maximum Pixel Value

### 2. **Developer-Friendly Testing**
For developers, a dedicated script `developer_test.py` is provided to run and experiment with the `ImageStatistics` class.

Modify the `image_path`, `width`, and `height` directly in the file:
```python
from ImageStatistics import ImageStatistics

# Modify these parameters as needed
image_path = "barbara_gray.raw"
width = 512
height = 512

image_statistics = ImageStatistics(image_path, width, height)
print(image_statistics.get_all_statistics())
```
Run the script:
```bash
python developer_test.py
```
This is ideal for debugging and customizing the inputs.

---

## File Structure
```
ImageStatistics/
├── ImageStatistics.py  # Core class to calculate image statistics
├── main.py             # CLI-based script for execution
├── developer_test.py   # Developer-friendly testing script
├── barbara_gray.raw    # Sample .raw image for testing
```

---

## Supported Image Format
- **.raw Format:**
  - Must be an 8-bit grayscale image.
  - Dimensions (width and height) must be provided.
  - File size must match the expected number of pixels (width x height). If the file contains extra bytes, they will be trimmed.

---

## Future Enhancements
1. Add support for other image formats (e.g., BMP, PGM).
2. Implement automatic dimension detection for `.raw` images (where applicable).
3. Extend functionality to handle multi-channel (color) `.raw` images.

---

## Notes
- This project is designed for 8-bit grayscale `.raw` images only.
- Ensure the `width` and `height` are accurate to avoid errors.
- For any issues, feel free to open an issue on the repository or contact the maintainer.

