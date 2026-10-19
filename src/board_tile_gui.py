from tkinter import CENTER, Frame, Label, StringVar


class BoardTileGUI(Frame):
    def __init__ (self, row: int, col: int, font_s: int,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._row = row
        self._col = col
        self._value = StringVar(value="")
        self._label = Label(self, textvariable=self._value)
        self._label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self._label.configure(font=('Arial', font_s), bg='white')

    def get_row(self) -> int:
        return self._row

    def get_col(self) -> int:
        return self._col

    def set_text(self, new_text:str="") -> None:
        self._value.set(new_text)
