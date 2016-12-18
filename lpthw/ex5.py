name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.4
weight = 180 # lbs
weight_kg = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall" % height
print "He's %d pounds heavy" % weight
print "He's %d cm tall" % height_cm
print "He's %d kgs heavy" % weight_kg
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on coffee" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (age, height, weight, age + height + weight)

# Using %r (print this no matter what

print_it = "no matter what"

print "Print this %r" % print_it # print_it has '' quotations around it, raw data
