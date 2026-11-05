numbers = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# Desi tarika
total = 0

for i in numbers:
    for j in i:
        for k in j:
            total = total + k

print(total)




# python way to do this question
# total = sum(k for i in numbers for j in i for k in j ) # here k is the number to add.
# print(total) 
