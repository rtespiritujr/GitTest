import pandas as pd
import os

if __name__ == "__main__":
	latest = [x for x in os.listdir() if x.endswith(".csv")][0]
	df = pd.read_csv(latest,dtype=str)
	df.to_parquet('df.linelist.140000000.gzip',compression='gzip')
	print("Done")