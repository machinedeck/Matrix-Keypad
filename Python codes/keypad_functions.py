import numpy as np

# This function is used for performing MDAS calculation from the given string
def opr(u):
    # Define the operations
    plus = "+"
    minus = "-"
    times = "*"
    divide = "/"
    operations = [plus, minus, times, divide]

    # Determine if the text is only digit. If yes then return the answer as is
    if u.isdigit() == True:
        answer = u

    # Else, perform the next steps
    else:
        # If it contains multiple operations within the string, check first 
        # if the first and last elements are not operations because each operation
        # require to have more than one operands.
        if u[0].isdigit() == True and u[-1].isdigit() == True:

            # Code for extracting the operations used in the string
            indices = []
            for index1, operation in enumerate(operations):
                for index2, element in enumerate(u):
                    # Scan each operation on the string
                    if operation == element:
                        # If found, record the operation and the location
                        indices.append([index1, index2])
            indices = np.array(indices)

            # This is to check that there are operands for each operation, or each
            # operand is not followed by another one
            truthval = []
            for i in indices[:, 1]:
                a1 = u[i-1]
                a2 = u[i+1]
                if a1.isdigit() == True and a2.isdigit() == True:
                    truthval.append(0)
                else:
                    truthval.append(1)
                    
            truthval = np.array(truthval)
            # Get the metric for determining if there is any repeated operation or
            # combination of operations next to each other
            truthval = truthval.sum()

            # Check. If yes, then return an error answer
            if truthval > 0:
                answer = "Syntax ERROR"

            # Otherwise, proceed with calculation.
            else:
                # Check if there is only one operation. Then perform it right away
                if indices.shape[0] == 1:
                    num1, num2 = int(u[:indices[0][1]]), int(u[indices[0][1] + 1:])
                    # Addition
                    if indices[0][0] == 0:
                        answer = num1 + num2
                    # Subtraction
                    elif indices[0][0] == 1:
                        answer = num1 - num2
                    # Multiplication
                    elif indices[0][0] == 2:
                        answer = num1 * num2
                    # Division
                    elif indices[0][0] == 3:
                        # Check if division by zero
                        if num1 != 0 and num2 == 0:
                            answer = "Division by zero!"
                        # Check if undefined
                        elif num1 == 0 and num2 == 0:
                            answer = "Undefined"
                        # Otherwise
                        else:
                            answer = num1 / num2

                            if answer == int(answer):
                                answer = int(answer)

                # If more than one operation
                else:
                    # Since after scanning, the recorded position are not in order
                    # Arrange them in ascending order to extract the numbers in between
                    # the operations

                    # Get the correct arrangement of locations
                    ord = np.argsort(indices[:, 1])
                    # Reorganize the correct order of operations within the string
                    ops = indices[:, 0][ord]

                    ords = np.stack((ord, np.sort(indices[:, 1])), axis = 1)
                    # Holder for the numbers
                    numbers = []
                    for index, val in enumerate(ords[:, 1]):
                        # Just check if the first element is not an operation
                        if val != 0:
                            # For number extraction, get the number before the
                            # operation. For the last operation, get the one after
                            # it as well

                            # Last operation
                            if index == len(ords[:, 1]) - 1:
                                # Before the operation
                                num = int(u[ords[:, 1][index - 1] + 1:val])
                                numbers.append(num)

                                # After the operation
                                num = int(u[val+1:])
                                numbers.append(num)

                            # First operation, start with the start of the string
                            elif index == 0:
                                num = int(u[:val])
                                numbers.append(num)
                    
                            # Operations that are not the first and last
                            else:
                                num = int(u[ords[:, 1][index - 1] + 1:val])
                                numbers.append(num)

                    # Use lists to copy the files above
                    # These will be used to perform the operation step by step
                    opsnew = list(ops).copy()
                    numbers1 = numbers.copy()
                    
                    # Start first with multiplication which is referred as 2
                    # This is a loop which perform all the multiplications within
                    # the string

                    # The following loop is similar to multiplication below but 
                    # for division instead
                    prompt = "Continue"
                    while 3 in opsnew:
                        op = 0
                        n = 0
                        while op != 3:
                            op = opsnew[n]

                            # Just do division when op == 3 to avoid division by zero and error
                            if op == 3:
                                # Check if division by zero
                                if numbers1[n] != 0 and numbers1[n+1] == 0:
                                    val = "Division by zero!"
                                # Check if both numerator and denominator are zero
                                elif numbers1[n] == 0 and numbers1[n+1] == 0:
                                    val = "Undefined"
                                # Otherwise
                                else:
                                    val = numbers1[n] / numbers1[n + 1]
                            n += 1
                        # Make the answer division by zero or undefined if detected
                        if val == "Division by zero!" or val == "Undefined":
                            answer = val
                            prompt = "Stop"
                            break
                        else:
                            opsnew.pop(n-1)
                            del numbers1[n-1:n+1]
                            numbers1.insert(n-1, val)
                            prompt = "Continue"

                    # Do this only if answer is not division by zero or undefined
                    if prompt == "Continue":
                        # This code stops when there are no more multiplication
                        while 2 in opsnew:
                            # Initialize the variables
                            op = 0
                            n = 0
                            # This one scans the operations from the operations sequence
                            # If it detects multiplication, it performs the operation
                            # below and re-update the index
                            # After the operation it stops this nested loop
                            while op != 2:
                                # Get the value of the next operation
                                op = opsnew[n]
    
                                # Apply multiplication
                                val = numbers1[n] * numbers1[n + 1]
                                n += 1
    
                            # Now, remove the multiplication operation recently performed
                            opsnew.pop(n-1)
                            # Delete the numbers involved in the previous operation
                            del numbers1[n-1:n+1]
                            # Then insert the new product
                            numbers1.insert(n-1, val)
    
                            # Although the multiplication stops, this is still within the
                            # another loop. This bigger loop checks again for 2 in the
                            # updated sequence of operations and performs the next set of
                            # multiplication.
                        
                        
                        # For subtraction, the process is to replace it with addition
                        # but make the number after subtraction operation negative
                        for index, i in enumerate(opsnew):
                            # Check if the operation is negative
                            if i == 1:
                                # If it is, change the corresonding number to negative
                                numbers1[index + 1] = -1 * numbers1[index + 1]
    
                        # All that is left is an list of numbers and the operation
                        # involved now is only addition. The list is converted to array
                        # then use the sum feature to get the answer
                        numbers1 = np.array(numbers1)
                        # Get the total sum after performing all the multiplication and
                        # division operations
                        answer = numbers1.sum()

                        if answer == int(answer):
                            answer = int(answer)
            
            # return answer

        # For this one, show error answer if there are operations that are written
        # next to each other
        else:
            answer = "Syntax ERROR"
            # return answer

    # Return the answer
    return answer

# Conversion
# As Arduino sends information from 1-16, they are converted to equivalent symbols
# which the Tkinter interface interprets
bvals = ["1", "2", "3", "AC", "4", "5", "6", "+", "7", "8", "9", "-", "*", "0", "/", "="]
def conv(val):
    # Return the converted symbol
    return bvals[val - 1]