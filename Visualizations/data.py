import pandas as pd
import os

cities = "../Resources/cities.csv"

cities_file_path = os.path.join(cities)

cities_csv = pd.read_csv(cities_file_path)

cities_csv.to_html("table.html", index=False, classes=["table","table-striped","table-hover"])


