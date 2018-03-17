import matplotlib.pyplot as plt
import time
class Plot_graph:
    def __init__(self, df,kind='line'):
        plt.figure()
        self.kind=kind
        self.df=df
    def plot_graph(self):
        plt.figure()
        self.df.plot(kind=self.kind, title="CryptoCurrency price", figsize=(15, 10))
        plt.savefig('Koinex.png')
        #plt.show(block=False)
        time.sleep(60)
        #plt.close('all')
        print("Done")