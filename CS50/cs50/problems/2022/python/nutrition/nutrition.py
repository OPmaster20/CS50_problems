d={"Apple":"130","Avocado":"50","Sweet Cherries":"100","Tomato":None,"Banana":"110",
"Cantaloupe":"50","Pear":"100","Peach":"60","Watermelon":"80","Tangerine":"50","Strawberries":"50","Plums":"70",
"Pineapple":"50","Orange":"80","Nectarine":"60","Lime":"20","Kiwifruit":"90","Honeydew Melon":"50","Grapes":"90",
"Grapefruit":"60"}
x=str(input("Item:"))
x=x.capitalize()
for k in d:
    if x==k:
        print("Calories:",d[k])
