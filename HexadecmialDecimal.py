import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):

    def build(self):
        layout = GridLayout(cols=2)

        #Hex converts to Dec
        DecButton = Button(text = "Convert to HexaDecimal")
        DecButton.bind(on_press = self.hexnum)

        self.HexNum = TextInput(text = "", multiline = False)

        self.DecResult = Label(text = "")

        #Dec converts to Hex

        HexButton = Button(text = "Convert to Decimal")
        HexButton.bind(on_press = self.decnum)

        self.DecNum = TextInput(text = "", multiline = False)


        self.HexResult = Label(text = "")


        #layouts
        layout.add_widget(self.HexNum)
        layout.add_widget(self.DecNum)

        layout.add_widget(HexButton)
        layout.add_widget(DecButton)


        layout.add_widget(self.DecResult)
        layout.add_widget(self.HexResult)


        return layout


    def hexnum(self,btn):
        try:

            HexNum = ""

            decNum = self.DecNum.text

            decNum = int(decNum)

            Done = False

            while Done == False:

                Division = decNum/16
                WholeNum = int(Division)
                UseNum = Division - WholeNum
                Remainder = UseNum % 16
                Result = Remainder * 16
                Result = int(Result)

                decNum = Division

                digit = str(Result)

                digits = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8",
                      "9": "9", "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

                if digit in digits:
                    Hexdec = digits.get(digit)
                    HexNum += str(Hexdec)


                if int(Division) == 0:
                    Done = True
                    HexNum = str(HexNum)
                    self.HexResult.text = HexNum[::-1]

        except ValueError:
            self.HexResult.text = "input error"



    def decnum(self,btn):

        try:

            hexNum = str(self.HexNum.text)

            decNum = 0
            power = 0

            for digit in range(len(hexNum), 0, -1):  # calculates for hex to dec
                decNum = decNum + 16 ** power * getDecDigit(hexNum[digit - 1])
                power += 1
            self.DecResult.text = str(decNum)

        except TypeError:
            self.DecResult.text = "input error"

def getDecDigit(digit):

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', "8", "9", "A", "B", "C", "D", "E", "F"]  # digit list

    for x in range(len(digits)):
        if digit == digits[x]:
            return x  # Returns the index in the list





if __name__ == "__main__":
    MyApp().run()