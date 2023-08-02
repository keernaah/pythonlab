#Q1:List comprehension
#divisible by 3
emp_age=[22,25,24,30,27,22,20,18,20]
div_by_3=[n for n in emp_age if n % 3==0]
print("Elements that are divisible by 3:",div_by_3)
#Square of even numbers in a list:
even_square=[n**2 for n in emp_age if n%2 == 0]
print("Square of even numbers in a list:",even_square)
#Sum of digits of all EVEN numbers in a list
sum_square=sum([n**2 for n in emp_age if n%2 == 0])
print("Sum of digits of all EVEN numbers in a list:",sum_square)
#Remove duplicate numbers in a list
new_list=[]
for n in emp_age:
    if n not in new_list:
        new_list.append(n)
print("New list after removing duplicate values:",new_list)        
#Create a dictionary to store the details of your company employees (name as key and birthdate as value).
emp_dob={"Keerthana":"5 February 2001","Deepthi":"16 November 2002","Meghana":"25 June 2001",
         "Anurag":"8 August 2002","Chari":"10 March 2000","Kevin":"31 December"}
def birthDate(birthday):
    print( emp_dob.get(birthday,"employee not found"))
birthDate("Chari")


