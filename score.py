scores = list(map(int, input("Enter scores: ").split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Total =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)