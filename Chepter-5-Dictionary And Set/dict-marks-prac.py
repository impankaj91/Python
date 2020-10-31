#Practical : Print Marks of Student According To Name.
p_marks=int(input("Enter Marks of Pankaj  :"))
r_marks=int(input("Enter Marks of Rahul   :"))
v_marks=int(input("Enter Marks of Vikash  :"))
d_marks=int(input("Enter Marks of Dherya  :"))
m_marks=int(input("Enter Marks of Meet    :"))
sub_marks={'Pankaj':p_marks ,'Rahul':r_marks , 'Vikash':v_marks , 'Dherya':d_marks
,'Meet':m_marks}
print(sub_marks.items()) # Print All Students Marks With Name.
stud_name=input("Enter Student Name :")
print(sub_marks.get(stud_name)) #print Desireble Student Mark.
u_stud_name=input("Enter Student Name :") #Enter the Name Want TO Update Mark.
u_marks=int(input("Update Mark:")) # Enter Value Of updated Marks.
update_mark=sub_marks.update({u_stud_name:u_marks})
print(sub_marks.items())
