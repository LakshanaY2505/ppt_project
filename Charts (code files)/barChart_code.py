# This code is to generate the bar chart that is shown slide5:Problem 

import matplotlib.pyplot as plt

#Data to be used
platforms=["Grooveshark","Spotify","Apple Music"]
fees=[0,2000000000,500000000]

plt.figure(figsize=(8,6))

plt.bar(platforms,fees,color=["orange","#E85D04","#BC3908"])
plt.title("Licensing Fees Paid by Music Streaming Platforms (2014 est.)")

#Increasing the gap between the title and axis
plt.xlabel("Platform", labelpad=15)
plt.ylabel("Licensing Fees (in USD)", labelpad=15)

#Get Current Axes, get_yaxis is used to get the Y-axis object of the current axes
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'${x/1e9:.1f}B') #Converts the number into billions and formats it
)

#x = the tick value (Platform)
#_ = the tick position (often unused)

plt.savefig("licensingFees.png")
plt.show()