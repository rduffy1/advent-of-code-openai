def solve_puzzle(filename):
  # Open the file and read the contents
  with open(filename, 'r') as f:
    lines = f.readlines()
  
  # Initialize the sum of priorities to 0
  sum_of_priorities = 0
  
  # Iterate over each line in the file
  for line in lines:
    # Get the first half of the line
    first_half = line[:len(line)//2]
    # Get the second half of the line
    second_half = line[len(line)//2:]
    
    # Iterate over each character in the first half
    for char in first_half:
      # If the character is in the second half, add its priority to the sum
      if char in second_half:
        sum_of_priorities += get_priority(char)
        # We found the common item type for this rucksack, so we can break out of the loop
        break
        
  # Return the sum of priorities
  return sum_of_priorities
  
# Helper function to get the priority of a given character
def get_priority(char):
  # Get the ASCII value of the character
  ascii_value = ord(char)
  
  # If the character is lowercase, its priority is its ASCII value minus 96
  if ascii_value >= 97 and ascii_value <= 122:
    return ascii_value - 96
  # If the character is uppercase, its priority is its ASCII value minus 38
  elif ascii_value >= 65 and ascii_value <= 90:
    return ascii_value - 38
  # If the character is not a letter, return 0
  else:
    return 0

# Example usage
print(solve_puzzle('input.txt'))
