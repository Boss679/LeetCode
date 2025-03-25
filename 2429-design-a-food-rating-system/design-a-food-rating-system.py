class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating = {} # food -> rating
        self.foodToCuisine = {} # food -> cuisine
        self.cuisineToSortedSet = defaultdict(SortedSet) # cuisine -> SortedSet[(rating, food)]

        for i in range(len(foods)):
            self.foodToRating[foods[i]] = ratings[i]
            self.foodToCuisine[foods[i]] = cuisines[i]
            self.cuisineToSortedSet[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        oldRating = self.foodToRating[food]

        self.cuisineToSortedSet[cuisine].remove((-oldRating, food))
        self.foodToRating[food] = newRating
        self.cuisineToSortedSet[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToSortedSet[cuisine][0][1]