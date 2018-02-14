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
		if 3 > len(message) > 0 and "9" >= message >= "0":
			with open("users.txt", 'a') as usernew:
				print(nickname, file=usernew)		
			with open("grades.txt", 'a') as gradenew:
				print("\n".join(*mtxt), file=gradenew)
			
		else:
			answer = 'Please input your grade number.'
	else:
		for i in range(0, len(uscheck)):
			if nickname.rstrip() == uscheck[i].rstrip():
				usnumber = i
				break
		grade = grades[usnumber].rstrip()
		if mtxt[0].rstrip().lower() in Week:
			day = mtxt[0].rstrip().lower()
		else:
			day = date.today().weekday()
			day = Week[day]
		path = grade + '/' + day + '.txt'
		schedule = open(path, 'r')
		answer = schedule.readlines()
		if len(answer) == 0:
			answer = "You either have no lessons today or we don't have information about them."
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