#!/bin/python3

import sys
from art import *
from colorama import init
from colorama import Fore, Back, Style
import time


#Make the colours easier to use
blue = Fore.CYAN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

def banner():
	title = "USR"
	header = text2art(title, font='speed')
	print(header + "[*] [U]seful [S]tudy [R]esources - Toby Jackson (@skunk)\n")

def line_break():
	print("-" * 40)

def footer():
	title = "skunk"
	header = text2art(title, font='speed')
	print(header + "[*] Cyaaaaaaaaaaaaaaaa! I hope you found something that interested you. \n")


def welcome_menu():
	banner()
	line_break()
	print("[*] Let's get started. What would you sort of thing would you like to learn about?")
	print("[*] I've colour coded the activities for you.")
	print("[*] " + red + "Red = Full Concentration Needed!")
	print("[*] " + yellow + "Yellow = Not too difficult to get start with!")
	print("[*] " + green + "Green = Chill out time!")
	line_break()
	print("[*] " + red + "1: Binary Exploitation?")
	print("[*] " + yellow + "2: Practice Penetration Testing?")
	print("[*] " + yellow + "3: Learn some programming?")
	print("[*] " + green + "4: Watch check out my favourite Youtubers?")
	print("[*] " + green + "5: Try out a CTF?")
	print("[*] " + green + "6: Let me quiz you on your Linux Commands?")
	line_break()
	
	print("[*] Take your pick!")
	response = input("[*] Your choice: ")
	if response == "1":
		binary_exploitation()
	elif response == "2":
		pen_testing()
	elif response == "3":
		programming()
	elif response == "4":
		youtube()
	elif response == "5":
		ctf()
	elif response == "6":
		gametime()
	else:
		print(red + "[!] Sorry, you need to choose between 1-6! Closing program..")
		sys.exit()
			


def binary_exploitation():
	line_break()
	print("[*] Great! Binary Exploitation it is.")
	print(yellow + "[*] Loading list of resources...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	line_break()
	print("[*] A real beginner level piece of writing explaining the basics of Binary Exploitation!")
	print("[*]" + blue + " https://www.opensourceforu.com/2015/12/the-basics-of-binary-exploitation/")
	line_break()
	print("[*] Slightly more detailed article than the previous, but well worth a read.")
	print("[*]" + blue + " https://ctf101.org/binary-exploitation/return-oriented-programming/")
	line_break()
	print("[*] The Cyber Mentor - Youtube Series. Without a doubt the best way to do your first buffer overflow!")
	print("[*]" + blue + " https://www.youtube.com/watch?v=qSnPayW6F7U")
	line_break()
	print("[*] LiveOverflow - Bullshit free hacking videos.")
	print("[*]" + blue + " https://old.liveoverflow.com/binary_hacking")
	line_break()
	print("[*] Microcorruption - A place to practice your new found binary exploitation knowledge.")
	print("[*]" + blue + " https://microcorruption.com/login")
	line_break()
	print("[*] RopEmporium - Hands on Binary Exploitation challenges, definitely not beginner level but a great thing to get stuck into when you improve your skills.")
	print("[*]" + blue + " https://ropemporium.com/")
	line_break()


def pen_testing():
	line_break()
	print("[*] Wahey, let's get some practice in.")
	print(yellow + "[*] Loading list of resources...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	line_break()
	print("[*] Hack The Box - The ultimate practice environment. £10/mo for VIP which is the best tenner you will spend in my opinion, but they do have a free limited tier! You DO have to hack your way in to get an invite code. How f*cking cool!")
	print("[*]" + blue + " https://www.hackthebox.eu")
	line_break()
	print("[*] VulnHub - Less organized than Hack the Box, but you just download a vulnerable machine and load up your Kali alongside and try to break into it!")
	print("[*]" + blue + " https://www.vulnhub.com/")
	line_break()
	print("[*] The Cyber Mentor - 15 hours of a full ethical hacking course for FREE! Super beginner level AND you can follow along. Can't rave enough about this!")
	print("[*]" + blue + " https://www.youtube.com/watch?v=WnN6dbos5u8")
	line_break()
	print("[*] TryHackMe - Some more hands on labs that will go through specific exploits or vulnerabilities and not only show them, but also how they're working behind the scenes.")
	print("[*]" + blue + " https://tryhackme.com/")
	line_break()
	print("[*] OverTheWire - Connect via SSH and slowly escalate your privileges on each target system. Great progression on this site, well worth a look.")
	print("[*]" + blue + " https://overthewire.org/wargames/")
	line_break()
	print("[*] Virtual Hacking Labs - Costs about £100 for a months access, but solid content, and prepares you well for any certifications you want to take.")
	print("[*]" + blue + " https://www.virtualhackinglabs.com/")
	line_break()
	print("[*] Burpsuite Web Application Academy - Amazing free course that is consistently updated that guides you through how to exploit web applications effectively.")
	print("[*]" + blue + " https://portswigger.net/web-security")
	line_break()
	print("[*] PayloadsAllTheThings - A huge repository on all types of exploits, shells and techniques to help you penetrate a target. Great resource to bookmark.")
	print("[*]" + blue + " https://github.com/swisskyrepo/PayloadsAllTheThings")
	line_break()
	print("[*] Hacking Articles by Raj Chandel - This site literally has guides for anything I could possibly wish for. Walkthroughs, exploits, privilege escalation techniques.. It's fantastic for having your hand held when trying something new.")
	print("[*]" + blue + " https://www.hackingarticles.in/")
	line_break()
	print("[*] Hack.Me - Start a sandboxed environment in your browser and complete challenges to exploit common vulnerabilities, there's literally a challenge for everything. Take your pick.")
	print("[*]" + blue + " https://hack.me/")
	line_break()


def programming():
	line_break()
	print("[*] Eeeeesh, brave choice!")
	print(yellow + "[*] Loading list of resources...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	line_break()
	print("[*] Free Code Camp - If you're looking to get a basic knowledge in a language then this is probably the place to start. Really easy, fun to follow tasks that help you learn.")
	print("[*]" + blue + " https://www.freecodecamp.org/")
	line_break()
	print("[*] HackerRank - Python is one of the most useful languages there is. If you feel you're a decent level, try to take these challenges and test yourself.")
	print("[*]" + blue + " https://www.hackerrank.com/domains/python")
	line_break()
	print("[*] Violent Python - A book I've been reading all about crafting offensive programming tools. It's a bit outdated, but teaches some good concepts and it's important to know how to build a tool on the fly.")
	print("[*]" + blue + " (Free PDF) https://www.academia.edu/4903104/Violent_Python_-_A_Cookbook_for_Hackers_Forensic_Analysts_Penetration_Testers_and_Security_Engineers")
	line_break()
	print("[*] Code Academy - I'm not the biggest fan but it has a large choice of activities and the free version isn't the worst.")
	print("[*]" + blue + " https://www.codecademy.com/")
	line_break()
	print("[*] EDx - From Harvard/MIT so it must be good. I find the layout a bit dull, but it might suit a more visual learner. Some top quality content.")
	print("[*]" + blue + " https://www.edx.org/course/subject/computer-science")
	line_break()
	print("[*] Learn Python - Get started learning python. Online console, so you don't even need to download anything to begin.")
	print("[*]" + blue + " https://www.learnpython.org/")
	line_break()
	print("[*] In the words of Ahmed the great. W3Schools! Literally never had a problem that this site didn't at least help me with a little bit.")
	print("[*]" + blue + " https://www.w3schools.com/")
	line_break()


def youtube():
	line_break()
	print("[*] Ayeee, let's relax and grab a beer.")
	print(yellow + "[*] Loading list of resources...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	line_break()
	print("[*] The Cyber Mentor - Mentioning him again because I cannot get enough of his content. It's so beginner friendly, and the perfect way to get involved.")
	print("[*]" + blue + " https://www.youtube.com/channel/UC0ArlFuFYMpEewyRBzdLHiw")
	line_break()
	print("[*] ComputerPhile - This guy has a bit of everything on his channel. Nicely explained, not too complex, and quick videos.")
	print("[*]" + blue + " https://www.youtube.com/user/Computerphile")
	line_break()
	print("[*] IppSec - Writeups on hack the box boxes that you can follow along when you complete one to learn the process. He goes quite fast though, probably not beginner level.")
	print("[*]" + blue + " https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA")
	line_break()
	print("[*] Eddie Woo - Probably one of the easiest people to learn Cryptography from on the whole of Youtube. Really great at breaking things down.")
	print("[*]" + blue + " https://www.youtube.com/user/misterwootube")
	line_break()
	print("[*] STOK - Bug Bounty Hunter - If you're interested in learning how to make a living from hunting for bugs in web applications.")
	print("[*]" + blue + " https://www.youtube.com/channel/UCQN2DsjnYH60SFBIA6IkNwg")
	line_break()
	print("[*] VbScrub - Relatively unknown youtuber that I came across on hack the box forums, a Windows SysAdmin who really breaks down specific Windows attacks nicely. Great videos on Active Directory.")
	print("[*]" + blue + " https://www.youtube.com/channel/UCpoyhjwNIWZmsiKNKpsMAQQ")
	line_break()
	print("[*] John Hammond - General videos covering all sorts of topics, super interesting stuff and a really talented guy to learn from.")
	print("[*]" + blue + " https://www.youtube.com/user/RootOfTheNull")
	line_break()
	print("[*] /dev/null - CTF Writeups and all things computer science and security related.")
	print("[*]" + blue + " https://www.youtube.com/channel/UCGISJ8ZHkmIv1CaoHovK-Xw")
	line_break()
	print("[*] HackerSploit - Dedicated channel primarily revolving around penetration testing. Can pretty much always find something to watch.")
	print("[*]" + blue + " https://www.youtube.com/channel/UC0ZTPkdxlAKf-V33tqXwi3Q")
	line_break()
	print("[*] JackkTutorials - Seems to have gone a bit quiet, but his videos are really unique and enjoyable to wind down with after a long day.")
	print("[*]" + blue + " https://www.youtube.com/channel/UC64x_rKHxY113KMWmprLBPA")
	line_break()

	
	


def ctf():
	line_break()
	print("[*] So you're interested in playing in CTFs huh..")
	print(yellow + "[*] Loading list of resources...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	line_break()
	print("[*] CTF Time - This website is dedicated to all the CTFs that are happening over the world. Sign up, maybe make a team, find the next one to enter!")
	print("[*]" + blue + " https://ctftime.org/")
	line_break()
	print("[*] GoogleCTF - If you wanna just jump into one now, Google leave their beginner level CTF online all year. I still think it's pretty damn tough though.")
	print("[*]" + blue + " https://capturetheflag.withgoogle.com/#beginners/")
	line_break()
	print("[*] PicoCTF - Another CTF that gets left online all year round, and a really fun one. Set in the style of a game. You walk around and find challenges to do. All levels of ability.")
	print("[*]" + blue + " https://2019game.picoctf.com/")
	line_break()
	print("[*] Hacker101 CTF - Another starting point for newer CTF players. It's a nice introduction with a good scaling up when you start to get better at challenges.")
	print("[*]" + blue + " https://ctf.hacker101.com/howtoplay")
	line_break()
	print("[*] Essential CTF Tools - A really simple collection of the sort of tools you might find yourself using during a CTF.")
	print("[*]" + blue + " https://resources.infosecinstitute.com/tools-of-trade-and-resources-to-prepare-in-a-hacker-ctf-competition-or-challenge/#gref")
	line_break()
	print("[*] CTFLearn - Bit of a clunky looking site, but has a scoreboard for those of you who like to compete and have challenges for all levels of ability.")
	print("[*]" + blue + " https://ctflearn.com/")
	line_break()
	print("[*] Awesome CTF - A repository that holds way more information than you could ever dream of about completing CTF challenges or creating your own.")
	print("[*]" + blue + " https://github.com/apsdehal/awesome-ctf")
	line_break()
	print("[*] Pwnable - Another game style CTF that has differing levels of challenges. Start up, get hacking, register the flags.")
	print("[*]" + blue + " https://pwnable.kr/")
	line_break()



def gametime():
	line_break()
	print("[*] So how well do you know your way around the terminal?")
	print(yellow + "[*] Loading list of questions...")
	for i in range (1, 50):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	score = 0
	q1 = input("[*] 1) How do you list files in your directory: ")
	q1 = q1.lower()
	if q1 == "ls":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ls'!")
	line_break()

	q2 = input("[*] 2) How do you change directories: ")
	q2 = q2.lower()
	if q2 == "cd":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cd'!")
	line_break()

	q3 = input("[*] 3) What tool is primarily used for scanning a target during enumeration: ")
	q3 = q3.lower()
	if q3 == "nmap":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'nmap'!")
	line_break()

	q4 = input("[*] What file holds information about all the users on the device: ")
	q4 = q4.lower()
	if "passwd" in q4:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is '/etc/passwd'!")
	line_break()

	q5 = input("[*] How do you return the current user that you are logged in as: ")
	q5 = q5.lower()
	if q5 == "whoami" or q1 == "id":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'whoami' or 'id'!")
	line_break()

	q6 = input("[*] How do you print your current working directory: ")
	q6 = q6.lower()
	if q6 == "pwd":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'pwd'!")
	line_break()

	q7 = input("[*] If you want to perform a command as a super user, you prefix your command with what word: ")
	q7 = q7.lower()
	if q7 == "sudo":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'sudo'!")
	line_break()

	q8 = input("[*] The command used to switch users in the terminal is:  ")
	q8 = q8.lower()
	if q8 == "su":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'su'!")
	line_break()

	q9 = input("[*] How do you view currently running processes: ")
	q9 = q9.lower()
	if "ps" in q9:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ps aux'!")
	line_break()

	q10 = input("[*] What very well known command allows you to search for a word in terminal output: ")
	q10 = q10.lower()
	if "grep" in q10:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'grep'!")
	line_break()

	q11 = input("[*] If you want to make a new directory, you should type: ")
	q11 = q11.lower()
	if q11 == "mkdir":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'mkdir'!")
	line_break()

	q12 = input("[*] How would you remove a file in the terminal: ")
	q12 = q12.lower()
	if q12 == "rm":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'rm'!")
	line_break()

	q13 = input("[*] If a file has readable text, how do you print the contents to the terminal (Meow): ")
	q13 = q13.lower()
	if q13 == "cat":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cat'!")
	line_break()

	q14 = input("[*] I need to move a file, what do I type: ")
	q14 = q14.lower()
	if q14 == "mv":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'mv'!")
	line_break()

	q15 = input("[*] Finally, how do I copy a file: ")
	q15 = q15.lower()
	if q15 == "cp":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cp'!")
	line_break()
	
	if score == 15:
		print("[*]" + green + " Unbelievable! You scored: " + str(score) + ". Ride oooooooooooon! ;)")
		line_break()

	elif score > 10 and score < 15:
		print("[*]" + green + " Congratulations, you scored: " + str(score) + ". Cracking result! :)")
		line_break()

	elif score > 5 and score <= 10: 
		print("[*]" + yellow + " Not bad. Room for improvement. You scored " + str(score) + " :/")
		line_break()

	else:
		print("[*]" + red + " Going to need to work on that I think. You scored " + str(score) + " :(")
		line_break()

def close_program():
	while True:
		print("[*] Would you like to go back to the main menu?")
		quit = input("[*] Yes or No: ")
		quit = quit.lower()	
		if quit == "yes":
			welcome_menu()
	
		elif quit == "no":
			footer()
			sys.exit()
	
		else:
			print("[*]" + red + " That's not a yes or no...")
			line_break()
			


init(autoreset=True)

try:
	welcome_menu()
	close_program()

except KeyboardInterrupt:
    print(red + "\nYou pressed Ctrl + C to exit!")
    sys.exit()