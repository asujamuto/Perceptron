import random 
from gui import GUI
class Perceptron: 

    def __init__(self, weights, threshold, file, turn_on_plot=False):
        self.weights = weights 
        self.threshold = threshold
        self.epoch = 0

        self.vec_training_file = []
        self.res_training_file = []
        
        self.final_weights = []
        self.final_threshold = 0

        self.gui = GUI()
        self.turn_on_plot = turn_on_plot 
        
        tmp_vec = []
        with open(file) as f:
            for line in f:
                vec = [i.strip().replace(',', '.') for i in line.split(" ") if i.strip() != '']
                tmp_vec.append(vec) 
                
            random.shuffle(tmp_vec)

            for v in tmp_vec:
                """ Przydziel vector x """
                self.vec_training_file.append([float(i) for i in v[:-1]])

                """ Zapisz rozwiązanie """
                self.res_training_file.append(int(v[-1] == "Iris-setosa"))  

        f.close()
        self.gui.add_info(self.vec_training_file, self.res_training_file)
        
    
    def compute(self, inputs):
        vec_sum = sum(i*j for i, j in zip(inputs, self.weights))
        return int(vec_sum >= self.threshold) 


    def learn(self, epochs):
        for i in range(epochs):
            for j in range(len(self.vec_training_file)):
                delta = self.res_training_file[j] - self.compute(self.vec_training_file[j])
                self.weights = [w + delta*x*0.01 for w, x in zip(self.weights, self.vec_training_file[j])]
                # self.threshold = self.threshold + (delta - self.res_training_file[i])*(-1)
                self.gui.append(self.weights, epoch=i, id=j)
                
        """  Wagi  """
        self.final_weights = self.weights 
        self.final_threshold = self.threshold

        print("Weights: ", self.final_weights)
        print("Threshold: ", self.final_threshold)
        if self.turn_on_plot == True:
            self.gui.show()

        
    def run_test(self):
        all_vec = []
        res_col = []
        with open('iris_test.txt') as f:
            for line in f:
                vec = [i.strip().replace(',', '.') for i in line.split() if i.strip()]
                try:
                    # all_vec.append([float(i) for i in vec[:-1]])  
                    all_vec.append([float(i) for i in vec[:-1]]) 

                    res_col.append(int(vec[-1] == "Iris-setosa"))  

                except ValueError as e:
                    print(f"Błąd konwersji w linii: {line.strip()}")
                    print(f"Nie można przekonwertować na float: {vec[:-1]}")
                    raise e 
        
        good_answ = 0
        for i in range(len(all_vec)):
            res = self.compute(inputs=all_vec[i])
            if(res == res_col[i]):
                good_answ += 1
            else:
                print("Przypadek błędny: wynik: ", res, " prawidłowy wynik: ", res_col[i]) 

        print("Dobre odpowiedzi: ", good_answ)
        print("Dokładnośc: ", good_answ/len(all_vec))
        