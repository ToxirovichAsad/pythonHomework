import numpy as np
from PIL import Image


#task1 
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
fahrenheit_temps = np.array([32, 68, 100, 212, 77])
celsius_temps = vectorized_conversion(fahrenheit_temps)
print("Celsius Temperatures:", celsius_temps)

#task2
def number_power(a,b):
    return a**b
vectorized_power = np.vectorize(number_power)
a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
result = vectorized_power(a,b)
print("Result:", result)
#task3
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

# Solving for x, y, z
solution = np.linalg.solve(A, B)

# Print the solution
print("Solution (x, y, z):", solution)
#task4
C= np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

D = np.array([12, -5, 15])

# Solving for l1, l2, l3
solution = np.linalg.solve(C, D)

# Print the solution
print("Solution (l1, l2, l3):", solution)

import numpy as np
from PIL import Image

def save_img(arr, name, mode='RGB'):
    """Saves the image array as a file."""
    img = Image.fromarray(arr.astype(np.uint8), mode)
    img.save(f'{name}.jpg')
    img.show()

def flip_image(img_arr, direction="horizontal"):
    """Flips the image either horizontally or vertically."""
    if direction == "horizontal":
        return img_arr[:, ::-1]  # Flip left-right
    elif direction == "vertical":
        return img_arr[::-1]  # Flip top-bottom
    else:
        raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

def add_noise(img_arr, noise_level=30):
    """Adds random noise to the image."""
    noise = np.random.randint(-noise_level, noise_level, img_arr.shape, dtype=np.int16)
    noisy_img = np.clip(img_arr + noise, 0, 255)  # Ensure valid pixel range
    return noisy_img.astype(np.uint8)

def brighten_channels(img_arr, value=40):
    """Brightens the image by increasing the intensity of all channels."""
    return np.clip(img_arr + value, 0, 255).astype(np.uint8)

def apply_mask(img_arr, mask_size=100):
    """Applies a black mask (0, 0, 0) to the center of the image."""
    h, w, _ = img_arr.shape
    center_x, center_y = w // 2, h // 2
    x1, x2 = center_x - mask_size // 2, center_x + mask_size // 2
    y1, y2 = center_y - mask_size // 2, center_y + mask_size // 2
    img_copy = img_arr.copy()  # Avoid modifying original array
    img_copy[y1:y2, x1:x2] = (0, 0, 0)
    return img_copy

# Load Image
with Image.open('birds.jpg') as img:
    img_arr = np.array(img)

# Apply transformations
flipped_horizontally = flip_image(img_arr, "horizontal")
flipped_vertically = flip_image(img_arr, "vertical")
noisy_img = add_noise(img_arr)
brightened_img = brighten_channels(img_arr)
masked_img = apply_mask(img_arr)

# Save transformed images
save_img(flipped_horizontally, 'flipped_horizontally')
save_img(flipped_vertically, 'flipped_vertically')
save_img(noisy_img, 'noisy_img')
save_img(brightened_img, 'brightened_img')
save_img(masked_img, 'masked_img')
