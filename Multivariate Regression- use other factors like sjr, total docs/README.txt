1. Assignment 2 is very similar to Assignment 1, the only difference is that this 
time we have to take into consideration multiple variables, and all of their combinations.
For that, I've used the concept of Multivariate Regression.

2. I've generated all combinations of variables using python library Itertools. Then, I
evaluated all coefficient matrices (1 of each combiation) for my training data set(80%)
and used these too predict impact factors for testing data set(20%).

3. Now that I have actual and predicted impact factors for my testing data, I evauluate
Mean Absolute Error(MAE), Mean Squared Error(MSE) and Root Mean Squared Error(RMSE) and
stored all these values for each combination i ERRORS_all.csv.

4. In RMSE_min.csv, I sorted my data set on the basis of RMSE.

5. In MAE_min.csv, I sorted my data set on the basis of MAE.

