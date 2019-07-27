/*
1) show dbs : server içerisindeki yer alan db'leri gösterir.
2) use <database adı> : çalışmak istediğiniz db adını vermeniz yeterlidir. Not : Case Sensitive.
3) show collections : db içerisinde yer alan koleksiyonları teslim eder. (tables)

*/
//alt+z : wordwrap
//shift+alt+f : kodları düzenle
// db.Kisiler.insert()

[ // kisi koleksiyonu
    { //tablo - collection içerisinde yer alacak bir kayıt
        "firstname": "Ahmet",
        "lastname": "Aksu",
        "phones": [
            {
                "name": "mobil",
                "phone": "+905309691590"
            },
            {
                "name": "home",
                "phone": "+902129691590"
            }
        ]
    }
]

/*
TelefonRehberi db içerisinde yer alacak olan Kisiler tablosuna(collection)  veri ekleme

1.Adım => mongo
2.Adım => use TelefonRehberi
3.Adım =>

db.Kisiler.insert({ 
        "firstname" : "Ahmet",
        "lastname"  : "Aksu",
        "phones" : [
            {
                "name" : "mobil",
                "phone" :  "+905309691590"
            },
            {
                "name" : "home",
                "phone" :  "+902129691590"
            }
        ] 
    })


4.Adım => db.Kisiler.find() = tablo(collection) içerisinde yer alan kayıtları teslim eder.
5.Adım => db.Kisiler.find().pretty() = tablo(collection) içerisinde yer alan kayıtları düzenli bir şekilde teslim eder.

6.Adım => Tablo içerisine ek bir adım eklenmesi

db.Kisiler.insert({ 
        "firstname" : "Ahmet",
        "lastname"  : "Aksu",
        "emails" : [
            {
                "email" : "ahmet.aksu@bilgeadam.com"
            },
            {
                "email" : "ahmet.aksu@hotmail.com"
            },
            {
                "email" : "ahmet.aksu@gmail.com"
            }
        ],
        "phones" : [
            {
                "name" : "mobil",
                "phone" :  "+905309691590"
            },
            {
                "name" : "home",
                "phone" :  "+902129691590"
            }
        ] 
    })
*/

[
    { 
        "_id": ObjectId("5d3c2736107c521dedd16c75"), 
        "firstname": "Ahmet", 
        "lastname": "Aksu", 
        "phones": [
            { "name": "mobil", "phone": "+905309691590" },
            { "name": "home", "phone": "+902129691590" }
        ] 
    }
]

//--------------------------------------------------------------------------------------------

[
    {        
        "_id" : ObjectId("5d3c2736107c521dedd16c75"),
        "firstname" : "Ahmet",
        "lastname" : "Aksu",
        "phones" : [
                {
                        "name" : "mobil",
                        "phone" : "+905309691590"
                },
                {
                        "name" : "home",
                        "phone" : "+902129691590"
                }
        ]
},
{
        "_id" : ObjectId("5d3c2be4107c521dedd16c76"),
        "firstname" : "Ahmet",
        "lastname" : "Aksu",
        "emails" : [
                {
                        "email" : "ahmet.aksu@bilgeadam.com"
                },
                {
                        "email" : "ahmet.aksu@hotmail.com"
                },
                {
                        "email" : "ahmet.aksu@gmail.com"
                }
        ],
        "phones" : [
                {
                        "name" : "mobil",
                        "phone" : "+905309691590"
                },
                {
                        "name" : "home",
                        "phone" : "+902129691590"
                }
        ]
}
]