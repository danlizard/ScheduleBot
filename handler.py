from datetime import *
def handle_message(message, nickname="user"):
	mtxt = message.split()
	answer = ''
	t = 0
	userlist = open("users.txt", 'r')
	uscheck = userlist.readlines()
	userlist.close()
	grd = open("grades.txt", 'r')
	grades = grd.readlines()
	grd.close()
	Week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
	print(nickname, uscheck)
	if nickname not in uscheck:
		if message.isnumeric():
			if 11 >= int(message) >= 5:
				with open("users.txt", 'a') as usernew:
					print(nickname.rstrip(), file=usernew, sep='\n')		
				with open("grades.txt", 'a') as gradenew:
					print(*mtxt, file=gradenew, sep='\n')
		else:
			answer = ['Please input your grade number.']
	elif mtxt[0].rstrip().lower() == "help" or mtxt[0].rstrip()[1:] == "help":
		answer = ["You may send a day's name to receive the schedule for that day or any other message to receive a schedule for today."]
	elif mtxt[0].rstrip().lower() == "/state":
		answer = ["On,", len(uscheck), "users."]
	else:
		for i in range(0, len(uscheck)):
			if nickname.rstrip() == uscheck[i].rstrip():
				usnumber = i
				break
		grade = grades[usnumber].rstrip()
		if mtxt[0].rstrip().lower() in Week:
			day = mtxt[0].rstrip().lower()
		elif mtxt[0].rstrip().lower() == "tomorrow":
			daynmb = (date.today().weekday()+1) % 7
			day = Week[daynmb]
		else:
			day = date.today().weekday()
			day = Week[day]
		path = grade + '/' + day + '.txt'
		schedule = open(path, 'r')
		answer = schedule.readlines()
		for st in range(len(answer)):
			answer[st] = answer[st].rstrip()
		if len(answer) == 0:
			answer = ["You either have no lessons today or we don't have information about them."]
		else:
			print("40", answer)
		schedule.close()

	return answer


if __name__ == "__main__":
	nick = input("Enter your nickname: ")

	while True:
		msg = input("Your message: ")
		ans = handle_message(msg, nick)

	print(ans)