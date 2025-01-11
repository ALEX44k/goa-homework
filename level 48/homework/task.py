#Keep up the hoop
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"

#Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s * 100000 / 3600)

#Switch it Up!
def switch_it_up(number):
    words = [ "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return words[number]

#Function 2 - squaring an argument
def square(n):
    return n * n

#Removing Elements
def remove_every_other(my_list):
    return my_list [:: 2]