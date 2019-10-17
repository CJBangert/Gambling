import numpy as np
import sys
import xlrd as xl
import matplotlib.pyplot as plt

data1 = ("/mnt/c/users/tony/git/Gambling_Software/Sample_Test_1.xlsx")

wb = xl.open_workbook(data1)
sheet = wb.sheet_by_index(0)


# Spread = cell_value(i, 5)
# ATS = cell_value(i, 4)
# OU = cell_value(i, 6)
# Total = cell_value(i, 7)

data = []
x = []
y = []
z = []

for i in range (1, sheet.nrows):
  data.append([sheet.cell_value(i,5), sheet.cell_value(i,7), sheet.cell_value(i,4), sheet.cell_value(i,6)])
  x.append(sheet.cell_value(i,5))
  y.append(sheet.cell_value(i,7))
  z.append(sheet.cell_value(i,4))

color = []

for j in range(1, sheet.nrows):
  if sheet.cell_value(j,4) == 1:
    color.append('black')
  else:
    color.append('red')

plt.scatter(x, y, c = color)
plt.savefig('/mnt/c/users/tony/git/Gambling_Software/plot1.png', format='png')


print(z)







# print(data)


w1 = np.random.normal(0,1)
w2 = np.random.normal(0,1)
b = 0
    
for j in range(1,3):
    
  wd1 = 0
  wd2 = 0
  bd = 0
    
  for i in range(0,164):
    
    x1 = data[i][0]
    x2 = data[i][1]
    y1 = data[i][2]
    y2 = data[i][3]

    z = (w1*x1) + (w2*x2) + b 
      
    if data[i][2] == 0:

      wd1 = wd1 - ((-x1) / (np.exp(-z) + 1))
      wd2 = wd2 - ((-x2) / (np.exp(-z) + 1))
      bd = bd - ((-1) / (np.exp(-z) + 1))
      
    elif data[i][2] == 1:
        
      wd1 = wd1 + (x1 * (np.exp(-z))) / (1 + (np.exp(-z)))
      wd2 = wd2 + (x2 * (np.exp(-z))) / (1 + (np.exp(-z)))
      bd = bd + (np.exp(-(z))) / (1 + np.exp(-z))
    
  w1 = w1 - (wd1/164) * .01
  w2 = w2 - (wd2/164) * .01
  b = b - (bd/164) * .01
      

theta = (w1, w2, b)
  
# print(theta)


ans = []
for i in range(0,82):
  za = -(theta[0]*data[i][0]) + (theta[1]*data[i][1]) + theta[2]
  ans.append(1/(1 + np.exp(za)))

# print(ans)

































# ###Problem 1
# ###Provided function to create training data
# def simplest_training_data(n):
#   w = 3
#   b = 2
#   x = np.random.uniform(0,1,n)
#   y = 3*x+b+0.3*np.random.normal(0,1,n)
#   return (x,y)

# def simplest_training(n, k, eta):
#   #TODO: Your Code Here
#   w = np.random.normal(0, 1)
#   b = 0
#   data = simplest_training_data(n)

#   for j in range(1, k):
#     wd = 0
#     bd = 0
    
#     for i in range(0,n-1):
      
#       der = w*data[0][i] + b
#       x = data[0][i]
#       y = data[1][i]
      
#       wd = wd + (2*x*(der-y))
#       bd = bd + (2*(der-y))

#     w = w - eta*(wd/n)
#     b = b - eta*(bd/n)

#   return(w,b)

# def simplest_testing(theta, x):
#   #TODO: Your Code Here
#   theta = simplest_training(theta[0], theta[1], theta[2])
#   y = []

#   for j in range(0,x):
#     #should be close to 3j+2 based off how well training does
#     y.append((theta[0]*j + theta[1]))

#   return y
  



# ###Problem 2
# ###Provided function to create training data
# def single_layer_training_data(trainset):
#   n = 10
#   if trainset == 1:
#     # Linearly separable
#     X = np.concatenate((np.random.normal((0,0),1,(n,2)), np.random.normal((10,10),1,(n,2))),axis=0)
#     y = np.concatenate((np.ones(n), np.zeros(n)),axis=0)

#   elif trainset == 2:
#     # Not Linearly Separable
#     X = np.concatenate((np.random.normal((0,0),1,(n,2)), np.random.normal((10,10),1,(n,2)), np.random.normal((10,0),1,(n,2)), np.random.normal((0,10),1,(n,2))),axis=0)
#     y = np.concatenate((np.ones(2*n), np.zeros(2*n)), axis=0)

#   else:
#     print ("function single_layer_training_data undefined for input", trainset)
#     sys.exit()

#   return (X,y)


# def single_layer_training(k, eta, trainset):
#   #TODO: Your Code Here
#   data = single_layer_training_data(trainset)
#   if trainset == 2:
#     n = 40
#   else:
#     n = 20
  
#   w1 = np.random.normal(0,1)
#   w2 = np.random.normal(0,1)
#   b = 0
    
#   for j in range(1,k):
    
#     wd1 = 0
#     wd2 = 0
#     bd = 0
    
#     for i in range(0,n-1):
      
#       x1 = data[0][i][0]
#       x2 = data[0][i][1]
#       y = data[1][i]
#       z = (w1*x1) + (w2*x2) + b 
      
#       if data[1][i] == 0:

#         wd1 = wd1 - ((-x1) / (np.exp(-z) + 1))
#         wd2 = wd2 - ((-x2) / (np.exp(-z) + 1))
#         bd = bd - ((-1) / (np.exp(-z) + 1))
      
#       elif data[1][i] == 1:
        
#         wd1 = wd1 + (x1 * (np.exp(-z))) / (1 + (np.exp(-z)))
#         wd2 = wd2 + (x2 * (np.exp(-z))) / (1 + (np.exp(-z)))
#         bd = bd + (np.exp(-(z))) / (1 + np.exp(-z))
    
#     w1 = w1 - (wd1/n) * eta
#     w2 = w2 - (wd2/n) * eta
#     b = b - (bd/n) * eta
      

#   theta = (w1, w2, b)
  
#   return theta


# def single_layer_testing(theta, X):
#   #TODO: Your Code Here
#   data = single_layer_training_data(theta[2])
#   trained = single_layer_training(theta[0], theta[1], theta[2])
#   ans = []
#   for i in range(0,len(data[1])-1):
#     za = -(trained[0]*data[0][i][0]) + (trained[1]*data[0][i][1]) + trained[2]
#     ans.append(1/(1 + np.exp(za)))

#   return ans


# ###Problem 3
# ###Provided function to create training data
# def pca_training_data(n, sigma):
#   m = 1
#   b = 1
#   x1 = np.random.uniform(0,10,n)
#   x2 = m*x1+b
#   X = np.array([x1,x2]).T
#   X += np.random.normal(0,sigma,X.shape)
#   return X

# def pca_training(k, eta, n, sigma):
#   #TODO: Your Code Here
#   data = pca_training_data(n, sigma)
#   w = np.random.normal(0,1,4)
#   b = np.random.normal(0,0,3)

#   for j in range(1,k):
#     w1 = 0
#     w2 = 0
#     w3 = 0
#     w4 = 0
#     b1 = 0
#     b2 = 0
#     b3 = 0

#     for i in range(0,n-1):
#       x1 = data[i][0]
#       x2 = data[i][1]

#       imp = w[0]*x1 + w[1]*x2 + b[0]

#       w1 = w1 + 2*(w[2]*(imp) + b[2] - x1)*(w[2]*x1) + 2*(w[3]*(imp) + b[2] - x2)*(x1*w[3])
#       w2 = w2 + 2*(w[2]*(imp) + b[2] - x1)*(w[2]*x2) + 2*(w[3]*(imp) + b[2] - x2)*(x2*w[3])
#       b1 = b1 + 2*(w[2]*(imp) + b[2] - x1)*w[2] + 2*(w[3]*(imp)+ b[2] - x2)*w[3]

#       w3 = w3 + 2*(w[2]*(imp) + b[1] - x1)*(imp)
#       w4 = w4 + 2*(w[3]*(imp) + b[2] - x2)*(imp)
#       b2 = b2 + 2*(w[2]*(imp) + b[1] - x1)
#       b3 = b3 + 2*(w[3]*(imp) + b[2] - x2)

#     w[0] = w[0] - (w1/n)*eta
#     w[1] = w[1] - (w2/n)*eta
#     b[0] = b[0] - (b1/n)*eta

#     w[2] = w[2] - (w3/n)*eta
#     w[3] = w[3] - (w4/n)*eta
#     b[1] = b[1] - (b2/n)*eta
#     b[2] = b[2] - (b3/n)*eta

#   theta = (w,b)

#   return theta


# def pca_test(theta, X):
#   #TODO: Your Code Here
#   y = []

#   for i in range(len(X)):
#     z1 = theta[0][2]*(theta[0][0]*X[i][0] + theta[0][1]*X[i][1] + theta[1][0]) + theta[1][1]
#     z2 = theta[0][3]*(theta[0][0]*X[i][0] + theta[0][1]*X[i][1] + theta[1][0]) + theta[1][2]
#     y.append((z1,z2))

#   return y


