class student:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
number_of_question = 4
g = correct = 0

sw1=student('1. Name the first planet.\n a) mercury\n b)marse\n c)jupiter\n d)earth\n','a')
sw2=student('2. Name the biggest planet.\n a) mercury\n b)marse\n c)jupiter\n d)earth\n','c')
sw3=student('3. Name the red planet.\n a) mercury\n b)marse\n c)jupiter\n d)earth\n','b')
sw4=student('4. Name our home planet.\n a) mercury\n b)marse\n c)jupiter\n d)earth\n','d')
listi = [sw1,sw2,sw3,sw4]

for i in range(len(listi)):
    g = input(listi[i].question)
    if g == listi[i].answer:
        correct += 1
if correct>2:
    print(f'Congrads! You have got {correct} questions right.')
elif correct <= 2 and correct>0:
    print(f'You have got only {correct} right!')
else:
    print(f'Sorry, You have got none right!')
