class Message:
    def __init__(self, sender, content):
        self.sender = sender;
        self.content = content;

    def __str__(self):
        return f"{self.sender}: {self.content}";

# User class
class User:
    def __init__(self, name):
        self.name = name;

    def send_message(self, chatroom, content):
        chatroom.receive_message(Message(self.name, content));

# ChatRoom class
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name;
        self.users = [];
        self.chat_history = [];

    def join(self, user):
        self.users.append(user);
        print(f"{user.name} joined the chatroom.");

    def leave(self, user):
        if user in self.users:
            self.users.remove(user);
            print(f"{user.name} Left the chatroom.");

    def receive_message(self, message):
        self.chat_history.append(message)
        print(f"{message.sender} sent a message.")

    def show_chat_history(self):
        print("\n--- Chat History---");
        for msg in self.chat_history:
            print(msg);
        print("----------------------");

# Create chatroom
room = ChatRoom("Python Chat Room")

# Create users
u1 = User("Abhishek")
u2 = User("Amit")
u3 = User("Ankit")

# Users join the chatroom
room.join(u1)
room.join(u2)
room.join(u3)

# Users send messages
u1.send_message(room, "Hello everyone!");
u2.send_message(room, "Hi Abhishek!");
u3.send_message(room, "Good to see you all!");

# View chat history
room.show_chat_history();

#User leaves the room
room.leave(u2);