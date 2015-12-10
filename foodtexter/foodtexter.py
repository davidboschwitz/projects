import urllib2
import smtplib

search_terms = ['Cheese Tortellini', 'Grilled Cheese', 'Snickerdoodle Cookie' ]
locations = ["Conversations", "Seasons"]
urls = ["http://www.dining.iastate.edu/menus/conversations", "http://www.dining.iastate.edu/menus/seasons"]
current_meal = ""
current_location = ""


def notify_for_meal(food, loc, meal):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('EMAIL', 'PASSWORD')
    server.sendmail('FROM', 'TO@txt.att.net', str(food) + " is available at " + str(loc) + " for " +str(meal) + "!")
    print "send message: " + str(food) + " is available at " + str(loc) + " for " +str(meal) + "! \n"

#do the food stuff
i = 0

#iterate through dining hall urls
for url in urls:
    current_location = locations[i]
    data = urllib2.urlopen(url)

    #iterate through webpage line by line
    for line in data:
        #get meal info
        if "<div class=\"event-header\"><h2>" in line:
            current_meal = line[30:33]
            if 'B' in current_meal:
                current_meal = "Breakfast"
            elif 'Lu' in current_meal:
                current_meal = "Lunch"
            elif 'La' in current_meal:
                current_meal = "Late Night"
            else:
                current_meal = "Dinner"
        #see if my fav foods are in that meal
        for search in search_terms:
            if search in line:
                #late night meals are always the same, don't notify
                if current_meal != "Late Night":
                    notify_for_meal(search, current_location, current_meal)
    i += 1
