
name = input("what is your name?")
print("It is nice to meet you", name, "my name is chatbot. (it's not very original, but I think that is the joke)")
location = input("where are you from?")
print("that is interesting! I do not know where that is because I am a string of code")
fav_number = input("I do not know how to make small talk. what is your favorite number?")


compare = 69420/int(fav_number)
print("an excellent choice. that just so happens to be", compare, "times smaller than my favorite number!")

car = input("what is your dream car?")
print("I do not know what that is, but I am glad you have something to appreciate in your few years on this planet.")
cost = input("how many units of currency does your dream car cost?")
print("I am not very good at sympathizing, but that seems like a lot!")
rate = input("how many units of currency is the monthly interest rate on a car loan?")
time = input("how many years would your hypothetical car loan be for?")
number_of_payments = int(time)*12

monthly_payment = (int(rate)*int(cost))/(1-(1+int(rate))**int(number_of_payments))