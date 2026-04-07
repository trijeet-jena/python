name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
reg_no = input("Enter registration number: ")

print("Enter marks for 5 subjects:")
marks = []
for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\n--- Student Details ---")
print(f"Name: {name}")
print(f"DOB: {dob}")
print(f"Registration No: {reg_no}")
print(f"Total Marks: {total:.2f}")
print(f"Percentage: {percentage:.2f}%")

if percentage >=50:
    print("Result: Pass")
else:  
     print("Result: Fail")



