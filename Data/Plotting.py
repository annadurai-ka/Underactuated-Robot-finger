import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection

# Define file paths
file_path1 = r'C:\Users\kaviarasu\iCloudDrive\RMC\Project\Trace Path_fingertip.csv.csv'
file_path2 = r'C:\Users\kaviarasu\iCloudDrive\RMC\Project\Trace Path_DIP_joint.csv.csv'
file_path3 = r'C:\Users\kaviarasu\iCloudDrive\RMC\Project\Trace Path_PIP_joint.csv.csv'
# Load the data from each file
data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)
data3 = pd.read_csv(file_path3)

# Create a figure for plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot

# Plot the data from each file
ax.plot(data1['X'], data1['Y'], data1['Z'], label='Trajectory by finger tip', marker='o')
ax.plot(data2['X'], data2['Y'], data2['Z'], label='Trajectory by DIP joint', marker='^')
ax.plot(data3['X'], data3['Y'], data3['Z'], label='Trajectory by PIP joint', marker='s')

# Setting labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('The range of motion in 3D Trajectory')

# Show the legend
ax.legend()

# Show the plot
plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Assuming the path to your CSV file is correctly set up for your environment
# # Note: You might need to change the path to match your system and ensure Python can access the file
# data = pd.read_csv('C:/Users/kaviarasu/Downloads/Trace Path4.csv')  # Use forward slashes or raw string for the path

# fig, ax = plt.subplots(figsize=(10, 10))  # Create a figure and a single subplot

# # Plot X, Y, Z values against S.no on the same axis
# ax.plot(data['S.no'], data['X'], label='X', marker='o', linestyle='-')  # Added marker and linestyle for clarity
# ax.plot(data['S.no'], data['Y'], label='Y', marker='^', linestyle='-')  # Adjust these as per your preference
# ax.plot(data['S.no'], data['Z'], label='Z', marker='s', linestyle='-')  # Example: marker='s', linestyle='--'

# ax.set_ylabel('Values')  # Adjust ylabel to represent what X, Y, Z stand for
# ax.set_xlabel('S.no')  # Since S.no is being used as the X-axis
# ax.legend()

# plt.suptitle('X, Y, Z values vs S.no')  # Title to represent the plotted data
# plt.grid(True)
# plt.show()


# # import pandas as pd
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection

# # # Update the file path to match your file's location
# # file_path = r'C:\Users\kaviarasu\Downloads\Trace Path4.csv'  # Note the 'r' before the string to handle backslashes as raw string

# # # Load the data
# # data = pd.read_csv(file_path)

# # # Create a figure for plotting
# # fig = plt.figure(figsize=(10, 7))
# # ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot

# # # Plot the data
# # ax.plot(data['X'], data['Y'], data['Z'], label='XYZ Trajectory', marker='o')

# # ax.set_xlabel('X Label')
# # ax.set_ylabel('Y Label')
# # ax.set_zlabel('Z Label')
# # plt.title('The range of motion by Finger Tip in 3D Trajectory')

# # # Show the legend
# # ax.legend()

# # # Show the plot
# # plt.show()
