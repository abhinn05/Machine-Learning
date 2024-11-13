import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


class BivariateGaussian():
  def __init__(self, mean_x, mean_y, var_x, var_y, cov):
    self.mean_x = mean_x
    self.mean_y = mean_y
    self.var_x = var_x
    self.var_y = var_y
    self.cov = cov

  def calculate_pdf(self, x, y):
    return multivariate_normal([self.mean_x, self.mean_y], [[self.var_x, self.cov], [self.cov, self.var_y]]).pdf([x, y])

  def marginal_pdf_x(self, x):
    return multivariate_normal([self.mean_x, self.mean_y], [[self.var_x, self.cov], [self.cov, self.var_y]]).pdf([x, self.mean_y])

  def marginal_pdf_y(self, y):
    return multivariate_normal([self.mean_x, self.mean_y], [[self.var_x, self.cov], [self.cov, self.var_y]]).pdf([self.mean_x, y])

  def plot_pdf_contour(self):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[self.calculate_pdf(x, y)
                 for x, y in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])
    plt.contour(X, Y, Z)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Contour Plot of the Joint PDF')
    plt.show()


distribution = BivariateGaussian(0, 0, 1, 1, 0.5)
pdf_value = distribution.calculate_pdf(1.5, 2.0)
marginal_pdf_x = distribution.marginal_pdf_x(1.0)
marginal_pdf_y = distribution.marginal_pdf_y(1.0)
distribution.plot_pdf_contour()
print(pdf_value)
