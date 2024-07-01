from add import add

def test_add():
   
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"
    
    
    result = add(-1, -1)
    assert result == -2, f"Expected -2 but got {result}"
    
    
    result = add(2, -3)
    assert result == -1, f"Expected -1 but got {result}"
    
   
    result = add(2.5, 3.5)
    assert result == 6.0, f"Expected 6.0 but got {result}"
    
    
    result = add(0, 0)
    assert result == 0, f"Expected 0 but got {result}"

if __name__ == "__main__":
    test_add()
    print("All test cases have passed!")
