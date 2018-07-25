#HW # 5 

import sys

""" This functions build the title-actors dictionary. 
The keys are movie titles, and the values are the cast
lists of each movie."""
def make_title_dict():
    titleActorDict = {} 
    infile = open('imdb.txt','r') # open file
    masterlist=[nextline.strip() for nextline in infile]
    infile.close()
    j=0
    while j < len(masterlist):
        title = masterlist[j]
        actor = masterlist[j+1]
        if title in titleActorDict:
            titleActorDict[title].append(actor)
        else:
            titleActorDict[title]=[actor]
        j+=2
    return titleActorDict

""" This function builds the actor-titles dictionary. The keys are actors,
and the values are lists of movies in which the actors appeared. """
def make_actor_dict():
    actorTitleDict = {}
    infile = open('imdb.txt','r') # open file
    masterlist=[nextline.strip() for nextline in infile]
    infile.close()
    i=0
    while i < len(masterlist):
        title = masterlist[i]
        actor = masterlist[i+1]
        if actor in actorTitleDict:
            actorTitleDict[actor].append(title)
        else:
            actorTitleDict[actor]=[title]
        i+=2
    return actorTitleDict

""" This function builds the collaboration graph. The keys are
actors, and values are lists of actors who worked in a film
with the key actor."""
def make_neighbor_graph(titleActorDict , actorTitleDict):
    actorCollDict = {}
    for A in actorTitleDict.keys():
        for film in actorTitleDict[A]:
            for B in titleActorDict[film]:
                if B != A:
                    if B in actorCollDict:
                        actorCollDict[B].append(A)
                    else:
                        actorCollDict[B] = [A]
    return actorCollDict

""" This function builds the colloboration tree for a given actor as root."""
def make_bfs_tree(actorCollDict , root):
    tree = {}
    current = [root]
    while len(current) != 0:
        temp = []
        for actor in current:
            for coll in actorCollDict[actor]:
                if coll not in tree:
                    tree[coll] = actor
                    temp.append(coll)
        current = temp
    return tree
  
""" This function prints the colloboration path between two actors."""
def print_colloboration_tree(actor1, actor2):
    titleActorDict = {}
    actorTitleDict = {} 
    actorCollDict = {}

    infile = open('imdb.txt','r')
    list0=[line.strip() for line in infile]
    infile.close()

    i=0
    while i < len(list0):
        title = list0[i]
        actor = list0[i+1]
        if title in titleActorDict:
            titleActorDict[title].append(actor)
        elif title not in titleActorDict:
            titleActorDict[title]=[actor]
        if actor in actorTitleDict:
            actorTitleDict[actor].append(title)
        elif actor not in actorTitleDict:
            actorTitleDict[actor]=[title]
        i+=2
    
    for A in actorTitleDict.keys():
        for film in actorTitleDict[A]:
            for B in titleActorDict[film]:
                if B != A:
                    temp = [A]
                    temp.append(film)
                    if B in actorCollDict:
                        actorCollDict[B].append(temp)
                    else:
                        actorCollDict[B] = [temp]
    
    tree = {}
    current = [actor2]
    while actor1 not in tree:
        new = []
        for actor in current:
            for Coll in actorCollDict[actor]:
                coll = Coll[0]
                if coll not in tree:
                    tree[coll] = [actor,Coll[1]]
                    new.append(coll)
        current = new
    
    person = actor1
    print "\t", actor1
    while person != actor2:
        print "\t", "\t", tree[person][1], "\n", "\t", tree[person][0]
        person = tree[person][0]

    
# This function solves the assignment problems, using the
# dictionaries constructed above.

def assignment():
    print '(Part 1) Using the titleActor dictionary to answer questions.'
    titleActorDict = make_title_dict()
    
    print '\t(A)What is the length of the longest cast list?'  
    maxLen = max([len(titleActorDict[film]) for film in titleActorDict.keys()])
    print "\t", maxLen

    print '\t(B)What film or films have the largest cast list?'
    listmax = [film for film in titleActorDict.keys() if len(titleActorDict[film])==maxLen]
    print "\t", listmax
    
    print '\t(C)How many films are in the database?'
    print "\t", len(titleActorDict.keys())

    print '\t(D)What is the length of the shortest cast list?'
    minLen = min([len(titleActorDict[film]) for film in titleActorDict.keys()])
    print "\t", minLen

    print '\t(E)What film or films have the shortest cast list?'
    listmin = [film for film in titleActorDict.keys() if len(titleActorDict[film])==minLen]
    print "\t", listmin

    print '\t(F)List all the movies in which Owen Wilson appears.'
    movies = [film for film in titleActorDict.keys() if "Owen Wilson" in titleActorDict[film]]
    print "\t", movies

    print '\t(G)List all the actors who appeared in both "Silver Linings Playbook" and "American Hustle" '
    SLPAH = [actor for actor in titleActorDict["Silver Linings Playbook"] if actor in titleActorDict["American Hustle"]]
    print "\t", SLPAH

    #*********************************
    #************ PART 2 *************
    #*********************************
   
    actorTitleDict = make_actor_dict( )
    print '*'*10
    print '(Part 2) User the actor dictionary to answer questions.'
    
    print '\t(A) List (again) all the movies in which Owen Wilson appears.'
    print "\t", actorTitleDict["Owen Wilson"]

    print '\t(B) How many actors are in the database?'
    print "\t", len(actorTitleDict.keys())

    print '\t(C) Which actor (or actors) has been in the largest number of films in the database?'
    maxlen = max(len(actorTitleDict[actor]) for actor in actorTitleDict.keys())
    listmax0 = [film for film in actorTitleDict.keys() if len(actorTitleDict[film]) == maxlen]
    print "\t", listmax0

    print '\t(D) What are all the films in which both Clint Eastwood and Morgan Freeman appeared?'
    CEMF = [film for film in actorTitleDict["Clint Eastwood"] if film in actorTitleDict["Morgan Freeman"]]
    print "\t", CEMF

    #*********************************
    #************ PART 3 *************
    #*********************************

    actorCollDict = make_neighbor_graph(titleActorDict , actorTitleDict)
    print '*'*10
    print '(Part 3) Answer questions using the collaboration graph.'
    
    print '\t(A) Who is the actor with the most collaborators?'
    maxColl = max(len(actorCollDict[actor]) for actor in actorCollDict.keys())
    collmax = [actor for actor in actorCollDict.keys() if len(actorCollDict[actor]) == maxColl]
    print "\t", collmax, maxColl
    
    print '\t(B) Is Kate Winslet a collaborator of Cate Blanchett?'
    print "\t", 'Kate Winslet' in actorCollDict["Cate Blanchett"]
    
    print '\t(C) Is Kate Winslet a collaborator of a collaborator of Cate Blanchett?'
    checker = False
    for coll in actorCollDict["Cate Blanchett"]:
        if "Kate Winslet" in actorCollDict[coll]:
            checker = True
    print "\t", checker

    #*********************************
    #************ PART 4 *************
    #*********************************
    root = 'Kate Winslet'
    tree = make_bfs_tree(actorCollDict , root)
    print '*'*10
    print '(Part 4) Answer questions  using tree for given root actor'

    print '\t(A) Print path from one actor to root actor of the created tree'
    
    person = "Tom Hanks"
    while person != root:
        print "\t", person
        person = tree[person]
    print "\t", root
    
    print '\t(B) What is the length of the longest path in the tree?'
    
    length = 0
    person = ""
    for actor in tree:
        actor0 = actor
        temp = []
        while actor != root:
            temp.append(actor)
            actor = tree[actor]
        
        if len(temp) > length:
            length = len(temp)
            person = actor0
    
    print "\t", length+1

    print '\t(C) Find an instance of a longest path in the tree.'

    while person != root:
        print "\t", person
        person = tree[person]
    print "\t", root
    
    #*********************************
    #************ PART 5 *************
    #*********************************
    
    print '*'*10
    print '(Part 5) Colloboation path including movie titles '
    print '\t(A) Print path between two actors'
    actor1 = 'Meryl Streep'
    actor2 = 'Don Cheadle'
    print_colloboration_tree(actor1, actor2)

try:
    assignment()
except IOError:
    print "Error"
