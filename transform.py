import pandas as pd

def transform_data(songs):
    # Convert the list of songs into a Pandas DataFrame
    df = pd.DataFrame(songs, columns=["song_name", "album_name"])
    
    # Remove any rows with missing or duplicate data
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    return df
