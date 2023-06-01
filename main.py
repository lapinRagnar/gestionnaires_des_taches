import pickle
import os 

# instructions
instruction = """
a Ranger = nouvelle tache "Ranger"
s Ranger = supprimer la tache "Ranger"
st = supprimer toutes les taches
l = afficher la liste des taches
i = re-afficher ces instructions
q = quitter l'app et sauvegarder
"""



class TaskManager:
  def __init__(self):
    self.tasks = []
    
    if(os.path.exists('save.txt')):
      self.loadData()
  
  def saveData(self):
    with open('save.txt', 'wb') as saveFile:
      pickle.dump(self.tasks, saveFile)
  
  def createTask(self, task):
    self.tasks.append(Task(task))
  
  def loadData(self):
    with open('save.txt', 'rb') as saveFile:
      self.tasks = pickle.load(saveFile)
  
  
class Task:
  def __init__(self, task):
    self.task = task


print(instruction)
taskManager = TaskManager()

while True:
  print('')
  prompt = input("Action: ")
  
  if (prompt[:2] == 'a '):
    newtask = prompt[2:]
    print(f"Ajout de la tache {newtask} ? (oui/non)")
    prompt = input()
    
    if (prompt == 'oui'):
      taskManager.createTask(newtask)
  
  elif(prompt[:2] == "s "):
    taskToDel = prompt[2:]
    taskToDelObject = None
    
    for element in taskManager.tasks:
      if (element.task == taskToDel):
        taskToDelObject = element
    
    if (taskToDelObject == None):
      print(f"il n'y a pas de tache {taskToDel}")
    else:
      print(f"suppression de la tache : {taskToDel} , (oui/non)?")
      prompt = input()
      if (prompt == 'oui'):
        taskManager.tasks.remove(taskToDelObject)
  
  elif(prompt == "st"):
    print(f"suppression de toutes les taches (oui/non)?")
    prompt = input()
    
    if (prompt == 'oui'):
      taskManager.tasks = []
    
  elif(prompt[0] == 'l'):
    
    if (len(taskManager.tasks) == 0):
      print(f"il n'y a pas de tache pour l'instant!")
      
    for element in taskManager.tasks:
      print(' - ' + element.task)
  
  elif (prompt[0] == "i"):
    print(instruction)
    
  elif (prompt[0] == "q"):
    prompt = input("Quitter ? (oui/non)")
    if (prompt == 'oui'):
      taskManager.saveData()
      quit()
    
        



