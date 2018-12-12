import numpy as np

def get_power_level(x, y, serial_number):
    """
    - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    - Begin with a power level of the rack ID times the Y coordinate.
    - Increase the power level by the value of the grid serial number (your puzzle input).
    - Set the power level to itself multiplied by the rack ID.
    - Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    - Subtract 5 from the power level.

    (3, 5)
    - The rack ID is 3 + 10 = 13.
    - The power level starts at 13 * 5 = 65.
    - Adding the serial number produces 65 + 8 = 73.
    - Multiplying by the rack ID produces 73 * 13 = 949.
    - The hundreds digit of 949 is 9.
    - Subtracting 5 produces 9 - 5 = 4
    """
    rack_id = x + 10
    power_level = rack_id * (rack_id * y + serial_number)
    power_level = (power_level % 1000) // 100
    power_level -= 5
    return power_level


def convolve2d(image, kernel):
    # http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html
    # This function which takes an image and a kernel
    # and returns the convolution of them
    # Args:
    #   image: a numpy array of size [image_height, image_width].
    #   kernel: a numpy array of size [kernel_height, kernel_width].
    # Returns:
    #   a numpy array of size [image_height, image_width] (convolution output).
    output = np.zeros_like(image)            # convolution output
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    image_padded[:] = -np.inf
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y, x] = (kernel * image_padded[y:y+3, x:x+3]).sum()
    return output



def get_array(serial_number):
    array = np.zeros(shape=(300,300))
    for i in range(300):
        for j in range(300):
            array[i, j] = get_power_level(i, j, serial_number)
    return array


def get_max_subsquare(size):
    kernel = np.ones(shape=(size, size))
    convolved = convolve2d(ARRAY, kernel)
    xmax, ymax = np.unravel_index(np.argmax(convolved), dims=ARRAY.shape)
    return xmax, ymax, convolved[xmax, ymax]


def part1():
    xmax, ymax, _ = get_max_subsquare(3)
    return xmax - 1, ymax - 1


if __name__ == '__main__':
    SERIAL_NUMBER = 9445
    ARRAY = get_array(SERIAL_NUMBER)
    print(part1())
