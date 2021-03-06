import matplotlib.pyplot as plt

class Plot_graph:
    def __init__(self,coin_name, df,kind='line'):
        plt.figure()
        self.kind=kind
        self.df=df
        self.coin_name=coin_name
    def plot_graph(self):
        plt.figure()
        self.df.plot(kind=self.kind, title="CryptoCurrency price", figsize=(15, 10))
        plt.savefig(self.coin_name)
        #plt.show(block=False)
        plt.close('all')
        print("Done")