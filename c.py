# 🎉 Congratulations Message Program 🎉

# --- Functions ---

def create_message(name, achievement):
    # Using string concatenation
    message1 = "Congratulations " + name + "!"
    
    # Using f-string formatting
    message2 = f"You have successfully achieved: {achievement}."
    
    # Using string methods
    message3 = "this is a proud moment!".upper()
    
    # Using string repetition
    message4 = "🎊 " * 5
    
    # Combine all parts
    full_message = message4 + "\n" + message1 + "\n" + message2 + "\n" + message3 + "\n" + message4
    return full_message

# --- Main Program ---

print("🎈 Welcome to the Congratulations Message Generator 🎈\n")

# Get user input
name = input("Enter the recipient's name: ")
achievement = input("Enter the achievement: ")

# Generate the message
congrats_message = create_message(name, achievement)

# Display the message
print("\n" + "-"*50 + "\n")
print(congrats_message)
print("\n" + "-"*50 + "\n")

print("✨ Message created successfully! Share it with your friend! ✨")
