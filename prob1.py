digits = []
nums = [61,12,153,124,15]
# Create dictionary with sublist of digits for number
##### get digits as strings
for number in nums:
        digits.append((list(str(number))))
################## get digits as ints
for item in digits:
        for digit in range(len(item)):
            item[digit] = int(item[digit])
            
## lambda fucntion
added_digits = list(map(lambda x: sum(x[:]), digits))

#output
print(added_digits)

