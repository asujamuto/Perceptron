class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = [0] * (input_size + 1)  # +1 for bias term

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = [1] + x  # Add bias term
        weighted_sum = sum(w * xi for w, xi in zip(self.weights, x))
        return self.activation(weighted_sum)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = [1] + xi  # Add bias term
                prediction = self.activation(sum(w * x for w, x in zip(self.weights, xi)))
                self.weights = [w + self.learning_rate * (target - prediction) * x for w, x in zip(self.weights, xi)]

if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1] 
    perceptron = Perceptron(input_size=2)
    perceptron.train(X, y)

    for xi in X:
        print(f"Input: {xi}, Predicted Output: {perceptron.predict(xi)}")
