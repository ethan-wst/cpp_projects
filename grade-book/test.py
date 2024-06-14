import textwrap
value = "Exam: 25%    Exam: 25%   Exam: 25%    Exam: 25%   Exam: 25%    Exam: 25%   Exam: 25%    Exam: 25%   Exam: 25%    Exam: 25%   "
wrapper = textwrap.TextWrapper(width=50) 
  
string = wrapper.fill(text=value) 
  
print (string) 