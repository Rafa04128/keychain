import bcrypt

def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def check_password(entered_password, stored_hash):
    # Check if the entered password matches the stored hash
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash.encode('utf-8'))

# Example usage:
original_password = "my_secure_password"
hashed_password = hash_password(original_password)

print(f"Original Password: {original_password}")
print(f"Hashed Password: {hashed_password}")

# Simulate user entering password for authentication
user_entered_password = "my_secure_password"
if check_password(user_entered_password, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password!")