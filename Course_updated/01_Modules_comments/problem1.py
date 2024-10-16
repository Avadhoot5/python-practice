import os
import pyttsx3

# 1. print a poem

poem = '''
टूटे हुए तारों से फूटे बासंती स्वर
पत्थर की छाती में उग आया नव अंकुर
झरे सब पीले पात
कोयल की कुहुक रात
प्राची में अरुणिमा की रेख देख पाता हूं
गीत नया गाता हूं।
टूटे हुए सपने की सुने कौन सिसकी
अंतर को चीर
व्यथा पलकों पर ठिठकी
हार नहीं मानूंगा, रार नहीं ठानूंगा
काल के कपाल पर लिखता मिटाता हूं
गीत नया गाता हूं।
'''

# print(poem)

# 2. REPL, print table of 5

def table(n):
    for i in range(1, 11):
        print(i * n)

# table(5)

# 3. external module
# python3 -m pygame.examples.aliens

engine = pyttsx3.init()
engine.say('Hello this is a audio sample')
engine.runAndWait()


# 4 print the contents of a directory using os module

# gets the current working directory path
cwd = os.getcwd()
print(cwd)

# prints the files in specific directory
print(os.listdir(cwd))

