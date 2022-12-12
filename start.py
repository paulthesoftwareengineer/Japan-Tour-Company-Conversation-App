# Define a function to greet the customer
def greet_customer():
  print("Hello, welcome to our store!")

# Define a function to get the customer's name
def get_customer_name():
  # Ask the customer for their name
  customer_name = input("What is your name? ")
  return customer_name

# Define a function to ask the customer what they want
def get_customer_request():
  # Ask the customer what they want
  customer_request = input("What can I help you with today? ")
  return customer_request

# Define a function to handle the customer's request
def handle_customer_request(request):
  # Check if the customer's request is "help"
  if request.lower() == "help":
    print("Here are some things you can ask for:")
    print("- products")
    print("- pricing")
    print("- promotions")
    print("- support")
  # If the customer's request is not "help", respond with a default message
  else:
    print("I'm sorry, I didn't understand your request. Please try again.")

# Define a function to end the conversation
def end_conversation():
  print("Thank you for chatting with us. Have a great day!")

# Define a function to run the customer conversation app
def run_customer_conversation():
  greet_customer()
  customer_name = get_customer_name()
  print("Nice to meet you, " + customer_name + "!")
  customer_request = get_customer_request()
  handle_customer_request(customer_request)
  end_conversation()

# Run the customer conversation app
run_customer_conversation()
