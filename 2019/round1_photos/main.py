
import numpy as np


# photo: ('V', 2, set(['selfie', 'smile']), index)

def readFile(fname):
    def linemap(line, index):
        vals = line.strip().split(' ')
        return (vals[0], int(vals[1]), set(vals[2:]), index)
    
    with open(fname) as f:
        lines = f.readlines()
        nphotos = int(lines[0].strip())
        linesData = [linemap(lines[i], i) for i in range(1, len(lines), 1) ]
        return nphotos, linesData

class Slide():
    def __init__(self, p1, p2=None):
        """
        parameters
        ----
        p1: photo1
        p2: optional: photo2
        """
        self.p1 = p1
        self.p2 = p2
        self.tags = []
        self.singleHorizontalPhoto = (p1[0] == 'H')

        # either pass 1 horizontal or 2 vertical
        if self.singleHorizontalPhoto: # if just 1 hor
            self.tags =  p1[2]
        elif p1[0] == 'V' and p2[0] == 'V': # if both vert
            self.tags = p1[2].union(p2[2])
        else:
            raise Exception("Slides(): bad input photos, can't create slide from a single vertical photo")
    
    def __repr__(self): # how it's returned in the console
        return self.__str__()
    
    def __str__(self): # how it looks like when printed
        return "Slide ( p1: {}{})".format(self.p1, ', p2: {}. Both [vertical]'.format(self.p2) if not self.singleHorizontalPhoto else " [horizontal]")

class Photo():
    def __init__(self, photo: tuple):
        # ('V', 2, set(['selfie', 'smile']), index)
        self.orientation = photo[0]
        self.isVertical = self.orientation == 'V'
        self.isHorizontal = not self.isVertical

        self.tagsCount = photo[1]
        self.tags = photo[2]
        self.index = photo[3]
        pass

def makeSlides(photos) -> list:
    # index of a vertical photo that's left hanging (single without a partner just like me ); )
    waitingVer = -1
    
    # making a list and filling it with slides
    slides = []
    
    # for each photo, create a slide out of it (if it's horizontal), or collect 2 verticals
    for i in range(nphotos):
        if photos[i][0] == 'V': # if vertical
            if waitingVer is not -1: # joing with other vertical
                slides.append( Slide(photos[i], photos[waitingVer]) ) # append new slide
                waitingVer = -1
            else:
                waitingVer = i
        else:
            slides.append(Slide(photos[i]))
    return slides


nphotos, photos = readFile("a.txt")

slides = makeSlides(photos)
import numpy as np
print("slides:", np.array( slides ))


