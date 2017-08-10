# PDB Tutorial
# 	- This tutorial is intended to teach the basics of pdb

# * What is the purpose of a debugger?
# 	1. Allows you to explore the state of a running program
# 	2. Test implementation code before applying it
# 	3. Follow a programs execution logic

# 	- Breakpoints can be used to apply the three points above
# 	- Is a better alternative than just printing things

# * PDB 101: Intro to pdb
# 	- import the mdoule
# 	- call a method to insert a breakpoint

# 	- This drops you into the middle of a running program

# * The 5 pdb commands that will leave you "speechless"
# 	1. l(ist) - Display 11 lines arount the current line or continue
# 				the previous listing
# 	2. s(tep) - Execute the current line, stopping at the first occasion
# 	3. n(ext) - Continue execution until the next line in the function
# 	4. b(reak) - Set a breakpoint (depending on the arguments provided)
# 	5. r(eturn) - Continue execution until the function returns

# 	- It's best practice to avoid using the shorthand letters in your code

# ** 1. l(ist) a.k.a I'm too laxy to open the file containing the source code
# 	 list [first, [,last]]
# 		- List 11 lines around the current line
# 		- List 11 lines around a specified line
# 		- List the given range

# ** 2. s(tep) a.ka let's see what this method does
# 	 s(tep)
# 	 	- Stop at first occasion

# ** 3. n(ext) a.k.a I hope this line doesn't throw an exception
# 	 n(ext)
# 	 	- Continue until the next line in the funtion (or return statement)

# ** 4. b(reak) a.k.a I don't want to type n anymore
# 	 b(reak)
# 	 	- List all breaks
# 	 	- Set a break at given line
# 	 	- Set a break at the first line of a given function
# 	 	- Give an expression that must evaluat to true before breaking

# You can list the breakpiunts with *b*
# You can delete them with *b* break number

# ** 5. r(eturn) a.k.a I want to get out of this function
# 	 r(eturn)
# 	 	- Continue execution until the current function returns
# 	 	- Only follows the path of execution for a single return

# ** Advanced pdb topics
# 	! bang -> lets pdb know the next statement is a python command
# 	post.mortem() -> Useful in except block
# 	pm() -> More powerful??