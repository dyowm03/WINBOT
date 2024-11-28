import webbrowser
import pyttsx3
import os



h = pyttsx3.init('sapi5')
voices = h.getProperty('voices')
print(voices[1].id)
h.setProperty('voice',voices[1].id)


def speak(audio):
    h.say(audio)
    h.runAndWait()

rate = h.getProperty('rate')
print(rate)
h.setProperty('rate', 130)




if __name__ == "__main__":
    speak("hello sir   i am Athena  your personal assistant how may i help you  please type your request ")






a=input("Hello Sir I am Your Personal Assistant How May I Help YOU Please Type Your Request::: ")
if 'youtube' in a :
     print("processing  O")
     if __name__ == "__main__":
         speak("sir your youtube is opening")
     webbrowser.open("youtube.com")

elif 'google'  in a :
     print("processing    O")
     if __name__ == "__main__":
         speak("  sir your google is opening")
     webbrowser.open("www.google.com")

elif  'your name'  in  a :
     speak("My name is Athena")
     print("Athena")

elif 'dps'  in  a :
     speak("it is my lord school ")
     print("it is my lord school")
     webbrowser.open('dps shaeedpath lucknow')
elif 'yahoo' in a:
     print("processing O")
     webbrowser.open("www.yahoo.com")
elif 'facebook'  in a :
     print("processing O")
     speak(" sir your facebook is opening")
     webbrowser.open("www.facebook.com")   

elif 'amazon' in a :
     print("processing O")
     speak(" sir your amazon is opening")
     webbrowser.open("www.amazon.in")



elif 'python' in a :
     print("processing  O")
     speak("  your python website is opening")
     webbrowser.open("python.org")



elif a=='Folder' or 'folder':
     speak("Enter the path of the folder")
     print("Enter the path of the folder")
     c=input()
     os.startfile(c)     

elif 'explore' in a :
     speak("  sir what do you want to explore")
     o=input("  sir what do you want to explore:::")
     if 'songs' in o:
          speak("what type of songs you  want to hear like bollywood 1 , hollywood 2 , trollywood 3 ,  punjabi 4, bengali 5 ")
          s=input("what type of songs you  want to hear like bollywood 1 , hollywood 2 , trollywood 3 ,  punjabi 4 , bengali  5  :::")
          if '1' in s :
               speak(" sir here are  your bollywood songs ")
               print(" sir here are  your bollywood songs")
               print("processing    O")
               webbrowser.open("top bollywood songs 2024")

          elif '2' in s :
               speak(" sir here are  your hollywood songs ")
               print(" sir here are  your hollywood songs")
               print("processing    O")
               webbrowser.open("top  hollywood   songs 2024")
          elif '3' in s :
               speak(" sir here are  your trollywood songs ")
               print(" sir here are  your trollywood  songs")
               print("processing    O")
               webbrowser.open("top trollywood  songs 2024")


          elif '4' in s :
               speak(" sir here are  your punjabi songs ")
               print(" sir here are  your punjabi songs")
               print("processing    O")
               webbrowser.open("top punjabi songs 2020")
          elif '5' in s :
               speak(" sir here are  your bengali songs ")
               print(" sir here are  your bengali songs")
               print("processing    O")
               webbrowser.open("top  bengali  songs 2024")
          else:
               speak("sorry sir press d to search it on onlin")

               print("sorry sir press d to search it on online")
               p=input("enter here::::")
               webbrowser.open ("top " + s + " songs 2024")

     elif o=='games':
          speak("which type off games sir like onlin 1 , offlin 2 , big games 3 , small games 4, or other 5 , google doodle games press any key ")
          print("which type off games sir like onlin 1 , offlin 2 , big games 3 , small games 4, or other 5  ,  google doodle  games press any key")

          x=input("Enter  Here :::")
          if x =='1':
               speak("here is your online games ")
               print("here is your online games")
               webbrowser.open("top 10 online games for pc")

          elif x=='2' :
               speak("here are your offlin games")
               print("here  are your offline games ")
               webbrowser.open("top 10 offline games for pc ")

          elif x=='3' :

               speak("here are your big  games")
               print("here  are your big games ")
               webbrowser.open("top 10 big  games for pc")
          elif x=='4' :
               speak("here are your small  games")
               print("here  are your small games ")
               webbrowser.open("top 10 small games for pc")
          elif x=='5' :
               speak("here are your other games")
               print("here  are your other games ")
               webbrowser.open("top 10 games for pc")


          else:
               speak(" sir ")
               print(" sir")
               webbrowser.open("top google doodle games")


     elif 'books' in o :
          speak(" sir which type of books you want press 1 for autobiographies, 2 for story books , 3 for cbse books 4 for motivating books")    
          print(" sir which type of books you want press 1 for autobiographies, 2 for story books , 3 for cbse books 4 for motivating books") 
          l=input("Enter Here:::")
          if l =='1':
               speak(" sir  i am opening autobiographies")
               webbrowser.open("top biographies")
          elif l=='2':
               speak(" sir  i am opening story books  ")
               webbrowser.open("top storybooks")
          elif l=='3':
               speak(" sir opening cbse  books ")
               webbrowser.open("cbse books")
          elif l=='4':
               speak(" sir i am opening motivational books ")
               webbrowser.open("top motivational books")
     elif 'movies' in o:
          speak(" sir enter which type of movies you want to watch   1-bollywood movies 2-hollywood movies 3-trollywood movies 4-a particular movi  ")
          print("sir please enter which type of movies you want to watch   1-bollywood movies 2-hollywood movies 3-trollywood movies 4-a particular movie")
          k=input("Enter Here:::")
          if k=='1':
               speak(" sir here are your bollywood movies ")
               print(" sir opening bollywood movies:::")
               webbrowser.open("top  new bollywood movie")
          elif k=='2':
              speak(" sir i am opening hollywood movie")
              print(" sir opening hollywood movie ")
              webbrowser.open("top new  hollywood movies")

          elif   k=='3':
               speak(" sir i am opening trollywood movies  ")
               print(" sir i am opening trollywood movies")
               webbrowser.open("top new  trollywood movies")

          elif k=='4':
               speak("which movie you want to search  ")
               print("which movie you want to search")
               q=input("Enter Here:::")
               webbrowser.open(q)
          else:
               speak("bye sir ")
               print("bye sir ")


     elif o=='news':
          speak("Which Type Of News like 1-hindi , 2- english")
          an=input("Which Type Of News like 1-hindi , 2- english :::")
          if an=='1':
               speak(" sir here are your hindi  news")
               print(" sir ")
               webbrowser.open("todays news in hindi")
          else:
               speak("here are your english news")
               print(" sir ")
               webbrowser.open("todays news in english")


     else:

          print(" Thank You sir ")
          speak(" Thank You sir ")

elif a=='dictionary':
     speak(" sir which word you want to search ")
     print(" sir which word you want to search ")
     my=input("Enter Here :::")
     speak(" sir in which language you want to search the meaning")
     print(" sir in which language you want to search the meaning")
     language=input("Enter Here::: ")
     webbrowser.open(my+" " +"meaning in "+ language  )

elif a=='study':
     speak(" sir which subject you want to study")
     print(" sir which subject you want to study")
     subject=input("Enter Here:::")
     speak(" sir select grade ")
     print("which grade")
     grade=input("Enter Here:::")
     speak(" sir which chapter you want to study")
     print(" sir which chapter you want to search")
     chapter=input("Enter Here:::")
     speak(" sir i am opening the content")
     a=("https://www.youtube.com/results?search_query=")
     webbrowser.open(a+"class" + grade + subject +"chaper " + chapter )


elif a=='maths':
     speak("ok sir what you want to calculate ")
     print("Sir Please Enter the number as well as the operator ")
     num1 =  float(input("Enter  Your First Number Here:::"))
     num2 = float(input("Enter your second number here:::"))
     op = input("Enter your operator :::")

     if op =='+':
          print(num1+num2)
          speak("you asked me addition problem it was easy")
     elif op=='-':
          print(num1-num2)
          speak("sir you asked me a subtraction problem")
     elif op=='/':
          print(num1/num2)
          speak("ok sir it was quite tough")
     elif op=='*':
          print(num1*num2)
          speak("sir it was little tricky  you asked me a multiplication problem ")


     else:
           print("your operator is wrong")


elif a== 'mobiles':
     speak("sir please tell me your price range ")
     price=input(" Enter here:::")

     print("Procssing O")
     webbrowser.open("top mobiles in "+ price )

elif a=='computer':
     speak("well good to hear please write your base price")
     enter=input("Enter Here:::")
     print("Processing  O")
     webbrowser.open("top computers starting from"+enter)


elif a=='best places to visit ':
      speak("ok sir just enter in which city ")
      city=input("Enter here :::")
      webbrowser.open("top places to visit in " + city)
      speak("ok sir opening these are your best places ")
      print("Processing  O ")

elif a=='therock':
     password ='iamthegreat123'

     for  i in range(1):
          i=0
          i=i-1
          speak("hello sir please type the password")
          print("you have 2 chances")
          this=input("Enter the Password:::")

          this=input("Enter the Password:::")
          if this==password:

               print("Welcome sir in our secret feature ")
               speak("welcome sir in our new feature ")

               speak("hello sir i am personal assistant how may i help you ")
               print("welcome sir in our new secret feature")
               z=input("Enter your Demand :::")

               if z=='creators number':
                    speak("ok sir i am providing you the number of my creator but please rewrite the password")
                    a='num'
                    hint=input("Enter your password::: ")
                    if hint==a:
                      print("9811260637")

                    else:
                         print("you are a lier please go home")




          else:
               print("sorry sir you cannot use this feature" )
               continue

elif a=="speed test":
     speak("ok sir i am going to do speed test")
     print("Processing  O  ")
     webbrowser.open("https://www.google.com/search?q=internet+speed+test&oq=internet+speed&aqs=chrome.0.0j69i57j0l6.4338j0j7&sourceid=chrome&ie=UTF-8")
elif 'gmail' in  a  :
     print("processing   O")
     speak(" your gmail is opening")
     webbrowser.open("https://mail.google.com")


elif a =="new meeting":
     speak("ok sir i am going to start a meeting ")
     print("Processing     O    ")
     webbrowser.open("https://meet.google.com/_meet/gba-sbps-jtb?ijlm=1592719220031&adhoc=1&hs=187")

elif a=="join meeting": 
     speak("ok sir ")
     print("Processing  O ")    
     webbrowser.open("https://meet.google.com/")
elif 'whatsapp' in a :
     print("processing  o ")
     speak(" your whatsapp is opening")
     webbrowser.open("https://www.whatsapp.com/")


elif 'wikipedia'  in  a :
     print("processing   O")
     speak(" your wikipedia is opening")
     webbrowser.open("https://www.wikipedia.org/")




elif 'twitter'   in a :
    print("processing   O")
    speak(" your twitter is opening")
    webbrowser.open("https://twitter.com/")




elif 'notepad' in  a :
     print("processing  O")
     speak(" sir your notepad app is opening")
     a='notepad'
     os.system(a)



elif a=='top hotels':
     speak("ok sir i just want to know that in which city you want to search ")
     city=input("Enter Here:::")
     speak(" ok sir i am going to give you details about the hotels of "  + city )
     print("ok sir searching the details about the hotel of this location:::")
     webbrowser.open("top hotels in " + city)

else:
    speak("sorry sir   i cant help at this moment")
    speak("can i search this for you in online if you want to change the text press b ")
    v=input("can i search this for you in online if you want to change the text press b:::")
    if v=='yes':
       webbrowser.open(a)

    elif v=='b':
       m=input("enter your different text:::")
       webbrowser.open(m)
    else:
          print(" sir thank you for choosing me ")
          speak(" sir thank you for choosing me do not forget to rate")
          rate =input("Rate us (from 1 to 5 )::: ")
          if rate =='1':
               print("Thanks for your feedback ")
               speak("ok sir thanks for your feedback but why your experience was not good with us would you like to share with us ")
               share =input("Enter Here::  ")
               if "yes" in share :
                    speak("Thanks for cooperating with us ")
                    h=input("Enter your problem:::")
               else:
                    speak("no problem sir ")
                    print("Thanks for your crucial time ")


          elif "2"or  "3"   in rate:
               speak("no problem sir ")
               print("Thanks for your crucial time ")

          elif "4 " or "5" in rate :
               speak("thank you sir for your feedback")
               print("thanks for your crucial time")

          else :
               speak("Thank you for your crucial time")
               print("Thank you for your feedback")
