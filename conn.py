
import sys
import requests

def filereader(domains, subdomains):
   """Method to parse and read every domains and subdomains line by line"""

   global i , j #Counters for reading lines in the domains.txt and sudomains.txt
   global dom_list
   global subdom_list

   dom = open(domains, "r") #file pointer to open domain file
   dom_list = [""] # initializing list to store domains
   i = 0
   dom_lines = dom.readline() 
   while dom_lines:
      dom_lines = dom_lines.rstrip('\n') # stripping newline associated to every domain in the file
      dom_list.append(dom_lines) # adding domains
      i = i+1
      dom_lines = dom.readline()
    
  #deleting empty members in the list 
   del dom_list[0] 
   del dom_list[i - 1]
   print("dom_list:",dom_list)
   dom.close()
   
   subdom = open(subdomains, "r")
   j = 0 # Counter for keeping track of number of elements in file
   subdom_list = [""]
   subdom_lines = subdom.readline()
   while subdom_lines:
      subdom_lines = subdom_lines.rstrip('\n')
      subdom_list.append(subdom_lines)
      subdom_lines = subdom.readline()
      j = j + 1
   del subdom_list[0]
   print("subdom_list:",subdom_list)
   subdom.close()
   n = 0

def connector():   
   """Method to concatentate domains and subdomains to check the connectivity """
 
   for i in range(0,j):
      url = "http://"+subdom_list[i]+"."+dom_list[i]+":80"
      print(url)

   for i in range(0,j):

      try:
         url = "http://"+subdom_list[i]+"."+dom_list[i]+":80"  
         response = requests.get(url)
         i = i+1
         if (response.status_code == 200):
       print('\n')
            print("Connection Established to -->",url)
       print("Headers:", response.headers['server']) 
      except: 
    print('\n')
    print("Exception Ocurred! Connection Aborted to the peer URL:",url)

if __name__ == "__main__":
   try:
         
      domains = str(sys.argv[1])
      subdomains = str(sys.argv[2])
      filereader(domains.txt, subdomains.txt)
      connector()

   except:
      print("Usage: connect.py domains.txt subdomains.txt -- Please pass the arguments")

