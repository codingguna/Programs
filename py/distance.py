import math

def calculate_distances(image):
  center_x, center_y = 2, 2
  center_value = image[center_x][center_y]

  for x in range(len(image)):
    for y in range(len(image[0])):
      if x == center_x and y == center_y:
        continue  # Skip the center pixel itself

      pixel_value = image[x][y]
      
      # Euclidean distance
      euclidean_distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
      
      # D4 distance
      d4_distance = abs(x - center_x) + abs(y - center_y)
      
      # D8 distance
      d8_distance = max(abs(x - center_x), abs(y - center_y))
      
      print(f"Pixel at ({x}, {y}) with value {pixel_value}:")
      print(f"  Euclidean distance: {euclidean_distance:.2f}")
      print(f"  D4 distance: {d4_distance}")
      print(f"  D8 distance: {d8_distance}")
      print()

# Example usage
image = [[3,1,2,1,4],
         [2,2,0,2,3],
         [1,2,1,1,1],
         [1,0,1,2,1],
         [2,3,1,2,0]]

calculate_distances(image)