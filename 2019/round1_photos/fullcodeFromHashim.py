def makeSlides(photos) -> list:
    waiting = None # index of a vertical photo that's left hanging (single without a partner just like me ); )
    slides = []
    for i in range(nphotos):
        if photos[i][0] == 1:
            if waiting is not None: # joing with other vertical
                slides.append( Slide(photos[i], photos[waiting]) ) # append new slide
                waiting = None
            else:
                waiting = i
        else:
            slides.append(Slide(photos[i]))
    return slides

def getComponents(slide1, slide2):
    tags1 = slide1.tags
    tags2 = slide2.tags

    aAndB = len(tags1.intersection(tags2))
    aminusB = len(tags1.difference(tags2))
    bminusA = len(tags2.difference(tags1))

    return (aAndB, aminusB, bminusA)

def makeSlideShow(slides):
    """
    Returns an order of the slides in a list
    """
    from copy import deepcopy
    slidesCopy = deepcopy(slides)
    slideShowOrder = []
    while slidesCopy:
        nextSlide = findNextSlide(slidesCopy[len(slidesCopy) - 1], slidesCopy)
        slideShowOrder.append(nextSlide)
        slidesCopy.remove(slidesCopy[len(slidesCopy) - 2])
    
    return slideShowOrder

def printToFile(solution):
    file = open('sol2.txt', "w+")
    file.write(str(len(solution)) + "\n") # number of slides
    for slide in solution:
        file.write(str(slide.p1[3]))
        if slide.p2 != None:
            file.write(" " + str(slide.p2[3]) + "\n")
        else:
            file.write("\n")

    file.close()

def readFile(fname):
    def linemap(line, index):
        vals = line.strip().split(' ')
        return ((1 if vals[0] == 'V' else 0), int(vals[1]), set(vals[2:]), index)
    
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
        # either pass 1 horizontal or 2 vertical
        if p1[0] == 0: # if just 1 hor
           self.tags =  p1[2]
        if p1[0] == 1 and p2[0] == 1:
            self.tags = p1[2].union(p2[2])

def findNextSlide (nominatedSlide, slides) -> int:
    slides_length = len(slides)
    components = [] # corresponding to the index of the slide index, each entry will be an array of all possible
    # slidesInWindow = slides[nominatedSlide:nominatedSlide+windowSize]
    
    # we could remove min() and just get the components
    for i in range(slides_length):
        components.append( [getComponents(slides[i], nominatedSlide)] )
    
    interestFactors = list(map(min, components))
    bestInterestFactor = max(interestFactors)
    index = interestFactors.index(bestInterestFactor)
    return index
        #returns the index of the next slide to add
        #the big list of slides , the index of starting , and the window of slides that we need to still modify


nphotos, photos = readFile("b.txt")
slides = makeSlides(photos)
sol = makeSlideShow(slides)
solutions = list(map(lambda i: slides[i], sol))
printToFile(solutions)

