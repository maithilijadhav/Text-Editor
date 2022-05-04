# Code need for the doubly-linked-list implementation used in Assignment 3
# The code is identical to that in the course notes, with several methods added.
#
# NOTE: that the insert routine needs to be implemented.
# Refrences: Ghunaym Yaha and Manav Powar
import shlex
class DLinkedListNode:
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if (initPrevious != None):
            initPrevious.next = self
        if (initNext != None):
            initNext.previous = self

    def __str__(self):
        return "%s" % (self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous= newPrevious

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = "[ "
        current = self.head;
        while current != None:
            s += "%s " % (current)
            current = current.getNext()
        s += "]"
        return s

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def add(self, item):
        temp = DLinkedListNode(item, self.head, None)
        if self.head != None:
            self.head.setPrevious(temp)
        else:
            self.tail = temp
        self.head = temp
        self.size += 1

    def append(self, item):
        temp = DLinkedListNode(item, None, None)
        if (self.head == None):
            self.head = temp
        else:
            self.tail.setNext(temp)
            temp.setPrevious(self.tail)
        self.tail = temp
        self.size +=1

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.tail = previous
        self.size -= 1

    def removeitem(self, current):
        previous = current.getPrevious()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.tail=previous
        if previous:
            self.curr = previous.getNext()
        else:
            self.curr = None
        self.size -= 1

    def insert(self, current, item, where):
        # You write this code
        # NOTE: there is an extra parameter here
        # Where = 0 (before current)
        # Where = 1 (after current)
        index = 0
        if where == 0 and current.getPrevious() == None:  #right at the beginning when there list is empty
            after = current
            new = DLinkedListNode(item,current,None)
            after.setPrevious(new)
            new.setNext(after)
            self.head = new
            self.size += 1
            current = self.head
        if where == 0 and current.getPrevious() != None: # beginning but list is not empty
            new = DLinkedListNode(item,current,current.getPrevious())
            current = self.head
            current.setPrevious(new)
            self.size += 1 
            current = new
        if where == 1:
            if current.getPrevious() != None: # at the end
                previous = current
                new = DLinkedListNode(item, current.getNext(), current)
                previous.setNext(new)
                new.setPrevious(previous)
                self.size += 1 
                current = new
            else:  # in the middle
                previous = current
                new = DLinkedListNode(item, current.getNext(), current)
                previous.setNext(new)
                current.setPrevious(new)
                self.size += 1   
                current = new


class TextFile:
    def __init__(self,name):
        self.name = name
        self.linked = DLinkedList()
        self.current = self.linked.getHead()
        
    def load(self,name):
        '''
        To load in file and read to put in DLinkedList
        '''
        a = open(name , "r")
        for line in a:
            line = line.strip()
            self.linked.append(line)
        current = self.linked.getTail()
        self.current = current
    

    def write(self,name):
        '''
        To update and save the new edited or same list to different or same file
        '''
        current = self.linked.getHead()
        a = open(name,"w")
        while current != None:
            a.write(str(current))
            a.write("")
            current = current.getNext()
        a.close()

    def print(self,offset):
        '''
        To print items in list one by one 
        '''
        done = False
        original = self.current # needed to print last item 
        current = self.current
        a = self.linked.index(current.getData()) # the index of the current
        Max = self.linked.size
        offset_count = 0 # so it will not produce error when printing lines 
        num = int(a) + 1  # the item postion in the list
        neg_num = -1 # for backwards printing same as offset_count but for negative offsets        
        if int(offset) == 0:
            print(str(num) + ": "+ str(current))
        if int(offset) > 0:  # to print for positive offset
            print(str(num) + ": "+ str(current))
            num += 1
            current = current.getNext()
            if current != None:
                while int(offset) > offset_count and num <= Max:
                    num = str(num)
                    print(num + ": "+ str(current))
                    num = int(num)
                    num += 1
                    offset_count += 1
                    current = current.getNext()
            if current == None: # if at the end of list
                current = self.linked.getTail()
                self.current = current 
        if int(offset) < 0:  # to print for negative offset
            b = int(num)
            while current.getPrevious() != None and b != 1:
                current = current.getPrevious()
                b -= 1
            x = int(self.linked.index(current.getData())) + 1
            while x != num:
                num = num - 1
            if current != None and num <= Max:
                num = str(num)
                print(num + ": "+ str(current))
                num = int(num)
                num += 1 
                current = current.getNext()                
                while current.getNext() != None:
                    if int(offset) <= neg_num and not done:
                        num = str(num)
                        print(num + ": "+ str(current))
                        num = int(num)
                        num += 1
                        neg_num = neg_num - 1
                        current = current.getNext()
                    if current.getNext() == None and current == original:
                        num = str(num)
                        print(num + ": "+ str(current))
                        done = True

    def linenum(self,lineno):
        '''
        Setting the lineno as the current line
        '''
        
        word = False
        while lineno == "x" and not word:
            current = self.current
            print(current)
            self.current = current.getNext()
            self.print(0)
            word = True
        if lineno != "x":
            current = self.linked.head 
            num = 0            
            lineno = int(lineno)-1
            if lineno < 0:
                raise Exception("line number is before first line")
            if lineno > self.linked.size:
                raise Exception("Beyond file")
            if lineno == 0:
                self.current = current
                print(self.current)
            while num != int(lineno):  #gets the correct line number with num
                num += 1
                current = current.getNext()
                if num == lineno and current != None:
                    self.current = current
                    print(self.current)
       
               
                
    def add(self,where):
        '''
        adding a word or sentence by user either before or after the current
        '''
        current = self.current
        a = [ ] # add and insert
        num = 0 
        if where == 1: # after the current
            Add = input("")
            a.append(Add)            
            while Add != "":
                Add = input("")
                a.append(Add)
            a.pop()
            for element in a:
                print(self.current)
                self.linked.insert(current,element,1)
                while current.getData() != element:
                    current = current.getNext()
                self.current = current
        if where == 0:  # before the current
            insert = input("")     
            a.append(insert)
            while insert != "":
                insert = input("")
                a.append(insert)                 
            a.pop()
            for element in a:
                self.linked.insert(current,element,0) 
                while current.getData() != element:
                    current = current.getPrevious()
            self.current = current   
    
    def delete(self,offset):
        '''
        deleting current line and more if offset is a number
        '''
        current = self.current
        num = 0 
        if int(offset) == 0: # delete just the current line
            self.linked.removeitem(current)
            current = current.getNext()
            self.current = current
        if int(offset) > 0:  # delete after the current lines
            self.linked.removeitem(current)
            current = current.getNext()
            while int(offset) != num:
                self.linked.removeitem(current)
                current = current.getNext()
                self.current = current
                num += 1
        if int(offset) < 0:  # before current lines
            self.linked.removeitem(current)
            current = current.getPrevious()
            while int(offset) != num:
                self.linked.removeitem(current)
                current = current.getPrevious()
                self.current = current
                num += -1            
        
    def search(self,text,where):
        '''
        Searching for a word given by the user
        '''
        punctuation = ".,?><:)({}&!;-"
        for punc in punctuation:
            text = text.replace(punc,"")
        found = False
        current = self.current
        if where == "/":  # searching forward
            while found == False and current.getNext() != None:
                current = current.getNext()
                t = current.getData()
                c_word = 0  # used so for loop does not run on
                t = shlex.split(t)  # split the word individually
                l_word = len(t)
                for word in t:  
                    if l_word >= c_word:
                        c_word += 1
                        for punc in punctuation: 
                            word = word.replace(punc,"")  # replacing any punctuation so word matches
                        if word == text: # if matched
                            self.current = current
                            self.print(0)
                            found = True
            while current.getPrevious() != None and found == False:
                current = current.getPrevious()
                t = current.getData()
                t = shlex.split(t)
                for word in t:
                    for punc in punctuation: 
                        word = word.replace(punc,"")                        
                    if word == text:
                        self.current = current
                        self.print(0)
                        found = True                
        
        if where == "?":  # searching backwards
            num = 0  
            lines = self.linked.size
            if current.getPrevious() == None:
                current = self.linked.getTail()
                t = current.getData()
                t = shlex.split(t)
                num += 1
                for word in t: 
                    for punc in punctuation: 
                        word = word.replace(punc,"")
                    if word == text:
                        self.current = current
                        self.print(0)
                        found = True
                while found == False and num < lines:
                    current = current.getPrevious()
                    t = current.getData()
                    t = shlex.split(t)
                    num += 1
                    for word in t:
                        for punc in punctuation: 
                            word = word.replace(punc,"")
                        if word == text:
                            self.current = current
                            self.print(0)
                            found = True
            while current.getPrevious != None and found == False:
                current = current.getPrevious()
                t = current.getData()
                t = shlex.split(t)
                num += 1
                for word in t:
                    for punc in punctuation: 
                        word = word.replace(punc,"")
                    if word == text:
                        self.current = current
                        self.print(0)
                        found = True
                while current.getPrevious() == None and found == False: # if the current is at the beginning
                    current = self.linked.getTail()
                    t = current.getData()
                    t = shlex.split(t)
                    num += 1
                    for word in t:
                        for punc in punctuation: 
                            word = word.replace(punc,"")                        
                        if word == text:
                            self.current = current
                            self.print(0)
                            found = True
                    while found == False and num <= lines:
                        current = current.getPrevious()
                        t = current.getData()
                        t = shlex.split(t)
                        num += 1
                        for word in t:
                            for punc in punctuation: 
                                word = word.replace(punc,"")
                            if word == text:
                                self.current = current
                                self.print(0)
                                found == True                
    def replace(self,text1,text2):
        '''
        Relplacing the words
        '''
        current = self.current
        orginal = text1
        replacement = text2
        data = current.getData()
        data = data.replace(orginal,replacement)
        current.setData(data)
        self.print(0)
        
    
    def sort(self):
        ''' 
        Did not complete
        '''
        pass 
                
            
    
    def getName(self):
        '''
        getting file name
        '''
        return self.name 
    
    def setName(self,name):
        '''
        setting file name
        '''
        self.name = name 
        
    def getCurr(self):
        '''
        getting the current
        '''
        self.current = current
        return self.current
    
    def setCurr(self,current):
        '''
        setting the current
        '''
        current = self.current
        
    
    def getLine(self):
        '''
        getting a current
        '''
        self.print(0)
        
    def setLine(self,line):
        '''
        set the line number of the current line
        '''
        self.current = line
        
        

def main():
    
    commands = ["p","r","/","?","a","i","l","","w"]
    linked = DLinkedList()
    text = TextFile(linked)

    print("Welcome to ed379")
    quit = False
    while not quit:      
        user = input("> ")
        user = user.split() 
        if user[0] == "l": 
            text.load(user[1])
        if len(user) == 0:
            text.linenum("x")
        if len(user) > 0:
            if user[0] == "p":
                if len(user) > 1:
                    text.print(user[1])
                else:
                    text.print(0)
            if user[0] == "a" or "i":
                if user[0] == "a":
                    text.add(1)
                if user[0] == "i":
                    text.add(0)
            if user[0] == "d":
                if len(user) > 1:
                    text.delete(user[1])
                else:
                    text.delete(user[0])
            if user[0] == "/" or "?":
                if user[0] == "/":
                    text.search(user[1],"/")
                if user[0] == "?":
                    text.search(user[1],"?")
            if user[0] == "r":
                if len(user) > 2:
                    text.replace(user[1],user[2])
                if len(user) == 2:
                    text.replace(user[1],"")
            if user[0] == "w":
                if len(user) > 1:
                    text.write(user[1])
                else:
                    text.write("A3-sample.txt")
            if user[0] not in commands:
                text.linenum(user[0])
            if user[0] == "q":
                print("Good-bye")
                quit = True     
        
main()