import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)
   

class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program


loc_A,loc_B,loc_C,loc_D='A','B','C','D'

class vaccumEnvironment():

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean''Dirty'])
                      }
        
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right': agent.location=loc_B
        elif action=='Left': agent.location=loc_A
        elif action=='DownLeft': agent.location=loc_C
        elif action=='DownRight': agent.location=loc_D
        elif action=='Suck':
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'
      

class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            print(percepts)
            action=table.get(tuple(percepts))
            print('Agent perceives ', percept, ' and does ', action)
            return action

        self.program=program



def tableDrivenVaccumAgent():
    table = {
        ##WRITE TABLE ACCORDING TO THE TASK ENVIRONMENT
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Clean'),):'DownLeft',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Clean'),):'DownRight',
              ((loc_B,'Dirty'),):'Suck',
              ((loc_C,'Clean'),):'DownRight',
              ((loc_C,'Clean'),):'Left',
              ((loc_C,'Dirty'),):'Suck',
              ((loc_D,'Clean'),):'Right',
              ((loc_D,'Clean'),):'DownLeft',
              ((loc_D,'Dirty'),):'Suck',


              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'DownLeft',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              
              ((loc_A, 'Dirty'), (loc_C, 'Clean')): 'DownRight',
              ((loc_A, 'Dirty'), (loc_B, 'Clean')): 'DownLeft',
              ((loc_A, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',

              ((loc_B, 'Clean'), (loc_A, 'Clean')): 'DownLeft',
              ((loc_B, 'Clean'), (loc_B, 'Clean')): 'DownRight',
              ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Right',
              ((loc_B, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              
              ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'DownLeft',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'DownRight',
              ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Dirty'), (loc_A, 'Dirty')): 'Suck',


              ((loc_C, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_B, 'Clean'), (loc_B, 'Clean')): 'DownRight',
              ((loc_C, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_C, 'Clean'), (loc_C, 'Dirty')): 'Suck',
              
              ((loc_C, 'Dirty'), (loc_D, 'Clean')): 'DownLeft',
              ((loc_C, 'Dirty'), (loc_C, 'Clean')): 'DownRight',
              ((loc_D, 'Dirty'), (loc_D, 'Clean')): 'DownLeft',
              ((loc_C, 'Dirty'), (loc_C, 'Dirty')): 'Suck',
              ((loc_D, 'Dirty'), (loc_C, 'Dirty')): 'Left',

              ((loc_D, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Clean'), (loc_D, 'Clean')): 'DownLeft',
              ((loc_D, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Clean'), (loc_D, 'Dirty')): 'Suck',
              
              ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'DownLeft',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'DownRight',
              ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_D, 'Dirty'), (loc_D, 'Dirty')): 'Suck',




             
              

                          }
    return tableDrivenAgent(table)



class reflexVaccumAgent(Agent):
    
    def __init__(self):
        Agent.__init__(self)        
 
        def program(percept):
            location=percept[0]
            status=percept[1]
 
            if status=='Dirty': action= 'Suck'
            elif location==loc_A: action=random.choice(['DownLeft','Right']) 
 
            elif location==loc_B: action=random.choice(['DownRight','Left'])  
 
            elif location==loc_C: action=random.choice(['DownRight','Left'])  
 
            elif location==loc_D: action =random.choice(['Right','DownLeft'])  
 
            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)
           
            return action
        
            
            
        self.program=program
        
        
Ragent=reflexVaccumAgent()
env=vaccumEnvironment()
env.add_object(Ragent)
 
 
for steps in range(10):
    print(env.percept(Ragent))
    action=Ragent.program(env.percept(Ragent))
    env.execute_action(Ragent,action)
class reflexVaccumAgent(Agent):
    
    def __init__(self):
        Agent.__init__(self)        

        def program(percept):
            location=percept[0]
            status=percept[1]

##            MODIFY THE CONDITION-ACTION RULE BELOW

            if status=='Dirty': action= 'Suck'
            elif location==loc_A: action= 'Right'
            elif location==loc_B: action= 'Left'
            elif location==loc_C: action= 'DownLeft'
            elif location==loc_D: action= 'DownRight'




            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action
        
            
            
        self.program=program




        
class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        
        model={loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):
         location=percept[0]
         status=percept[1]
           
        model[location]=status
            
        if model[loc_A]==model[loc_B]==model[loc_C]==model[loc_D]=='Clean': return 'NoOp'
        elif status=='Dirty': action= 'Suck'
        elif location==loc_A: action= random.choice(['Right','DownLeft'])
        elif location==loc_B: action= random.choice(['Left','DownRight'])
        elif location==loc_C: action= random.choice(['DownRight','Left'])
        elif location==loc_D: action= random.choice(['DownLeft','Right'])
            

        percept=(location,status)
        print('Agent perceives ', percept, ' and does ', action)

        return action                    
            
        self.program=program
        
        


print("---For tableDrivenVaccumAgent---")

Tagent=tableDrivenVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)

for _ in range(10):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)



print("----For reflex Vaccum Agent----")

Tagent=reflexVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)

for _ in range(10):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)


print("-----For model BasedVaccumAgent------")

Magent=modelBasedVaccumAgent()
env=vaccumEnvironment()
env.add_object(Magent)

for _ in range(15):
    action=Magent.program(env.percept(Magent))
    env.execute_action(Magent,action)




    
