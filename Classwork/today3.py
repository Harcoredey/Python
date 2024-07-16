language = input ('enter your preferred language: ')
match language:
	case 'java':
		print("you're a java programmer")
	case 'python':
		print("you're a python programmer")
	case_:
		print("you're a software engineer")