headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
i = 0
limit = 140

while(len(news_ticker) <= 140 and i < len(headlines)):
    hlen = len(headlines[i])
    nlen = len(news_ticker)
    if(nlen + hlen > limit):
        mod = limit-nlen
        news_ticker += " " + headlines[i][:mod]
    else:
        news_ticker += " " + headlines[i]
    i+=1

print(news_ticker)
print(len(news_ticker))
    

        
    