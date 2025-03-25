from perceptron import Perceptron
from gui import GUI
import random

weights = [1.2, 0.2, 1.3, 2.1]
threshold = 1
p = Perceptron(weights, threshold, file='iris_training.txt', turn_on_plot=False)

p.run_test()

turn_on_plot = False
epochs = 3
user_vec = []

while True:
    
    print("""Wybierz jedną z dostęnych opcji: \n
        0. Oceń dokładność
        1. Zaklasyfikuj czy to Iris-Setosa 
        2. Wytrenuj Model Perceptronu 
        3. Ustaw wektor wag (aktualny wektor wag: {})
        4. Wylosuj wektor wag
        5. Włącz wizualizacje ({})
        6. Ustaw ilość epoch (aktualna liczba epok: {})
        7. Zakończ """.format(p.weights, turn_on_plot, epochs))
    choice = int(input("Wpisz numer: ").replace(',', ' '))

    if(choice == 0):
        p.run_test()
    elif(choice == 1):
        user_vec = list(map(float, input("Podaj vector wejść: ").split()))
        print("Iris-setosa:    ", p.compute(user_vec))

    elif(choice == 2):
        p.learn(epochs=epochs)
    
    elif(choice == 3):
        weights = list(map(float, input("Podaj vector wag: ").split()))
        p.weights = weights
        
    elif(choice == 4):
        p.weights = [random.uniform(-2, 2) for _ in range(4)]
    
    elif(choice == 5):
        turn_on_plot = str(input("Włączyć wizualizacje? [y/N]")).strip(" ").upper() == "Y"
        p.turn_on_plot = turn_on_plot 

    elif(choice == 6):
        epochs = int(input("Wpisz liczbę epoch: "))
        
    elif(choice == 7):
        break; 

