from  sklearn import  linear_model


class mylinear:

    def test(self):

        reg = linear_model.LinearRegression()
        reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
        reg.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
        print(reg.coef_)

if __name__ == '__init__':
   mylinear.test()
