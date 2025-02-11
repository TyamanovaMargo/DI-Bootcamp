import math


class Pagination:
    def __init__(self, items = [],pageSize = 10):
        self.items = items # It will contain a list of contents to paginate.
        self.pageSize = pageSize #The amount of items to show in each page.
        self.now_page = 1 #current page
        self.all_pages = math.ceil(len(items)/ pageSize) # to round up to the next whole number

    def getVisibleItems(self):   # returns a list of items visible depending on the pageSize
        # for i in range(self.pageSize ):
        #     # print(f"{self.pageSize}---- self.pageSize, {i}----- i")
        #     if i <= len(self.items):
        #         # print(f"{i}-----i second time in if")
        #         print(self.items[i])
        start_point = (self.now_page - 1) *self.pageSize
        final_point = start_point +self.pageSize
        return print(self.items[start_point:final_point]) # to do slice because its list

    def prevPage(self):
        if self.now_page > 1:
            self.now_page  -= 1
        return self

    
    def nextPage(self):
        if self.now_page < self.all_pages:
            print(self.all_pages)  
            self.now_page += 1 
        # print(f'Current Page: {self.now_page}')  

    def firstPage(self):
        self.now_page  = 1  
        return self
    
    def lastPage(self):
        self.now_page  = self.all_pages
        return self
    
    def goToPage(self,pageNum):
        self.now_page  = max(1, min(pageNum, self.all_pages))
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.getVisibleItems()


p.nextPage()
p.getVisibleItems()


p.lastPage()

p.getVisibleItems()