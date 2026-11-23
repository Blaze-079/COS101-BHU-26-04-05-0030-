numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)


# Sum function
def total(numbers):
    answer = 0
    for num in numbers:
        answer += num
    return answer


# Mean function
def mean(numbers):
    return total(numbers) / len(numbers)


# Median and Mode functions 
def median_mode(numbers):
    numbers.sort()

    n = len(numbers)

    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]

    mode = numbers[0]

    for num in numbers:
        if numbers.count(num) > numbers.count(mode):
            mode = num

    return median, mode


print("List:", numbers)
print("Sum:", total(numbers))
print("Mean:", mean(numbers))

median, mode = median_mode(numbers)

print("Median:", median)
print("Mode:", mode)
