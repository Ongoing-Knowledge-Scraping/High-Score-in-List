print("Welcome to the Highest Score Finder! \n")

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(f"Current Score List: \n{student_scores}")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highScore = 0

for score in student_scores:
    if score > highScore:
        highScore = score
print(f"The highest score in the list is: {highScore}")
