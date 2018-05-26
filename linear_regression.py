import pandas
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv("data.csv")

x_df = df["x"]
y_df = df["y"]

plt.scatter(x_df, y_df)

def meanSquaredError(slope, intercept, x_values, y_values):
    sq_err = 0
    N = len(y_values)
    for i in range(N):        
        prediction = (slope * x_values[i] + (intercept) )
        sq_err += ( prediction - y_values[i] )**2
    return sq_err / float(N)

def graph_line( slope, intercept , x_range):  
    x = np.array(x_range)  
    y = slope * x + (intercept) 
    plt.plot(x, y)

def gradient_step(slope, intercept, x_values, y_values, learning_rate):
    slope_gradient = 0
    intercept_gradient = 0
    N = float(len(y_values))
    for i in range(int(N)):
        x = x_values[i]
        y = y_values[i]
        error = y - ( slope * x + (intercept) )
        slope_gradient += - 2 / N * x * error # This is the partial derivative of MSE w.r.t slope / theta_1
        intercept_gradient += - 2 / N * error # This is the partial derivative of MSE w.r.t intercept / theta_0
    new_slope = slope - (learning_rate * slope_gradient)
    new_intercept = intercept - (learning_rate * intercept_gradient)
    return [new_slope, new_intercept]

def gradient_descent(slope, intercept, x_values, y_values, learning_rate, iterations):
    starting_slope = slope
    starting_intercept = intercept
    for i in range(iterations):
        starting_slope, starting_intercept = gradient_step(starting_slope, starting_intercept, x_df, y_df, learning_rate)
        if i % 10 == 0:
            print ("After %s iterations\nSlope: %s\nIntercept:%s\nMSE: %s\n" %(i, starting_slope, starting_intercept, meanSquaredError(starting_slope, starting_intercept, x_df, y_df) ))
    
    return [starting_slope, starting_intercept]

# This is the graph of the line y = mx + b where m and b = 0, our first guess
graph_line(0,0,range(int(x_df.min()) - 1, int(x_df.max()) + 1))

#This calls our gradient descent function
final_slope, final_intercept = gradient_descent(0, 0, x_df, y_df, 0.0001, 101)

#This graphs all our data and our final line of best fit found out by the gradient descent
graph_line(final_slope, final_intercept , range(int(x_df.min()) - 1, int(x_df.max()) + 1))

#This shows us the mean sqaured error of our best fit line
plt.text(23, 100, "MSE: " + str(meanSquaredError(final_slope, final_intercept, x_df, y_df)))

try:
    plt.show()
except KeyboardInterrupt:
    print("Shutting down program...")