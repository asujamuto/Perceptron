from perceptron import Perceptron
from gui import GUI

weights = [1.2, 0.2, 1.3, 2.1]
threshold = 1

# p = Perceptron(weights, threshold, file='iris_training.txt')
p = Perceptron(weights, threshold, file='iris_training.txt', plot_disabled=False)
p.learn(epochs=3)

print("Iris-virginica: ", p.compute([7.2, 3.6, 6.1, 2.5]))

print("Iris-setosa:    ", p.compute([5.1, 3.5, 1.4, 0.2]))

p.plot_disabled = False 
p.run_test()
