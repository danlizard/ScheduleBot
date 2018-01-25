def handle_message(message, nickname="user"):
	mtxt = message.split(' ')
	answer = ''
	if len(mtxt) != 2:
		answer = 'Remember, the message must look like that: "<day> <grade_number>"'
	else:
		try:
			grade = A[1]
			if int(grade) > 11 or int(grade) < 5:
				answer
		except:
			answer = 'Remember, the message must look like that: "<day> <grade_number>"'
		if answer == '':
			weekday = mtxt[0]
			ansday = weekday.lower() + '/' + grade + '.txt'
			Tab = open(ansday, 'r')
    		answer = Tab.readlines()
    		if answer == '':
    			answer = "Looks like you're free on" + '' + weekday + '!' + " (or the bot doesn't have the information about that grade/day" + ').'

    return answer


if __name__ == "__main__":
    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)