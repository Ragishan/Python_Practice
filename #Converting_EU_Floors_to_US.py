#Program converting European Floors to US Floors
#inp = input("European Floor(s)? ")
#usf = int(inp) + 1
#print("US Floors", usf)

#program to check ratings in a list using a conditional while loop
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
Rating = PlayListRatings[0]
while (Rating >= 6 and i < len(PlayListRatings)):
    print(Rating) 
    i+=1   
    Rating = PlayListRatings[i]
    