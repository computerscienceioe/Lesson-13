# import matplotlib.pyplot as plt
# plt.plot([1,3,4,2,1])
# plt.show()







# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# plt.plot(numSiblings)
# plt.show()


# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# plt.plot(numSiblings,"yo")
# plt.title("Siblings")
# plt.xlabel("List index")
# plt.ylabel("Number of siblings")
# plt.show()

# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
# plt.plot(names, numSiblings, "yo")
# plt.title("Siblings")
# plt.xlabel("Student name")
# plt.ylabel("Number of siblings")
# plt.show()

# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
# plt.bar(names, numSiblings)
# plt.set_color('r')
# plt.title("Siblings")
# plt.xlabel("List index")
# plt.ylabel("Number of siblings")
# plt.show()

# plt.set_color('r')

# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
# plt.bar(names, numSiblings, color=(0,0.5,0))
# plt.title("Siblings")
# plt.xlabel("Students")
# plt.ylabel("Number of siblings")
# plt.show()

import matplotlib.pyplot as plt
numSiblings = [1, 3, 4, 2, 1]
names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
plt.scatter(names, numSiblings, color=(1,0.4,0.6,0.6))
plt.title("Siblings")
plt.xlabel("Students")
plt.ylabel("Number of siblings")
plt.show()

# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
# plt.pie(numSiblings, labels=names)
# plt.title("Siblings")
# plt.show()

# import matplotlib.pyplot as plt
# numSiblings = [1, 3, 4, 2, 1]
# names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
# age = [17, 16, 18, 17, 16]
# plt.plot(names, numSiblings, "yo")
# plt.plot(age, "rs")
# plt.legend(["Number of Siblings","Age"])
# plt.title("Siblings")
# plt.xlabel("Students")
# plt.ylabel("Number of siblings")
# plt.show()
