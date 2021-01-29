import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv('data/student-mat.csv')

def student_test1():
    students['G1'].plot(kind='hist', figsize=(15, 6))
    plt.show()

def student_study_time():
    students['studytime'].value_counts().plot(kind='pie', figsize=(8, 8))
    plt.show()
def correlation():
    corr = students.corr()
    fig =plt.figure(figsize=(8, 8))
    plt.matshow(corr, cmap='RdBu', fignum=fig.number)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title('Figure 1: Correlation')
    plt.savefig('correlation.png')
    plt.show()
    # Postive correlation between parents eduction and results in the two tests and final
    # Positively Strong correlation between each test results
    # Positive correlation between study time and results
    # negatively strong correlation between failures and results
    # negative correlation between going out and results
    # negative correlation between age and results
    # Strong negative correlation between alcohol consumption on weekday and results
    # No correlation between schools

def failuresVsfinalMark():
    students.plot(kind='scatter', x='failures', y='G3', figsize=(8, 8))
    plt.ylabel('Final Test Score')
    plt.xlabel('Failures')
    plt.title('Figure 2: Failures Vs Final Test Scores')
    plt.savefig('images/Final_test_vs_Failures.png')
    plt.show()

def MothersEducationVsfinalMark():
    students.plot(kind='scatter', x='Medu', y='G3', figsize=(8, 8))
    plt.ylabel('Final Test Score')
    plt.xlabel('Mothers Education')
    plt.title('Figure 3: Mothers Education Vs Final Test Scores')
    plt.savefig('images/Final_test_vs_Mothers_education.png')
    plt.show()

def GoingOutVsfinalMark():
    students.plot(kind='scatter', x='goout', y='G3', figsize=(8, 8))
    plt.ylabel('Final Test Score')
    plt.xlabel('Going out')
    plt.title('Figure 4: Going Out Vs Final Test Scores')
    plt.savefig('images/Final_test_vs_Going_out.png')
    plt.show()

def DailyDrinkingVsfinalMark():
    students.plot(kind='scatter', x='Dalc', y='G3', figsize=(8, 8))
    plt.ylabel('Final Test Score')
    plt.xlabel('Daily Drinking')
    plt.title('Figure 5: Daily Drinking Vs Final Test Scores')
    plt.savefig('images/Final_test_vs_Daily_drinking.png')
    plt.show()

#correlation()
#failuresVsfinalMark()
#MothersEducationVsfinalMark()
#GoingOutVsfinalMark()
#DailyDrinkingVsfinalMark()

print(students.describe())
