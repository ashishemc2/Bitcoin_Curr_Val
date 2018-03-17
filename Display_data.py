import Koinex_Get_data
import Fetch_time
import Koinex_GUI
import pandas as pd
import json
import matplotlib.pyplot as plt
import Plot_graph
def main():

    time=Fetch_time.Fetch_time()
    coin = Koinex_GUI.Koinex_GUI().getCoin()
    print coin

    Koinex={}
    while True:
        curr_time = time.currentTime()
        url1=Koinex_Get_data.Getdata("https://koinex.in/api/ticker")
        url1.getdatafromurl()
        finaldict={curr_time:url1.convertdatafromurl().get('prices')}
        Koinex.update(finaldict)
        df = pd.read_json(json.dumps(Koinex))
        graph=Plot_graph.Plot_graph(df.transpose()[coin])
        graph.plot_graph()
if __name__ == '__main__':
    main()