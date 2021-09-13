'''
#ARMY REGIMENTS
						
																													  Corps
																														|
																														|
																														|
																											-------------------------
																											|						|
																											|						|
																										division                  division
																									        |
																									        |
																			----------------------------------------------------------------
																			|		                          | 		                   |					
																			|								  |						       |
																			|								  |						       |
																		brigade                            brigade                     brigade
																	 (3 battalions)								
																			|
																			|
																			|
																			|
																			|
																			|
																		battalion
																	(4 or more companies)
																		  	|
																		    |-------------------------------------------------------------------
																		    |															       |
																		    |																Delta Company
																		    |																Charlie Company
																		    |                                                               Bravo Company
																		    |																Alpha Company
																			|
																			|
																		company(4-5 platoons)
																			|
																			|------------------------------------------------------------------------------------
																			|																					|
							   ------------------------------------ platoon(4-3 squads) --------------------------											platoon-2
							   ^										(42)									^												|	
							   | 																				|											platoon-3											
							   |																				|												|
							   |																				|											platoon-4	
		--------------------section----------------                                     --------------------section----------------								|
		^					 (24)				  ^                     				^					 (24)				  ^ 						platoon-5
		|                               	      |										|                               	      |
^-----squad-----^(9)              		   ^-----squad-----^(9)                 ^-----squad-----^(9)              	     ^-----squad-----^(9)                     
|				|						   |			   |					|				|						 |			     |
team 1 		team 2        				team 1 		    team 2                 team 1 		team 2        				team 1 		    team 2                             
'''



class Corps:
	pass

class Division:
	pass

class Brigade:
	pass

class Battalion:
	pass

class Company:
	pass

class Platoon:
	pass

class Section:
	pass

class Squad(Section):
	def __init__(self,team_1=None,team_2=None):
		if team_1 is None:
			self.team_1 = []
		else:
			self.team_1 = team_1
		if team_2 is None:
			self.team_2 = []
		else:
			self.team_2 = team_2

	def set_pvt(self):
		import random
		private = random.choice(self.team_1)
		return ("Pvt. {}".format(private)) 
		
	def set_cpl(self):
		import random
		corporal = random.choice(self.team_2)
		return ("Cpl. {}".format(corporal))

	def patrol_duty(self):
		from datetime import date
		date_today = date.today()
		print ("Date: {:%B %d, %Y}".format(date_today))
		on_duty = ("-------On Patrol-------\n{1}\n{0}".format(self.set_cpl(),self.set_pvt()))
		print(on_duty)

	def all_teams(self):
		return "Team 1: {}\nTeam 2: {}".format(self.team_1,self.team_2)


sq_team_1 = Squad(['John Phelps','Edward Barn','Barry Green'],['Thomas Nord','Chris White','James Anderson'])
sq_team_2 = Squad(['Michael Gart','Harry Johnson','Mark Highs'],['Peter Kites','Leo Tur','George Schafer'])

print(sq_team_1.all_teams())

sq_team_1.patrol_duty()

sq_team_2.patrol_duty()






