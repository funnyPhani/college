import seaborn as sns
#import tensorflow as tf
import matplotlib.pyplot as plt
import  matplotlib.style as style
style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

df=sns.load_dataset('iris')
print(df.sample(6))
for i in df.iloc[:,0:4].columns:
    for j in df.iloc[:,0:4].columns:
        sns.FacetGrid(df,hue='species',size=5).map(sns.scatterplot,i,j).add_legend()
        plt.show()
plt.tight_layout()


