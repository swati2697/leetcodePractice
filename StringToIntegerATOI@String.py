'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Valid
        "42" -> 42
        "    42" -> 42
        "9999999999999999" -> 2**31-1(int_max)
        "1234fghj" -> 1234
        
        Invalid
        "gjsdyjcg" -> 0
        "  bgibi 809" -> 0
        
        points to work:
        1. whitespaces
        2. 1 +/- symbol
        3. number
        4. random characters
        5. between min_int and max_int
        '''
        
       #OVERFLOW NOT HANDLED but works 
        i = 0 #to iterate over the string
        res = 0 #number to be formed using the digits
        sign = 1 #to determine +/- sign of the number- initializing with positive value
        INT_MAX = 2**31-1 #2147483647
        INT_MIN = -2**31 #-2147483648
        #whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        #+/- symbol
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
            
        #check numbers
        num_check = set('0123456789')#set in a python is similar to hashmap and works like a dictionary, difference being there are no key,value pairs -> only keys. Sets are used to store multiple items in a single variable.
        while i < len(s) and s[i] in num_check:
            res = res*10 + int(s[i])#int to convert string character to integer value
            i += 1
        
        res = res * sign
        #check for number constraint range and return
        return max(INT_MIN, min(res, INT_MAX))
      
      
        
        
        #OVERFLOW HANDLED - it is to be handled keeping INT_MAX and INT_MIN values in mind- number shouldn't exceed this limit
        i = 0 #to iterate over the string
        res = 0 #number to be formed using the digits
        sign = 1 #to determine +/- sign of the number- initializing with positive value
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        
        #whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        #+/- symbol
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
            
        #check numbers
        num_check = set('0123456789')#set in a python is similar to hashmap and works like a dictionary, difference being there are no key,value pairs -> only keys. 
        #Sets are used to store multiple items in a single variable.
        while i < len(s) and s[i] in num_check:
            if res > INT_MAX/10 or (res == INT_MAX/10 and int(s[i]> 7)): #res value at any point of time during iteration shouldn't exceed the value, since res is being *10 in every iteration thus we 
        #need to see if the value has reached the limit before updating the res value in the ongoing iteration.
               if sign = 1 return INT_MAX else INT_MIN
           
            res = res*10 + int(s[i])#int to convert string character to integer value
            i += 1
        
        return res * sign
     
    
    #int(s[i]> 7) is important as it keeps a check on the last digit of the res value which would be at max 7 (if sign =1) and 8 (if sign =-1),
    #either way when they both are >7, limit has been reached
    
    #Time Complexity - O(n) since iterating over the string length
    #Space Complexity - O(1) since at a time res value is being updated yet it hold the same amount of memory as it has been restricted within a certain range 
    #as determined by overflow
