import requests
import random


def get_user_options():
    url_values=""
    user_score = 0
    num_of_questions = ""
    quiz_difficulty_options = ['easy', 'medium', 'hard', "any"]
    quiz_difficulty_ans = ""
    while not num_of_questions or num_of_questions == "0":
        num_of_questions = input("How many questions are you willing to take?: ")
        if num_of_questions.strip() == "" or num_of_questions == "0":
            print("Enter correct number of questions to proceed")
            num_of_questions = ""
        else:
            try:
                user_value = int(num_of_questions)
                url_values += str(user_value)
            except ValueError:
                if num_of_questions.isalpha():
                    print("You entered a string that is not a number")
                    num_of_questions = ""

    while quiz_difficulty_ans not in quiz_difficulty_options:
        quiz_difficulty_ans = input("Choose difficultly either, Easy, Medium, Hard, Any: ").lower()
        if quiz_difficulty_ans not in quiz_difficulty_options:
            print("Enter either Easy, Medium, Hard or Any")
            quiz_difficulty_ans = ""

    

    if quiz_difficulty_ans and quiz_difficulty_ans != "any":
        url_values += '&difficulty=' + quiz_difficulty_ans
    questions_Arr = get_questions_online(url_values)
    # Show user questions
    if questions_Arr:
        for question in questions_Arr:
            user_score += show_user_question(question)
            print("Current Score: ", user_score)

    total_score = str(user_score) + "/" + str(len(questions_Arr))
    print()
    print()
    print("Total Score: ", total_score)


def get_questions_online(url_values):
    #Our OpenTrivia Api endpoint
    url = 'https://opentdb.com/api.php?amount='
    url += url_values
    try:
        response = requests.get(url)

        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts["results"]
        else:
            print('Error:', response.status_code )
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def show_user_question(quiz_obj):
    print()
    print("Difficulty: ", quiz_obj["difficulty"])
    quiz_obj["incorrect_answers"].append(quiz_obj["correct_answer"])
    random.shuffle(quiz_obj["incorrect_answers"])
    options_string = ', '.join(quiz_obj["incorrect_answers"])
    print("Question: ",quiz_obj["question"])
    print("Options: ", options_string)
    print(quiz_obj["correct_answer"])
    userans = input("Enter Ans: ").lower()
    score = mark_answer(userans, quiz_obj["correct_answer"])
    return score
    


def mark_answer(userAnswer, correctAnswer):
    if userAnswer == correctAnswer.lower():
        print("Correct! Yeahhhh!")
        return 1
    else:
        print("Sorry, better luck next time")
        print("Correct Answer is: ", correctAnswer)
        return 0



get_user_options()