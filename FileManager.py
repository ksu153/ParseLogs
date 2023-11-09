import pprint
import pandas as pd

class FileManager:
    def __init__(self):
        pass

def createdataframe(date_list: object, state_list: object, description_list: object, excep_list: object) -> object:
    # data frame python
    df = pd.DataFrame(columns=['Date', 'State', 'Description'])

    df['Date'] = pd.Series(date_list)
    df['State'] = pd.Series(state_list)
    df['Description'] = pd.Series(description_list + excep_list)
    df.to_csv("output.txt")
    pprint.pprint(df)