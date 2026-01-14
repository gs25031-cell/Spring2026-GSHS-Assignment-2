import numpy as np

def logistic_regression(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray) -> np.ndarray:
    '''
    Implements the logistic regression algorithm.

    Parameters:
        - x_train: Training features of shape (n_samples, 2).
                    For this assignment, each training sample has two features: [feature1, feature2]
        - y_train: Training labels (0/1)
                    All the predictions will be binary (0 or 1), since it is Logistic Regression.
        - x_test: Test features of shape (n_samples, 2).

    Returns:
        y_pred: Predicted labels for the test set
    '''
    # Your code here
    def f(z):
        return 1/(1+np.exp(-z))
    x=x_train
    y=y_train
    m,n=X.shape

    a,b=(0.001,300)
    for_in range(b):
      z=x*p+q
      r=f(z)
      dp=(x.T*(r-y))/m
      dq=np.sum(r-y)/m

      p=p-a*dp
      q=q-a*dq
    t=f(x_test*w+b)
    if t>=0.5: ans=1
    else: ans=0
    return ans
    
