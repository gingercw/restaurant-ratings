"""Restaurant rating lister."""
# create function
# open file
# remove spaces
# define the restaurant name and the ratings

def show_restaurant_ratings(scores_file):
  '''Stores restaurant and ratings in a dictionary.'''

  restaurant_ratings = open(scores_file)

  restaurant_ratings_dict = {}

  for line in restaurant_ratings:
    line = line.rstrip()
    words = line.split(":")
    restaurant = words[0]
    rating = words[1]

    restaurant_ratings_dict[restaurant] = rating

  for restaurant, rating in sorted(restaurant_ratings_dict.items()):
    print(f'{restaurant} is rated at {rating}.')    
  # return sorted(restaurant_ratings_dict.items())

# create new function
# ask for new restaurant and score
# add to dictionary
# write into the filegit



show_restaurant_ratings("scores.txt")
# put your code here
