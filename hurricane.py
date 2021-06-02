# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
damages_updated = []
for element in damages:
  if element[-1] == "M":
    element = element.replace("M", "0")
    damages_updated.append(int(float(element)) * 1000000)
  elif element[-1] == "B":
    element = element.replace("B", "0")
    damages_updated.append(int(float(element))*1000000000)
  else:
    damages_updated.append(element)
# test function by updating damages
print(damages_updated)
# 2 
# Create a Table
hurricane_dictionary_names = {}
for i in range(len(names)):
  value = hurricane_dictionary_names.setdefault(names[i], {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Winds": max_sustained_winds[i], "Area Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]})
# Create and view the hurricanes dictionary
print(hurricane_dictionary_names)
# 3
# Organizing by Year
hurricane_dictionary_years = {}
# create a new dictionary of hurricanes with year and key
for i in range(len(years)):
  value = hurricane_dictionary_years.setdefault(years[i], {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Winds": max_sustained_winds[i], "Area Affected": areas_affected[i], "Damage": damages_updated[i], "Death": deaths[i]})
print(hurricane_dictionary_years)
# 4
# Counting Damaged Areas
damaged_area_count = {}
# create dictionary of areas to store the number of hurricanes involved in
for i in areas_affected:
  for k in i:
    if k in damaged_area_count:
      damaged_area_count[k] += 1
    else:
      damaged_area_count[k] = 1
print(damaged_area_count)
# 5 
# Calculating Maximum Hurricane Count
max_area = "Central America"
max_area_count = 0
for key in damaged_area_count:
  if damaged_area_count[key] > max_area_count:
    max_area = key
    max_area_count = damaged_area_count[key]
# find most frequently affected area and the number of hurricanes involved in
print("The most frequently affected area is: " +max_area+" with count of : "+str(max_area_count)+".")

# 6
# Calculating the Deadliest Hurricane
dealiest_hurricane = "Cuba I"
max_death_count = 0
for i in range(len(deaths)):
  if deaths[i] > max_death_count:
    max_death_count = deaths[i]
    deadliest_hurricane = names[i]
# find highest mortality hurricane and the number of deaths
print("The Hurricane with the highest mortality rate is: \""+deadliest_hurricane+ "\" with the Death Count of: "+ str(max_death_count))
# 7
# Rating Hurricanes by Mortality
mortality_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
for i in deaths:
  if i == 0:
    mortality_rating[0].append(i)
  if i > 0 and i <= 100:
    mortality_rating[1].append(i) 
  elif i > 100 and i <=500:
    mortality_rating[2].append(i)
  elif i > 500 and i <= 1000:
    mortality_rating[3].append(i)
  elif i > 1000 and i <= 10000:
    mortality_rating[4].append(i)
  else:
    mortality_rating[5].append(i)
# categorize hurricanes in new dictionary with mortality severity as key
print("Hurricane Rating based on mortality" + str(mortality_rating))


# 8 Calculating Hurricane Maximum Damage
max_damage_cane = "Cuba I"
max_damage = 0
for i in range(len(damages_updated)):
  if damages_updated[i] != "Damages not recorded":
    if int(damages_updated[i]) > 0:
      max_damage_cane = names[i]
      max_damage = damages_updated[i]
# find highest damage inducing hurricane and its total cost
print("The hurricane that caused the greatest damage is: \""+ max_damage_cane + "\" which cost $" + str(max_damage))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damages = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
for i in damages_updated:
  if i != "Damages not recorded":
    if i >0 and i <= 100000000:
      hurricanes_by_damages[1].append(i)
    elif i >0 and i <= 1000000000:
      hurricanes_by_damages[2].append(i)
    elif i >0 and i <= 10000000000:
      hurricanes_by_damages[3].append(i)
    elif i >0 and i <= 50000000000:
      hurricanes_by_damages[4].append(i)
    else:
      hurricanes_by_damages[5].append(i)
print("Hurricanes rating based on damages :"+ str(hurricanes_by_damages))

    
