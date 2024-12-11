# User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        # Remove leading zeros to simplify calculations
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')

        # Handle edge cases where inputs become empty strings
        if not s1: return s2 if s2 else "0"
        if not s2: return s1

        # Ensure s1 is the longer string
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        # Pad the shorter string with zeros on the left
        s2 = s2.zfill(len(s1))

        result = []
        carry = 0

        # Perform binary addition from right to left
        for i in range(len(s1) - 1, -1, -1):
            bit1 = int(s1[i])
            bit2 = int(s2[i])
            total = bit1 + bit2 + carry
            result.append(str(total % 2))  # Append the current binary bit
            carry = total // 2  # Calculate carry for the next iteration

        # If there's a carry left after the loop, append it
        if carry:
            result.append(str(carry))

        # Reverse the result as it was constructed backwards
        return ''.join(reversed(result))


# Main program
if __name__ == "__main__":
    # Take user input
    s1 = input("Enter the first binary string: ").strip()
    s2 = input("Enter the second binary string: ").strip()
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Perform the addition
    result = solution.addBinary(s1, s2)
    
    # Display the result
    print(f"The result of adding {s1} and {s2} is: {result}")
