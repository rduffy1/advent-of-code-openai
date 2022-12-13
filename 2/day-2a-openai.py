def rock_paper_scissors(input_file: str) -> int:
    # Initialize the total score to 0
    total_score = 0

    # Open the input file for reading
    with open(input_file, "r") as f:
        # Read the lines from the input file
        lines = f.readlines()

        # For each line in the input file
        for line in lines:
            # Split the line into the opponent's move and our response
            opponent, response = line.split()

            # Translate the opponent's move and our response to Rock, Paper, or Scissors
            if opponent == "A":
                opponent = "Rock"
            elif opponent == "B":
                opponent = "Paper"
            elif opponent == "C":
                opponent = "Scissors"

            if response == "X":
                response = "Rock"
            elif response == "Y":
                response = "Paper"
            elif response == "Z":
                response = "Scissors"

            # Check if the round is a draw
            if opponent == response:
                # If the round is a draw, add 3 to the total score
                total_score += 3
            else:
                # If the round is not a draw, check if we win
                if (opponent == "Rock" and response == "Paper") or (opponent == "Paper" and response == "Scissors") or (opponent == "Scissors" and response == "Rock"):
                    # If we win, add 6 to the total score
                    total_score += 6

            # Calculate the score for the shape we selected
            if response == "Rock":
                # If we chose Rock, add 1 to the total score
                total_score += 1
            elif response == "Paper":
                # If we chose Paper, add 2 to the total score
                total_score += 2
            elif response == "Scissors":
                # If we chose Scissors, add 3 to the total score
                total_score += 3

    # Return the total score
    return total_score



total_score = rock_paper_scissors("input.txt")
print(total_score)