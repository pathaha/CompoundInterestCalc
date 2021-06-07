import tkinter as tk
from tkinter import font

import math
from decimal import Decimal

class MainApplication:
    def __init__(self, master):
        self.color_theme = {
            'app_background_color' : '#3498DB',
            'box_background_color' : '#87AFC7',
            'btn_background_color' : '#87AFC7',
            'error_background_color': '#3498DB',
            'highlight_background' : '#000000',
            'active_background' : '#595959',
            'text_color' : '#ffffff',
            'font_style_label' : font.Font(family = 'Times', size = 17),
            'font_style_entry' : font.Font(family = 'Times', size = 15)
        }

        self.master = master
        self.master.title('Compound Interest Calculator')
        self.master.geometry('500x370')
        self.master.resizable(False, False)
        self.master.configure(bg = self.color_theme['app_background_color'])

        self.ci_calculator_frame = tk.Frame(self.master)
        self.create_cic_frame(self.ci_calculator_frame, self.color_theme)

    def create_cic_frame(self, frame, color_theme):
        frame.config(bg = color_theme['app_background_color'])

        self.display_result = tk.Text(frame, state = 'disabled', height = 3, font = color_theme['font_style_label'], bg = color_theme['box_background_color'], fg = color_theme['text_color'], borderwidth = 0, highlightbackground = color_theme['highlight_background'])
        self.display_result.grid(row = 0, columnspan = 5)

        self.principal_label = tk.Label(frame, text = 'Principal: ', font = color_theme['font_style_label'], bg = color_theme['app_background_color'], fg = color_theme['text_color'])
        self.principal_label.grid(row = 1, pady = (40, 15))

        self.principal = tk.Entry(frame, justify = 'center', font = color_theme['font_style_entry'], bg = color_theme['box_background_color'], fg = color_theme['text_color'], borderwidth = 0, highlightbackground = color_theme['highlight_background'])
        self.principal.grid(row = 1, column = 1, pady = (40, 15))

        self.period_label = tk.Label(frame, text = 'Years: ', font = color_theme['font_style_label'], bg = color_theme['app_background_color'], fg = color_theme['text_color'])
        self.period_label.grid(row = 2, pady = 15)

        self.period = tk.Entry(frame, justify = 'center', font = color_theme['font_style_entry'], bg = color_theme['box_background_color'], fg = color_theme['text_color'], borderwidth = 0, highlightbackground = color_theme['highlight_background'])
        self.period.grid(row = 2, column = 1, pady = 15)

        self.interest_label = tk.Label(frame, text = 'Interest: %', font = color_theme['font_style_label'], bg = color_theme['app_background_color'], fg = color_theme['text_color'])
        self.interest_label.grid(row = 3, pady = 15)

        self.interest = tk.Entry(frame, justify = 'center', font = color_theme['font_style_entry'], bg = color_theme['box_background_color'], fg = color_theme['text_color'], borderwidth = 0, highlightbackground = color_theme['highlight_background'])
        self.interest.grid(row = 3, column = 1, pady = 15)

        self.calculate_button = tk.Button(frame, text = 'Calculate', font = color_theme['font_style_entry'], bg = color_theme['btn_background_color'], fg = color_theme['text_color'], borderwidth = 0, highlightbackground = color_theme['highlight_background'], activebackground = color_theme['active_background'], command = lambda: MainApplication.calculate_ci(self.principal, self.period, self.interest, self.display_result, color_theme))
        self.calculate_button.grid(row = 4, columnspan = 2, pady = (30, 0))

        frame.pack(expand = False)

    def calculate_ci(principal, period, interest, textbox, color_theme):
        try:
            error_occurred = False
            principal.config(highlightbackground = color_theme['highlight_background'])
            period.config(highlightbackground = color_theme['highlight_background'])
            interest.config(highlightbackground = color_theme['highlight_background'])

            p = tk.StringVar()
            p = principal.get()

            if not (MainApplication.__is_float(p) and p):
                principal.config(highlightbackground = color_theme['error_background_color'])
                error_occurred = True
            else:
                p = float(p)

            n = tk.StringVar()
            n = period.get()

            if not (MainApplication.__is_integer(n) and n):
                period.config(highlightbackground = color_theme['error_background_color'])
                error_occurred = True
            else:
                n = int(n)

            i = tk.StringVar()
            i = interest.get()

            if not (MainApplication.__is_float(i) and i):
                interest.config(highlightbackground = color_theme['error_background_color'])
                error_occurred = True
            else:
                i = float(i)

            if error_occurred:
                raise ValueError

            ci = p * (math.pow(1.0 + i / 100.0, n) - 1.0)
            ci = round(ci, 2)
            ci_str_result = 'Compound interest: ' + str(ci) + '\n'

            total_amount = p + ci
            total_amount_str_result = 'Total amount: ' + str(total_amount)

            result_message = ci_str_result + total_amount_str_result

            MainApplication.insert_textbox_message(textbox, result_message)
        except Exception as e:
            MainApplication.insert_textbox_message(textbox, '\nERROR: Invalid input')

    def insert_textbox_message(textbox, msg):
        textbox.config(state = 'normal')
        textbox.delete('1.0', tk.END)
        textbox.insert('1.0', msg)
        textbox.config(state = 'disabled')

    def __is_float(x):
        try:
            float(x)
            return True
        except:
            return False

    def __is_integer(x):
        try:
            int(x)
            return True
        except:
            return False

if __name__ == '__main__':
    app = tk.Tk()
    app_gui = MainApplication(app)
    app.mainloop()
