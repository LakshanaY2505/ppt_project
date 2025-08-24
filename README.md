# GROOVESHARK

## DESCRIPTION

## FILE STRUCTURE




## REQUIRED MODULES
```
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from wordcloud import WordCloud
```
## INSTALLATION OF THE MODULES



## SLIDE 1 - INTRODUCTION
## SLIDE 2 - TIMELINE
## SLIDE 3 - ESTABLISHMENT AND GROWTH
## SLIDE 4 - PROBLEM
1. **Slide Layout**
  - Uses the **Two Titles and Content** layout (`slide_layouts[4]`).
  - Adds a main slide title: `"PROBLEM"`.
  - Adds two subtitles, and content placeholders.

2. **Subtitles**
 - Subtitle 1: `"LEGAL FALLOUT"`.
 - Subtitle 2: `"FEES COMPARISON"`.

3. **Content Box**
  - Adds a rounded rectangle on the left placeholder.
  - Text frame includes margins and word wrap for readability.
  - Bullet points include:
    - Lack of Licensing
    - Legal Actions
    - Court Rulings and Penalties

4. **Right-Side Image**
  - Displays `licensingFees.png`, a bar chart visualizing licensing fees for different platforms.
  - Automatically scales to fit the placeholder dimensions.

5. **Licensing Fees Image Generation**
 - The `licensingFees.png` image visualizes estimated licensing fees paid by music streaming platforms in 2014. 
 - It was generated using **Python** and **Matplotlib** and then integrated into the slide.
 - The PowerPoint script imports this exact PNG file, creating a complete data-to-presentation pipeline.

## SLIDE 5 - COLLAPSE
1. **Slide Layout**
 - Uses a **Blank layout** (`slide_layouts[5]`) for complete flexibility.
 - Adds a main slide title: `"COLLAPSE"`.

2. **Three Key Event Boxes**
  - Each box represents an event in the collapse of Grooveshark
    - **Settlement Agreement**  
    - **Shutdown & Public Apology**  
    - **Impact on the Industry**  

3. **Design**
  - Rectangles are evenly spaced and centered horizontally on the slide.
  - Rounded internal margins ensure text is not touching the edges.
  - Text is centered within the rectangles.

4. **Illustrative Images**
  - Each box has a vinyl record positioned relative to the box:
    - First and third images stick out above the boxes.
    - Second image sticks out below the box.
  - Images are sized 2×2 inches and horizontally centered relative to the box.
  - Image files used:
    - `yellowVinyl.png`
    - `orangeVinyl.png`
    - `redVinyl.png`

## SLIDE 6 - A CLOUD OF CONTROVERSY
1. **Slide Layout**
 - Uses a **Blank layout** (`slide_layouts[5]`) for complete flexibility.
 - Adds a main slide title: `"A Cloud of Controversy"`.

2. **Features**
- The `wordcloud.png` highlights key terms from Grooveshark’s legal controversies, emphasizing words like “lawsuit,” “violation,” and “shutdown” to visualize the main issues.
- It was generated using  **Python**, **WordCloud** and **Matplotlib** and then integrated into the slide.
- The wordcloud is customized using:
  - Dark background (`black`) for contrast.
  - Red color palette (`Reds` colormap).
  - Horizontal layout for all words.
  - Font sizes ranging from 20 to 100.
- Adjusts the WordCloud image position and size to align perfectly within the slide.

## SLIDE 7 - LESSONS LEARNT
## SLIDE 8 - LEGACY
## SLIDE 9 - REFERENES
1. **Slide Layout**
 - Uses a **Blank layout** (`slide_layouts[5]`) for complete flexibility.
 - Adds a main slide title: `"REFERENCES"`.

2. **Design**
- Rounded Rectangle Container, positioned centrally below the title, with dark red fill and border.
- Music Controls Image, placed above the reference links for visual appeal.
- Four rectangles representing links, each with:
    - A clickable hyperlink
    - A small circle numbered sequentially
    - Text with proper spacing
- Colors, fonts, and alignments are applied to all elements.

3. **Reference Links**
- The current script includes these sample links:
    - BBC Technology News
    - Rolling Stone Music News
    - Cinch Solution Analysis
    - Wired Technology Article


## NOTES


