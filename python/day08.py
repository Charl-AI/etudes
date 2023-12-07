import argparse
from typing import Literal


class SpaceImage:
    """The Space Image Format is (L x H x W), where L is the number of layers"""

    def __init__(self, data: list[int], height: int, width: int) -> None:
        assert len(data) % (height * width) == 0
        num_layers = len(data) // (height * width)

        self.layers = []
        for i in range(num_layers):
            layer = []
            for j in range(height):
                row = []
                for k in range(width):
                    row.append(data[i * height * width + j * width + k])
                layer.append(row)
            self.layers.append(layer)

    @property
    def shape(self) -> tuple[int, int, int]:
        return len(self.layers), len(self.layers[0]), len(self.layers[0][0])

    def __repr__(self):
        for layer in self.layers:
            print("")
            for row in layer:
                print(row)

    def flatten_layers(self) -> list[list[int]]:
        """Convert to (L x HW)"""

        layers = []
        for layer in self.layers:
            layers.append([item for sublist in layer for item in sublist])
        return layers

    def render_image(self) -> None:
        """Convert to (H x W) by interpreting the transparency map:
        0 -> black, 1 -> white, 2 -> transparent. Layer 0 is in the
        front, and transparent pixels are overridden by the first
        colour underneath them."""

        image = self.layers[0]
        for layer in self.layers[1:]:
            for i, row in enumerate(layer):
                for j, pixel in enumerate(row):
                    if image[i][j] == 2:
                        image[i][j] = pixel

        # replace 0s with spaces and 1s with hashes for readability

        for i, row in enumerate(image):
            for j, pixel in enumerate(row):
                if pixel == 0:
                    image[i][j] = " "
                elif pixel == 1:
                    image[i][j] = "#"

        for row in image:
            print("")
            for pixel in row:
                print(pixel, end="")


def get_input_data(file_path: str) -> list[int]:
    with open(file_path, "r") as f:
        return [int(char) for char in f.read().strip()]


def count_zeros_per_layer(image: SpaceImage) -> list[int]:
    counts = []
    for layer in image.flatten_layers():
        counts.append(layer.count(0))
    return counts


def argmin(lst: list[int]) -> int:
    return min(range(len(lst)), key=lst.__getitem__)


def main(question: Literal["a", "b"], file_path: str):
    data = get_input_data(file_path)
    image = SpaceImage(data, 6, 25)

    if question == "a":
        zeros_per_layer = count_zeros_per_layer(image)
        min_layer = image.flatten_layers()[argmin(zeros_per_layer)]
        num_ones = min_layer.count(1)
        num_twos = min_layer.count(2)
        print(f"Answer: {num_ones * num_twos}")

    elif question == "b":
        image.render_image()

    else:
        raise ValueError(f"Invalid question: {question}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
