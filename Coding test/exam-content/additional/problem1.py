import pandas as pd 
import glob

wx_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/wx_data/*.txt'
yld_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/yld_data/*.txt'
answers = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers'


wx_files = glob.glob(wx_data)
yld_files = glob.glob(yld_data)

wx_header = ['Date', 'MAX', 'MIN', 'PRECIP']
yld_header = ['YEAR', 'CORN_YIELD']

NAN = -9999

#for file in wx_files:

def show_station(wx_file):
	return wx_file.split('/')[-1].split('.')[0]

class PreparedData(object):
	def __init__(self):
		self.base_df = self.aggregate_wx()
		self.stations = [ show_station(wx_file) for wx_file in wx_files]
		self.years = list(self.base_df['YEAR'].sort_values().drop_duplicates())
		self.masks = self.find_masks()

	def aggregate_wx(self):
		agg_list = []
		for wx_file in wx_files:
			wx = show_station(wx_file)
			wx_df = pd.read_csv(wx_file,
								delim_whitespace=True,
								header=None,
								names=wx_header)
			wx_df['YEAR'] = wx_df['DATE'].apply(lambda yyyymmdd: int(str(yyyymmdd)[:4]))
			wx_df['STATION'] = pd.Series([wx]*wx_df.shape[0])
			agg_list.append(wx_df)
		agg_df = pd.concat(agg_list)
		return agg_df

	def find_masks(self):
		masks = {'year':{},'station':{}}
		for station in self.stations:
		    masks['station'][station] = self.base_df['STATION'].apply(lambda val: (val == station))
		for year in self.years:
		    masks['year'] = self.base_df['YEAR'].apply(lambda val: (val == year))
		return masks

	def get(self, wx_file):
		station = show_station(wx_file)
		mask = self.masks['station'][station]
		return self.base_df[mask]		

WX = PreparedData()

def wx_filter(row):
	return  ((row['HIGH'] != NAN) and (row['LOW'] != NAN) and (row['PRECIP'] == NAN))

def no_of_days(wx_file):
	df = WX.get(wx_file)
	station = show_station(wx_file)
	rows_find = df[df.apply(lambda row: wx_filter(row), axis=1)]
	return {'STATION': station, 'COUNT':rows_find.shape[0]}

def problem1_out():
	results = {'STATION': [], 'COUNT':[]}
	for wx_file in wx_files:
		res = no_of_days(wx_file)
		for key in results.keys():
			results[key].append(res[key])
	return results

problem1 = problem1_out()
problem1_df = pd.DataFrame(problem1, columns=problem1.keys())
problem1_df = problem1_df.sort_values(by='STATION', ascending=True)

problem1_output =  'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/MissingPrcpData.out'
problem1_df[['STATION', 'COUNT']].to_csv(problem1_output,
										sep='\t',
										encoding='utf-8',
										index=False)




















