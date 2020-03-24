highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
print("\n")

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)
highlighted_poems_stripped = [name.strip() for name in highlighted_poems_list]
print("\n")
print(highlighted_poems_stripped)
print("\n")
highlighted_poems_details = []
for name in highlighted_poems_stripped:
  highlighted_poems_details.append(name.split(':'))
print(highlighted_poems_details)
print("\n")
titles = []
poets = []
dates = []
for name in highlighted_poems_details:
  titles.append(name[0])
  poets.append(name[1])
  dates.append(name[2])
for i in range(len(highlighted_poems_details)):
  print("The poem {titles} was published by {poets} in {dates}".format(titles=titles[i],poets=poets[i],dates=dates[i]))