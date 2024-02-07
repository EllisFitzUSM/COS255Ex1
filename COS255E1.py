# Author: Ellis Fitzgerald
# Date: Feb 6, 2024
# COS : 255 Experiment 1
# Number converter.

# Individual digit to corresponding value.
digitToValue : dict[str, int] = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15 # etc...
}

# Value to individual digit.
valueToDigit = dict((v,k) for k,v in digitToValue.items())

# Function runs on entry point.
def main() -> None:
    prompt_conversion_type()

# Prompts the user for a conversion type.
def prompt_conversion_type() -> None:
    print("\nWelcome to number converter for COS 255 Experiment 1 by EF")
    
    while True:
        print("Select the conversion you wish to do 1-6. ")
        try:
            uncastedInput = input(' 1. Binary to Decimal \n 2. Decimal to Binary \n 3. Hex to Decimal \n 4. Decimal to Hex \n 5. Hex to Binary \n 6. Binary to Hex \n')
            conversionType = int(uncastedInput)
            if conversionType <= 6 and conversionType >= 1: 
                break
            else:
                print("\"" + str(uncastedInput) + "\" is not a number within 1-6. Please try again \n")
        except:
            print("\"" + str(uncastedInput) + "\" is not a number within 1-6. Please try again \n")

    if conversionType == 1:
        print(binary_to_decimal())
    elif conversionType == 2:
        print(decimal_to_binary())
    elif conversionType == 3:
        print(hex_to_decimal())
    elif conversionType == 4:
        print(decimal_to_hex())
    elif conversionType == 5:
        print(hex_to_binary())
    else:
        print(binary_to_hex())

    returnedInput = input("Convert a different number? Y/N\n")
    if 'y' in returnedInput or 'Y' in returnedInput:
        main()


# Helper function to get a number to a decimal.
def base_n_to_decimal(value : any, base : int) -> int: 
    decimalNumber : int = 0
    while True:
        try:
            valueString : str = str(value)
            position : int = 0
            for i in reversed((range(0, len(valueString)))):
                digitAtPos : int = digitToValue[valueString[i]]
                if digitAtPos >= 0 and digitAtPos < base:
                    decimalNumber += ((base**position) * digitAtPos)
                    position += 1
                else:
                    raise "Digit is not within bounds of the base.\n"
            break
        except:
            print("Failed to convert value, please try again.\n")

    return decimalNumber

# Helper function to get a decimal to base n.
def decimal_to_base_n(decimalValue : int, base : int) -> str:
    quotient : int = decimalValue // base
    remainder : int = decimalValue % base
    if quotient == 0:
        return valueToDigit[remainder]
    baseNNumber : str = str(remainder)
    while quotient >= 1:

        prevQuotient = quotient
        quotient = prevQuotient // base
        remainder = prevQuotient % base
        baseNNumber = valueToDigit[remainder] + baseNNumber

    return baseNNumber

# Binary to Decimal.
def binary_to_decimal() -> int:
    inputValue : any = input("You have chosen Binary to Decimal, input digits 0-1\n")
    result : int = base_n_to_decimal(inputValue, 2)
    print(result)
    return result

# Decimal to Binary.
def decimal_to_binary() -> int:
    while True:
        try:
            inputValue : int = int(input("You have chosen Decimal to Binary, input digits 0-9\n"))
            result : str = decimal_to_base_n(inputValue, 2)
            print(result)
            return result
        except:
            print("Please input only base-10 numbers for this conversion.")

# Hex to Decimal.
def hex_to_decimal() -> int:
    inputValue : any = input("You have chosen Hex to Decimal, input digits 0-F\n")
    result : int = base_n_to_decimal(inputValue, 16)
    print(result)
    return result
    

# Decimal to Hex.
def decimal_to_hex() -> str:
    while True:
        try:
            inputValue : int = int(input("You have chosen Decimal to Hex, input digits 0-9.\n"))
            result : str = decimal_to_base_n(inputValue, 16)
            print(result)
            return result
        except:
            print("Please input only base-10 numbers for this conversion.")

# Hex to Binary.
def hex_to_binary() -> int:
    inputValue : any = input("You have chosen Hex to Binary, input digits 0-F\n")
    hexToDecimal : int = base_n_to_decimal(inputValue, 16)
    decimalToBinary : str = decimal_to_base_n(hexToDecimal, 2)
    return int(decimalToBinary)

# Binary to Hex.
def binary_to_hex() -> str:
    inputValue : int = int(input("You have chosen Binary to Hex, input digits 0-1.\n"))
    binaryToDecimal : int = base_n_to_decimal(inputValue, 2)
    decimalToHex : str = decimal_to_base_n(binaryToDecimal, 16)
    return decimalToHex

# Trigger entry point.
if __name__ == "__main__":
    main()