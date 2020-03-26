dictionary = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant"}

print ( list ( dictionary.items() ) )

print ( list (zip (list (dictionary) , list ( dictionary.values() ) ) ) )