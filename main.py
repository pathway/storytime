
def menu(question,items):
  while True:
    for idx, it in enumerate(items):
      print(idx,it)
    answer= input(question+" > ")
    index = int(answer)
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

items = ['Johnny','Sandy','Bob','sand','fillup','rock','billy','jacob']
Name = menu("Choose a name",items)

items = ['apple', 'rock', 'Sand', 'dragon']
Food = menu("Choose food",items)
items = ['Valcano erapshen', 'apiring black hole', 'Shaknaydo', 'baby asprin']
Desaster = menu("Choose a item",items)

items = ['Tunami sumoner', 'Time mashin', 'Nuke','' super milk']
Artifact = menu("Choose artifact",items)



make_story(Name, Food, Desaster, Artifact )


#'''
#make_story('Johnny', 'eggs', 'volcano erapshen', 'tunami sumoner' )

#make_story('Sandy', 'pizza', 'apiring blackhole', 'Timemashin')

##make_story('bob', 'stone', 'sharknato', 'Nuke',binana)

print("._.")

##'''




