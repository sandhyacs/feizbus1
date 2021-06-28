output = ""



# for i in range(1,101):
# 	# print(i)
# 	if i%3==0:
# 		print(i)
# 		output = "feiz"
# 	if i%5==0:
# 		print(i)
# 		output = "bus"
# 	if i%15==0:
# 		print(i)
# 		output = "feizbus"
# 	print(output)


for i in range(1,101):
	# print(i)
	if i%3==0 or i%5==0:
		print(i)
		output += "feiz"
	if i%5==0:
		print(i)
		output += "bus"
	# if i%15==0:
	# 	print(i)
	# 	output = "feizbus"
	print(output // i)
