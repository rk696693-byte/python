# 1) Store the given values:

# `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.

# 2) Calculate the total sum using the wrong mean:

# - Multiply `mean1` by `total_number`

# - Store it in `sum`

# - Print the sum.

# 3) Fix the sum to get the correct total:

# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`

# - Print the corrected sum.

# 4) Find the correct mean:

# - Divide `num2` by `total_number`

# - Store it in `mean2`

# - Print `mean2`.
mean1= 123
wrong_number=234
correct_number=345
total_number=456
sum=mean1*total_number
print(sum)
num2=sum-(wrong_number-total_number)
mean2=num2/total_number
print(mean2)