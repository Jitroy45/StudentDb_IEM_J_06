def read_test_scores():
    print("Enter School ID:")
    ID = int(input())
    print("Enter Exam Score:")
    Exam = int(input())
    print("Enter al test Scores:")
    Score1 = int(input())
    Score2 = int(input())
    Score3 = int(input())
    Score4 = int(input())
    Score5 = int(input())
    Score6 = int(input())

    sum =(Score1 + Score2 + Score3 + Score4 + Score5 + Score6)

    TAvg = sum/6.0
    return(TAvg,ID,sum)

def compute_final_score(TAvg, Exam):
    final_score = 0.4*TAvg + 0.6*Exam
    return(final_score)

def final_grade(final_score):
    if 92<= final_score <=100:
        grade = "A+"
    elif 85<= final_score <=92:
        grade = "A"
    elif 75<= final_score <=85:
        grade = "B+"
    elif 68<= final_score <=75:
        grade = "B"
    elif 60<= final_score <=68:
        grade = "C+"
    elif 50<= final_score <=60:
        grade = "C"
    elif 45<= final_score <=50:
        grade = "D+"
    elif 40<= final_score <=45:
        grade = "D"
    else:
        grade = "F"
    return grade

def print_comment(grade):
    if grade == ("A+", "A"):
        print("Comment: Very good")
    elif grade == ("B+", "B"):
        print("Comment: Good, but could be better")
    elif grade == ("C+", "C"):
        print("Comment: Satisfactory, needs more improvement")
    elif grade == ("D+", "D"):
        print("Comment: Poor")
    elif grade == ("F"):
        print("Comment: FAIL")



(TAvg, ID, Exam) = read_test_scores()
print("Test Average is: " + str(TAvg))
My_variable = compute_final_score(TAvg, Exam)
print("FINAL SCORE IS:  " + str(My_variable))
grade = final_grade(My_variable)
print("LETTER GRADE IS:  " + str(grade))
print_comment(grade)


