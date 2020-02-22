import pymysql
import sys

myDB = pymysql.connect(host='localhost',user='root',passwd='',database='minor')

myCursor = myDB.cursor()

#------------------------------------------------------------------------------
def adminWork():
      while True:
            print('')
            print('')
            print('1. Add Technology')
            print('2. Add Questions')
            print('3. Add Student')
            ch=int(input('choose: '))

            if ch == 1:
                  techname = input('enter techname: ')
                  try:
                        
                        myCursor.execute("insert into technology(tname) values ('{}')".format(techname))
                        print('technolgy added successfully!')
                        myDB.commit()
                  except:
                        print('technolgy not added!')
            elif ch == 2:
                  myCursor.execute("select * from technology")
                  techs = myCursor.fetchall()
                  j=1
                  for i in techs:
                        print(j,i[1])
                        j+=1
                  ind=int(input('select technology: '))
                  tech_id = techs[ind-1][0]
                  print(tech_id)
                  ques = input('enter question:')
                  opta = input('enter option A: ')
                  optb = input('enter option B: ')
                  optc = input('enter option C: ')
                  optd = input('enter option D: ')
                  correct = input('enter correct (A|B|C|D): ')

                  myCursor.execute("insert into questions(question,optionA,optionB,optionC,optionD,correct,techid) values ('{}','{}','{}','{}','{}','{}',{})".format(ques,opta,optb,optc,optd,correct,tech_id))
                  myDB.commit()
                  print('question added: ')
            elif ch==3:
                  pass
            elif ch == 4:
                  sys.exit(0)

            
      
def studentWork():
      print('student hai')
      
      myCursor.execute("select * from questions")
      user = myCursor.fetchall()
      
def startApp():
      uname=input('entor username: ')
      password=input('entor password: ')

      myCursor.execute("select * from user where username='{}' and password='{}'".format(uname,password))
      user = myCursor.fetchone()
      if user:
            print('=====welcome {}====='.format(user[1]))
            if user[6] == 'admin':
                  adminWork()
            elif user[6] == 'student':
                  studentWork()
            
            
      else:
            print('invalid credintials!')

      

startApp()
      


