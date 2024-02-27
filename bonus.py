# Document
""" 
Single Responsibility Principle (SRP):
    Each class has a single responsibility:
        User class: Represents user data.
        Activity classes: Represent different types of activities and handle data collection.
        ActivityMonitor class: Manages observers and notifies them when new activity data is available.
        Display class: Displays activity data.

Open/Closed Principle (OCP):
    The ActivityMonitor class follows the Observer pattern, allowing new types of activities to be added without modifying existing classes. The addition of a new activity type requires creating a new subclass of Activity and implementing the collect_data method.

Liskov Substitution Principle (LSP):
    The Activity class and its subclasses adhere to the Observer pattern's contracts. Each subclass of Activity implements the collect_data method, ensuring compatibility with the notification mechanism in ActivityMonitor.

Interface Segregation Principle (ISP):
    Separate interfaces are defined for observers (Observer), subjects (Subject), and activities (Activity). This ensures that classes only depend on the interfaces they use, preventing them from being forced to implement methods they don't need.

Dependency Inversion Principle (DIP):
    Dependencies are injected into the ActivityMonitor class, promoting loose coupling and easier testing. This allows different implementations of observers to be easily swapped without modifying the ActivityMonitor class.

 """


from abc import ABC, abstractmethod
from typing import List


# Interface for observers
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Concrete subject
class ActivityMonitor(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._data = {}

    def attach(self, observer: Observer):
        #Attach an observer to the subject.
        self._observers.append(observer)

    def detach(self, observer: Observer):
        #Detach an observer from the subject.
        self._observers.remove(observer)

    def notify(self):
        #Notify all attached observers.
        for observer in self._observers:
            observer.update(self._data)

    def track_activity(self, activity_data):
        #Track user activity and notify observers.
        self._data = activity_data
        self.notify()


# Concrete observer
class Display(Observer):
    def update(self, data):
        #Update method called by the subject.
        print("Displaying activity data:", data)


# Separate class for user data
class User:
    def __init__(self, user_id, name):
        #Initialize user data.
        self.user_id = user_id
        self.name = name


# Interface for activity
class Activity(ABC):
    @abstractmethod
    def collect_data(self):
        pass


# Concrete activity class
class Walking(Activity):
    def collect_data(self):
        #Collect data for walking activity.
        return {"activity": "Walking", "steps": 5000, "distance": 2.5, "calories": 200}


# Client code
def main():
    # Create instances of classes
    activity_monitor = ActivityMonitor()
    display = Display()

    # Attach observer
    activity_monitor.attach(display)

    # Simulate activity tracking
    walking_activity = Walking()
    activity_data = walking_activity.collect_data()
    activity_monitor.track_activity(activity_data)


if __name__ == "__main__":
    main()
