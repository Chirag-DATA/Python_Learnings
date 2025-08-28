import time 

class ChatUser():
    def __init__(self,username,chat_file = "chat.txt"):
        self.username = username
        self.file = chat_file
    
    def send_msg(self,message):          #to append message in the chat file
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open (self.file,"a") as f:
            f.write(f"{timestamp} : {self.username} : {message}\n")

    def read_chat(self):
        try:
            with open (self.file,"r") as f:
                chat = f.read()
                print("...CHAT HISTORY...")
                print(chat)
        except FileNotFoundError:
            print("No Chat History yet...")

    
def startChat():
    username = input("Enter your username : ")
    user = ChatUser(username)

    print("\n1 -> Send Message")
    print("2 -> Read Chat")
    print("3 -> change user")
    print("4 -> Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            msg = input("Enter your message: ")
            user.send_msg(msg)
        elif choice == 2:
            user.read_chat()
        elif choice == 3:
            print("This is the other user on chat...")
            startChat()
        elif choice == 4:
            break
        else:
            print("Invalid Choice...")
    

#if __name__ == "__main__":
startChat()

