string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"
string_splite = string.split(' ')

string_dictionary = {'Nine' : 9 , 'Eight' : 8 , 'Seven' : 7 , 'Six':6 , "Five":5 , 'Four':4 , 'Three':3 , 'Two':2 , 'One':1 ,'Ziro':0 , 'Dash' :"-" }
for x in string_splite:
  print(string_dictionary.get(x,x[0]),end='')
