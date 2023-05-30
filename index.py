print("Mark Sheet:)")
computertotalmarks = 100
sciencetotalmarks = 100
mathstotalmarks = 100
englishtotalmarks = 100
computerobtmarks = 99
scienceobtmarks = 70
mathsobtmarks = 70
englishobtmarks = 80
total = computertotalmarks + sciencetotalmarks + mathstotalmarks + englishtotalmarks
obtain = computerobtmarks + scienceobtmarks + mathsobtmarks + englishobtmarks
print("Computer Marks", computerobtmarks, "out of", computertotalmarks)
print("Science Marks", scienceobtmarks, "out of", sciencetotalmarks)
print("Maths Marks", mathsobtmarks, "out of", mathstotalmarks)
print("Engish Marks", englishobtmarks, "out of", englishtotalmarks)
print("Obtained Marks", obtain, " out of Total Marks", total)
percentage = obtain / total * 100
a = percentage
print("%.2f" % percentage)
if percentage >= 70:
    print("passed")
else:
    print("failed")
    
    if percentage>=80:
    print("A-One Grade")
elif percentage>=70:
    print("A Grade")
elif percentage>=60:
    print("B Grade")
elif percentage>=50:
    print("C Grade")
else:
    print("Failed")

