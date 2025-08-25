import time
now=time.ctime()

def chatbot():        
    print("welcome to the chatbot")
        
    while True:
        user=input("you: ").lower().strip()      
      
        if user=="hello":
            print("Bot: hy👋")
            
        elif user=="hy":
            print("Bot: hello👋")
            
        elif user=="how are you":
            print("Bot: I'm fine, what about you?")
            
        elif user=="i am fine":
            print("Bot: okay good!🥰")
            
        elif user=="i am good":
            print("Bot: okay good!🥰")
            
        elif user=="what is the time now":
            print("bot: ",now)
            
        elif user == "what is today's date":
            print("Bot:", time.strftime("%Y-%m-%d"))
            
        elif user == "what are you doing":
            print ("Bot: nothing")
            
        elif user == "do you like me":
            print("Bot: Of course! You're awesome😍")
            
        elif user== "do you wanna talk to me":
            print("Bot: yes of cousre!")  
            
        elif user == "what can you do":
            print("Bot: I can chat, tell the time, and even make you smile😄 ")
          
        elif user=="what is your name":
            print("Bot: I'm just a simple bot")    
            
        elif user=="bye":
            print("Bot: bye <3")
            break

        else:
            print("I don't understand")     
                 
chatbot()