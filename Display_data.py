import Koinex_Get_data
import Fetch_time
import Koinex_GUI
import pandas as pd
import json
import time
import Plot_graph
import multiprocessing

def backend():
    time=Fetch_time.Fetch_time()
    Koinex = {}
    while True:
        curr_time = time.currentTime()
        url1=Koinex_Get_data.Getdata("https://koinex.in/api/ticker")
        url1.getdatafromurl()
        finaldict={curr_time:url1.convertdatafromurl().get('prices')}
        Koinex.update(finaldict)
        df = pd.read_json(json.dumps(Koinex))
        plot_graphs(df)

def plot_graphs(df):
    coins=['BTC','LTC','XRP']
    for coin in coins:
        graph = Plot_graph.Plot_graph(coin, df.transpose()[coin])
        graph.plot_graph()
    time.sleep(60)
def frontend():
    Koinex_GUI.Koinex_GUI().getCoin()
def main():

    backend_process = multiprocessing.Process(target=backend(), args=())
    backend_process.start()

    gui_process = multiprocessing.Process(target=frontend(), args=())
    gui_process.start()

    backend_process.join()
    gui_process.join()


    print("whatever")

if __name__ == '__main__':
    main()