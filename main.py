import random

#random.randint(1,4)

def menu(question,items):
  while True:

    for idx, it in enumerate(items):
      print(idx,it)
    print(idx+1,"Random")

    answer= input(question+" > ")
    index = int(answer)

    if index==len(items):
      picked= random.choice(items)
      print("You selected: ",picked)
      return picked

    if index<0 or index>=len(items):
      print("Invalid answer")
      continue

    picked = items[ index ]
    print("You selected: ",picked)
    return picked

 
def make_story(name, food, desaster, artifact):
  item='meteor'
  about_item='going straight at you'

  print("==========================================")
  print(name,' woke up and saw a', Desaster,'that was going strate at him')
  print("you have 1 min")
  print("this is an emergency")

  print(name,"eat breafast you had", food)
  print ("then you say",)
  print (food,"IS GOOD")
  print ("the", food,"was posioned")
  print ("then you say oh uh")
  print ("theres an" ,Artifact, "standing in your corner of the room you grab it and say")
  print ("i gotta get some ", artifact)
  print ("you run to home but the",desaster,"in front of your eyes blew up you house ")
  print("oh well")
  print("---------------- THE END -----------------")

  print("PS. Its over, you can stop reading now ")
  print("PPS. Why are you still here??")


items = ['Johnny','Sandy','Bob','sand','fillup','rock','billy','jacob','Artifact']
Name = menu("Choose a name",items)

items = ['apple', 'rock', 'Sand', 'dragon']
Food = menu("Choose food",items)

disaster_dict = {
  'Valcano erapshen' : " burned by hot ash",
  'Shaknaydo' : " bitten by a shark ",
}
#print( disaster.keys() )

#items = ['Valcano erapshen', 'apiring black hole', 'Shaknaydo', 'baby asprin']

Desaster = menu("Choose a item", list(disaster_dict.keys()) )
print(" Method of death: ", disaster_dict[ Desaster ] )

items = ('Tunami sumoner', 'Time mashin', 'Nuke','super milk')
Artifact = menu("Choose artifact",items)

items = ('your mom','1 mm of water')
death = menu("Choose your death",items)



make_story(Name, Food, Desaster, Artifact )


'''
#make_story('Johnny', 'eggs', 'volcano erapshen', 'tunami sumoner' )

#make_story('Sandy', 'pizza', 'apiring blackhole', 'Timemashin')

##make_story('bob', 'stone', 'sharknato', 'Nuke',binana)



'''

