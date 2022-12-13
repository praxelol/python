import tkinter as tk
import RealSRGAN

# Load the model weights
model = RealSRGAN.load_model("model_weights.h5")

# Create the main window
root = tk.Tk()
root.title("RealSRGAN Upscale")

# Create the input and output labels
input_label = tk.Label(root, text="Input:")
input_label.grid(row=0, column=0)
output_label = tk.Label(root, text="Output:")
output_label.grid(row=1, column=0)

# Create the input and output fields
input_field = tk.Entry(root)
input_field.grid(row=0, column=1)
output_field = tk.Entry(root)
output_field.grid(row=1, column=1)

# Create the "Upscale" button
button = tk.Button(root, text="Upscale", command=upscale)
button.grid(row=2, column=0, columnspan=2)

# Define the "upscale" function
def upscale():
    # Get the input and output filenames
    input_filename = input_field.get()
    output_filename = output_field.get()

    # Upscale the photo
    upscaled_photo = RealSRGAN.upscale(input_filename)

    # Save the upscaled photo
    upscaled_photo.save(output_filename)

# Run the main loop
root.mainloop()
