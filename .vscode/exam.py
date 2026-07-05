# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.

# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':

# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):

# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"
medical_cause=input("enter the medical cause in y or n")
if medical_cause==y:
    print("student is allow to write their exam")
else:
    atten=int(input("enter your percentage"))
    if attent>=75:
        print("allow")
    else:
        print("not allowed")