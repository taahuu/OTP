import random
import time

# Step 1: Generate a 6-digit OTP
def generate_otp():
    otp = random.randint(1000, 9999)  # Generate a 6-digit OTP
    otp_expiry = time.time() + 300  # OTP valid for 5 minutes (300 seconds)
    return otp, otp_expiry

# Step 2: Verify OTP
def verify_otp(input_otp, generated_otp, otp_expiry):
    current_time = time.time()
    if current_time > otp_expiry:
        return "OTP expired"
    elif input_otp == generated_otp:
        return "OTP verified"
    else:
        return "Invalid OTP"

# Step 3: Get user input, retry if blank
def get_user_otp():
    while True:
        user_input = input("Enter the OTP: ")
        if user_input.strip():  # Check if input is not blank
            try:
                return int(user_input)  # Convert to int and return
            except ValueError:
                print("Please enter a valid numeric OTP.")
        else:
            print("Input cannot be blank. Please enter the OTP.")

# Example Usage
generated_otp, otp_expiry_time = generate_otp()
print(f"Generated OTP: {generated_otp}")

# Simulate user input for OTP
user_input_otp = get_user_otp()

# Step 4: Verify the user input OTP
verification_result = verify_otp(user_input_otp, generated_otp, otp_expiry_time)
print(verification_result)
