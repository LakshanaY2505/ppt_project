# GROOVESHARK

## DESCRIPTION
This project creates an automated PowerPoint presentation using Python's `python-pptx` library to analyze the rise and fall of GrooveShark, a pioneering online music streaming service that operated from 2007 to 2015.

The script demonstrates how to programmatically add slides, insert images, and format text using Python, making it a practical example for automating presentation creation.

## FILE STRUCTURE
```
ppt_project
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
├── complete_code.py              # Main program code
│
├── Charts (code files)/          # Folder with chart-related Python code
│   ├── barChart_code.py          # Code for generating the bar chart
│   └── wordcloud_code.py         # Code for generating the word cloud
│
└── Images/                       # Images used in the project
    ├── bg.jpg
    ├── cd1.jpg
    ├── cd2.jpg
    ├── cd3.jpg
    ├── groovesharklogo.png
    ├── licensingFees.png
    ├── musicControls.png
    ├── orangeVinyl.png
    ├── red cover.jpg
    ├── redVinyl.png
    ├── tameImpala.jpg
    ├── vinyl.png
    ├── wordcloud.png
    └── yellowVinyl.png
```



## REQUIRED MODULES

- from pptx import Presentation
- from pptx.util import Pt, Inches
- from pptx.enum.text import PP_ALIGN
- from pptx.dml.color import RGBColor
- from pptx.enum.shapes import MSO_SHAPE
- from PIL import Image
- import requests
- from io import BytesIO
- import matplotlib.pyplot as plt
- from wordcloud import WordCloud

## INSTALLATION OF THE MODULES

This project requires Python 3 and the following Python modules:

- **python-pptx** – for creating and editing PowerPoint presentations.
- **Pillow (PIL)** – for image handling.
- **requests** – for fetching images from URLs.
- **matplotlib** – for plotting and displaying images.
- **wordcloud** – for generating word clouds.

### Installation Steps

Open a terminal or command prompt and run:

```pip install python-pptx pillow requests matplotlib wordcloud```


## SLIDE 0 - TABLE OF CONTENTS
1. *Slide Layout*
  - Uses a Title Only layout slide_layouts[5]..

2. *Placeholders/Shapes*
  - shapes.title → Title text “TABLE OF CONTENTS”.
  - Slide background → solid fill, dark red (RGB(90,3,10)).
  - Nine alternating images (cd1.jpg, cd2.jpg, cd3.jpg) and textboxes for each TOC entry.

3.*Content*
  - TOC_array = ["Introduction", "Problem", "Lessons", "Timeline", "Collapse", "Legacy", "Growth", "Cloud", "References"]
  - Each entry is paired with an image (rotating between CD1/CD2/CD3) and a small white-text textbox.

4.*Images*
 - Images/cd1.jpg, Images/cd2.jpg, Images/cd3.jpg.
## SLIDE 1 - INTRODUCTION
1. *Slide Layout* 
 - slide_layouts[6] → Blank.

2. *Shapes & Placeholders*
 - Background image: bg.jpg, stretched to full slide size.
 - Title textbox: → “INTRODUCTION” 
 - Yellow rectangle (content area): shape type 5 (Rectangle)
 - Text content textbox: 
    - Grooveshark’s history, founders, and mission.

3. *Sidebars*
 - Left: Two vertical rectangles (dark red + orange).
 - Right: Two vertical rectangles (dark red + orange).

4.*Images*
 - Images/vinyl.png
 -  Images/tameimpala.jpg.
## SLIDE 2 - TIMELINE
1. *Layout*
- Uses Blank layout (slide_layouts[6]).

2. *Background*
- Image fetched from a URL (https://wallpapercave.com/wp/wp4465178.png).
- Converted to RGB, rotated 180°, cropped, and applied to the entire slide.

3. *Title*
- Text: "TIMELINE"

4. *Timeline Line & Shapes*
- Vertical black line (rectangle) positioned at (5, 2), height 5 in.
- Colored circles (oval shapes) placed along the line, one per event.
- Gradient colors: Orange → Red (RGB(255,165,0) … RGB(255,0,0)).

5. *Events*
- Alternating layout:
   - Even-indexed events → left side of line.
   - Odd-indexed events → right side of line.
 - Year textboxes: Bold black text above each circle.
 - Description boxes: Positioned near each year, filled with the same color as its circle.


## SLIDE 3 - ESTABLISHMENT AND GROWTH
1. *Layout*
- Uses Blank layout (slide_layouts[6]).

2. *Background & Design*
- Background image: Images/bg.jpg, covering full slide.
- Decorative circle shape (red, top-left).
- Decorative circle shape (orange, bottom-right).
- Right-side image: Images/red cover.jpg filling vertical space.

3. *Title*
- Text: "GROWTH"

4. *Content*
- Black rectangle spanning left content area.
- Overlaying textbox with bullet-style growth notes:
    - Peer-to-peer beginnings → transition to streaming.
    - Free, on-demand music with playlists & sharing.
    - Mobile apps launch → 35M users by 2011.
    - Social features → music community feel.
    - Expanded reach to 150+ countries.

## SLIDE 4 - PROBLEM
1. *Slide Layout*
  - Uses the *Two Titles and Content* layout (slide_layouts[4]).
  - Adds a main title, two subtitles, and content placeholders.

2. *Subtitles*
 - Subtitle 1: "LEGAL FALLOUT".
 - Subtitle 2: "FEES COMPARISON".

3. *Content Box*
  - Adds a rounded rectangle on the left placeholder.
  - Text frame includes margins and word wrap for readability.
  - Bullet points include:
    - Lack of Licensing
    - Legal Actions
    - Court Rulings and Penalties

4. *Right-Side Image*
  - Displays licensingFees.png, a bar chart visualizing licensing fees for different platforms.
  - Automatically scales to fit the placeholder dimensions.

5. *Licensing Fees Image Generation*
 - The licensingFees.png image visualizes estimated licensing fees paid by music streaming platforms in 2014. 
 - It was generated using *Python* and *Matplotlib* and then integrated into the slide.
 - The PowerPoint script imports this exact PNG file, creating a complete data-to-presentation pipeline.

## SLIDE 5 - COLLAPSE
1. *Slide Layout*
 - Uses a *Blank layout* (slide_layouts[5]) for complete flexibility.
 - Adds a main slide title: "COLLAPSE".

2. *Three Key Event Boxes*
  - Each box represents an event in the collapse of Grooveshark
    - *Settlement Agreement*  
    - *Shutdown & Public Apology*  
    - *Impact on the Industry*  

3. *Design*
  - Rectangles are evenly spaced and centered horizontally on the slide.
  - Rounded internal margins ensure text is not touching the edges.
  - Text is centered within the rectangles.

4. *Illustrative Images*
  - Each box has a vinyl record positioned relative to the box:
    - First and third images stick out above the boxes.
    - Second image sticks out below the box.
  - Images are sized 2×2 inches and horizontally centered relative to the box.
  - Image files used:
    - yellowVinyl.png
    - orangeVinyl.png
    - redVinyl.png

## SLIDE 6 - A CLOUD OF CONTROVERSY
1. *Slide Layout*
 - Uses a *Blank layout* (slide_layouts[5]) for complete flexibility.
 - Adds a main slide title: "A Cloud of Controversy".

2. *Features*
- The wordcloud.png highlights key terms from Grooveshark’s legal controversies, emphasizing words like “lawsuit,” “violation,” and “shutdown” to visualize the main issues.
- It was generated using  *Python, **WordCloud* and *Matplotlib* and then integrated into the slide.
- The wordcloud is customized using:
  - Dark background (black) for contrast.
  - Red color palette (Reds colormap).
  - Horizontal layout for all words.
  - Font sizes ranging from 20 to 100.
- Adjusts the WordCloud image position and size to align perfectly within the slide.

## SLIDE 7 - LESSONS LEARNT
1. *Slide Layout*
- slide_layouts[6] → Blank
- Background image: bg.jpg, stretched to full slide size.
- Added a title text box and content text box 

2. *Design*
- Three cards created:
  - Title Card (Rounded Rectangle)
  - Music Player Controls (Text Box)
  - Content Card (Rounded Rectangle)
- Each card has a fixed width and height

## SLIDE 8 - LEGACY
1. *Slide Layout*
- slide_layouts[6] → Blank
- Contains title and content textbox 

2. *Design*
- Title texbox - center aligned, Font: Constantia, 40 pt, Bold, Dark Gray
- Subtitle textbox - center aligned, Font: Constantia, 28 pt, Bold, Dark Gray
- Content textbox - positioned below the title, word wrapped enabled, center aligned, Font: Arial, 20 pt, Bold, Dark Gray

3. *Table*
- A 5×5 table compares Grooveshark with Spotify, YouTube Music, and SoundCloud.
- Conatins formating for header row, header column (first column), data cells (special formating for symbols)


## SLIDE 9 - REFERENCES
1. *Slide Layout*
 - Uses a *Blank layout* (slide_layouts[5]) for complete flexibility.
 - Adds a main slide title: "REFERENCES".

2. *Design*
- Rounded Rectangle Container, positioned centrally below the title, with dark red fill and border.
- Music Controls Image, placed above the reference links for visual appeal.
- Four rectangles representing links, each with:
    - A clickable hyperlink
    - A small circle numbered sequentially
    - Text with proper spacing
- Colors, fonts, and alignments are applied to all elements.

3. *Reference Links*
- The current script includes these sample links:
    - BBC Technology News
    - Rolling Stone Music News
    - Cinch Solution Analysis
    - Wired Technology Article
