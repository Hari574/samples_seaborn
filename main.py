import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

rs = np.random.RandomState(10)
d = rs.normal(size=10)

def draw_hist_with_kde():
    sns.histplot(d, kde=True, color='r')


def draw_hist_with_rug():
    # sns.distplot(d, rug=True, hist=True, kde=True)
    sns.displot(d, rug=True, color='orange', kind='hist')

if __name__=="__main__":
    # draw_hist_with_kde()
    # draw_hist_with_rug()
    
    plt.show()
    read = input('Enter to exit')