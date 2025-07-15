# Performs slicing on the input sequence using the provided start, stop, and step indices.

# Args:
#     sequence (Sequence): The sequence (such as a list, tuple, or string) to be sliced.
#     start (int, optional): The starting index of the slice. Defaults to None (beginning of sequence).
#     stop (int, optional): The ending index of the slice (exclusive). Defaults to None (end of sequence).
#     step (int, optional): The step size between elements. Defaults to None (step of 1).

# Returns:
#     Sequence: A new sequence containing the sliced elements.

# Example:
#     # The indexing format is: sequence[start:stop:step]
#     sliced = slice_sequence([1, 2, 3, 4, 5], 1, 4, 2)  # Returns [2, 4]

credit_number = "1234-5678-9875-7951"

print(credit_number[4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
# This will count the numbers by 2 like 13-6897-91   
print(credit_number[::2])

last_digits = credit_number[-4:]
print(f"XXX-XXX-XXX-{last_digits}")

# This will display the account number by reverse
credit_number = credit_number[::-1]
print(credit_number)