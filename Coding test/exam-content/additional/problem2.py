import pandas as pd 
import glob
from problem1 import PreparedData

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

class EfficientProblem2Solver(object):
    def __init__(self):
        self.df = None
        self.yrs = None
        self.yr_masks = None
        self.description = {'AVG_LOW':[],
                            'AVG_HIGH':[],
                            'TOTAL_PRECIP':[],
                            'YEAR':[]}
        
    def describe_values(self, wx_file):
        self.df = WX.PreparedData.get(wx_file)
        self.find_years()
        self.set_yr_masks()
        self.description['YEAR'].extend(self.yrs)
        self.description['AVG_LOW'].extend(self.find_mean('LOW'))
        self.description['AVG_HIGH'].extend(self.find_mean('HIGH'))
        self.description['TOTAL_PRECIP'].extend(self.find_sum('PRECIP'))
        self.round_description()
        return self.description
      
    def find_years(self):
        self.yrs = list(self.df['YEAR'].drop_duplicates())

    def set_yr_masks(self):
        self.yr_masks = {}
        for yr in self.yrs:
            self.yr_masks[yr] = self.df['YEAR'].apply(lambda val: (val == yr))
        
    def find_mean(self, column_key):
        result = []
        mask_nan = self.df[column_key].apply(lambda val: self.wx_nan_filter(val))
        for yr in self.yrs:
            mask_yr = self.yr_masks[yr]
            result.append(self.df[column_key][mask_nan & mask_yr].mean())
        return result
        
    def find_sum(self, column_key):
        result = []
        mask_nan = self.df[column_key].apply(lambda val: self.wx_nan_filter(val))
        for yr in self.yrs:
            mask_yr = self.yr_masks[yr]
            result.append(self.df[column_key][mask_nan & mask_yr].sum())
        return result
        
    def wx_nan_filter(self, value):
        return not (value == NAN)
    
    def round_description(self):
        for key in ['AVG_LOW', 'AVG_HIGH', 'TOTAL_PRECIP']:
                self.description[key] = map(lambda x: round(x, 2), self.description[key])


def find_problem2_results():
    results = {'STATION':[],
               'AVG_LOW':[],
               'AVG_HIGH':[],
               'TOTAL_PRECIP':[],
               'YEAR':[]}
    for wx_file in wx_files:
        wx = show_station(wx_file)
        efps = EfficientProblem2Solver()
        file_description = efps.describe_values(wx_file)
        num_of_yrs = len(file_description['YEAR'])
        results['STATION'].extend([wx]*num_of_yrs)
        for key in file_description.keys():
            results[key].extend(file_description[key])
    return results

problem2_results = find_problem2_results()
problem2_df = pd.DataFrame(problem2_results, columns=problem2_results.keys())
problem2_df = problem2_df.sort_values(by=['STATION','YEAR'], ascending=True)


problem2_output = 'C:/Users/reddy/Desktop/python/Coding test/exam-content/coding-data-exam/answers/YearlyAverages.out' 
problem2_df[['STATION','YEAR','AVG_LOW','AVG_HIGH','TOTAL_PRECIP']].to_csv(problem2_output, 
                                     sep='\t', 
                                     encoding='utf-8', 
                                     index=False)

