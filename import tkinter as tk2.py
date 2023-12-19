import tkinter as tk

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def sort_button_clicked():
    input_str = input_entry.get()
    input_list = list(map(int, input_str.split()))
    
    sorted_list = merge_sort(input_list)
    
    output_str = ' '.join(map(str, sorted_list))
    output_label.config(text=output_str)

# Create the main window
window = tk.Tk()
window.title("Merge Sort")
window.geometry("400x300")
window.configure(bg="#f2f2f2")

# Create the input label and entry
input_label = tk.Label(window, text="Enter space-separated integers:", bg="#f2f2f2", fg="#333333", font=("Arial", 12))
input_label.pack(pady=10)

input_entry = tk.Entry(window, font=("Arial", 12))
input_entry.pack()

# Create the sort button
sort_button = tk.Button(window, text="Sort", command=sort_button_clicked, bg="#333333", fg="#ffffff", font=("Arial", 12))
sort_button.pack(pady=10)

# Create the output label
output_label = tk.Label(window, text="", bg="#f2f2f2", fg="#333333", font=("Arial", 12))
output_label.pack(pady=10)

# Start the main event loop
window.mainloop()
