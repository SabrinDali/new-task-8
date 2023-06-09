
import subject_module
import student_module

# Creating objects of Subject class
subject1 = subject_module.Subject("Math", 90)
subject2 = subject_module.Subject("PE", 80)
subject3 = subject_module.Subject("Science", 75)



student1 = student_module.Student("Zakaria", 18, "Gaza")
student2 = student_module.Student("Ahmed", 17, "Khanyunis")
student3 = student_module.Student("Ali", 19, "Jabalia")


student1.add_mark(80)
student1.add_mark(90)
student1.add_mark(72)

student2.add_mark(89)
student2.add_mark(77)
student2.add_mark(63)

student3.add_mark(75)
student3.add_mark(76)
student3.add_mark(96)

average1 = student1.calc_average()
average2 = student2.calc_average()
average3 = student3.calc_average()

print("Average for", student1.name, ":", average1)
print("Average for", student2.name, ":", average2)
print("Average for", student3.name, ":", average3)
