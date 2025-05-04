class Counter:
    count = 0 # Class variable to track number of instances
    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Total Counts: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  # Output: Count: 3