import sys
var=1
global check_word
def listtostring(vlist):
   str1=', '.join(vlist);
   str1=str1.replace(',','');
   str1=str1.replace(' ','');
   return str1;
    
def correctvowels( check_word,check_string ):
   nvowels=['a','e','i','o','u']  
   vowels="aeiou";
   cstr=[];
   print check_word;
   lens=len(check_word);
   for i in range(lens):
      print i;
      if check_word[i] in vowels:
         
            check_word=list(check_string);
            for vindex in range(len(nvowels)):
              print vindex;
              check_word[i]=nvowels[vindex];
              print check_word;
              cstr.insert(vindex,listtostring(check_word));
              
   print cstr;
   check_word=list(cstr[1]);
      
            
   return;
while var:
   check_word=raw_input("\n\n >")
   check_word=check_word.lower();
   if check_word =="":
      break;
   else:
      check_word=list(check_word)
   #print lens;
   index=0;
   while index<len(check_word)-2:
       #print len(check_word);
       if check_word[index]== check_word[index+1]== check_word[index+2]:
         del check_word [index];
         index=0;
         
       else:
         index=index+1;
   print check_word;
   index1=0;
   while index1<len(check_word)-1:
      if check_word[index1]== check_word[index1+1]:
         del check_word[index1];
         #print check_word;
         index1=0;
      else:
         index1=index1+1;

   print check_word;
   check_string =listtostring(check_word);
   #print check_string;
   correctvowels( check_word,check_string);
  
