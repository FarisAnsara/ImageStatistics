from ImageStatistics import ImageStatistics
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Calculate statistics for a grey-scale .raw image (8-bit)."
    )
    parser.add_argument(
        "--input_image_path", 
        type=str, 
        required=True,
        help="Path to the input .raw image file."
    )
    parser.add_argument(
        '--width',
        type=int,
        required=True,
        help="Width of the image in pixels."
    )
    parser.add_argument(
        '--height',
        type=int,
        required=True,
        help="Height of the image in pixels."
    )

    args = parser.parse_args()

    input_image_path = args.input_image_path
    width = args.width
    height = args.height

    image_statistics = ImageStatistics(input_image_path, width, height)
    stats = image_statistics.get_all_statistics()

    print(f"Statistics for {input_image_path}:")
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
