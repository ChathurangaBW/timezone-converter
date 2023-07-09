import tkinter as tk
from datetime import datetime
import pytz


def copy_to_clipboard(result):
    window.clipboard_clear()
    window.clipboard_append(result)


def convert_timezones():
    # Get the input datetime string from the entry widget
    input_datetime_str = entry.get()

    try:
        # Convert the input string to a datetime object
        input_datetime = datetime.strptime(input_datetime_str, "%d-%b-%Y %H:%M:%S")

        # Convert input datetime to UTC
        utc_datetime = pytz.utc.localize(input_datetime)

        # Convert UTC to PST
        pst_timezone = pytz.timezone('US/Pacific')
        pst_datetime = utc_datetime.astimezone(pst_timezone)
        pst_datetime_str = pst_datetime.strftime("%d-%b-%Y %H:%M:%S")

        # Convert UTC to IST
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_datetime = utc_datetime.astimezone(ist_timezone)
        ist_datetime_str = ist_datetime.strftime("%d-%b-%Y %H:%M:%S")

        # Convert UTC to AEST
        aest_timezone = pytz.timezone('Australia/Sydney')
        aest_datetime = utc_datetime.astimezone(aest_timezone)
        aest_datetime_str = aest_datetime.strftime("%d-%b-%Y %H:%M:%S")

        # Display the results in the label widget
        result_label.config(text=f"PST: {pst_datetime_str}\nIST: {ist_datetime_str}\nAEST: {aest_datetime_str}")

        # Enable copying each result individually
        pst_copy_button.config(state=tk.NORMAL)
        ist_copy_button.config(state=tk.NORMAL)
        aest_copy_button.config(state=tk.NORMAL)

        # Set the command for each copy button
        pst_copy_button.config(command=lambda: copy_to_clipboard(pst_datetime_str))
        ist_copy_button.config(command=lambda: copy_to_clipboard(ist_datetime_str))
        aest_copy_button.config(command=lambda: copy_to_clipboard(aest_datetime_str))

    except ValueError:
        result_label.config(text="Invalid input format!")


# Create the main application window
window = tk.Tk()
window.title("Time Zone Converter")
window.geometry("400x180")
window.attributes("-topmost", True)  # Set the window to always be on top
# Create a frame for the input section
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create a label for the input prompt
prompt_label = tk.Label(input_frame, text="Enter UTC datetime (d-Mon-yyyy H:M:S):")
prompt_label.pack(side=tk.LEFT)

# Create an entry widget for the user to enter the datetime
entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT)

# Create a button to initiate the conversion
convert_button = tk.Button(window, text="Convert", command=convert_timezones)
convert_button.pack(pady=10)

# Create a label to display the converted datetimes
result_label = tk.Label(window, text="")
result_label.pack()

# Create a frame for the copy buttons
copy_frame = tk.Frame(window)
copy_frame.pack(pady=10)

# Create copy buttons for each result
pst_copy_button = tk.Button(copy_frame, text="PST", state=tk.DISABLED)
pst_copy_button.pack(side=tk.LEFT, padx=5)
ist_copy_button = tk.Button(copy_frame, text="IST", state=tk.DISABLED)
ist_copy_button.pack(side=tk.LEFT, padx=5)
aest_copy_button = tk.Button(copy_frame, text="AEST", state=tk.DISABLED)
aest_copy_button.pack(side=tk.LEFT, padx=5)

# Start the application event loop
window.mainloop()
