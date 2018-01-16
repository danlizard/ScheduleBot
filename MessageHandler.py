def handle_message(message, nickname="user"):
	A = message.split(' ')
	answer = ''
	if len(A) != 2:
		answer = 'Remember, the message must look like that: "<day> <grade_number>", with all letters typed low-case'
	else:
		try:
			gr = A[1]
			if gr > 11 or gr < 5:
				answer
		except:
			answer = 'Remember, the message must look like that: "<day> <grade_number>", with all letters typed low-case'
		if answer == '':
			wd = A[0]
			ad = wd + '/' + gr + '.txt'
			Tab = open(ad, 'r')
    		answer = Tab.readlines()
    		if answer == '':
    			answer = "Looks like you're free on" + '' + wd + '!' + " (or the bot doesn't have the information about that grade/day" + ').'

    return answer


if __name__ == "__main__":
    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)