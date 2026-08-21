students = {
    "asra": 80,
    "sara": 90,
    "aliya": 70
}
print(students["sara"])
print(students.get("aliya"))
students["zara"] = 85
students["asra"] = 88
students.pop("aliya")
print("Total",len(students))