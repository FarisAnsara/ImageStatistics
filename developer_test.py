from ImageStatistics import ImageStatistics

image_path = "barbara_gray.raw"  # Change this to any .raw file
width = 512  # Change width if using a different image
height = 512  # Change height if using a different image

try:
    image_statistics = ImageStatistics(image_path, width, height)
    stats = image_statistics.get_all_statistics()
    print(f"Statistics for {image_path}:")
    for key, value in stats.items():
        print(f"{key}: {value}")

except Exception as e:
    print(f"Error: {e}")
