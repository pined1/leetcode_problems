class ListNode:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    
        
class BrowserHistory:

    def __init__(self, homepage: str):
        # saying my current pointer is at this initiated ListNode passing in
        # the current homepage
        if homepage:
            self.cur = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        # Given the new URl to visit 
        # current pointer will be pointing to this new node
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next
        

    def back(self, steps: int) -> str:
        # Agreed that dont want to go out of bounds
        # so.. check if the self.cur.prev is not out of bounds first
        # and the steps taken are still valid
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
            
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        # same thing as moving backwards
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
            
        return self.cur.val
        

if __name__ == "__main__":
    obj = BrowserHistory(homepage="google.com")
    obj.visit(url="photos.com")
    
    param_2 = obj.back(steps=1)
    print(f"Backed up to: {param_2}") # Should be google.com
    
    param_3 = obj.forward(steps=1)
    print(f"Forward to: {param_3}")   # Should be photos.com
    
    
# Summary: Walk through the problem carefully understanding what it means for each function and draw it out to see if you notice
# or can catch any edge cases. In this case we are using a doubly linked list so what does that look like when you visit
# you wil have to create a new listnode pointing to that visit page now. Also for forward draw out the nodes and test out
# what happens when you jump out x steps how we are handling that case. same for forward. What the time complexity will be
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)