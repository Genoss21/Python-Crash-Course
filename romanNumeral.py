romanValues = { 'I': 1, 'V': 5, 'X': 10, 
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000 
                   }

def romanToInt(roman):
    total = 0 
    i = 0
    explanation = []
    
    while i < len(roman):
        if i + 1 < len(roman) and romanValues[roman[i]] < romanValues[roman[i + 1]]:
            pair = roman[i] + roman[i + 1]
            value = romanValues[roman[i + 1]] - romanValues[roman[i]]
            explanation.append(f"{pair} = {value}")
            total += value
            i += 2
        else:
            value = romanValues[roman[i]]
            explanation.append(f"{roman[i]} = {value}")
            total += value
            i += 1
    
    return total, explanation

while True:
    romanInput = input("Please enter a Roman numeral (or type 'exit' to quit): ").upper()
    
    if romanInput == "EXIT":
        print("Goodbye!")
        break

    if all(char in romanValues for char in romanInput):
        result, explanation = romanToInt(romanInput)
        print(f"Input: {romanInput}")
        print(f"Output: {result}")
        
        if len(explanation) > 1:
            explanation_str = ", ".join(explanation[:-1]) + " and " + explanation[-1]
        else:
            explanation_str = explanation[0]
        
        print(f"Explanation: {explanation_str}")
    else:
        print("Invalid input: contains non-Roman Characters.")