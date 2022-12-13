
def solve_puzzle(file_name):
  # Open the file and read the lines
  with open(file_name) as f:
    lines = f.readlines()

  # Initialize the elves list with a single element (for the first Elf)
  elves = [0]

  # Initialize variables to keep track of the Elf with the most Calories
  # and their total Calories
  max_calories = 0
  max_calorie_elf = 0

  # Initialize a variable to keep track of the current Elf we are processing
  current_elf = 0

  # Iterate over the lines in the file
  for line in lines:
    # If the line is empty, we are starting a new Elf's inventory
    if line == "\n":
      # Increment the current_elf variable
      current_elf += 1

      # Add a new element to the elves list for the new Elf
      elves.append(0)
    else:
      # Otherwise, we are reading a food item with a certain number of Calories

      # Convert the line to an integer
      calories = int(line)

      # Update the current Elf's total Calories
      elves[current_elf] += calories

      # If the current Elf has more Calories than the Elf with the most Calories,
      # update the max_calories and max_calorie_elf variables
      if elves[current_elf] > max_calories:
        max_calories = elves[current_elf]
        max_calorie_elf = current_elf

  # Return the Elf with the most Calories and their total Calories
  return (max_calorie_elf, max_calories)


elf, calories = solve_puzzle("input.txt")
print("Elf %d is carrying the most Calories, with a total of %d Calories" % (elf, calories))




