from DataSource import Extract
import json
import pandas as pd
import numpy as np 

class Transformation:

	def __init__(self):
		extractObj = Extract()

		# load API data
		self.goal_data = extractObj.getAPISData('Goals')
		self.player_data = extractObj.getAPISData('Players')
		self.team_data = extractObj.getAPISData('Teams')
		self.games_data = extractObj.getAPISData('Games')
		self.rounds_data = extractObj.getAPISData('Rounds')

	def GoalData(self):
		# list of columns to be added in a dataframe
		id_=[]
		person_id=[]
		game_id =[]
		team_id = []
		penalty = []
		owngoal = []
		minute=[]
		team_score=[]
		opponent_score=[]
		# function to append data into lists
		def append_goal_data(dict_):
			id_.append(dict_['id'])
			person_id.append(dict_['person_id'])
			game_id.append(dict_['game_id'])
			team_id.append(dict_['team_id'])
			penalty.append(dict_['penalty'])
			owngoal.append(dict_['owngoal'])
			minute.append(dict_['minute'])
			team_score.append(dict_['score1'])
			opponent_score.append(dict_['score2'])
		#extract dictionary from string and append it in a list
		my_list = self.goal_data.split('\n') 
		for i in range(1,len(my_list)-1):
			if i != len(my_list)-2:
				dict_ = json.loads(my_list[i][:-1])
				append_goal_data(dict_)
			else: 
				dict_ = json.loads(my_list[i])
				append_goal_data(dict_)
				
		# create dataframe using lists 
		self.data_csv = pd.DataFrame({'id':id_,'person_id':person_id,'game_id':game_id,'team_id':team_id,
			'penalty':penalty,'owngoal':owngoal,'minute':minute,'team_score':team_score,
			'opponent_score':opponent_score})
		return self.data_csv #return a dataframe

	def PlayerData(self):
		id_=[]
		name=[]
		def append_player_data(dict_):
			id_.append(dict_['id'])
			name.append(dict_['name'])
		my_list = self.player_data.split('\n')
		for i in range(1,len(my_list)-1):
			if i != len(my_list)-2:
				dict_ = json.loads(my_list[i][:-1])
				append_player_data(dict_)
			else: 
				dict_ = json.loads(my_list[i])
				append_player_data(dict_)
		self.data_csv = pd.DataFrame({'id':id_,'name':name})		
		return self.data_csv
		
	def TeamData(self):
		id_=[]
		title=[]
		def append_team_data(dict_):
			id_.append(dict_['id'])
			title.append(dict_['title'])
		my_list = self.team_data.split('\n')
		for i in range(1,len(my_list)-1):
			if i != len(my_list)-2:
				dict_ = json.loads(my_list[i][:-1])
				append_team_data(dict_)
			else: 
				dict_ = json.loads(my_list[i])
				append_team_data(dict_)
		self.data_csv = pd.DataFrame({'id':id_,'title':title})
		return self.data_csv

	def GameData(self):
		id_=[]
		team1_id=[]
		team2_id=[]
		knockout = []
		round_id = []
		def append_game_data(dict_):
			id_.append(dict_['id'])
			team1_id.append(dict_['team1_id'])
			team2_id.append(dict_['team2_id'])
			knockout.append(dict_['knockout'])
			round_id.append(dict_['round_id'])
		my_list = self.games_data.split('\n')
		for i in range(1,len(my_list)-1):
			if i != len(my_list)-2:
				dict_ = json.loads(my_list[i][:-1])
				append_game_data(dict_)
			else: 
				dict_ = json.loads(my_list[i])
				append_game_data(dict_)
		self.data_csv = pd.DataFrame({'id':id_,'team1_id':team1_id,'team2_id':team2_id,'knockout':knockout,
			'round_id':round_id})
		return self.data_csv

	def RoundsData(self):
		id_=[]
		title=[]
		def append_round_data(dict_):
			id_.append(dict_['id'])
			title.append(dict_['title'])
		my_list = self.rounds_data.split('\n')
		for i in range(1,len(my_list)-1):
			if i != len(my_list)-2:
				dict_ = json.loads(my_list[i][:-1])
				append_round_data(dict_)
			else: 
				dict_ = json.loads(my_list[i])
				append_round_data(dict_)
		self.data_csv = pd.DataFrame({'id':id_,'title':title})
		return self.data_csv

#test run
# Transformation().GoalData()
# Transformation().GameData()
# Transformation().PlayerData()
# Transformation().RoundsData()
# Transformation().TeamData()

# print('Successfully Transformed')


