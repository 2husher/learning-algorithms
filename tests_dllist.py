from dllists import *

def test_push():
    colors = DoubleLinkedList()
    assert colors.count() == 0
    colors.push("Yellow")
    assert colors.count() == 1
    colors.push("Blue")
    assert colors.count() == 2

def test_pop():
    colors = DoubleLinkedList()
    colors.push("red")
    colors.push("green")
    assert colors.pop() == "green"
    assert colors.pop() == "red"
    assert colors.pop() == None

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("black")
    colors.push("white")
    colors.push("gray")
    assert colors.unshift() == "black"
    assert colors.unshift() == "white"
    assert colors.unshift() == "gray"
    assert colors.unshift() == None

def test_shift():
    colors = DoubleLinkedList()

    colors.shift("Yellow")
    assert colors.count() == 1
    colors.shift("Blue")
    assert colors.count() == 2
    assert colors.pop() == "Yellow"
    assert colors.count() == 1
    assert colors.pop() == "Blue"
    assert colors.count() == 0

def test_detach_node():
    colors = DoubleLinkedList()
    colors.push("black")
    colors.push("white")
    colors.push("gray")
    colors.push("yellow")
    
    node = colors.begin.next
    colors.detach_node(node)
    assert colors.count() == 3

    node = colors.begin
    colors.detach_node(node)
    assert colors.first() == "gray"
    
    node = colors.end
    colors.detach_node(node)
    assert colors.last() == "gray"

    node = colors.begin
    colors.detach_node(node)
    assert colors.count() == 0

def test_remove():
    colors = DoubleLinkedList()
    colors.push("black")
    colors.push("white")
    colors.push("gray")
    colors.push("yellow")
    colors.dump("complete list")
    assert colors.remove("black") == 0
    colors.dump("before yellow")
    assert colors.remove("yellow") == 2
    colors.dump("after yellow")
    assert colors.remove("gray") == 1
    assert colors.remove("white") == 0
    assert colors.remove("red") == None

def test_first():
    colors = DoubleLinkedList()
    assert colors.first() == None
    colors.push("black")
    assert colors.first() == "black"
    colors.push("white")
    assert colors.first() == "black"
    colors.shift("gray")
    assert colors.first() == "gray"

def test_last():
    colors = DoubleLinkedList()
    assert colors.last() == None
    colors.push("black")
    assert colors.last() == "black"
    colors.push("white")
    assert colors.last() == "white"
    colors.shift("gray")
    assert colors.last() == "white" 

def test_get():
    colors = DoubleLinkedList()
    assert colors.get(0) == None
    colors.push("yellow")
    assert colors.get(0) == "yellow"
    colors.push("green")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "green"
    colors.push("red")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "green"
    assert colors.get(2) == "red"
    assert colors.pop() == "red"
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "yellow"
    colors.pop()
    assert colors.get(0) == None

test_push()
test_pop()
test_unshift()
test_shift()
test_detach_node()
test_remove()
test_first()
test_last()
test_get()
