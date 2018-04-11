import numpy as np
import csv

class Straight:
	
	def __init__(self):
		ind=1
		print('Enter length')
		l=input()
		print('Enter orientation wrt x')
		a=input()
		self.pts=fetch(ind)

	def get_length(self):
		return np.linalg.norm(np.array(self.pts[0])-np.array(self.pts[-1]))

	def get_orient(self):
		return np.arctan2(np.array(self.pts[-1])-np.array(self.pts[0]))



# Defines Arc
class Arc:
	
	def __init__(self):
		ind=2
		print('Enter Radius')
		l=input()
		print('Enter orientation wrt x')
		a=input()
		print('Enter subtending angle')
		th=input()
		self.pts=fetch(ind)

	def get_arc_length(self):
		return np.linalg.norm(np.array(self.pts[0])-np.array(self.pts[-1]))

	def get_orient(self):
		return np.arctan2(np.array(self.pts[-1])-np.array(self.pts[0]))



# Calls one of the above based on ind  
class TrajGenerator:
	def __init__(self,ind):
		options={1:Straight,2:Arc}
		return options[ind]()





############ Code for generating waypoints ##############
## Need to implement: If file 'traj.csv' not found run an algorithm to generate waypoints ##

def fetch(ind):
			traj_pts=[]
			try:
				with open('traj.csv', 'rb') as csvfile:
					ind=ind-1
					spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
					spamreader=list(spamreader)
					for row in spamreader:
						row=row[0].split(',')
						traj_pts.append(row[ind])
					return traj_pts
			except:
				## Generate points here


