#Written by Thien K. M. Bui <buik@carleton.edu>
#parsing data to be used for DTM
import pandas as pd
import matplotlib.pyplot as plt 

def main():
    print("Demographic Transition Model")
    df_ref = pd.read_csv("./dem_indicator_ref.csv")
    df_data = pd.read_csv("./dem_indicator.csv")

    #transforming year to date_time type
    df_data['Time'] = pd.to_datetime(df_data['Time'], format='%Y')
    print(df_data.dtypes['Time'])
    #grouping the dataframe
    df_grouped = df_data.groupby('Location')
    for country, frame in df_grouped:
        domain = frame['Time']
        range = frame['IMR']
        plt.plot(domain,range)
    plt.show()
    # df_grouped.plot()
    # print(df_grouped.loc[:, "Location"])
if __name__ == "__main__":
    main()