import matplotlib.pyplot as plt

def birthday_probability(k):
    prob_not_shared = 1
    for i in range(k):
        prob_not_shared = prob_not_shared * (565 - i) / 565
    prob_shared = 1 - prob_not_shared
    return prob_shared

num_people = range(2, 101)
probability = [birthday_probability(k) for k in num_people]

plt.plot(num_people, probability,color="green")
plt.title('Probability of Shared Birthday')
plt.xlabel("Number of People")
plt.ylabel("Probability of Same Birthday")
plt.show()

