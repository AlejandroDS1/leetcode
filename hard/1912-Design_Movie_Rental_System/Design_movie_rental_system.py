from collections import defaultdict
from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]], v :bool = False):
        self.v = v
        self.nshops: int = n

        self.movies_shops_relation = defaultdict(list)
        self.movies_dict = defaultdict(list) 
        
        self.rented = set()

        for shop, movie, price in entries:
            l = [price, shop, movie]

            # Add new movie to the heap, the are all unrented at first.
            # Heap node structure is (price, shop)
            self.movies_shops_relation[(shop, movie)] = [price, False]
            
            self.movies_dict[movie].append(l)


        for movie in self.movies_dict.keys():
            self.movies_dict[movie].sort(key= lambda x: (x[0], x[1], x[2]))

        if self.v:
            print("Init method")
            print(f"top_five: {self.top_five}")
            print("\n"*3)
    
    def search(self, movie: int) -> List[int]:
       
        '''
            Finds the cheapest 5 shops that have an unrented copy of a given movie
        '''

        if movie not in self.movies_dict: return []
       
        cheapest_movies = []
        for m in self.movies_dict[movie]:
            if len(cheapest_movies) == 5: return cheapest_movies
            if not self.movies_shops_relation.get((m[1], movie))[1]:
                cheapest_movies.append(m[1])

        if self.v:
            print(f"Search method: movie = {movie}")
            print(f"Cheapest movies: {cheapest_movies}")
            print(f"movies dict: {self.movies_dict[movie]}")
        return cheapest_movies

    def rent(self, shop: int, movie: int) -> None:
       

        self.movies_shops_relation[(shop, movie)][1] = True

        self.rented.add((self.movies_shops_relation[(shop, movie)][0], shop, movie))

        if self.v:
            print(f"Rent method -> [shop = {shop}, movie = {movie}]")
            print("\n"*3)

    def drop(self, shop: int, movie: int) -> None:
        
        self.movies_shops_relation[(shop, movie)][1] = False
        
        self.rented.remove((self.movies_shops_relation[(shop, movie)][0], shop, movie))

        if self.v:
            print(f"Drop method [ shop: {shop}, movie: {movie}]")
            print("\n"*3)

    def report(self) -> List[List[int]]:
        '''
        Returns the cheapest 5 rented movies.
        res[j] = [shopj, moviej]
        '''
        top_five = sorted(self.rented, key = lambda x: (x[0], x[1], x[2]))
        
        return [[shop, movie] for _, shop, movie in top_five[:5]]