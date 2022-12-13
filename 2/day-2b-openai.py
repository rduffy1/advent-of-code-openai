def rock_paper_scissors(input_file: str) -> int:
    # Initialize the total score to 0
    total_score = 0

    # Open the input file for reading
    with open(input_file, "r") as f:
        # Read the lines from the input file
        lines = f.readlines()

        # For each line in the input file
        for line in lines:
            # Split the line into the opponent's move and the desired outcome
            opponent, outcome = line.split()

            # Translate the opponent's move to Rock, Paper, or Scissors
            if opponent == "A":
                opponent = "Rock"
            elif opponent == "B":
                opponent = "Paper"
            elif opponent == "C":
                opponent = "Scissors"

            # Determine the shape to choose based on the desired outcome
            if outcome == "Z":
                # If we need to win, choose Rock if the opponent chose Paper or Scissors, or choose Paper if the opponent chose Rock or Scissors, or choose Scissors if the opponent chose Rock or Paper
                if opponent == "Rock":
                    response = "Paper"
                elif opponent == "Paper":
                    response = "Scissors"
                elif opponent == "Scissors":
                    response = "Rock"
            elif outcome == "Y":
                # If we need to end the round in a draw, choose the same shape as the opponent
                # If we need to end the round in a draw, choose the same shape as the opponent
                response = opponent

            else:
                # If we need to lose, choose Rock if the opponent chose Scissors or Paper, or choose Paper if the opponent chose Rock or Scissors, or choose Scissors if the opponent chose Rock or Paper
                if opponent == "Rock":
                    response = "Scissors"
                elif opponent == "Paper":
                    response = "Rock"
                elif opponent == "Scissors":
                    response = "Paper"

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