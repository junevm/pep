class ChatWindow:
    def __init__(self):
        self.messages = []
        self.current = -1 

    def type_message(self,msg):
        self.messages.append(msg)
        self.current+=1
    
    def undo(self):
        if self.current>0:
            self.current-=1
            self.show_message()
    
    def redo(self):
        if self.current<=len(self.messages):
            self.current+=1
            self.show_message()
    
    def show_message(self):
        if not self.messages:
            print("no element")
        else:
            print(self.messages[self.current])


chat = ChatWindow()
chat.type_message("hello")
chat.type_message("how are you")
chat.type_message("Goodbye")

chat.undo()
chat.undo()
chat.redo()
chat.redo()



