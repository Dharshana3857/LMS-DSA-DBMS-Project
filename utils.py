class AVLNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
        self.height = 1

def insert(root, book):
    if not root:
        return AVLNode(book)
    if book.isbn < root.book.isbn:
        root.left = insert(root.left, book)
    else:
        root.right = insert(root.right, book)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Rotations
    if balance > 1 and book.isbn < root.left.book.isbn:
        return right_rotate(root)
    if balance < -1 and book.isbn > root.right.book.isbn:
        return left_rotate(root)
    if balance > 1 and book.isbn > root.left.book.isbn:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and book.isbn < root.right.book.isbn:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def search(root, isbn):
    if not root or root.book.isbn == isbn:
        return root
    if isbn < root.book.isbn:
        return search(root.left, isbn)
    return search(root.right, isbn)
