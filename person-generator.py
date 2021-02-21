import pandas
import csv
from tkinter import *
import random
import sys

# If no file was specified, then pull up GUI
if len(sys.argv) == 1:
    # Set the state options for GUI to display
    OPTIONS = [
        'ak',
        'az',
        'ca',
        'co',
        'hi',
        'id',
        'mt',
        'nm',
        'nv',
        'or',
        'ut',
        'wa',
        'wy'
    ]

    window = Tk()

    # Create/display options menu
    pick_state_label = Label(window, text='Pick a State')
    pick_state_label.pack(side=TOP)
    state = StringVar(window)
    state.set(OPTIONS[0])
    menu = OptionMenu(window, state, *OPTIONS)
    menu.pack()

    # Create/display box for number of addresses to generate
    num_addresses_label = Label(window, text='Number of Addresses to Generate')
    num_addresses_label.pack(side=TOP)
    num_addresses = Entry(window, bd=5)
    num_addresses.pack(side=TOP)


    def display():
        """
        This function will pop up a Tkinter window to display the output of the
        number of addresses that the user specifies
        """
        newWindow = Tk()

        # Open the output file that was just generated
        with open('output.csv', newline='') as file:
            output = csv.reader(file)
            # Display each row of output.csv
            r = 0
            for col in output:
                c = 0
                for row in col:
                    label = Label(newWindow, text=row)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        newWindow.mainloop()


    def generate():
        """
        This function will get a state and number of addresses to generate from the
        user, create a csv file and call the display function to show the output
        :return:
        """
        # Get state and number to generate from user
        state_choice = state.get()
        state_choice += '.csv'
        # Set fields i.e. column names
        fields = ['NUMBER', 'STREET', 'CITY', 'POSTCODE']
        num = int(num_addresses.get())
        # Read the data
        df = pandas.read_csv(state_choice, usecols=fields)
        # Generate first row of output
        row = random.randint(1, 10000)
        output = pandas.DataFrame(
            [[state.get(), str(num), 'Street Address',
              str(df['NUMBER'][1]) + ' ' +
              str(df['STREET'][row]) + ' ' + str(df['CITY'][row]) + ' ' + str(
                  df['POSTCODE'][row])]],
            columns=['State', 'Number to Generate', 'Type', 'Value'])
        output.to_csv('output.csv', index=False)
        # Append the rest of the rows based on number specified by user
        for i in range(2, num + 1):
            row = random.randint(1, 10000)
            output = pandas.DataFrame(
                [[state.get(), str(num), 'Street Address',
                  str(df['NUMBER'][row]) + ' ' +
                  str(df['STREET'][row]) + ' ' + str(
                      df['CITY'][row]) + ' ' + str(
                      df['POSTCODE'][row])]],
                columns=['State', 'Number to Generate', 'Type', 'Value'])
            output.to_csv('output.csv', mode='a', header=False, index=False)
        display()


    button = Button(window, text='Generate', command=generate)
    button.pack()

    mainloop()

# If a file was given, then open that file and generate csv data
else:
    # Read input file
    df = pandas.read_csv(sys.argv[1])
    # Get state and number to generate from input file
    state_choice = df['input_state'][0]
    save_state = df['input_state'][0]
    state_choice += '.csv'
    # Set fields i.e. column names
    fields = ['NUMBER', 'STREET', 'CITY', 'POSTCODE']
    num = df['input_number_to_generate'][0]
    # Read the data
    df = pandas.read_csv(state_choice, usecols=fields)
    # Generate first row of output
    row = random.randint(1, 10000)
    output = pandas.DataFrame(
        [[save_state, str(num), 'Street Address', str(df['NUMBER'][1]) + ' ' +
          str(df['STREET'][row]) + ' ' + str(df['CITY'][row]) + ' ' + str(
            df['POSTCODE'][row])]],
        columns=['State', 'Number to Generate', 'Type', 'Value'])
    output.to_csv('output.csv', index=False)
    # Append the rest of the rows based on number specified by user
    for i in range(2, num + 1):
        row = random.randint(1, 10000)
        output = pandas.DataFrame(
            [[save_state, str(num), 'Street Address',
              str(df['NUMBER'][row]) + ' ' +
              str(df['STREET'][row]) + ' ' + str(df['CITY'][row]) + ' ' + str(
                  df['POSTCODE'][row])]],
            columns=['State', 'Number to Generate', 'Type', 'Value'])
        output.to_csv('output.csv', mode='a', header=False, index=False)
