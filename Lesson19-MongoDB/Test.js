/*
db.users.insertMany([{ 
    "_id" : 1,
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
},
{ 
    "_id" :2,
    "firstname" : "Berke",
    "lastname"  : "Aksu",
    "emails" : [
        {
            "email" : "berke.aksu@bilgeadam.com"
        },
        {
            "email" : "berke.aksu@hotmail.com"
        },
        {
            "email" : "berke.aksu@gmail.com"
        }
    ],
    "phones" : [
        {
            "name" : "mobil",
            "phone" :  "+901309691590"
        },
        {
            "name" : "home",
            "phone" :  "+902169691590"
        }
    ] 
}])





db.movies.insertMany([{
    "_id" : 1,
    "title" : "Carmencita",
    "year" : 1894,
    "imdbId" : "tt0000001",
    "mpaaRating" : "NOT RATED",
    "genre" : "Documentary, Short",
    "viewerRating" : 5.9,
    "viewerVotes" : 1032,
    "runtime" : 1,
    "director" : "William K.L. Dickson",
    "cast" : [
            "Carmencita"
    ],
    "plot" : "Performing on what looks like a small wooden stage, wearing a dress with a hoop skirt and white high-heeled pumps, Carmencita does a dance with kicks and twirls, a smile always on her face."
},
{
    "_id" : 2,
    "title" : "Un bon bock",
    "year" : 1892,
    "imdbId" : "tt0000004",
    "genre" : "Animation, Short",
    "viewerRating" : 6.6,
    "viewerVotes" : 78,
    "director" : "èmile Reynaud"
},
{
    "_id" : 3,
    "title" : "Edison Kinetoscopic Record of a Sneeze",
    "year" : 1894,
    "imdbId" : "tt0000008",
    "genre" : "Documentary, Short",
    "viewerRating" : 5.9,
    "viewerVotes" : 988,
    "runtime" : 1,
    "director" : "William K.L. Dickson",
    "cast" : [
            "Fred Ott"
    ],
    "plot" : "A man (Thomas Edison's assistant) takes a pinch of snuff and sneezes. This is one of the earliest Thomas Edison films and was the first motion picture to be copyrighted in the United States."
},
{
    "_id" : 4,
    "title" : "Chinese Opium Den",
    "year" : 1894,
    "imdbId" : "tt0000006",
    "genre" : "Short",
    "viewerRating" : 6,
    "viewerVotes" : 56,
    "runtime" : 1,
    "director" : "William K.L. Dickson",
    "language" : "English"
},
{
    "_id" : 5,
    "title" : "Corbett and Courtney Before the Kinetograph",
    "year" : 1894,
    "imdbId" : "tt0000007",
    "mpaaRating" : "NOT RATED",
    "genre" : "Short, Sport",
    "viewerRating" : 5.5,
    "viewerVotes" : 390,
    "runtime" : 1,
    "director" : "William K.L. Dickson, William Heise",
    "cast" : [
            "James J. Corbett",
            "Peter Courtney"
    ],
    "plot" : "James J. Corbett and Peter Courtney meet in a boxing exhibition."
}])

*/