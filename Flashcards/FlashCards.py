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
		os.sytem("clear")

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
		SaveFlashcards()
		MainMenu()
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
	szExit = input("Are you sure you want to leave?\n 'Y' or 'N'\n")
	if szExit == "y".strip().lower():
		exit()
	elif szExit == "n".strip().lower():
		MainMenu()
	else:
		ClearTerminal()
		print("Incorrect input enter 'Y' or 'N'")
		time.sleep(1.5)
		ExitProgram()

def NewFlashcard():
	ClearTerminal()
	szTitle = ""
	szTitle = input("What is the title/subject of the new set of flascards?:  ").strip()
	if szTitle == "":
		print("Title can not be empty. Try again:  ")
		time.sleep(2)
		NewFlashcard()
	else:
		print(f"The title has been saved as {szTitle}")
		

def NewQuestion():
	ClearTerminal()
	szQuestion = ""
	szQuestion = input("What is the question:  ")
	if len(szQuestion.strip()) == 0:
		print("Error: Question cannot be empty")
		time.sleep(0.5)
		print("Please try again")
		time.sleep(2)
		NewQuestion()
	else:
		AnswerList.append(szQuestion)
		print(f"{szQuestion} has been saved as a question")

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
		QuestionList.append(szAnswer)
		print(f"{szAnswer} has been saved as a question")

def SaveFlashcards():
	global QuestionList, AnswerList, TitleList
	i = 0
	with open("flashcards.csv", "w", newline = "") as file:
		writer = csv.writer(file)
		writer.writerow(["Title", "Question", "Answer"])
		for i in range(len(QuestionList)):
			writer.writerow([QuestionList[i], AnswerList[i]])

def LoadFlashcards():
	global QuestionList, AnswerList, TitleList
	if os.path.exists("flashcards.csv"):
		with open ("flashcards.csv", "r") as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				QuestionList.append(row[0])
				AnswerList.append(row[1])
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
		

LoadFlashcards()
MainMenu()