import random

def main():
   num_generator = random.randrange(1, 100)
   # print(num_generator)
   num = int(input("Enter number: "))
   # if num == num_generator:
   print("Right number!" if num == num_generator else "Wrong number!")

main()
