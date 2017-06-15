
places = {}
while True:
	place = raw_input("Tell me where you went: ")
	# print(place)
	if (place == ''):
		break
	else:
		stateCountry = place.split(', ')
		if len(stateCountry) != 2:
			print("That's not a legal city, state combination")
			continue
		else:
			if stateCountry[1] in places:
				places[stateCountry[1]].append(stateCountry[0])
			else:
				places.setdefault(stateCountry[1], [stateCountry[0]])


# places = {'USA': ['New York', 'Chicago', 'Boston'], 'England': ['London'], 'China': ['Shanghai', 'Beijing']}
print("\nYou visited:")
for key in sorted(places.keys()):
	print(key)
	for item in sorted(places[key]):
		print("   {0}".format(item))
