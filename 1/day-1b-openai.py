def solve_puzzle(file_name):
  # Open the file and read the lines
  with open(file_name) as f:
    lines = f.readlines()

  # Initialize the elves list with a single element (for the first Elf)
  elves = [0]

  # Initialize a list to store all of the Elves and their total Calories
  all_elves = []

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

      # Add the current Elf and their total Calories to the list of all Elves
      all_elves.append((current_elf, elves[current_elf]))

  # Sort the list of all Elves by the number of Calories they are carrying, in descending order
  all_elves.sort(key=lambda x: x[1], reverse=True)

  # Return the top three Elves and their total Calories
  return all_elves[:3]


top_elves = solve_puzzle("input.txt")

# Print the number of the top three Elves and their total Calories
for elf, calories in top_elves:
  print("Elf %d is carrying %d Calories" % (elf, calories))

# Calculate and print the total Calories carried by the top three Elves
total_calories = sum([c for e, c in top_elves])
print("The top three Elves are carrying a total of %d Calories" % total_calories)
