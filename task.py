import pandas as pd
import matplotlib.pyplot as plt

# For Testing graphing UI :
# df = pd.DataFrame({"col1":[1,2,3,4,5], "col2":[2,3,4,5,6]})
# df1 = pd.DataFrame({"col1":[1,2,3,4,5], "col2":[2,3,4,5,6]})

# To extract csv file
df = pd.read_csv("pet_supplies_2212.csv")




# >> Task1 : Data Validation
# Getting the name of all columns
hd = df.columns
print('\n------// Checking Headers')
print(hd)

# Extract the value in each column
lst_df_dt = [df[['product_id']], 
             df[['category']], 
             df[['animal']], 
             df[['size']], 
             df[['price']], 
             df[['sales']], 
             df[['rating']], 
             df[['repeat_purchase']]]


# Check the datatype of each coloumn
# Check the number of "null" values

for dataframe in lst_df_dt:
    print('------// Checking Columns : {}'.format(dataframe.columns[0]))
    print('------// Checking Datatypes')
    print(dataframe.dtypes)
    print('\n------// Checking Null Values')
    print(dataframe.isna().sum())
    
    #  For data range check
    dataframe_unique = dataframe.drop_duplicates()
    print('\n------// Checking Data Range')
    print(dataframe_unique)
    print('\n')



# Data correction
# 1. In category column, replace "-" with "Unknown"
print('\n------// Data correction - Category - start')
df['category'] = df['category'].replace({'-', 'Unknown'})

print('\n------// Data correction - Category - end')

# 2. In size column, unify the data
print('\n------// Data correction - Size - start')
df['size'] = df['size'].replace({'small':'Small', 'SMALL':'Small', 
                                'medium':'Medium', 'MEDIUM':'Medium', 
                                'large':'Large', 'LARGE':'Large'})

print('\n------// Data correction - Size - end')

# 3. Cast the data in price column to the float datatype
print('\n------// Data correction - Price - start')
print('Datatype of price column : {}'.format(df['price'].dtype))
df['price'] = df['price'].fillna(0)
df['price'] = df['price'].replace({'unlisted':0})
df['price'] = pd.to_numeric(df['price'])
print('Datatype of price column : {}'.format(df['price'].dtype))
print('------// Data correction - Price - end')


# 4. Replace null value in rating column with 0
print('\n------// Data correction - Rating - start')
print('Number of null value in column rating : {}'.format(df['rating'].isna().sum()))
df['rating'] = df['rating'].fillna(0)
print('Number of null value in column rating : {}'.format(df['rating'].isna().sum()))
print('------// Data correction - Rating - end')



# >> Task 2 : Data Visualizasion -> Repeat Purchase across Categories
df_viz_1 = df.groupby('category')['repeat_purchase'].sum()

df_viz_1.plot(kind = 'bar', 
              title = 'Repeat Purhase v.s. Category')

plt.show()



#  >> Task 3 : Analyzing distribution of the sales data
df_viz_2 = df['sales']
df_viz_2.plot(kind = 'hist', title = 'Sales Distribution', bins = 10, grid = False)

print('\n------//Fetching Sales distribution data')
print('Mean of sales distribution : {}'.format(round(df_viz_2.mean(), 3)))
print('Median of sales distribution : {}'.format(round(df_viz_2.median(), 3)))
print('Standard Deviation of sales distribution : {}'.format(round(df_viz_2.std(), 3)))

plt.show()




#  >> Task 4 : Analyze the relationship b/w repeat_purchase and sales
df.boxplot(column = 'sales', by = 'repeat_purchase')
plt.show()




