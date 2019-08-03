/*


> show collections
Product
>
>
> db.Product.find({"ProductID" : 77}).pretty() -------> Equality ==
{
        "_id" : ObjectId("5d4537924766780cd352316e"),
        "ProductID" : 77,
        "ProductName" : "Original Frankfurter grüne Soße",
        "CategoryID" : 2,
        "UnitPrice" : 13,
        "UnitsInStock" : 32
}


#----------------------------------------------------------------------------------------------

--> 8 numaralı CategoryID değerine sahip olan ürünleri listeleyiniz.

> db.Product.find({"ProductID" : 77}).pretty()
{
        "_id" : ObjectId("5d4537924766780cd352316e"),
        "ProductID" : 77,
        "ProductName" : "Original Frankfurter grüne Soße",
        "CategoryID" : 2,
        "UnitPrice" : 13,
        "UnitsInStock" : 32
}
>
>
>
>
> db.Products.find({"CategoryID" : 8}).pretty()
> db.Product.find({"CategoryID" : 8}).pretty()
{
        "_id" : ObjectId("5d4537924766780cd352312b"),
        "ProductID" : 10,
        "ProductName" : "Ikura",
        "CategoryID" : 8,
        "UnitPrice" : 31,
        "UnitsInStock" : 31
}
{
        "_id" : ObjectId("5d4537924766780cd352312e"),
        "ProductID" : 13,
        "ProductName" : "Konbu",
        "CategoryID" : 8,
        "UnitPrice" : 6,
        "UnitsInStock" : 24
}
{
        "_id" : ObjectId("5d4537924766780cd3523133"),
        "ProductID" : 18,
        "ProductName" : "Carnarvon Tigers",
        "CategoryID" : 8,
        "UnitPrice" : 62.5,
        "UnitsInStock" : 42
}
{
        "_id" : ObjectId("5d4537924766780cd352313f"),
        "ProductID" : 30,
        "ProductName" : "Nord-Ost Matjeshering",
        "CategoryID" : 8,
        "UnitPrice" : 25.89,
        "UnitsInStock" : 10
}
{
        "_id" : ObjectId("5d4537924766780cd3523145"),
        "ProductID" : 36,
        "ProductName" : "Inlagd Sill",
        "CategoryID" : 8,
        "UnitPrice" : 19,
        "UnitsInStock" : 112
}
{
        "_id" : ObjectId("5d4537924766780cd3523146"),
        "ProductID" : 37,
        "ProductName" : "Gravad lax",
        "CategoryID" : 8,
        "UnitPrice" : 26,
        "UnitsInStock" : 11
}
{
        "_id" : ObjectId("5d4537924766780cd3523149"),
        "ProductID" : 40,
        "ProductName" : "Boston Crab Meat",
        "CategoryID" : 8,
        "UnitPrice" : 18.4,
        "UnitsInStock" : 123
}
{
        "_id" : ObjectId("5d4537924766780cd352314a"),
        "ProductID" : 41,
        "ProductName" : "Jack's New England Clam Chowder",
        "CategoryID" : 8,
        "UnitPrice" : 9.65,
        "UnitsInStock" : 85
}
{
        "_id" : ObjectId("5d4537924766780cd352314e"),
        "ProductID" : 45,
        "ProductName" : "Rogede sild",
        "CategoryID" : 8,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 5
}
{
        "_id" : ObjectId("5d4537924766780cd352314f"),
        "ProductID" : 46,
        "ProductName" : "Spegesild",
        "CategoryID" : 8,
        "UnitPrice" : 12,
        "UnitsInStock" : 95
}
{
        "_id" : ObjectId("5d4537924766780cd352315b"),
        "ProductID" : 58,
        "ProductName" : "Escargots de Bourgogne",
        "CategoryID" : 8,
        "UnitPrice" : 13.25,
        "UnitsInStock" : 62
}
{
        "_id" : ObjectId("5d4537924766780cd352316a"),
        "ProductID" : 73,
        "ProductName" : "Röd Kaviar",
        "CategoryID" : 8,
        "UnitPrice" : 15,
        "UnitsInStock" : 101
}

#----------------------------------------------------------------------------------------------
--> Less than
---> Fiyatı 50$'dan az olan ürünlerin listelenmesi
> db.Product.find({"UnitPrice" : {$lt:50}}).pretty()

--> Ürünlerin sıralanması
---> Ascending +1 A'dan Z'ye, 0'dan 9'a
---> Descending -1 Z'den A'ya, 9'dan 0'a 
> db.Product.find({"UnitPrice" : {$lt:10}}).pretty().sort({"UnitPrice" : 1})
{
        "_id" : ObjectId("5d4537924766780cd3523142"),
        "ProductID" : 33,
        "ProductName" : "Geitost",
        "CategoryID" : 4,
        "UnitPrice" : 2.5,
        "UnitsInStock" : 112
}
{
        "_id" : ObjectId("5d4537924766780cd3523139"),
        "ProductID" : 24,
        "ProductName" : "Guaraná Fantástica",
        "CategoryID" : 1,
        "UnitPrice" : 4.5,
        "UnitsInStock" : 20
}
{
        "_id" : ObjectId("5d4537924766780cd352312e"),
        "ProductID" : 13,
        "ProductName" : "Konbu",
        "CategoryID" : 8,
        "UnitPrice" : 6,
        "UnitsInStock" : 24
}
{
        "_id" : ObjectId("5d4537924766780cd3523155"),
        "ProductID" : 52,
        "ProductName" : "Filo Mix",
        "CategoryID" : 5,
        "UnitPrice" : 7,
        "UnitsInStock" : 38
}
{
        "_id" : ObjectId("5d4537924766780cd3523157"),
        "ProductID" : 54,
        "ProductName" : "Tourtière",
        "CategoryID" : 6,
        "UnitPrice" : 7.45,
        "UnitsInStock" : 21
}
{
        "_id" : ObjectId("5d4537924766780cd352316c"),
        "ProductID" : 75,
        "ProductName" : "Rhönbräu Klosterbier",
        "CategoryID" : 1,
        "UnitPrice" : 7.75,
        "UnitsInStock" : 125
}
{
        "_id" : ObjectId("5d4537924766780cd3523138"),
        "ProductID" : 23,
        "ProductName" : "Tunnbröd",
        "CategoryID" : 5,
        "UnitPrice" : 9,
        "UnitsInStock" : 61
}
{
        "_id" : ObjectId("5d4537924766780cd3523134"),
        "ProductID" : 19,
        "ProductName" : "Teatime Chocolate Biscuits",
        "CategoryID" : 3,
        "UnitPrice" : 9.2,
        "UnitsInStock" : 25
}
{
        "_id" : ObjectId("5d4537924766780cd352314e"),
        "ProductID" : 45,
        "ProductName" : "Rogede sild",
        "CategoryID" : 8,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 5
}
{
        "_id" : ObjectId("5d4537924766780cd3523150"),
        "ProductID" : 47,
        "ProductName" : "Zaanse koeken",
        "CategoryID" : 3,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 36
}
{
        "_id" : ObjectId("5d4537924766780cd352314a"),
        "ProductID" : 41,
        "ProductName" : "Jack's New England Clam Chowder",
        "CategoryID" : 8,
        "UnitPrice" : 9.65,
        "UnitsInStock" : 85
}



> db.Product.find({"UnitPrice" : {$lt:10}}).pretty().sort({"UnitPrice" : -1})
{
        "_id" : ObjectId("5d4537924766780cd352314a"),
        "ProductID" : 41,
        "ProductName" : "Jack's New England Clam Chowder",
        "CategoryID" : 8,
        "UnitPrice" : 9.65,
        "UnitsInStock" : 85
}
{
        "_id" : ObjectId("5d4537924766780cd352314e"),
        "ProductID" : 45,
        "ProductName" : "Rogede sild",
        "CategoryID" : 8,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 5
}
{
        "_id" : ObjectId("5d4537924766780cd3523150"),
        "ProductID" : 47,
        "ProductName" : "Zaanse koeken",
        "CategoryID" : 3,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 36
}
{
        "_id" : ObjectId("5d4537924766780cd3523134"),
        "ProductID" : 19,
        "ProductName" : "Teatime Chocolate Biscuits",
        "CategoryID" : 3,
        "UnitPrice" : 9.2,
        "UnitsInStock" : 25
}
{
        "_id" : ObjectId("5d4537924766780cd3523138"),
        "ProductID" : 23,
        "ProductName" : "Tunnbröd",
        "CategoryID" : 5,
        "UnitPrice" : 9,
        "UnitsInStock" : 61
}
{
        "_id" : ObjectId("5d4537924766780cd352316c"),
        "ProductID" : 75,
        "ProductName" : "Rhönbräu Klosterbier",
        "CategoryID" : 1,
        "UnitPrice" : 7.75,
        "UnitsInStock" : 125
}
{
        "_id" : ObjectId("5d4537924766780cd3523157"),
        "ProductID" : 54,
        "ProductName" : "Tourtière",
        "CategoryID" : 6,
        "UnitPrice" : 7.45,
        "UnitsInStock" : 21
}
{
        "_id" : ObjectId("5d4537924766780cd3523155"),
        "ProductID" : 52,
        "ProductName" : "Filo Mix",
        "CategoryID" : 5,
        "UnitPrice" : 7,
        "UnitsInStock" : 38
}
{
        "_id" : ObjectId("5d4537924766780cd352312e"),
        "ProductID" : 13,
        "ProductName" : "Konbu",
        "CategoryID" : 8,
        "UnitPrice" : 6,
        "UnitsInStock" : 24
}
{
        "_id" : ObjectId("5d4537924766780cd3523139"),
        "ProductID" : 24,
        "ProductName" : "Guaraná Fantástica",
        "CategoryID" : 1,
        "UnitPrice" : 4.5,
        "UnitsInStock" : 20
}
{
        "_id" : ObjectId("5d4537924766780cd3523142"),
        "ProductID" : 33,
        "ProductName" : "Geitost",
        "CategoryID" : 4,
        "UnitPrice" : 2.5,
        "UnitsInStock" : 112
}

--> Less Than Equals
> db.Product.find({"UnitsInStock" : {$lte:50}}).pretty()
> db.Product.find({"UnitsInStock" : {$lte:50}}).pretty().sort({"UnitsInStock" : 1})

--> Greater Than
---> Fiyatı 100$ 'dan fazla olanları listeleyiniz.
> db.Product.find({"UnitPrice" : {$gt:100}}).pretty()
{
        "_id" : ObjectId("5d4537924766780cd352313e"),
        "ProductID" : 29,
        "ProductName" : "Thüringer Rostbratwurst",
        "CategoryID" : 6,
        "UnitPrice" : 123.79,
        "UnitsInStock" : 0
}
{
        "_id" : ObjectId("5d4537924766780cd3523147"),
        "ProductID" : 38,
        "ProductName" : "Côte de Blaye",
        "CategoryID" : 1,
        "UnitPrice" : 263.5,
        "UnitsInStock" : 17
}


> db.Product.find({"UnitPrice" : {$gt:100}}).pretty().sort({"UnitPrice" : -1})
{
        "_id" : ObjectId("5d4537924766780cd3523147"),
        "ProductID" : 38,
        "ProductName" : "Côte de Blaye",
        "CategoryID" : 1,
        "UnitPrice" : 263.5,
        "UnitsInStock" : 17
}
{
        "_id" : ObjectId("5d4537924766780cd352313e"),
        "ProductID" : 29,
        "ProductName" : "Thüringer Rostbratwurst",
        "CategoryID" : 6,
        "UnitPrice" : 123.79,
        "UnitsInStock" : 0
}


--> Greater Than Equals
> db.Product.find({"UnitPrice" : {$gte:50}}).pretty().sort({"UnitPrice" : -1})
{
        "_id" : ObjectId("5d4537924766780cd3523147"),
        "ProductID" : 38,
        "ProductName" : "Côte de Blaye",
        "CategoryID" : 1,
        "UnitPrice" : 263.5,
        "UnitsInStock" : 17
}
{
        "_id" : ObjectId("5d4537924766780cd352313e"),
        "ProductID" : 29,
        "ProductName" : "Thüringer Rostbratwurst",
        "CategoryID" : 6,
        "UnitPrice" : 123.79,
        "UnitsInStock" : 0
}
{
        "_id" : ObjectId("5d4537924766780cd352312a"),
        "ProductID" : 9,
        "ProductName" : "Mishi Kobe Niku",
        "CategoryID" : 6,
        "UnitPrice" : 97,
        "UnitsInStock" : 29
}
{
        "_id" : ObjectId("5d4537924766780cd3523135"),
        "ProductID" : 20,
        "ProductName" : "Sir Rodney's Marmalade",
        "CategoryID" : 3,
        "UnitPrice" : 81,
        "UnitsInStock" : 40
}
{
        "_id" : ObjectId("5d4537924766780cd3523133"),
        "ProductID" : 18,
        "ProductName" : "Carnarvon Tigers",
        "CategoryID" : 8,
        "UnitPrice" : 62.5,
        "UnitsInStock" : 42
}
{
        "_id" : ObjectId("5d4537924766780cd352315c"),
        "ProductID" : 59,
        "ProductName" : "Raclette Courdavault",
        "CategoryID" : 4,
        "UnitPrice" : 55,
        "UnitsInStock" : 79
}
{
        "_id" : ObjectId("5d4537924766780cd3523154"),
        "ProductID" : 51,
        "ProductName" : "Manjimup Dried Apples",
        "CategoryID" : 7,
        "UnitPrice" : 53,
        "UnitsInStock" : 20
}

--> Not Equals
---> CategoryID değeri 8 olmayan ürünlerin listelenmesi
> db.Product.find({"CategoryID" : {$ne:8}}).pretty().sort({"CategoryID" : 1})



--> and ve or kullanımı
---> and
> db.Product.find({$and:[{"CategoryID" : 8},{"UnitPrice" : {$lte:30}}]}).pretty()
{
        "_id" : ObjectId("5d4537924766780cd352312e"),
        "ProductID" : 13,
        "ProductName" : "Konbu",
        "CategoryID" : 8,
        "UnitPrice" : 6,
        "UnitsInStock" : 24
}
{
        "_id" : ObjectId("5d4537924766780cd352313f"),
        "ProductID" : 30,
        "ProductName" : "Nord-Ost Matjeshering",
        "CategoryID" : 8,
        "UnitPrice" : 25.89,
        "UnitsInStock" : 10
}
{
        "_id" : ObjectId("5d4537924766780cd3523145"),
        "ProductID" : 36,
        "ProductName" : "Inlagd Sill",
        "CategoryID" : 8,
        "UnitPrice" : 19,
        "UnitsInStock" : 112
}
{
        "_id" : ObjectId("5d4537924766780cd3523146"),
        "ProductID" : 37,
        "ProductName" : "Gravad lax",
        "CategoryID" : 8,
        "UnitPrice" : 26,
        "UnitsInStock" : 11
}
{
        "_id" : ObjectId("5d4537924766780cd3523149"),
        "ProductID" : 40,
        "ProductName" : "Boston Crab Meat",
        "CategoryID" : 8,
        "UnitPrice" : 18.4,
        "UnitsInStock" : 123
}
{
        "_id" : ObjectId("5d4537924766780cd352314a"),
        "ProductID" : 41,
        "ProductName" : "Jack's New England Clam Chowder",
        "CategoryID" : 8,
        "UnitPrice" : 9.65,
        "UnitsInStock" : 85
}
{
        "_id" : ObjectId("5d4537924766780cd352314e"),
        "ProductID" : 45,
        "ProductName" : "Rogede sild",
        "CategoryID" : 8,
        "UnitPrice" : 9.5,
        "UnitsInStock" : 5
}
{
        "_id" : ObjectId("5d4537924766780cd352314f"),
        "ProductID" : 46,
        "ProductName" : "Spegesild",
        "CategoryID" : 8,
        "UnitPrice" : 12,
        "UnitsInStock" : 95
}
{
        "_id" : ObjectId("5d4537924766780cd352315b"),
        "ProductID" : 58,
        "ProductName" : "Escargots de Bourgogne",
        "CategoryID" : 8,
        "UnitPrice" : 13.25,
        "UnitsInStock" : 62
}
{
        "_id" : ObjectId("5d4537924766780cd352316a"),
        "ProductID" : 73,
        "ProductName" : "Röd Kaviar",
        "CategoryID" : 8,
        "UnitPrice" : 15,
        "UnitsInStock" : 101
}


----> Fiyatı 30$ 'dan büyük ve stok adedi 100'den küçük olanların listlenmesi
> db.Product.find({$and:[{"UnitsInStock" : {$lt:100}},{"UnitPrice" : {$gt:30}}]}).pretty()

--> or 
---> Fiyatı 100$ üzeri veya stock adedi 100 üzeri olan ürünlerin fiyata göre asc olarak sıralı listelenmesi
> db.Product.find({$or:[{"UnitsInStock" : {$gt:100}},{"UnitPrice" : {$gt:100}}]}).pretty().sort({"UnitPrice": 1})
{
        "_id" : ObjectId("5d4537924766780cd3523142"),
        "ProductID" : 33,
        "ProductName" : "Geitost",
        "CategoryID" : 4,
        "UnitPrice" : 2.5,
        "UnitsInStock" : 112
}
{
        "_id" : ObjectId("5d4537924766780cd352316c"),
        "ProductID" : 75,
        "ProductName" : "Rhönbräu Klosterbier",
        "CategoryID" : 1,
        "UnitPrice" : 7.75,
        "UnitsInStock" : 125
}
{
        "_id" : ObjectId("5d4537924766780cd3523143"),
        "ProductID" : 34,
        "ProductName" : "Sasquatch Ale",
        "CategoryID" : 1,
        "UnitPrice" : 14,
        "UnitsInStock" : 111
}
{
        "_id" : ObjectId("5d4537924766780cd352316a"),
        "ProductID" : 73,
        "ProductName" : "Röd Kaviar",
        "CategoryID" : 8,
        "UnitPrice" : 15,
        "UnitsInStock" : 101
}
{
        "_id" : ObjectId("5d4537924766780cd3523149"),
        "ProductID" : 40,
        "ProductName" : "Boston Crab Meat",
        "CategoryID" : 8,
        "UnitPrice" : 18.4,
        "UnitsInStock" : 123
}
{
        "_id" : ObjectId("5d4537924766780cd3523145"),
        "ProductID" : 36,
        "ProductName" : "Inlagd Sill",
        "CategoryID" : 8,
        "UnitPrice" : 19,
        "UnitsInStock" : 112
}
{
        "_id" : ObjectId("5d4537924766780cd3523137"),
        "ProductID" : 22,
        "ProductName" : "Gustaf's Knäckebröd",
        "CategoryID" : 5,
        "UnitPrice" : 21,
        "UnitsInStock" : 104
}
{
        "_id" : ObjectId("5d4537924766780cd3523158"),
        "ProductID" : 55,
        "ProductName" : "Pâté chinois",
        "CategoryID" : 6,
        "UnitPrice" : 24,
        "UnitsInStock" : 115
}
{
        "_id" : ObjectId("5d4537924766780cd3523127"),
        "ProductID" : 6,
        "ProductName" : "Grandma's Boysenberry Spread",
        "CategoryID" : 2,
        "UnitPrice" : 25,
        "UnitsInStock" : 120
}
{
        "_id" : ObjectId("5d4537924766780cd352315e"),
        "ProductID" : 61,
        "ProductName" : "Sirop d'érable",
        "CategoryID" : 2,
        "UnitPrice" : 28.5,
        "UnitsInStock" : 113
}
{
        "_id" : ObjectId("5d4537924766780cd352313e"),
        "ProductID" : 29,
        "ProductName" : "Thüringer Rostbratwurst",
        "CategoryID" : 6,
        "UnitPrice" : 123.79,
        "UnitsInStock" : 0
}
{
        "_id" : ObjectId("5d4537924766780cd3523147"),
        "ProductID" : 38,
        "ProductName" : "Côte de Blaye",
        "CategoryID" : 1,
        "UnitPrice" : 263.5,
        "UnitsInStock" : 17
}

----> Ürün Adı, fiyat ve stok adedini listeleyiniz.
> db.Product.find({},{ProductName : 1, UnitPrice : 1, UnitsInStock : 1, _id : 0}).sort({ProductName : 1})
{ "ProductName" : "Alice Mutton", "UnitPrice" : 39, "UnitsInStock" : 0 }
{ "ProductName" : "Aniseed Syrup", "UnitPrice" : 10, "UnitsInStock" : 13 }
{ "ProductName" : "Boston Crab Meat", "UnitPrice" : 18.4, "UnitsInStock" : 123 }
{ "ProductName" : "Camembert Pierrot", "UnitPrice" : 34, "UnitsInStock" : 19 }
{ "ProductName" : "Carnarvon Tigers", "UnitPrice" : 62.5, "UnitsInStock" : 42 }
{ "ProductName" : "Chai", "UnitPrice" : 18, "UnitsInStock" : 39 }
{ "ProductName" : "Chang", "UnitPrice" : 19, "UnitsInStock" : 17 }
{ "ProductName" : "Chartreuse verte", "UnitPrice" : 18, "UnitsInStock" : 69 }
{ "ProductName" : "Chef Anton's Cajun Seasoning", "UnitPrice" : 22, "UnitsInStock" : 53 }
{ "ProductName" : "Chef Anton's Gumbo Mix", "UnitPrice" : 21.35, "UnitsInStock" : 0 }
{ "ProductName" : "Chocolade", "UnitPrice" : 12.75, "UnitsInStock" : 15 }
{ "ProductName" : "Côte de Blaye", "UnitPrice" : 263.5, "UnitsInStock" : 17 }
{ "ProductName" : "Escargots de Bourgogne", "UnitPrice" : 13.25, "UnitsInStock" : 62 }
{ "ProductName" : "Filo Mix", "UnitPrice" : 7, "UnitsInStock" : 38 }
{ "ProductName" : "Flotemysost", "UnitPrice" : 21.5, "UnitsInStock" : 26 }
{ "ProductName" : "Geitost", "UnitPrice" : 2.5, "UnitsInStock" : 112 }
{ "ProductName" : "Genen Shouyu", "UnitPrice" : 15.5, "UnitsInStock" : 39 }
{ "ProductName" : "Gnocchi di nonna Alice", "UnitPrice" : 38, "UnitsInStock" : 21 }
{ "ProductName" : "Gorgonzola Telino", "UnitPrice" : 12.5, "UnitsInStock" : 0 }
{ "ProductName" : "Grandma's Boysenberry Spread", "UnitPrice" : 25, "UnitsInStock" : 120 }
Type "it" for more
> it
{ "ProductName" : "Gravad lax", "UnitPrice" : 26, "UnitsInStock" : 11 }
{ "ProductName" : "Guaraná Fantástica", "UnitPrice" : 4.5, "UnitsInStock" : 20 }
{ "ProductName" : "Gudbrandsdalsost", "UnitPrice" : 36, "UnitsInStock" : 26 }
{ "ProductName" : "Gula Malacca", "UnitPrice" : 19.45, "UnitsInStock" : 27 }
{ "ProductName" : "Gumbär Gummibärchen", "UnitPrice" : 31.23, "UnitsInStock" : 15 }
{ "ProductName" : "Gustaf's Knäckebröd", "UnitPrice" : 21, "UnitsInStock" : 104 }
{ "ProductName" : "Ikura", "UnitPrice" : 31, "UnitsInStock" : 31 }
{ "ProductName" : "Inlagd Sill", "UnitPrice" : 19, "UnitsInStock" : 112 }
{ "ProductName" : "Ipoh Coffee", "UnitPrice" : 46, "UnitsInStock" : 17 }
{ "ProductName" : "Jack's New England Clam Chowder", "UnitPrice" : 9.65, "UnitsInStock" : 85 }
{ "ProductName" : "Konbu", "UnitPrice" : 6, "UnitsInStock" : 24 }
{ "ProductName" : "Lakkalikööri", "UnitPrice" : 18, "UnitsInStock" : 57 }
{ "ProductName" : "Laughing Lumberjack Lager", "UnitPrice" : 14, "UnitsInStock" : 52 }
{ "ProductName" : "Longlife Tofu", "UnitPrice" : 10, "UnitsInStock" : 4 }
{ "ProductName" : "Louisiana Fiery Hot Pepper Sauce", "UnitPrice" : 21.05, "UnitsInStock" : 76 }
{ "ProductName" : "Louisiana Hot Spiced Okra", "UnitPrice" : 17, "UnitsInStock" : 4 }
{ "ProductName" : "Manjimup Dried Apples", "UnitPrice" : 53, "UnitsInStock" : 20 }
{ "ProductName" : "Mascarpone Fabioli", "UnitPrice" : 32, "UnitsInStock" : 9 }
{ "ProductName" : "Maxilaku", "UnitPrice" : 20, "UnitsInStock" : 10 }
{ "ProductName" : "Mishi Kobe Niku", "UnitPrice" : 97, "UnitsInStock" : 29 }
Type "it" for more
> it
{ "ProductName" : "Mozzarella di Giovanni", "UnitPrice" : 34.8, "UnitsInStock" : 14 }
{ "ProductName" : "Nord-Ost Matjeshering", "UnitPrice" : 25.89, "UnitsInStock" : 10 }
{ "ProductName" : "Northwoods Cranberry Sauce", "UnitPrice" : 40, "UnitsInStock" : 6 }
{ "ProductName" : "NuNuCa Nuß-Nougat-Creme", "UnitPrice" : 14, "UnitsInStock" : 76 }
{ "ProductName" : "Original Frankfurter grüne Soße", "UnitPrice" : 13, "UnitsInStock" : 32 }
{ "ProductName" : "Outback Lager", "UnitPrice" : 15, "UnitsInStock" : 15 }
{ "ProductName" : "Pavlova", "UnitPrice" : 17.45, "UnitsInStock" : 29 }
{ "ProductName" : "Perth Pasties", "UnitPrice" : 32.8, "UnitsInStock" : 0 }
{ "ProductName" : "Pâté chinois", "UnitPrice" : 24, "UnitsInStock" : 115 }
{ "ProductName" : "Queso Cabrales", "UnitPrice" : 21, "UnitsInStock" : 22 }
{ "ProductName" : "Queso Manchego La Pastora", "UnitPrice" : 38, "UnitsInStock" : 86 }
{ "ProductName" : "Raclette Courdavault", "UnitPrice" : 55, "UnitsInStock" : 79 }
{ "ProductName" : "Ravioli Angelo", "UnitPrice" : 19.5, "UnitsInStock" : 36 }
{ "ProductName" : "Rhönbräu Klosterbier", "UnitPrice" : 7.75, "UnitsInStock" : 125 }
{ "ProductName" : "Rogede sild", "UnitPrice" : 9.5, "UnitsInStock" : 5 }
{ "ProductName" : "Röd Kaviar", "UnitPrice" : 15, "UnitsInStock" : 101 }
{ "ProductName" : "Rössle Sauerkraut", "UnitPrice" : 45.6, "UnitsInStock" : 26 }
{ "ProductName" : "Sasquatch Ale", "UnitPrice" : 14, "UnitsInStock" : 111 }
{ "ProductName" : "Schoggi Schokolade", "UnitPrice" : 43.9, "UnitsInStock" : 49 }
{ "ProductName" : "Scottish Longbreads", "UnitPrice" : 12.5, "UnitsInStock" : 6 }
Type "it" for more
> it
{ "ProductName" : "Singaporean Hokkien Fried Mee", "UnitPrice" : 14, "UnitsInStock" : 26 }
{ "ProductName" : "Sir Rodney's Marmalade", "UnitPrice" : 81, "UnitsInStock" : 40 }
{ "ProductName" : "Sir Rodney's Scones", "UnitPrice" : 10, "UnitsInStock" : 3 }
{ "ProductName" : "Sirop d'érable", "UnitPrice" : 28.5, "UnitsInStock" : 113 }
{ "ProductName" : "Spegesild", "UnitPrice" : 12, "UnitsInStock" : 95 }
{ "ProductName" : "Steeleye Stout", "UnitPrice" : 18, "UnitsInStock" : 20 }
{ "ProductName" : "Tarte au sucre", "UnitPrice" : 49.3, "UnitsInStock" : 17 }
{ "ProductName" : "Teatime Chocolate Biscuits", "UnitPrice" : 9.2, "UnitsInStock" : 25 }
{ "ProductName" : "Thüringer Rostbratwurst", "UnitPrice" : 123.79, "UnitsInStock" : 0 }
{ "ProductName" : "Tofu", "UnitPrice" : 23.25, "UnitsInStock" : 35 }
{ "ProductName" : "Tourtière", "UnitPrice" : 7.45, "UnitsInStock" : 21 }
{ "ProductName" : "Tunnbröd", "UnitPrice" : 9, "UnitsInStock" : 61 }
{ "ProductName" : "Uncle Bob's Organic Dried Pears", "UnitPrice" : 30, "UnitsInStock" : 15 }
{ "ProductName" : "Valkoinen suklaa", "UnitPrice" : 16.25, "UnitsInStock" : 65 }
{ "ProductName" : "Vegie-spread", "UnitPrice" : 43.9, "UnitsInStock" : 24 }
{ "ProductName" : "Wimmers gute Semmelknödel", "UnitPrice" : 33.25, "UnitsInStock" : 22 }
{ "ProductName" : "Zaanse koeken", "UnitPrice" : 9.5, "UnitsInStock" : 36 }



#------------------------------------------------------------------------------------------------------




*/

