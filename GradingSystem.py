marks = float(input("Give your Mark: "))

if marks >= 93 and marks <= 100:
    print("A Excellent(4.00)")
elif marks >= 90 marks <= 92:
    print("A- (3.7)")
elif marks >= 87 marks <= 89:
    print("B+ (3.3)")
elif marks >= 83 marks <= 86:
    print("B Good (3.0)")
elif marks >= 80 marks <= 82:
    print("B- (2.7")
elif marks >= 77 marks <= 79:
    print(" C+ (2.3)")
elif marks >= 73 marks <= 76:
    print("C Average (2.0)")
elif marks >= 70 marks <= 72:
    print("C- (2.0)")
elif marks >= 67 marks <= 69:
    print("D+ (1.3)")
elif marks >= 60 marks <= 66:
    print("D Poor (1.0)")
elif marks >= 0 and marks <= 59:
    print("F* Failure (0.0)")
else:
    print("Not Valid.")
