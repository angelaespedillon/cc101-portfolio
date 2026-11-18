count = 1
total = 0
while count <= 3:
    score = int(input("Enter score: "))
    total = total + score
    count= count + 1
average = total / 3
if average >= 75 :
    print("PASSED")
else:
    print("FAILED")
print("Average: " + str(average))