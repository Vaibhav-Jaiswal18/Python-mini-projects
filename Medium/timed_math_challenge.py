import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERANDS = 1
MAX_OPERANDS = 15
TOTAL_PROBLEMS = 10

def generate_problem():
    left_num = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right_num = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)

    ques = str(left_num) + " " + operator + " " + str(right_num)
    ans = eval(ques)
    return ques, ans

wrong = 0
correct = 0
print("-----------------------------------")
input("Press enter to start!")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    ques, ans = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + ques + " = ")
        if guess == str(ans):
            correct += 1
            break
        wrong += 1
        break

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("-----------------------------------")
print("Nice Work! You finished in", total_time, "Seconds and You get", correct,"correct and",wrong,"wrong.")