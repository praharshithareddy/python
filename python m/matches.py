def match(s1,s2):
 count=0
 
 for i in range(min(len(s1),len(s2))):
    if a1[i].lower()==s2[i].lower():
     count=count+1
 return count
s1="what"
s2="watch"
print("total number of matches:")
print(match(s1,s2))
