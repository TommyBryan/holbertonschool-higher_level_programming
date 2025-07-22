s1 = "Best School"
s2 = "Best School"
print(s1 is s2)         # Likely True

s3 = "Best " + "School" # Still likely interned
print(s1 is s3)         # Might be True

s4 = "".join(["Best", " School"])
print(s1 is s4)         # Usually False (not interned)


l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)

#
