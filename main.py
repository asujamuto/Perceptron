from perceptron import Perceptron

weights = [1.2, 0.2, 1.3, 2.1]
inputs = [5.1, 3.5, 1.4, 0.2]
threshold = 1

# p = Perceptron(weights, threshold, file='iris_training.txt')
p = Perceptron(weights, threshold, file='iris_training.txt')
p.learn(epochs=70)

#Iris-virginica
print("Iris-virginica: ", p.compute([7.2, 3.6, 6.1, 2.5]))

#Iris-setosa
print("Iris-setosa:    ", p.compute([5.1, 3.5, 1.4, 0.2]))

p.run_test()
