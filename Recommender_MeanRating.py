import numpy
import pandas

class Popularity_Recommender():

	# Initialize all the variables
	def __init__(self):
		# Tha training data which is been provided.
		self.train_data = None

		# The user id of the product/item for which the recommendations is needed.
		self.user_id = None
        
		# The id of the product/item for which the recommendations is needed.
		self.item_id = None

		# The ratings of the items.
		self.ratings = None

		# The final result which is going to be returned as a dataframe. 
		self.popularity_recommendataions = None

	# Create the recommendations.
	def create(self,train_data,user_id, item_id,ratings):

		# The training data
		self.train_data = train_data

		# The id of the items for which the recommendations is needed.
		self.user_id = user_id        
        
		# The id of the items for which the recommendations is needed.
		self.item_id = item_id

		# The ratings of the Products etc.
		self.ratings = ratings


		# The items are grouped by item_id aggregated with the average of the ratings and the index is reseted.
		train_data_grouped = train_data.groupby([self.user_id, self.item_id]).agg({self.ratings: 'mean'}).reset_index()
		# The column named ratings is replaced by the name score.
		#train_data_grouped.rename(columns = {'ratings': 'score'}, inplace = True)


		# The training data is sorted according to the score in descending order and by item_id in ascending order.
		train_data_sort = train_data_grouped.sort_values([self.user_id, self.item_id], ascending = [0,1])
		# The new column named Rank is created by score sorted in ascending order.
		#train_data_sort['Rank'] = train_data_sort['score'].rank(ascending = 0, method = 'first')


		# The first 10 items are saved into the popularity_recommendataions and it is returned. 
		self.popularity_recommendataions = train_data_sort.head(10)


	# Method to item created recommendations
	def recommend(self, item_id):

		# Init the item_recommendataion var by popularity_recommendataions since the recommendations has been saved into this column.
		item_recommendataion = self.popularity_recommendataions

		# Get the user_id
		item_recommendataion['productId'] = item_id

		# Set the columns
		cols = item_recommendataion.columns.tolist()
		cols = cols[-1:] + cols[:-1]
		item_recommendataion = item_recommendataion[cols]

		return item_recommendataion