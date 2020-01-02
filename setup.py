from appJar import gui
from datetime import datetime

def press():
    dates = app.getDatePicker('dp')
    app.label("l1", "Name", row=0, column=0)
    app.label("l2", app.entry('Name'), row=0, column=1, fg='purple')
    
    app.label("l3", "Birth date", row=1, column=0)
    app.label("l4", f"{dates}", row=1, column=1, fg='purple')
    # --------------------------
    d1 = datetime(dates.year,dates.month,dates.day,00, 00, 00)
    d2 = datetime.today()
    diff = (d2 - d1)

    app.label("l5", "Days", row=2, column=0)
    app.label("l6", abs(diff.days), row=2, column=1, fg='purple')
    
    app.label("l7", "Hours", row=3, column=0)
    app.label("l8", "0", row=3, column=1, fg='purple')
    
    app.label("l9", "Minutes", row=4, column=0)
    app.label("l10", '0', row=4, column=1, fg='purple')

    app.label("l9", "Minutes", row=4, column=0)
    app.label("l10", '0', row=4, column=1, fg='purple')
    
    app.label("l11", "Today", row=5, column=0)
    app.label("l12", f"{datetime.today()}", row=5, column=1, fg='blue')

with gui("Challenge 4", "600x500", font={'size':14}) as app:
    app.label("Welcome to Challenge 4", fg='blue')
    app.entry("Name", label=True, focus=True)
    
    app.label("Enter your birth date")
    app.addDatePicker("dp")
    app.setDatePickerRange("dp", 1900, 2020)
    app.setDatePicker("dp")

    app.buttons(["Entrer", "Fermer"], [press, app.stop])
    app.startLabelFrame("Result")
    app.setSticky("ew")