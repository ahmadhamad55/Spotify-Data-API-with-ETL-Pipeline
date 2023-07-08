from services.extract import extract_data
from services.transform import transform_data
from services.load import load_data

if __name__ == "__main__":
    # Extract data for the Weezer artist
    songs = extract_data("3jOstUTkEu2JkjvRdBA5Gu")
    
    # Transform the data into a DataFrame
    df = transform_data(songs)
    
    # Load the data into the database
    load_data(df)
