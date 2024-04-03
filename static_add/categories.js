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
        console.log(response);
        
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
    { name: "Fiction", created_by_id: 1 },
    { name: "Fantasy", created_by_id: 1 },
    { name: "Historical Fiction", created_by_id: 1 },
    { name: "Novel", created_by_id: 1 },
    { name: "Romance", created_by_id: 1 },
    { name: "Gothic Fiction", created_by_id: 1 },
    { name: "Psychological Fiction", created_by_id: 1 },
    { name: "Epic Poetry", created_by_id: 1 },
    { name: "Dystopian Fiction", created_by_id: 1 },
    { name: "Satire", created_by_id: 1 }
];

  
  addCategories(categories);