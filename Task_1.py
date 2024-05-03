# task 1
#-----List----
a=[10,20,30,40,50]
# Adding
a.append(60)
# removing
a.remove(60)
# Modify
a[4]=60

#----Dictionary----
b={1:10,2:20,3:30,4:40,5:50}
# Adding
b[6]=60
# Removing
del b[6]
# Modifying
b[5]=60

#----set----
c={10,20,30,40,50}
# Adding
c.add(60)
# Removing
c.remove(60)
# Modifying
old_value = 30
new_value = 60
if old_value in c:
    c.remove(old_value)
    c.add(new_value)

print(a,b,c)