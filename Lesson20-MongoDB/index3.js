/*

db.Categories.insertMany(
[
  {
    "CategoryID": 1,
    "CategoryName": "Beverages",
    "Description": "Soft drinks, coffees, teas, beers, and ales"
  },
  {
    "CategoryID": 2,
    "CategoryName": "Condiments",
    "Description": "Sweet and savory sauces, relishes, spreads, and seasonings"
  },
  {
    "CategoryID": 3,
    "CategoryName": "Confections",
    "Description": "Desserts, candies, and sweet breads"
  },
  {
    "CategoryID": 4,
    "CategoryName": "Dairy Products",
    "Description": "Cheeses"
  },
  {
    "CategoryID": 5,
    "CategoryName": "Grains/Cereals",
    "Description": "Breads, crackers, pasta, and cereal"
  },
  {
    "CategoryID": 6,
    "CategoryName": "Meat/Poultry",
    "Description": "Prepared meats"
  },
  {
    "CategoryID": 7,
    "CategoryName": "Produce",
    "Description": "Dried fruit and bean curd"
  },
  {
    "CategoryID": 8,
    "CategoryName": "Seafood",
    "Description": "Seaweed and fish"
  }])

> db.Categories.find({}, {CategoryID : 1, CategoryName : 1, _id : 0})
{ "CategoryID" : 1, "CategoryName" : "Beverages" }
{ "CategoryID" : 2, "CategoryName" : "Condiments" }
{ "CategoryID" : 3, "CategoryName" : "Confections" }
{ "CategoryID" : 4, "CategoryName" : "Dairy Products" }
{ "CategoryID" : 5, "CategoryName" : "Grains/Cereals" }
{ "CategoryID" : 6, "CategoryName" : "Meat/Poultry" }
{ "CategoryID" : 7, "CategoryName" : "Produce" }
{ "CategoryID" : 8, "CategoryName" : "Seafood" }
  

*/

db.Categories.aggregate( // Ana tablo
    {
        $lookup : {
            from : 'Product', // Join yapılacak tablo
                localField : 'CategoryID', // ana tablo içerisindeki pk (primary key) birincil anahtar
                foreignField : 'CategoryID', // fk (foreign key) ikincil anahtar
                as : 'Product' // sorgu sonucu kategoriye bağlı ürünlr listelenirken, verilecek olan isim (opsiyonel). Dilediğiniz ismi yazabilirsiniz.

            }
    
    })

/*


db.Categories.aggregate(
{
    $lookup : {
        from : 'Product',
            localField : 'CategoryID',
            foreignField : 'CategoryID',
            as : 'Product'
    }}).pretty()


#----------------------------------------------------------------------
--> CategoryID'si 1 olan Productları çıkar.

  > db.Categories.aggregate(
...   {
...     $lookup : {
...         from : 'Product',
...         localField : 'CategoryID',
...         foreignField : 'CategoryID',
...         as : 'Product'
...     }
...   },
...   {
...     $match : {
...         "CategoryID" : 1
...     }
...   }).pretty()
{
        "_id" : ObjectId("5d45553db81b6f83e0cc099a"),
        "CategoryID" : 1,
        "CategoryName" : "Beverages",
        "Description" : "Soft drinks, coffees, teas, beers, and ales",
        "Product" : [
                {
                        "_id" : ObjectId("5d4537924766780cd3523122"),
                        "ProductID" : 1,
                        "ProductName" : "Chai",
                        "CategoryID" : 1,
                        "UnitPrice" : 18,
                        "UnitsInStock" : 39
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523123"),
                        "ProductID" : 2,
                        "ProductName" : "Chang",
                        "CategoryID" : 1,
                        "UnitPrice" : 19,
                        "UnitsInStock" : 17
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523139"),
                        "ProductID" : 24,
                        "ProductName" : "Guaraná Fantástica",
                        "CategoryID" : 1,
                        "UnitPrice" : 4.5,
                        "UnitsInStock" : 20
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523143"),
                        "ProductID" : 34,
                        "ProductName" : "Sasquatch Ale",
                        "CategoryID" : 1,
                        "UnitPrice" : 14,
                        "UnitsInStock" : 111
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523144"),
                        "ProductID" : 35,
                        "ProductName" : "Steeleye Stout",
                        "CategoryID" : 1,
                        "UnitPrice" : 18,
                        "UnitsInStock" : 20
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523147"),
                        "ProductID" : 38,
                        "ProductName" : "Côte de Blaye",
                        "CategoryID" : 1,
                        "UnitPrice" : 263.5,
                        "UnitsInStock" : 17
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523148"),
                        "ProductID" : 39,
                        "ProductName" : "Chartreuse verte",
                        "CategoryID" : 1,
                        "UnitPrice" : 18,
                        "UnitsInStock" : 69
                },
                {
                        "_id" : ObjectId("5d4537924766780cd352314c"),
                        "ProductID" : 43,
                        "ProductName" : "Ipoh Coffee",
                        "CategoryID" : 1,
                        "UnitPrice" : 46,
                        "UnitsInStock" : 17
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523164"),
                        "ProductID" : 67,
                        "ProductName" : "Laughing Lumberjack Lager",
                        "CategoryID" : 1,
                        "UnitPrice" : 14,
                        "UnitsInStock" : 52
                },
                {
                        "_id" : ObjectId("5d4537924766780cd3523167"),
                        "ProductID" : 70,
                        "ProductName" : "Outback Lager",
                        "CategoryID" : 1,
                        "UnitPrice" : 15,
                        "UnitsInStock" : 15
                },
                {
                        "_id" : ObjectId("5d4537924766780cd352316c"),
                        "ProductID" : 75,
                        "ProductName" : "Rhönbräu Klosterbier",
                        "CategoryID" : 1,
                        "UnitPrice" : 7.75,
                        "UnitsInStock" : 125
                },
                {
                        "_id" : ObjectId("5d4537924766780cd352316d"),
                        "ProductID" : 76,
                        "ProductName" : "Lakkalikööri",
                        "CategoryID" : 1,
                        "UnitPrice" : 18,
                        "UnitsInStock" : 57
                }
        ]
}



*/