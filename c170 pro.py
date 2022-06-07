from tkinter import *
root=Tk()
root.title("Grades")
root.geometry("600x600")

grade3_percentage_label=Label(root)
grade5_percentage_label=Label(root)
grade10_percentage_label=Label(root)






class Grade3():
    def __init__(self,language_arts,Mathemathics):
        self.ELA=language_arts
        self.math=Mathemathics
    def percentage(self):
        score=self.ELA+self.math
        total_marks=score/200
        grade3_percentage=total_marks*100
        grade3_percentage_label['text']=grade3_percentage
        
class Grade5():
    def __init__(self,science,language_arts,mathemathics):
        self.sci=science
        self.language=language_arts
        self.math=mathemathics
    def percentage(self):
        score=self.sci+self.language+self.math
        total_marks=score/300
        grade5_percentage=total_marks*100
        grade5_percentage_label['text']=grade5_percentage
        
class Grade10():
    def __init__(self,science,language_arts,mathemathics,technology):
        self.sci=science
        self.language=language_arts
        self.math=mathemathics
        self.tech=technology
    def percentage(self):
        score=self.sci+self.language+self.math+self.tech
        total_marks=score/400
        grade10_percentage=total_marks*100
        grade10_percentage_label['text']=grade10_percentage
        
obj1_3=Grade3(40,50)  
obj2_5=Grade5(50,70,90)
obj3_10=Grade10(40,60,80,100)

btn_grade3=Button(root,text="Grade 3 Percentage",command=obj1_3.percentage)
btn_grade5=Button(root,text="Grade 5 Percentage",command=obj2_5.percentage)
btn_grade10=Button(root,text="Grade 10 percentage",command=obj3_10.percentage)
btn_grade3.pack(padx=20,pady=20)
grade3_percentage_label.pack(padx=20,pady=20)
btn_grade5.pack(padx=20,pady=20)
grade5_percentage_label.pack(padx=20,pady=20)
btn_grade10.pack(padx=20,pady=20)
grade10_percentage_label.pack(padx=20,pady=20)
root.mainloop()
