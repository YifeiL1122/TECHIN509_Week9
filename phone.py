class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # Constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []
    
    def check_messages(self):
        if self.messages:
            print(f"Messages for {self.name}:")
            for msg in self.messages:
                print(f"- {msg}")
        else:
            print(f"No messages for {self.name}.")
    
    def call(self, number):
        print(f"Calling {number} from {self.phone_number}...")
    
    def airdrop(self, filename, recipient):
        if recipient:
            print(f"Airdropping '{filename}' to {recipient}...")
        else:
            print(f"Airdropping '{filename}' but no recipient specified.")
    
    def airreceive(self, filename):
        self.files.append(filename)
        print(f"Received file '{filename}'.")
    
    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 characters.")
        else:
            self.name = new_name

    def send_message(self, recipient, message):
        if isinstance(recipient, iPhone):
            recipient.messages.append(f"From {self.name}: {message}")
            print(f"Message sent from {self.name} to {recipient.name}: '{message}'")
        else:
            print("Recipient must be an iPhone instance.")

# Create two iPhone instances
iphone1 = iPhone(
    name="John's iPhone",
    version="18",
    phone_number="111-222-3333",
    color="black",
    model="iPhone 16"
)

iphone2 = iPhone(
    name="Jane's iPhone",
    version="18",
    phone_number="444-555-6666",
    color="white",
    model="iPhone 16 Pro"
)

# Change names
iphone1.set_name("John's New iPhone")
iphone2.set_name("Jane's Updated iPhone")

# Send iMessage from phone1 to phone2
iphone1.send_message(iphone2, "Hey Jane! How are you?")

# phone2 checks messages
iphone2.check_messages()
