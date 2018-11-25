import numpy as np
import numpy.linalg as linalg


y60 = []    
y40 = []
x60 = []
x40 = [] 
h = []


dataSet=np.loadtxt("petrol_data.txt",delimiter=',')
x=dataSet[:,:4]
y=dataSet[:,4]
print("Imprimiendo y verificando los valores del dataset\n",x, "\n")
print("Imprimiendo y verificando los valores del dataset\n",y, "\n")



n =  int((np.size(dataSet))/len(dataSet[0])) #Numero de filas
p60 = round(n*0.60)
p40 = n-p60
for i in range(0,p60):
    x60.append(x[i])
    y60.append(y[i])
x60 = np.array(x60).reshape(np.shape(x60))
y60 = np.array(y60).reshape(np.shape(y60))
x60 = np.c_[np.ones(p60),x60]

theta = (linalg.inv((x60.T)@x60)@(x60.T))@y60

for i in range(p60,n):
    x40.append(x[i])
    y40.append(y[i])
x40 = np.array(x40).reshape(np.shape(x40))
x40 = np.c_[np.ones(p40),x40]
y40 = np.array(y40).reshape(np.shape(y40))

error = 0
for i in range(p40):
    model = theta[0]*x40[i][0] + theta[1]*x40[i][1] + theta[2]*x40[i][2]+ theta[3]*x40[i][3]+ theta[4]*x40[i][4]
    print("Output:",i+1)
    print("Model output:",model)
    print("Real price: "+str(y40[i])+"\n")
    h.append(model)
for i in range(p40):
    error = error + (abs((y40[i] - h[i]) / y40[i]))
error = (error/p40)*100
print("MAPE:"+str(error)+("%"))
print("H:",theta)