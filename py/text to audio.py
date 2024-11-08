from gtts import gTTS
import playsound
text = input( "Enter your Text :")
sound = gTTS( text, lang="ta")

sound. save( "C:\\Users\\gs400\\Documents\\New.mp3")
playsound. playsound( "C:\\Users\\gs400\\Documents\\New.mp3" )
