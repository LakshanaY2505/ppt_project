# This code is to generate the wordCloud picture that is shown slide7:A cloud of controversy

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Grooveshark legal action liability fine contract appeal litigation lawsuit settlement licensing songs violation copyright piracy shutdown music media users songs platform illegal streaming"

wordcloud=WordCloud(
    width=800,
    height=400,
    background_color="black", #Dark background for contrast
    colormap="Reds",    #Check colour
    max_font_size=100,  
    min_font_size=20,
    prefer_horizontal=1.0   #Used to keep the words horizontal
).generate(text)


# Display the WordCloud
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off") #Removes the axis

# Save the picture with a custom name
plt.savefig("wordcloud.png", dpi=300, bbox_inches="tight")  
plt.show()