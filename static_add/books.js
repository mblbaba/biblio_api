const books = [
    {
      "name": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "release_date": "1960-07-11",
      "editor": "J.B. Lippincott & Co.",
      "language": "English",
      "genre": "Novel",
      "resume": "To Kill a Mockingbird is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.",
      "page_number": 281,
      "loans_count": 25,
      "banner": "/assets/images/books/1.webp",
      "rate_count": 345,
      "created_by_id": 1,
      "categories": [1, 3],
      "tags": ["Social Issues", "Legal Drama"]
    },
    {
      "name": "1984",
      "author": "George Orwell",
      "release_date": "1949-06-08",
      "editor": "Secker & Warburg",
      "language": "English",
      "genre": "Dystopian",
      "resume": "1984 is a dystopian novel by George Orwell published in 1949. The story takes place in a totalitarian society where the government, led by Big Brother, exercises total control over the lives of its citizens.",
      "page_number": 328,
      "loans_count": 30,
      "banner": "/assets/images/books/2.png",
      "rate_count": 289,
      "created_by_id": 1,
      "categories": [2, 5],
      "tags": ["Totalitarianism", "Surveillance"]
    },
    {
      "name": "Pride and Prejudice",
      "author": "Jane Austen",
      "release_date": "1813-01-28",
      "editor": "T. Egerton, Whitehall",
      "language": "English",
      "genre": "Romance",
      "resume": "Pride and Prejudice is a romantic novel by Jane Austen, first published in 1813. The story follows the main character, Elizabeth Bennet, as she navigates issues of manners, morality, and marriage in the society of the landed gentry of early 19th-century England.",
      "page_number": 279,
      "loans_count": 20,
      "banner": "/assets/images/books/3.jpg",
      "rate_count": 412,
      "created_by_id": 1,
      "categories": [1, 5],
      "tags": ["Regency Era", "Social Commentary"]
    },
    {
      "name": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "release_date": "1925-04-10",
      "editor": "Charles Scribner's Sons",
      "language": "English",
      "genre": "Novel",
      "resume": "The Great Gatsby is a novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the1l towns of West Egg and East Egg on prosperous Long Island in the summer of 1922.",
      "page_number": 180,
      "loans_count": 15,
      "banner": "/assets/images/books/4.jpg",
      "rate_count": 372,
      "created_by_id": 1,
      "categories": [1, 7],
      "tags": ["Jazz Age", "American Dream"]
    },
    {
      "name": "Harry Potter and the Philosopher's Stone",
      "author": "J.K. Rowling",
      "release_date": "1997-06-26",
      "editor": "Bloomsbury",
      "language": "English",
      "genre": "Fantasy",
      "resume": "Harry Potter and the Philosopher's Stone is a fantasy novel by British author J.K. Rowling, first published in 1997. It follows the journey of young wizard Harry Potter and his friends Hermione Granger and Ron Weasley as they attend Hogwarts School of Witchcraft and Wizardry.",
      "page_number": 223,
      "loans_count": 50,
      "banner": "/assets/images/books/5.jpg",
      "rate_count": 520,
      "created_by_id": 1,
      "categories": [1, 2],
      "tags": ["Magic", "Coming of Age"]
    },
    {
      "name": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "release_date": "1951-07-16",
      "editor": "Little, Brown and Company",
      "language": "English",
      "genre": "Novel",
      "resume": "The Catcher in the Rye is a novel by J.D. Salinger, first published in 1951. It follows Holden Caulfield, a teenager who has been expelled from prep school and goes on a journey through New York City.",
      "page_number": 277,
      "loans_count": 18,
      "banner": "/assets/images/books/6.jpg",
      "rate_count": 298,
      "created_by_id": 1,
      "categories": [1, 4],
      "tags": [8, "Teenage Angst"]
    },
    {
      "name": "The Lord of the Rings",
      "author": "J.R.R. Tolkien",
      "release_date": "1954-07-29",
      "editor": "Allen & Unwin",
      "language": "English",
      "genre": "Fantasy",
      "resume": "The Lord of the Rings is an epic fantasy novel by J.R.R. Tolkien, published in three volumes from 1954 to 1955. It follows the quest undertaken by the hobbit Frodo Baggins and his companions to destroy the One Ring and defeat the Dark Lord Sauron.",
      "page_number": 1178,
      "loans_count": 40,
      "banner": "/assets/images/books/7.jpg",
      "rate_count": 480,
      "created_by_id": 1,
      "categories": [1, 7],
      "tags": [2, "Quest"]
    },
    {
      "name": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "release_date": "1937-09-21",
      "editor": "George Allen & Unwin",
      "language": "English",
      "genre": "Fantasy",
      "resume": "The Hobbit, or There and Back Again is a children's fantasy novel by J.R.R. Tolkien, published in 1937. It follows the journey of Bilbo Baggins, a hobbit who is swept into an epic quest to reclaim the lost Dwarf Kingdom of Erebor from the fearsome dragon Smaug.",
      "page_number": 310,
      "loans_count": 35,
      "banner": "/assets/images/books/8.jpg",
      "rate_count": 390,
      "created_by_id": 1,
      "categories": [1, 9],
      "tags": [2, "Quest"]
    },
    {
      "name": "Moby-Dick",
      "author": "Herman Melville",
      "release_date": "1851-10-18",
      "editor": "Richard Bentley",
      "language": "English",
      "genre": "Novel",
      "resume": "Moby-Dick; or, The Whale is an epic novel by Herman Melville, published in 1851. The story follows the narrator Ishmael's journey aboard the whaling ship Pequod, commanded by the monomaniacal Captain Ahab, who is in pursuit of the giant white sperm whale known as Moby Dick.",
      "page_number": 635,
      "loans_count": 12,
      "banner": "/assets/images/books/9.jpg",
      "rate_count": 255,
      "created_by_id": 1,
      "categories": [1, 2],
      "tags": ["Whaling", "Obsession"]
    },
    {
      "name": "The Odyssey",
      "author": "Homer",
      "release_date": "8th century BCE",
      "editor": "Various",
      "language": "Ancient Greek",
      "genre": "Epic Poetry",
      "resume": "The Odyssey is one of two major ancient Greek epic poems attributed to Homer. It is, in part, a sequel to the Iliad, the other Homeric epic. The poem mainly centers on the Greek hero Odysseus (or Ulysses, as he was known in Roman myths) and his long journey home to Ithaca following the fall of Troy.",
      "page_number": null,
      "loans_count": 10,
      "banner": "/assets/images/books/10.jpeg",
      "rate_count": 200,
      "created_by_id": 1,
      "categories": [7, 5],
      "tags": ["Mythology", "Hero's Journey"]
    },
    {
        "name": "Don Quixote",
        "author": "Miguel de Cervantes",
        "release_date": "1605-01-16",
        "editor": "Francisco de Robles",
        "language": "Spanish",
        "genre": "Novel",
        "resume": "Don Quixote is a novel by Miguel de Cervantes, published in two parts in 1605 and 1615. It follows the adventures of Alonso Quixano, a hidalgo who reads so many chivalric romances that he decides to set out to revive chivalry, under the name Don Quixote.",
        "page_number": 863,
        "loans_count": 22,
        "banner" : "/assets/images/books/11.jpg",
        "rate_count": 320,
        "created_by_id": 1,
        "categories": ["Fiction", "Satire"],
        "tags": ["Chivalry", "Madness"]
      },
      {
        "name": "War and Peace",
        "author": "Leo Tolstoy",
        "release_date": "1869-01-01",
        "editor": "The Russian Messenger",
        "language": "Russian",
        "genre": "Historical Fiction",
        "resume": "War and Peace is a novel by the Russian author Leo Tolstoy, published serially in 1865–69. It depicts the French invasion of Russia and the impact of the Napoleonic era on Tsarist society through the stories of five Russian aristocratic families.",
        "page_number": 1225,
        "loans_count": 28,
        "banner" : "/assets/images/books/12.jpg",
        "rate_count": 410,
        "created_by_id": 1,
        "categories": ["Fiction", "Historical Novel"],
        "tags": ["Napoleonic Wars", "Russian Society"]
      },
      {
        "name": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "release_date": "1866-12-22",
        "editor": "The Russian Messenger",
        "language": "Russian",
        "genre": "Psychological Fiction",
        "resume": "Crime and Punishment is a novel by the Russian author Fyodor Dostoevsky, first published in 1866. It is the story of Rodion Raskolnikov, an impoverished ex-student in St. Petersburg who formulates a plan to kill an unscrupulous pawnbroker for her money.",
        "page_number": 551,
        "loans_count": 18,
        "banner" : "/assets/images/books/13.png",
        "rate_count": 365,
        "created_by_id": 1,
        "categories": ["Fiction", "Psychological Novel"],
        "tags": ["Guilt", "Redemption"]
      },
      {
        "name": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "release_date": "1880-11-26",
        "editor": "The Russian Messenger",
        "language": "Russian",
        "genre": "Philosophical Novel",
        "resume": "The Brothers Karamazov is a novel by Fyodor Dostoevsky, published in 1880. It is the final novel of the author and is considered one of the greatest literary works ever written. The novel explores questions of faith, reason, and morality through the story of the Karamazov family.",
        "page_number": 796,
        "loans_count": 15,
        "banner" : "/assets/images/books/14.jpg",
        "rate_count": 290,
        "created_by_id": 1,
        "categories": ["Fiction", "Philosophical Fiction"],
        "tags": ["Family Drama", "Religious Themes"]
      },
      {
        "name": "Les Misérables",
        "author": "Victor Hugo",
        "release_date": "1862-03-15",
        "editor": "A. Lacroix, Verboeckhoven & Cie.",
        "language": "French",
        "genre": "Historical Novel",
        "resume": "Les Misérables is a French historical novel by Victor Hugo, first published in 1862. It follows the lives and interactions of several characters, focusing on the struggles of ex-convict Jean Valjean and his experience of redemption.",
        "page_number": 1463,
        "loans_count": 35,
        "banner" : "/assets/images/books/15.jpg",
        "rate_count": 480,
        "created_by_id": 1,
        "categories": ["Fiction", "Historical Fiction"],
        "tags": ["Redemption", "French Revolution"]
      },
      {
        "name": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "release_date": "1890-07-20",
        "editor": "Lippincott's Monthly Magazine",
        "language": "English",
        "genre": "Gothic Fiction",
        "resume": "The Picture of Dorian Gray is a Gothic and philosophical novel by Oscar Wilde, first published complete in the July 1890 issue of Lippincott's Monthly Magazine. The story is about a young man named Dorian Gray, the subject of a painting by artist Basil Hallward, who becomes obsessed with his own youth and beauty and wishes to sell his soul to ensure that the portrait ages and he remains young and handsome.",
        "page_number": 254,
        "loans_count": 20,
        "banner" : "/assets/images/books/16.jpg",
        "rate_count": 360,
        "created_by_id": 1,
        "categories": ["Fiction", "Gothic Literature"],
        "tags": ["Aestheticism", "Moral Decay"]
      },
      {
        "name": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "release_date": "1967-05-30",
        "editor": "Editorial Sudamericana",
        "language": "Spanish",
        "genre": "Magical Realism",
        "resume": "One Hundred Years of Solitude is a landmark 1967 novel by Colombian author Gabriel García Márquez that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio Buendía, founds the town of Macondo, a fictitious town in the country of Colombia.",
        "page_number": 417,
        "loans_count": 25,
        "banner" : "/assets/images/books/17.jpg",
        "rate_count": 400,
        "created_by_id": 1,
        "categories": ["Fiction", "Magical Realism"],
        "tags": ["Latin American Literature", "Family Saga"]
      },
      {
        "name": "Anna Karenina",
        "author": "Leo Tolstoy",
        "release_date": "1877-01-28",
        "editor": "The Russian Messenger",
        "language": "Russian",
        "genre": "Realist Fiction",
        "resume": "Anna Karenina is a novel by the Russian author Leo Tolstoy, first published in book form in 1878. Widely regarded as a pinnacle in realist fiction, Anna Karenina recounts St. Petersburg aristocrat Anna Karenina's ill-fated affair with the affluent Count Vronsky.",
        "page_number": 964,
        "loans_count": 30,
        "banner" : "/assets/images/books/18.webp",
        "rate_count": 450,
        "created_by_id": 1,
        "categories": ["Fiction", "Realist Fiction"],
        "tags": ["Adultery", "Russian Society"]
      },
      {
        "name": "The Divine Comedy",
        "author": "Dante Alighieri",
        "release_date": "14th century",
        "editor": "Various",
        "language": "Italian",
        "genre": "Epic Poetry",
        "resume": "The Divine Comedy is a long Italian narrative poem by Dante Alighieri, begun c. 1308 and completed in 1320, a year before his death in 1321. It is widely considered to be the preeminent work in Italian literature and one of the greatest works of world literature.",
        "page_number": null,
        "loans_count": 15,
        "banner" : "/assets/images/books/19.jpg",
        "rate_count": 320,
        "created_by_id": 1,
        "categories": ["Poetry", "Epic Poetry"],
        "tags": ["Allegory", "Christian Theology"]
      },
      {
        "name": "Frankenstein; or, The Modern Prometheus",
        "author": "Mary Shelley",
        "release_date": "1818-01-01",
        "editor": "Lackington, Hughes, Harding, Mavor, & Jones",
        "language": "English",
        "genre": "Gothic Fiction",
        "resume": "Frankenstein; or, The Modern Prometheus is a novel written by English author Mary Shelley that tells the story of Victor Frankenstein, a young scientist who creates a sapient creature in an unorthodox scientific experiment.",
        "page_number": 280,
        "loans_count": 25,
        "banner" : "/assets/images/books/20.jpg",
        "rate_count": 380,
        "created_by_id": 1,
        "categories": ["Fiction", "Gothic Literature"],
        "tags": ["Science Fiction", "Morality"]
      }
  ]
  


  const add_books =async (books) =>{ 
    for(const book of books){
        try{
            const response = await fetch("http://127.0.0.1:5000/books/add", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(book)
            }
            )
            if (!response.ok) {
                throw new Error(`Failed to add book ${book.name}`);
            }
            console.log(`Book ${book.name} added successfully.`);
            
        }
        catch(err){
        console.log(err)
    }
}
  } 

add_books(books)