#Defining the main function and asking user to input scores.
def main():
     def get_average():
        score_1 = float(input("Enter score for test 1: "))
        score_2 = float(input("Enter score for test 2: "))
        score_3 = float(input("Enter score for test 3: "))
        average = (score_1 + score_2 + score_3) / 3        #Calculating the average
        return average

     def check_average(average):
        if average > 95:
           print("Congratulations, Yoy did great...!")
        elif average >= 85 and average <= 95:
           print("You did great, but did not reach the top high...!")
        elif average >=70 and average <= 84:
           print("Great Effort, but you can do better...!")
        else:
           print("You need to study harder next time")

     #Displaying final outputs.
     average=get_average()
     print(f"Your average is: {average:.1f}")
     check_average(average)

main()