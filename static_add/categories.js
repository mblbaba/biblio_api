async function addCategories(categories) {
    for (const category of categories) {
      try {
        const response = await fetch('http://127.0.0.1:5000/categories/add', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(category)
        });
        // console.log(response);
        
        if (!response.ok) {
          throw new Error(`Failed to add category ${category.name}`);
        }
  
        console.log(`Category ${category.name} added successfully.`);
      } catch (error) {
        console.error(error.message);
      }
    }
  }


  const categories = [
    { id: 1, name: "Science-fiction", created_by_id: 1 },
    { id: 2, name: "Policier", created_by_id: 1 },
    { id: 3, name: "Thriller", created_by_id: 1 },
    { id: 4, name: "Horreur", created_by_id: 1 },
    { id: 5, name: "Mystère", created_by_id: 1 },
    { id: 6, name: "Aventure", created_by_id: 1 },
    { id: 7, name: "Poésie", created_by_id: 1 },
    { id: 8, name: "Théâtre", created_by_id: 1 },
    { id: 9, name: "Biographie", created_by_id: 1 },
    { id: 10, name: "Autobiographie", created_by_id: 1 },
    { id: 11, name: "Fantastique", created_by_id: 1 },
    { id: 12, name: "Conte", created_by_id: 1 },
    { id: 13, name: "Mythologie", created_by_id: 1 },
    { id: 14, name: "Documentaire", created_by_id: 1 },
    { id: 15, name: "Essai", created_by_id: 1 },
    { id: 16, name: "Art", created_by_id: 1 },
    { id: 17, name: "Cuisine", created_by_id: 1 },
    { id: 18, name: "Santé", created_by_id: 1 },
    { id: 19, name: "Bien-être", created_by_id: 1 },
    { id: 20, name: "Spiritualité", created_by_id: 1 },
    { id: 21, name: "Voyage", created_by_id: 1 },
    { id: 22, name: "Histoire", created_by_id: 1 },
    { id: 23, name: "Politique", created_by_id: 1 },
    { id: 24, name: "Philosophie", created_by_id: 1 },
    { id: 25, name: "Éducation", created_by_id: 1 },
    { id: 26, name: "Langues", created_by_id: 1 },
    { id: 27, name: "Loisirs", created_by_id: 1 },
    { id: 28, name: "Humour", created_by_id: 1 },
    { id: 29, name: "Mode", created_by_id: 1 },
    { id: 30, name: "Finance", created_by_id: 1 },
    { id: 31, name: "Roman d'amour", created_by_id: 1 },
    { id: 32, name: "Roman historique", created_by_id: 1 },
    { id: 33, name: "Roman de fantasy", created_by_id: 1 },
    { id: 34, name: "Roman graphique", created_by_id: 1 },
    { id: 35, name: "Littérature jeunesse", created_by_id: 1 },
    { id: 36, name: "Roman érotique", created_by_id: 1 },
    { id: 37, name: "Roman épistolaire", created_by_id: 1 },
    { id: 38, name: "Roman policier historique", created_by_id: 1 },
    { id: 39, name: "Roman psychologique", created_by_id: 1 },
    { id: 40, name: "Roman initiatique", created_by_id: 1 }
];


  
  addCategories(categories);