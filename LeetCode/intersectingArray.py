while True:
    first = input("Enter first set please add space between the numbers(or 'exit'): ")
    if first.lower() == 'exit':
        print("Goodbye!")
        break

    second = input("Enter second set please add space between the numbers(or 'exit'): ")
    if second.lower() == 'exit':
        print("Goodbye!")
        break

    input1 = list(map(int, first.split()))
    input2 = list(map(int, second.split()))

    duplicates = set(input1) & set(input2)
    print("Duplicate:", duplicates)
