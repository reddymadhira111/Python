import pandas as pd 
import seaborn as sns
import glob
from problem1 import PreparedData
from problem2 import problem2_df

wx_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/wx_data/*.txt'
yld_data = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/yld_data/*.txt'
answers = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers'

wx_files = glob.glob(wx_data)
yld_files = glob.glob(yld_data)

wx_header = ['Date', 'MAX', 'MIN', 'PRECIP']
yld_header = ['YEAR', 'CORN_YIELD']

NAN = -9999

def show_station(wx_file):
	return wx_file.split('/')[-1].split('.')[0]

WX = PreparedData()


class EfficientProblem3Solver(object):
    def __init__(self):
        self.base_df = problem2_df
        self.stations = WX.stations
        self.yrs = WX.years
        self.station_records = {'AVG_LOW':NAN,'AVG_HIGH':NAN,'TOTAL_PRECIP':NAN}
        self.df = None
        self.station_masks = None  
        self.list_dfs = []
        self.sum_df = None
        
    def set_station_masks(self):
        self.station_masks = {}
        for station in self.stations:
            self.station_masks[station] = self.base_df['STATION'].apply(lambda x: (x == station))
    
    def process_file(self, station):
        self.station_records = {'AVG_LOW':NAN, 'AVG_HIGH':NAN, 'TOTAL_PRECIP':NAN}
        self.df = self.base_df[self.station_masks[station]]
        rdf = pd.DataFrame(list(self.df.apply(lambda row: self.find_record_yrs(row), axis=1)))
        self.list_dfs.append(pd.merge(self.df,rdf,on='YEAR'))
        
    def find_record_yrs(self, row):
        record_yr = {'AVG_LOW':0, 'AVG_HIGH':0, 'TOTAL_PRECIP':0}
        for key in self.station_records.keys():
            if row[key] > self.station_records[key]:
                self.station_records[key] = row[key]
                record_yr[key] = 1
        result = {'YEAR':row['YEAR'],
                  'RLOW':record_yr['AVG_LOW'],
                  'RHIGH':record_yr['AVG_HIGH'],
                  'RPRECIP':record_yr['TOTAL_PRECIP']}
        return result
    
    def sum_year(self, year, targets=['RLOW','RHIGH','RPRECIP']):
        result = {'RLOW':None,
                  'RHIGH':None,
                  'RPRECIP':None,
                  'YEAR':[year]}
        rsum = self.df[targets][self.df['YEAR'] == year].sum()
        for target in targets:
            result[target] = [rsum[target]]
        self.list_dfs.append(pd.DataFrame(result))
    
    def find_solution(self):
        self.set_station_masks()
        
        self.list_dfs = []
        for station in self.stations:
            self.process_file(station)
        self.df = pd.concat(self.list_dfs)
        
        self.list_dfs = []
        for yr in self.yrs:
            self.sum_year(yr)
        self.sum_df = pd.concat(self.list_dfs)
        
ep3s = EfficientProblem3Solver()
ep3s.find_solution()

problem3_output = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/YearHistogram.out'
problem3_png =  'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/YearHistogram.png'
ep3s.sum_df[['YEAR','RHIGH','RLOW','RPRECIP']].to_csv(problem3_output, 
                                     sep='\t', 
                                     encoding='utf-8', 
                                     index=False)

get_ipython().magic('matplotlib inline')

p3 = ep3s.sum_df[['YEAR','RHIGH','RLOW','RPRECIP']].set_index('YEAR')
p3_plot = p3.plot.bar()
fig = p3_plot.get_figure()
fig.savefig(problem3_png, format='png', dpi=1200)
