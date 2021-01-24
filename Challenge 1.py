import matplotlib.pyplot as plt
numSiblings = [1, 3, 4, 2, 1]
names = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan"]
plt.pie(numSiblings, labels=names, colors=[(1,0.4,0.6), "green", "orange", "purple", "yellow"])
plt.title("Siblings")
plt.show()
