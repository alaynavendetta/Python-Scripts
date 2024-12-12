DDHunter.py was created by Alayna N. Ferdarko, https://github.com/alaynavendetta, on 11 December, 2024.

This script parses a .dd file for known headers in order to recover files manually and save them
to a new folder in the same directory as DDHunter. This is useful for filecarving images from hard drives
where it may be difficult for programs such as FTKImager or Autopsy/TSK to recover individual files from
a damaged drive. This program parses through the hex characters in the .dd image to recover files.

DDHunter will only take a .dd file in it's current setup. I made this decision as .E01 files have compression
built in, and can cause data in fileslack to be truncated. This makes it more difficult to recover files from
letting the script parse the hex characters, and recover the files. This works as a sort of last ditch effort
of sorts to recover files, as the size of the .dd file being parsed impacts how long it will take the script to
run. However, this automation makes it much easier than trying to manually parse the file yourself in your chosen
forensic program (HxD, FTK/FTKImager, Autopsy, Oxygen, Axiom, EnCase, X-Ways...the list goes on and on!)

The file headers I have in this program were gained from my time as a student at Bloomsburg University from 
Dr. Scott Inch in Files 1 and 2, and the python programming from Dr. Phil Polstra. Without them, I wouldn't
have gained the skills I needed to write this program. 