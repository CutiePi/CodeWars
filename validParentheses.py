import time

def validBraces(string):
    #your code here
    opened = [0,0,0]
    lastOpened = []
    for x in string:
      if( x == "("):
          lastOpened.append("(")
          opened[0]+=1
      elif(x == ")"):
          if(len(lastOpened) > 0):
              if(lastOpened[-1] == "("): opened[0]-=1; del lastOpened[-1]
              else: return False
      if( x == "{"):
          lastOpened.append("{")
          opened[1]+=1
      elif(x == "}"):
          if(len(lastOpened) > 0):
              if (lastOpened[-1] == "{"): opened[1] -= 1; del lastOpened[-1]
              else:return False
      if( x == "["):
          lastOpened.append("[")
          opened[2]+=1
      elif(x == "]"):
          if(len(lastOpened) > 0):
              if (lastOpened[-1] == "["): opened[2] -= 1; del lastOpened[-1]
              else: return False
    return opened[0] == opened[1] == opened[2] == 0



def validBraces1(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''






start_time_me = time.time()
print(validBraces("("))
print(validBraces("""()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
"""))
print("--- %s seconds ---"  %  (time.time() - start_time_me))

start_time_other = time.time()
print(validBraces1("("))
print(validBraces1("""()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
"""))
print("--- %s seconds ---"  %  (time.time() - start_time_other))