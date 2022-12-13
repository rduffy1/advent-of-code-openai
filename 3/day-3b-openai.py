def solve_puzzle(filename):
  # Open the file and read the contents
  with open(filename, 'r') as f:
    lines = f.readlines()
  
  # Initialize the sum of priorities to 0
  sum_of_priorities = 0
  
  # Iterate over the lines in groups of three
  for i in range(0, len(lines), 3):
    # Get the lines for the current group
    group_lines = lines[i:i+3]
    
    # Initialize the set of common item types to the set of all characters in the first line
    common_items = set(list(group_lines[0]))
    
    # Iterate over each line in the group
    for line in group_lines:
      # Find the common item types between the current line and the set of common items
      common_items = common_items.intersection(set(line))
      
      # If there are no common item types, we can break out of the loop
      if len(common_items) == 0:
        break
    
    # If there are common item types, add the priority of the first one to the sum
    if len(common_items) > 0:
      sum_of_priorities += get_priority(common_items.pop())
        
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
