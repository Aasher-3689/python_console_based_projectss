# Quiz game

from colorama import Fore
#--------------------------------------
class MyQuizeApp:
    def __init__(self):
        self.questions = ("What are the number of elements in a periodic table?",
                     "The largest country in the world by area is?",
                     "The hottest planet in our solar system is?",
                     "Pakistan is a part of which continent?",
                     "Total numbers of bones in a human body are?")

        self.options = (("A. 112", "B. 114 ", "C. 118 ", "D. 120 "),
                   ("A. India", "B. Russia", "C. Australia", "D. China"),
                   ("A. Mars", "B. Mercury", "C. Venus", "D. Earth"),
                   ("A. Asia", "B. Australia", "C. Africa", "D. South America"),
                   ("A. 106", "B. 200", "C. 306", "D. 206 "))

        self.answers = ("C", "B", "C", "A", "D")
        self.question_num = 0
        self.guesses = []
        self.score = 0

    #----------------------
    def show_questions(self):
        for question in self.questions:
            print("-------------------------------------")
            print(question)

            for option in self.options[self.question_num]:
                print(option)
            
            #getting answers    
            while True:
                guess = input("Enter you guess (A, B, C, D): ").upper()
                if guess.upper() == self.answers[self.question_num]:
                    self.score += 1
                    print(Fore.MAGENTA +"CORRECT!" + Fore.RESET)
                    break
                else:
                    if guess != "A" and guess != "B" and guess != "C" and guess != "D":
                        print("Please select in range A-D")
                    else:
                        print(Fore.RED + "INCORRECT!" + Fore.RESET)
                        print(f"{self.answers[self.question_num]} is the correct answer")
                        break

            self.guesses.append(guess)
            self.question_num += 1

    #----------------------------------
    def main(self):
        self.show_questions()
        
        print()
        print("---------------------------------")
        print("             RESULT")
        print("---------------------------------")
        print()

        #--------------------
        print("answers:", end=" ")
        for answer in self.answers:
            print(answer, end=" ")

        print()

        print("guesses:", end=" ")
        for guess in self.guesses:
            print(guess, end=" ")

        result = self.score/len(self.questions) * 100
        print()
        print(Fore.CYAN + f"Your score is: {result:.2f}%" + Fore.RESET)
        
if __name__ == "__main__":
    quize_1 = MyQuizeApp()
    quize_1.main()
