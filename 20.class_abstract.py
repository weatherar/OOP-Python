# abstract class
# class biasa instancenya adalah object
# class abstrak instancenya adalah class

# abc adalah abstrac base class
from abc import ABC,abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass
        
class PushButton(Button):
    def click(self):
        print('Push button clicked')
    
        
class RadioButton(Button):
    def click(self):
        print('Radio button clicked')
        
tombol1 = PushButton()
tombol2 = RadioButton()


tombol2.click()
tombol1.click() 
# Output: Push button clicked
help