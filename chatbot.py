def chatbot():
    print("Hello! I am your AI Chatbot.")
    name = input("What's your name?").strip()
    
    if not name:
        name = "Friend"
        
    print(f"Nice to meet you {name}!")
    
    while True:
        user_input = input(f"{name}: ").lower()
        
        if any(word in user_input for word in["hi", "hello", "hey"]):
            print(f"Bot: Hello {name}👋, How are you today?")
        
        elif "how are you?" in user_input:
            print(f"Bot: I'm doing great! Thank you for asking.😊")
            
        elif "my name" in user_input:
            print(f"Bot: Of course! Your name is {name}.😊")
            
        elif "sad" in user_input:
            print(f"Bot: I'm so sorry to hear that. Is there anything I can help with to make you feel better?😔")
            
        elif "bored" in user_input:
            print(f"Bot: Really? Here are some fun games you can play if you are bored: 1. Tic Tac Toe  2. Puzzle Solving  3. Monopoly  4. Scrabble  5. Ludo, etc. Do you want me to tell you more games?🎮")
            
        elif "excited" in user_input:
            print(f"Bot: What are you so excited about? If you want you can share it with me!😁")
      
        elif "happy" in user_input:
            print(f"Bot: I'm so glad to hear that! Keep smiling!😁")
            
        elif any(word in user_input for word in["bye", "exit", "quit"]):
            print(f"Bot: Bye {name}! It was really nice to meet you. See you later!👋")
            break
        else:
            print(f"Bot: That's really interesting! Tell me more about it.😁")
            

chatbot()            