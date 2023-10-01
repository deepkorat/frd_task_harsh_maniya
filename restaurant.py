# data from ChatGPT
restaurant_data = [
    {"ID": 1, "Type of Dish": "Appetizer", "Item Name": "Caprese Salad", "Description": "Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.", "Price": 8.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 250, "Allergens": "Gluten-free", "Recommended Drink": "White Wine"},
    {"ID": 2, "Type of Dish": "Main Course", "Item Name": "Grilled Salmon", "Description": "Grilled salmon fillet served with lemon butter sauce and roasted vegetables.", "Price": 18.99, "Availability": "Yes", "Spiciness Level": "Moderate", "Calories": 350, "Allergens": "Dairy-free, Gluten-free", "Recommended Drink": "Chardonnay"},
    {"ID": 3, "Type of Dish": "Dessert", "Item Name": "Chocolate Lava Cake", "Description": "Warm chocolate cake with a molten chocolate center, served with vanilla ice cream.", "Price": 6.99, "Availability": "Yes", "Spiciness Level": "Moderate", "Calories": 400, "Allergens": "Nut-free", "Recommended Drink": "Coffee"},
    {"ID": 4, "Type of Dish": "Appetizer", "Item Name": "Spinach Artichoke Dip", "Description": "Creamy dip with spinach, artichokes, and cheese, served with tortilla chips.", "Price": 7.49, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 300, "Allergens": "Nut-free, Gluten-free", "Recommended Drink": "Beer"},
    {"ID": 5, "Type of Dish": "Main Course", "Item Name": "Chicken Alfredo", "Description": "Fettuccine pasta with creamy Alfredo sauce, grilled chicken, and Parmesan cheese.", "Price": 14.99, "Availability": "Yes", "Spiciness Level": "Moderate", "Calories": 600, "Allergens": "Gluten-free", "Recommended Drink": "White Wine"},
    {"ID": 6, "Type of Dish": "Dessert", "Item Name": "Tiramisu", "Description": "Classic Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cheese.", "Price": 8.49, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 450, "Allergens": "Nut-free", "Recommended Drink": "Espresso"},
    {"ID": 7, "Type of Dish": "Appetizer", "Item Name": "Shrimp Spring Rolls", "Description": "Fresh spring rolls filled with shrimp, vegetables, and rice vermicelli, served with peanut sauce.", "Price": 9.99, "Availability": "Yes", "Spiciness Level": "Moderate", "Calories": 200, "Allergens": "Gluten-free, Dairy-free", "Recommended Drink": "Iced Tea"},
    {"ID": 8, "Type of Dish": "Main Course", "Item Name": "Beef Stir Fry", "Description": "Sliced beef, mixed vegetables, and soy sauce stir-fried to perfection, served with steamed rice.", "Price": 16.49, "Availability": "Yes", "Spiciness Level": "Spicy", "Calories": 500, "Allergens": "Nut-free", "Recommended Drink": "Sake"},
    {"ID": 9, "Type of Dish": "Dessert", "Item Name": "Cheesecake", "Description": "New York-style cheesecake topped with strawberries and whipped cream.", "Price": 7.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 550, "Allergens": "Nut-free", "Recommended Drink": "Coffee"},
    {"ID": 10, "Type of Dish": "Appetizer", "Item Name": "Bruschetta", "Description": "Grilled bread rubbed with garlic, topped with diced tomatoes, basil, and olive oil.", "Price": 6.29, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 180, "Allergens": "Dairy-free, Nut-free", "Recommended Drink": "White Wine"},
    {"ID": 11, "Type of Dish": "Main Course", "Item Name": "Vegetarian Curry", "Description": "Mixed vegetables and tofu cooked in a flavorful curry sauce, served with naan bread.", "Price": 12.99, "Availability": "Yes", "Spiciness Level": "Spicy", "Calories": 400, "Allergens": "Dairy-free", "Recommended Drink": "Lassi"},
    {"ID": 12, "Type of Dish": "Dessert", "Item Name": "Fruit Sorbet", "Description": "Refreshing sorbet made with a blend of seasonal fruits.", "Price": 5.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 150, "Allergens": "Dairy-free, Nut-free", "Recommended Drink": "Water"},
    # Continue with more entries as needed
]

# extended data from chatGPT with No "Allergens" column
restaurant_data_extend = [
    {"ID": 13, "Type of Dish": "Appetizer", "Item Name": "Mozzarella Sticks", "Description": "Fried mozzarella cheese sticks served with marinara sauce.", "Price": 7.49, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 320, "Recommended Drink": "Beer"},
    {"ID": 14, "Type of Dish": "Main Course", "Item Name": "Pasta Carbonara", "Description": "Spaghetti pasta with creamy egg and pancetta sauce.", "Price": 12.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 450, "Recommended Drink": "White Wine"},
    {"ID": 15, "Type of Dish": "Dessert", "Item Name": "Red Velvet Cake", "Description": "Moist red velvet cake with cream cheese frosting.", "Price": 6.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 380, "Recommended Drink": "Coffee"},
    {"ID": 16, "Type of Dish": "Appetizer", "Item Name": "Chicken Wings", "Description": "Crispy chicken wings tossed in your choice of sauce (BBQ, Buffalo, or Honey Mustard).", "Price": 9.99, "Availability": "Yes", "Spiciness Level": "Spicy", "Calories": 420, "Recommended Drink": "Iced Tea"},
    {"ID": 17, "Type of Dish": "Main Course", "Item Name": "Steak Fajitas", "Description": "Sizzling marinated steak strips served with sautéed bell peppers and onions, tortillas, and condiments.", "Price": 17.99, "Availability": "Yes", "Spiciness Level": "Moderate", "Calories": 550, "Recommended Drink": "Margarita"},
    {"ID": 18, "Type of Dish": "Dessert", "Item Name": "Key Lime Pie", "Description": "Tangy key lime pie with a graham cracker crust, topped with whipped cream.", "Price": 7.49, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 320, "Recommended Drink": "Lemonade"},
    {"ID": 19, "Type of Dish": "Appetizer", "Item Name": "Nachos", "Description": "Tortilla chips topped with melted cheese, jalapeños, guacamole, and sour cream.", "Price": 8.99, "Availability": "Yes", "Spiciness Level": "Spicy", "Calories": 480, "Recommended Drink": "Beer"},
    {"ID": 20, "Type of Dish": "Main Course", "Item Name": "Vegetable Stir Fry", "Description": "Assorted vegetables stir-fried in a savory sauce, served with steamed rice.", "Price": 11.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 380, "Recommended Drink": "Green Tea"},
    {"ID": 21, "Type of Dish": "Dessert", "Item Name": "Mango Sorbet", "Description": "Refreshing sorbet made with ripe mangoes.", "Price": 5.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 180, "Recommended Drink": "Water"},
    {"ID": 22, "Type of Dish": "Appetizer", "Item Name": "Caesar Salad", "Description": "Crisp romaine lettuce, croutons, Parmesan cheese, and Caesar dressing.", "Price": 6.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 220, "Recommended Drink": "White Wine"},
    {"ID": 23, "Type of Dish": "Main Course", "Item Name": "Margherita Pizza", "Description": "Classic pizza with tomato sauce, mozzarella cheese, and fresh basil.", "Price": 10.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 300, "Recommended Drink": "Beer"},
    {"ID": 24, "Type of Dish": "Dessert", "Item Name": "Strawberry Shortcake", "Description": "Sponge cake layered with fresh strawberries and whipped cream.", "Price": 7.99, "Availability": "Yes", "Spiciness Level": "Mild", "Calories": 380, "Recommended Drink": "Coffee"}
]

# import pandas library
import pandas as pd

# first data set into "df" DataFrame
df = pd.DataFrame.from_dict(restaurant_data)

# second data set into "df2" DataFrame
df2 = pd.DataFrame.from_dict(restaurant_data_extend)

# Drop Unnecessary columns from both DataFrame
res_df_dropped = df.drop(["Allergens", "Calories", "Availability"], axis=1)
res_df_dropped_2 = df2.drop(["Calories", "Availability"], axis=1)

# Merged both data data frame into single data set which we use into further. 
res_df = pd.concat([res_df_dropped, res_df_dropped_2], ignore_index=True)


###### FILTER FUNCTIONS DEFINATION
def type_of_dish(t_o_d):
    filter_TOD = res_df[res_df["Type of Dish"] == t_o_d]
    print(filter_TOD)

def item_name(item_count):
    filter_item = res_df[res_df["ID"] == item_count]
    print(filter_item)

def price(min, max):
    filter_price_range = res_df[res_df["Price"].between(min, max, inclusive=True)]
    print(filter_price_range)


###### CATEGORY WISE FUNCTION DEFINATION
# funciton of choise 1. Type of Dish
def main_menu_type_of_dish():
    print("Welcome to our Menu. Chhose your type of Dish.")
    print("1. Appetizer")
    print("2. Main Course")
    print("3. Dessert")
    
    try:
        type_of_dish_choice = int(input("Enter Your dish type choise in Number: "))
        print("\n")
        if type_of_dish_choice > 3 or type_of_dish_choice < 1:
            print("!!! Please enter valid choise !!! ")
        if type_of_dish_choice == 1:
            type_of_dish("Appetizer")
        elif type_of_dish_choice == 2:
            type_of_dish("Main Course")
        else:
            type_of_dish("Dessert")
    except ValueError:
        print("No valid integer! Please try again ...")
        
# function of choise 2. Price Range
def main_menu_price_range():
    print("Kindly enter Your minimum price or maximum price between 5 to 18")
    min = int(input("Enter minimum price: "))
    max = int(input("Enter maximum price: "))
    price(min, max)

# function of choise 3. Item name
def main_menu_item_name():
    print(res_df.loc[: ,  ['ID' , 'Item Name']])
    print("\n", "Chhose your Item to see full details of item")
    item_count = int(input("Enter your choise in number:  "))
    item_name(item_count)


##### MAIN CODE

while True:
    print("\n\n", "Make choise through this topics:-")
    print("1. Type of Dish ")
    print("2. Price Range")
    print("3. Item name")
    
    try:
        choice = int(input("Enter your choise : "))
        print("\n")
        if choice > 3 or choice < 1:
            print("!!! Please enter valid choise !!! ")
        elif choice == 1:
            main_menu_type_of_dish()
        elif choice == 2:
            main_menu_price_range()
        else:
            main_menu_item_name()
    except ValueError:
        print("No valid integer! Please try again ...")

        