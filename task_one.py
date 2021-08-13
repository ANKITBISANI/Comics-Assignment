# Write a script called task_one.py that when called will output something like this to theconsole. (reference below).



###############################################################################################################
# Created by : Ankit Bisani
# Date:12-08-2021
# 
# 
###############################################################################################################


import requests
import random
import json



import sys
 
# total arguments


  
# api-endpoint

 
def comic_details():
    
    list=[]
    
    for i in random.sample(range(1, 84), 15):
        web= 'https://xkcd.com/'
        number=str(i)
        extension='/info.0.json'
    
  #URL Generation
        URL=web+number+extension
        
        
    
  # sending get request 

        try:
            r = requests.get(url = URL)
            r.raise_for_status()
            
            
    
   # extracting data in json format and cleaning/transforming the the data 

        
        
            title = r.json()['title']
            alt_text = r.json()['alt']
            num = r.json()['num']
            link = r.json()['link']
            image_link = r.json()['img']
            image=r.json()['img'].rsplit('/', 1)[1]
            
            #print(title,alt_text,num,link,image_link,image)
            
    
            dict_format = {'comic' : title,
                       'comic_meta' : {
                            'alt_text' : alt_text,
                            'number' : num,
                            'link' : link,
                            'image' : image,
                            'image_link' : image_link}}
            
            list.append(dict_format)
    

            
            
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            
    json_object = json.dumps(list, indent = 4)
    print(json_object)


        
def main():
    comic_details()
    
if __name__=='__main__':
    main()
    
    
    
 

  
