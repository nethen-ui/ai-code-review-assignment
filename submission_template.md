# Task 1

Findings:
The issue I encountered in Task 1 was related to incorrect averaging due to the way the count variable was calculated.

In the original code, the #count variable was set to the length of #orders, which included both valid and
cancelled orders. This led to incorrect division because the total amount of valid orders was being divided by the count of all orders, including the cancelled ones which made the average result inaccurate.

Fixes:
Two potential fixes were considered to solve this problem. 
1. Keep the count variable as is and adjust it by reducing 1 each time the order was cancelled, OR
2. Start the count variable at 0 and add 1 to count everytime the order is valid.

For both cases we need to check if #count becomes 0 so that we don't face division-by-zero error.

I chose the second method because because it is more readable and straight forward. It is clearly indicates 
that #count represents the number of cancelled orders, while on the first one is a bit 
confusing to understand for readers.

# Task 2

Finding:
The issue on the second task is related to security problems. 
Since there could be different arrangement of characters in emails it doesn't mean it is a valid email address if it includes the "@" symbol    .

The original code would accep any string conatining an @ symbol, regardless of the rest of the characters. 
For example: @1233hjkh would be accepted as a valid email. 

Fixes:
To solve this issue, I used regular expressions to figure out if an email is valid or not.
The updated approach ensures that the email :
1. Starts with one or more letters, digits, or certain symbols (._%+-)
2. Contains the @ symbol followed by a domain name (gmail)
3. Ends with a dot (.) followed by a top-level domain (com, et, org) that consists of atleast 2 characters

This validation will improve the security problem of the original code.

# Task 3

Finding:
The issue with Task 3 is similar to the one in Task 1.
the count variable was calculated as the length of #values which included the None values.

As a result, the code was dividing the sum of valid values by the total number of elements, including
None values. This led to incorrect average. 

Fixes:
To solve this issue we have two possible fixes like before:
1. Leave the count variable unchanged and adjust it by reducing it by 1 for every None value encountered.
2. Start the count variable from 0 and increment it only if the value is different from None.

I chose the second solution for the same reason as in Task 1: clarity.
In the updated code, #count only represents valid values which makes it possible to calculate
the average of valid measurements only as intended.