


def computeGrades(score):
  
    letter = []
    for x in score:
        
        if x < 60:
            letter.append('F')
             
        elif x >= 60 and x <= 69:
            letter.append ('D')
             
        elif x >= 70 and x <= 79:
            letter.append('C')
             
        elif x >= 80 and x < 90:
            letter.append( 'B')
             
        elif x >=90:
            letter.append('A')
             
    return letter


def gradeRemark(score):

    remark = []
    for x in score:

        if x >= 96:
            remark.append('Outstanding')
      
        elif x >= 90 and x <= 95:
            remark.append('Exceeds Expectations')
      
        elif x >= 80 and x <= 89:
            remark.append('Acceptable')
       
        elif x <= 79:
            remark.append('Trollish')
        
    return remark

def getinput(num):
    i = 0

    list = []
    while i != num:
         j = int(input("Grade? "))
         list.append(j)
         i = i+1

    return list




def main():
 
   count = int(input("How Many? "))
   score = getinput(count)
   remark = gradeRemark(score)
   y = 0
   for x in computeGrades(score):
       print(x + " " + remark[y])
       y = y+1

   
main()


