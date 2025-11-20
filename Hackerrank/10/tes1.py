def makePN(A, PN):
    return [A, PN]

def Akar(T):
    return T[0]

def Anak(T):
    return T[1]

def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(Anak(PN)) == True)

# Function to check if an element X is present in the children of a given node
def FindParent(X, PN):
    if IsTreeNEmpty(PN):
        return None  # No parent found if the tree is empty
    for subtree in Anak(PN):
        if X == Akar(subtree):
            return PN  # Found the parent (the node containing X)
    # Recurse into the children of the root node
    for subtree in Anak(PN):
        parent = FindParent(X, subtree)
        if parent is not None:
            return parent
    return None

# Function to find siblings of a node X in the tree PN
def Saudara(X, PN):
    parent = FindParent(X, PN)  # Find the parent of X
    if parent is None:
        return []  # No siblings if no parent found

    # Get the children of the parent and return those except X
    siblings = []
    for child in Anak(parent):
        if Akar(child) != X:  # Exclude the target node (X)
            siblings.append(Akar(child))
    return siblings

# Example Usage:
tree = makePN("Ridho", [
    makePN("Silvani", [makePN("Nuha", []), makePN("Syahrafi", [])]),
    makePN("Rendi", [makePN("Fikhrul", [])]),
    makePN("Ruth", [makePN("Aji", [])]),
    makePN("Eko", [makePN("Raffi", [])])
])

# Find siblings of "Nuha"
siblings_of_nuha = Saudara("Ridho", tree)
print(siblings_of_nuha)  # Expected Output: ['Syahrafi']
print(FindParent("Syahrafi", tree))