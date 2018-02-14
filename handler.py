from datetime import *
def handle_message(message, nickname="user"):
	mtxt = message
	answer = ''
	t = 0
	userlist = open("users.txt", 'r')
	uscheck = userlist.readlines()
	userlist.close()
	grd = open("grades.txt", 'r')
	grades = grd.readlines()
	grd.close()
	Week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
	if nickname not in uscheck:
		if 3 > len(message) > 0 and "9" >= message[0] >= "0":
			usernew = open("users.txt", 'w')
			print(nickname, file=usernew)
			usernew.close()
			gradenew = open("grades.txt", 'w')
			print(mtxt, file=gradenew)
			gradenew.close()
		else:
			answer = 'Please input your grade number.'
	else:
		usnumber = uscheck.find(nickname)
		grade = grades[usnumber]
		if mtxt.lower in Week:
			day = mtxt.lower
		else:
			day = date.today().weekday()
			day = Week[day]
		path = grade + '/' + day + '.txt'
		schedule = open(path, 'w')
		answer = schedule.readlines()
		if answer = '':
			answer = "You either have no lessons tomorrow or we don't have information about them."
		schedule.close()

    return answer


if __name__ == "__main__":
    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)