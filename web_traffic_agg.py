import pandas as pd
import string

# fetch data from public URL provided
traffic_url_root = "https://public.wiwdata.com/engineering-challenge/data/"
file_name_list = list(string.ascii_lowercase)

imported_traffic_dfs = []

for file in file_name_list:
    url = traffic_url_root + file + '.csv'
    data = pd.read_csv(url)
    imported_traffic_dfs.append(data)

# combine all files into a single dataframe
columns = ['drop', 'length', 'path', 'user_agent', 'user_id']
imported_traffic = pd.DataFrame(columns=columns)

imported_traffic = pd.concat(imported_traffic_dfs)

# aggregate traffic metric by user, pivoting on path
web_traffic_pivot = pd.pivot_table(
                            imported_traffic, 
                            values='length', 
                            index='user_id', 
                            columns='path',
                            aggfunc='sum'
                            )

# export results as CSV to local path
web_traffic_pivot.to_csv(
                path_or_buf='web_traffic_pivot.csv',
                index=True
                )