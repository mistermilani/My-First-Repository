import flet as ft
import random

def main(page: ft.Page):
    answer = ""
    #Functions
    def answers(e):
        nonlocal answer
        answers = ["Yes", "No", "Maybe", "Ask again later"]
        answer = random.choice(answers)
        textresult.value = answer

    #Main Page
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    input = ft.TextField(hint_text = "Ask the 8-Ball", on_submit = answers)
    textresult = ft.Text(value = (answer))
    page.add(input, textresult)
ft.run(main = main)