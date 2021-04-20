import webbrowser

print("Hello my name is Jumppy, I am a chatbot.")
print()
nm=input("What is your Name? ")
print(f"Great, {nm}! ")
print("How can I help you? Here are some Topics you can select from: ")
ans="yes"
while(ans=="yes"):
    print(">> Network") 
    print(">> Business Plan")
    print(">> Events")
    print(">> Funding")
    ch=input("").title()
    ch_list = ["Network", "Business Plan", "Events",  "Funding"]
    if ch not in ch_list:
        print( "Sorry. We dont have this topic.")
        print(">> Network") 
        print(">> Business Plan")
        print(">> Events")
        print(">> Funding")
        ch=input("").title()
        print(f"Great I would love to help you on the topic {ch}.")
    if ch in ch_list:        
        if(ch=="Network"):
            with open(file= "texts/network.txt", mode="r") as network_file:
                print(network_file.read())         
        if(ch=="Business Plan"):
            with open(file = "texts/business_plan.txt", mode="r") as plan_file:
                print(plan_file.read())    
        if(ch=="Events"):
            with open(file= "texts/events.txt", mode= "r") as events_file:
                print(events_file.read())
                print()
                events_more=input("Would you like know about the Events? [Yes/No] ")
                if events_more == "yes":
                    events_day = input("Type 1 for: AUF-Workshop - Rüstzeug für den Perspektivenwechsel. \nType 2 for: Girls‘ Day: Mut zu MINT – Frauen in zukunftssicheren Berufen stellen sich vor. \nType 3 for: AUF-Workshop - Trittsicher auf allen Wegen. \nType 4 for: Fragen kostet nichts – auch in der Krise!.")
                    if events_day == "1":
                        webbrowser.open_new_tab("https://www.jumpp.de/AUF-Perspektive")
                    if events_day == "2":
                        webbrowser.open_new_tab("https://www.jumpp.de/Mut_zu_MINT")
                    if events_day =="3":
                        webbrowser.open_new_tab("https://www.jumpp.de/AUF-Wege")
                    if events_day =="4":
                        webbrowser.open_new_tab("https://www.jumpp.de/fragen-kostet-nichts")
                    if events_more == "no":
                        pass
        if(ch=="Funding"):
            with open (file = "texts/funding.txt", mode="r") as funding_file:
                print(funding_file.read())
                print()
                print("Would you like some more information?")
                fund_ans=input("Type 1 for: Bankgespräch (Christine Acker, Ramona Lange). \nType 2 for: Fördermittel (Christine Acker).\nType 3: Versicherungen (Isolde Mischke-Flach).\n ")
                if fund_ans == "1":
                    webbrowser.open_new_tab("https://www.jumpp.de/content/kredite-und-f-rdermittel-erfolgreich-beantragen")
                if fund_ans=="2":
                    webbrowser.open_new_tab("https://www.jumpp.de/content/orientierungshilfe-f-rdermittel-auch-f-r-kmu-und-freiberuflerinnen")
                if fund_ans== "3":
                    webbrowser.open_new_tab("https://www.jumpp.de/content/sich-gezielt-und-relevant-absichern")              
    ans=input("Was it helpful [Yes/No] ")
    ans=ans.lower()
    if(ans=="yes"):
        print("Great thx for the Feedback")
        cont=input("Do you wish to continue with other topics or Quit the session [Yes/No] ")
        cont=cont.lower()
        if(cont=="yes"):
            print("Thx and Have A lovely day Good Bye")
            ans="yes"
        else:
            ans="no"
    else:
        print("Thanks for Feedback, I am sorry I could not help.")
        print("You may contact our Support for Help. Here is their Number:  069 71589550 ")
        print("Thank you and Have a great day")
        break

else:
    print(f"Goodbye {nm}. Have a beautiful day! ")