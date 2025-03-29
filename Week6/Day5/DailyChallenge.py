import pandas as pd

# Upload CSV file
df = pd.read_csv("globalterrorismdb_0718dist.csv",sep=',',encoding="latin-1")

# Show first lines
df.head()