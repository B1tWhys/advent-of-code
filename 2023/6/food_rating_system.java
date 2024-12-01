class Food implements Comparable<Food> {
    String name;
    String cuisine;
    Integer rating;

    public Food(String name, String cuisine, Integer rating) {
        this.name = name;
        this.cuisine = cuisine;
        this.rating = rating;
    }

    public int compareTo(Food other) {
        int result = rating.compareTo(other.rating);
        if (result == 0) {
            result = -name.compareTo(other.name);
        }
        return result;
    }
}

class FoodRatings {
    private Map<String, List<Food>> cuisines = new HashMap<>();
    private Map<String, Food> foods = new HashMap<>();

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (String cuisine : cuisines) {
            this.cuisines.putIfAbsent(cuisine, new ArrayList<>());
        }

        for (int i = 0; i < foods.length; i++) {
            Food food = new Food(foods[i], cuisines[i], ratings[i]);
            this.cuisines.get(food.cuisine).add(food);
            this.foods.put(food.name, food);
        }

        for (List<Food> foodList : this.cuisines.values()) {
            foodList.sort(null);
        }
    }
    
    public void changeRating(String foodName, int newRating) {
        Food food = foods.get(foodName);
        if (food.rating == newRating) return;
        List<Food> cuisineList = cuisines.get(food.cuisine);
        
        int oldFoodIdx = Collections.binarySearch(cuisineList, food);
        assert oldFoodIdx >= 0;
        cuisineList.remove(oldFoodIdx);

        food.rating = newRating;
        int newIdx = Collections.binarySearch(cuisineList, food);
        assert newIdx < 0;
        cuisineList.add(-newIdx-1, food);
    }
    
    public String highestRated(String cuisine) {
        List<Food> cuisineList = cuisines.get(cuisine);
        return cuisineList.get(cuisineList.size()-1).name;
    }
}
