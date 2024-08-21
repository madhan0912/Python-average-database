import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore  import *
from PyQt5.QtGui import *
import mysql.connector

class Stu_form(QWidget):

    def __init__ (self):
        super().__init__()
        self.windows()

    def windows(self):
        self.fbox =QFormLayout()
        self.hbox = QHBoxLayout()

        self.lb1 = QLabel("Students Name")
        self.stu_name = QLineEdit()

        self.lb2 = QLabel("Roll No")
        self.roll_no = QLineEdit()

        
        self.lb3 = QLabel("SUBJECTS")
        self.lb3.setAlignment(Qt.AlignCenter)
        
        
        
        self.lb4 = QLabel("Tamil")
        self.tamil = QLineEdit()

        self.lb5 = QLabel("english")
        self.english = QLineEdit()
        
        self.lb6 = QLabel("Maths")
        self.maths = QLineEdit()

        self.lb7 = QLabel("Science")
        self.science = QLineEdit()
        
        self.lb8 = QLabel("Social")
        self.social = QLineEdit()

        self.lb9 = QPushButton("submit")
        self.lb9.clicked.connect(self.submit)
        self.lb10 = QPushButton("cancel")
        self.lb10.clicked.connect(self.cancel)        

      

        self.fbox.addRow(self.lb1,self.stu_name)
        self.fbox.addRow(self.lb2,self.roll_no)
        self.fbox.addRow(self.lb3)
        self.fbox.addRow(self.lb4,self.tamil)
        self.fbox.addRow(self.lb5,self.english)
        self.fbox.addRow(self.lb6,self.maths)
        self.fbox.addRow(self.lb7,self.science)
        self.fbox.addRow(self.lb8,self.social)
        self.fbox.addRow(self.lb9,self.lb10)
        #msgox 1
        self.msg_1 = QMessageBox()
        self.msg_1.setIcon(QMessageBox.Information)
        self.msg_1.setText("values insetred into madhan database")
        #msgbox 2
        self.msg_2 = QMessageBox()
        self.msg_2.setIcon(QMessageBox.Information)
        self.msg_2.setText("enter the mark within 100")
        #msgbox 3
        self.msg_3 = QMessageBox()
        self.msg_3.setIcon(QMessageBox.Information)
        self.msg_3.setText("Are sure want to  cancel")
        


        self.setLayout(self.fbox)
        self.setGeometry(100,100,400,250)
        self.setWindowTitle("Student  form")
        self.show()
        

    def submit(self):
        try:
             database = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="madhan",
                auth_plugin="mysql_native_password",
                database = "madhan"

            )
             
             cursorobject = database.cursor()
            

             s1 = self.stu_name.text()
             s2 = self.roll_no.text()
             s3 = self.tamil.text()
             s4 = self.english.text()
             s5 = self.maths.text()
             s6 = self.science.text()
             s7 = self.social.text()

             tamil = int(self.tamil.text())
             english = int(self.english.text())
             maths= int(self.maths.text())
             science = int(self.science.text())
             social = int(self.social.text())
             
             #print marks
             print("name",s1)
             print("Roll.no",s2)
             print("Tamil",tamil)
             print("English",english)
             print("Maths",maths)
             print("Science",science)
             print("Social",social)
             

             #get the total form the subject
             if (tamil<=100 and english<=100 and maths<=100 and science<=100 and social<=100):
                 total =(tamil + english + maths + science + social)
                 s8 = total
                 print("total",total)
             else:
                 print("enter the mark within 100")
                 msgbox = self.msg_2.exec_()
                 sys.exit()

             s9 = ""
             #get the average form the subject
             if (tamil<=100 and english<=100 and maths<=100 and science<=100 and social<=100):
                 average =(total)/5
                 s9 = average
                 print("Average",average)
                
             else:
                 print("enter the mark within 100")
                 #msg box calling function
                 msgbox = self.msg_2.exec_()
                 
                
            
             #insert the data into database
             sql = "Insert into students_form (Student_name, Roll_no,Tamil,English,Maths,Science,Social,total,average)\
             values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             values = (s1,s2,s3,s4,s5,s6,s7,s8,s9)

             
           
             cursorobject.execute(sql,values)
            
             database.commit()
             print("value inserted into database")
            
            
             #msg box calling function
             msgbox = self.msg_1.exec_()

        except Exception as e:
            print(e)


   
    def cancel(self):
        print("Are sure want to  cancel")
        #msg box calling function
        msgbox = self.msg_3.exec_()
        self.close()
def main():
    app = QApplication(sys.argv)
    em = Stu_form()
    sys.exit(app.exec())

    
if __name__ == '__main__':
    main()

        







