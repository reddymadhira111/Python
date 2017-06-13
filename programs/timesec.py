'''class Time_In_Sec(object):
	total=24*60*60
	def __init__(self,sec,mint,hr):
		self.sec=sec
		self.mint=mint
		self.hr=hr
	def totalsec(self):
		total1=24*60*60
		return total1
	def cal_time_dif(start,end):
		total=24*60*60
		start=int(input('enter start time:'))
		end=int(input('enter end time:'))
		dif=(end-start)*(0.6)*(60)
		other_dif=total-dif
		return abs(dif),abs(other_dif)
my_time=Time_In_Sec.cal_time_dif(930,1530)
print(my_time)
print()
'''
'''
class Time1(object):
    def __init__(self,hr,mint,sec):
    	self.hr=hr
    	self.min=mint
    	self.sec=sec

    def cal_time(hr,mint,sec):
        start=input('enter start time:%d %d %d',hr,mint,sec)
        end=input('enter end time:',(hr,mint,sec))


m=Time1.cal_time(23,59,59)
print(m)
'''
class Time1(object):
	def __init__(self,hr,mint,sec):
		self.sec=sec
		self.mint=mint
		self.hr=hr
	def cal_time(ehr,emint,esec):
		ehr=23
		emint=59
		esec=59
		shr=00
		smint=00
		ssec=00
		dmint=abs((emint-smint)*60)
		dsec=abs((esec-esec))
		if (ehr-shr)>12:
			dhr=(24-(ehr-shr

				))*(3600)
			print(dhr)
		else:
			dhr=(ehr-shr)*3600
		total=24*3600
		timed=dhr+dmint+dsec
		timedother=total-timed
		print('time dif',timed)
		print('time remain',timedother)
m=Time1.cal_time(23,59,59)
print(m)