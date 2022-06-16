import pandas as pd


if __name__ == "__main__":
	df = pd.read_csv("20220325_CAR.csv",dtype=str)

	df.to_parquet('df.linelist.140000000.gzip',compression='gzip')