# Helper function to check if the tree is empty
def IsTreeEmpty(P):
    return P == []

# Helper function to create a new tree node
def MakePB(value, left, right):
    return [value, left, right]

# Function to get the root value of a tree
def Akar(P):
    return P[0] if not IsTreeEmpty(P) else None

# Function to get the left subtree
def Left(P):
    return P[1] if not IsTreeEmpty(P) else []

# Function to get the right subtree
def Right(P):
    return P[2] if not IsTreeEmpty(P) else []

# DEFINISI DAN SPESIFIKASI
# AddX: Tree, integer --> BST
# AddX Menambahkan elemen x ke dalam Tree
def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    else:
        if X < Akar(P):
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        else:
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))

# Function to find the minimum element in a subtree
def FindAkar(P):
    while not IsTreeEmpty(Left(P)):
        P = Left(P)
    return Akar(P)

# Function to delete an element X from the BST
def DelX(P, X):
    if IsTreeEmpty(P):  # Tree is empty
        return []

    root_value = Akar(P)
    
    if X < root_value:
        # Delete from the left subtree
        return MakePB(root_value, DelX(Left(P), X), Right(P))
    elif X > root_value:
        # Delete from the right subtree
        return MakePB(root_value, Left(P), DelX(Right(P), X))
    else:
        # We found the element to delete
        # Case 1: No children (leaf node)
        if IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
            return []
        # Case 2: One child
        elif IsTreeEmpty(Left(P)):
            return Right(P)
        elif IsTreeEmpty(Right(P)):
            return Left(P)
        # Case 3: Two children
        else:
            # Find the smallest value in the right subtree (in-order successor)
            min_value = FindAkar(Right(P))
            # Replace root with the in-order successor
            return MakePB(min_value, Left(P), DelX(Right(P), min_value))

# Testing the function with the provided sample calls
print(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 100))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 75))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 35))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 50))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 60))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 200))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 60))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 100))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 75))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 35))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 50))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 200), 25), 40), 50))
