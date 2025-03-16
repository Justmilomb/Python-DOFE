import os 
import time
import csv

QuestionList = []
AnswerList = []
TitleList = []

def ClearTerminal():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def MainMenu():
	ClearTerminal()
	print("Welcome to your flashcard maker\nLets get started...")
	time.sleep(0.5)
	print("Choose 1 to add a new flashcard set")
	time.sleep(0.5)
	print("Choose 2 to use your flashcards")
	time.sleep(0.5)
	print("Choose 3 to edit your flashcards")
	time.sleep(0.5)
	print("Choose 4 to wipe data")
	time.sleep(0.5)
	print("Choose 5 to exit the program")
	time.sleep(0.5)
	iChosen = int(input("What number do you choose:  "))
	if iChosen == 1:
		NewFlashcard()
	elif iChosen == 2:
		UseFlashcard()
	elif iChosen == 3:
		EditFlashcard()
	elif iChosen == 4:
		ClearData()
	elif iChosen == 5:
		ExitProgram()
	else:
		ClearTerminal()
		print("Invalid")
		time.sleep(0.5)
		print("Choose a numerical digit between 1-5")
		time.sleep(1.5)
		MainMenu()

def ExitProgram():
	ClearTerminal()
	szExit = input("Are you sure you want to leave?\n 'y' or 'n'\n").strip().lower()
	if szExit == "y":
		exit()
	elif szExit == "n":
		MainMenu()
	else:
		ClearTerminal()
		print("Incorrect input enter 'y' or 'n'")
		time.sleep(1.5)
		ExitProgram()

def NewFlashcard():
	ClearTerminal()
	global szTitle
	szTitle = ""
	szTitle = input("What is the title/subject of the new set of flascards?:  ").strip()
	if szTitle == "":
		print("Title can not be empty. Try again:  ")
		time.sleep(2)
		NewFlashcard()
	else:
		TitleList.append(szTitle)
		print(f"The title has been saved as {szTitle}")
		NewQuestion()
		

def NewQuestion():
	ClearTerminal()
	global QuestionList
	szQuestion = ""
	szQuestion = input("What is the question:  ")
	if len(szQuestion.strip()) == 0:
		print("Error: Question cannot be empty")
		time.sleep(0.5)
		print("Please try again")
		time.sleep(2)
		NewQuestion()
	else:
		QuestionList.append(str(szQuestion))
		print(f"{szQuestion} has been saved as a question")
		NewAnswer()

def NewAnswer():
	szAnswer = ""
	szAnswer = input("What is the answer:  ")
	if len(szAnswer.strip()) == 0:
		print("Error: Question cannot be empty")
		time.sleep(0.5)
		print("Please try again")
		time.sleep(2)
		NewAnswer()
	else:
		AnswerList.append(szAnswer)
		print(f"{szAnswer} has been saved as a question")
		SaveFlashcards()
		MainMenu()

def SaveFlashcards():
	global QuestionList, AnswerList, TitleList
	i = 0
	with open("flashcards.csv", "w", newline = "") as file:
		writer = csv.writer(file)
		writer.writerow(["Title", "Question", "Answer"])
		for i in range(len(QuestionList)):
			writer.writerow([TitleList[i], QuestionList[i], AnswerList[i]])

def LoadFlashcards():
	global QuestionList, AnswerList, TitleList
	if os.path.exists("flashcards.csv"):
		with open ("flashcards.csv", "r") as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				TitleList.append(row[0])
				QuestionList.append(row[1])
				AnswerList.append(row[2])
	else:
		SaveFlashcards()


def ClearData():
	ClearTerminal()
	szAnswer = input("All data would be lost. Are you sure?: 'y' or 'n'").strip().lower()
	if szAnswer == "y":
		global QuestionList, AnswerList, TitleList
		if os.path.exists("flashcards.csv"):
			QuestionList = ""
			AnswerList = ""
			SaveFlashcards()
			LoadFlashcards()
			MainMenu()
		else:
			SaveFlashcards()
			ClearData()
	elif szAnswer == "n":
		print("Going back to the main menu:  ")
		time.sleep(2)
		MainMenu()
	else:
		print("INVALID...")
		time.sleep(0.5)
		print("Please enter 'y' or 'n'")
		ClearData()
		
def UseFlashcard():
	global TitleList, AnswerList, QuestionList
	ClearTerminal()
	NewTitles = list(set(TitleList))
	if len(NewTitles) == 0:
		print("No flashcards saved. Please add some first.")
		time.sleep(2)
		MainMenu()
	else:
		print("Loading Flashcards...")
		print("Available Flashcards")
		for i, title in enumerate(NewTitles):
			print(f"{i + 1}.{title}")
	try:
		title_choice = int(input("Select a flashcard set by entering a number:  ")) - 1
		if title_choice < 0 or title_choice >= len(NewTitles):
			print("Invalid choice. Please enter a valid number")
			time.sleep(1)
			UseFlashcard()
	except ValueError:
		print("Invalid input. Please enter a number.")
		time.sleep(1)
		UseFlashcard()
	selected_title = NewTitles[title_choice]
	matching_questions = [(i, QuestionList[i], AnswerList[i]) for i in range(len(TitleList)) if TitleList[i] == selected_title]

	print(f"\nFlashcard Questions under '{selected_title}':")
	for index, (question) in enumerate(matching_questions):
		print(f"{i + 1}. {question}")
	try:
		question_choice = int(input("Enter the number of the question you want to see the answer for:  ")) - 1
		if question_choice < 0 or question_choice >= len(matching_questions):
			print("Invalid choice. Please enter a valid number")
			time.sleep(1)
			UseFlashcard()
	except ValueError:
		print("Invalid input. Please enter a number.")
		time.sleep(1)
		UseFlashcard()
	_, selected_question, selected_answer = matching_questions[question_choice]
	print(f"Question: {selected_question}")
	input("Press any key to reveal the answer")
	print(f"Answer: {selected_answer}")




LoadFlashcards()
MainMenu()