red = int(input("Enter number of red balls: "))
blue = int(input("Enter number of blue balls: "))
white = int(input("Enter number of white balls: "))

total = red + blue + white

prob_second_white_given_first_white = white / total

print("\nProbability that the second ball is white given that the first ball is white:")
print(round(prob_second_white_given_first_white, 3))
