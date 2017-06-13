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


class EfficientProblem4Solver(object):
    def __init__(self):
        self.base_df = problem2_df
        self.stations = WX.stations
        self.yield_df = pd.read_csv(yld_files[0], 
                                    delim_whitespace=True, 
                                    header=None, 
                                    names=yld_header)
        self.df = None
        self.station_masks = ep3s.station_masks 
        self.list_corrs = []
        
    def process_file(self, station):
        self.df = self.base_df[self.station_masks[station]]
        station_corr = self.find_corr(station)
        self.list_corrs.append(station_corr)
        
    def find_corr(self,station):
        rmap = {'AVG_LOW':'LOW_YIELD',
                'AVG_HIGH':'HIGH_YIELD',
                'TOTAL_PRECIP':'PRECIP_YIELD'}
        result = {'LOW_YIELD':None,'HIGH_YIELD':None,'PRECIP_YIELD':None,'STATION':station}
        merged_df = pd.merge(self.df,self.yield_df,on='YEAR')
        for key in rmap.keys():
            rkey = rmap[key]
            result[rkey] = merged_df[[key,'CORN_YIELD']].corr(method='pearson').iloc[0][1]
        return result
    
    def find_solution(self):
        self.list_corrs = []
        for station in self.stations:
            self.process_file(station)
        self.df = pd.DataFrame(self.list_corrs)
        self.df.sort_values(by=['STATION'], ascending=True)
        
ep4s = EfficientProblem4Solver()
ep4s.find_solution()

problem4_output = answers_folder + '/Correlations.out'
ep4s.df[['STATION','HIGH_YIELD','LOW_YIELD','PRECIP_YIELD']].to_csv(problem4_output, 
                                     sep='\t', 
                                     encoding='utf-8', 
                                     index=False)
