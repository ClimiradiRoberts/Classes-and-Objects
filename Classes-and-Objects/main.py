class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name (self, new_name):
        self.name = new_name
        print (f"Name has been changed to {new_name}")

    def change_age (self, new_age):
        try:
            new_age = int(new_age)
        except:
            print ("Age cannot be changed. Re-input a valid data type")
            return

        self.age = new_age
        print(f"Age has been changed to {new_age}")

    def add_track (self, new_track):
        self.tracks.append(new_track)
        print(f"Track has been changed to {new_track}")              

    def get_score(self):
        return self.score    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print (Bob.get_score())
