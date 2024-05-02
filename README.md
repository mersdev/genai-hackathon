# Google AI Hackathon

# Welcome to GripeNWipe App

GripeNWipe is a web app that empowers users to improve the hygiene and maintenance of public restrooms. It leverages image recognition and user feedback to automatically assess restroom conditions and assign cleaning tasks to the responsible parties. This eliminates the need for manual reporting and ensures a prompt response to sanitation issues.

## Inspiration

Public toilets are an essential part of our daily lives, but let's be honest, they often leave much to be desired. Inspired by the Malaysian government's initiative to promote cleaner public toilets through the BMW (Bersih, Menawan, Wangi) standard, we noticed a gap between these goals and reality. With a growing number of unhygienic restrooms in Malaysia and Singapore, we saw the need for a user-friendly app to address this issue. GripeNWipe empowers users to take action and create a cleaner tomorrow for public toilets.

## What it does

GripeNWipe is an innovative solution that automates the toilet complaint process. Here's how it works:

1.  **Snap a Picture:** Users simply take a picture of the toilet's condition.
2.  **AI-powered Analysis:** Generative AI analyzes the image to assess the severity of the issue (e.g., clogged toilet, overflowing trash bin).
3.  **Feedback and Recommendation:** Users provide additional details about the problem through a user-friendly interface. GripeNWipe then suggests potential solutions based on the analysis.
4.  **Automated Complaint:** With user confirmation, GripeNWipe automatically sends a comprehensive report, including the image, analysis, and suggested solutions, to the designated cleaning personnel.

This eliminates the need for manual reporting, streamlining the complaint process and ensuring faster resolution.

## How we built it

Developing GripeNWipe involved leveraging cutting-edge technologies:

- **Generative AI:** We trained a generative AI model to accurately identify and classify various toilet issues from user-uploaded images.
- **Natural Language Processing (NLP):** NLP allows GripeNWipe to understand user feedback and integrate it with the AI analysis to generate a clear and detailed report.
- **Automation:** The system automates the entire complaint process, from image analysis to report generation and delivery.

## Challenges we ran into

Getting GripeNWipe off the ground wasn't without its hurdles:

- **Finding the Perfect Testers:** Identifying the ideal users to test our initial prototype proved tricky.
- **Location, Location, Location:** Using GPS to pinpoint restroom locations proved unreliable due to the close proximity of toilets.
- **Privacy Concerns:** Some users were hesitant to participate, understandably unwilling to share photos of unclean restrooms publicly.

We tackled these challenges head-on:

- **QR Code Savior:** We swapped GPS location tracking for a simpler solution - QR code stickers placed on toilet doors for easy user identification.
- **Collaboration is Key:** Partnering with universities allowed us to test and improve GripeNWipe in real-world settings, with their permission to upgrade their restroom facilities.

By thinking creatively and working together, we were able to overcome these initial roadblocks and pave the way for GripeNWipe's success

## Accomplishments that we're proud of

GripeNWipe is a unique solution that addresses a common yet critical issue. We are proud to have developed a system that:

- **Empowers Users:** GripeNWipe puts the power in users' hands to report problems and hold authorities accountable.
- **Improves Hygiene:** By ensuring timely resolution of toilet issues, GripeNWipe contributes to cleaner and more hygienic restrooms.
- **Increases Efficiency:** The automated complaint process eliminates manual reporting, saving time and resources.

## What we learned

Building GripeNWipe was a valuable learning experience. We gained expertise in:

- **Generative AI Applications:** The project pushed the boundaries of how generative AI can be used in practical scenarios.
- **User-Centered Design:** We learned the importance of designing an interface that is both informative and easy to use.

## What's next for Team OwO: GRIPEnWIPE

We envision GripeNWipe expanding beyond complaint reporting. Future iterations could include:

- **Real-time Maintenance Monitoring:** Integrating with IoT sensors to monitor toilet cleanliness and trigger preventive maintenance.
- **Tissue Dispensing Functionality:** Partnering with restroom facilities to enable users to request tissue refills through the GripeNWipe app.

GripeNWipe has the potential to revolutionize restroom hygiene and user experience. We are committed to continuously improving the system and making toilets cleaner and more pleasant for everyone.

## How to use our GripeNWipe app?

1. Clone the github repo using `git clone https://github.com/mersdev/genai-hackathon.git`
1. Create the Python Virtual Environment via `python -m venv venv`
1. Activate the Python Virtual Environment via `source venv/bin/activate`
1. Install all the modules needed via `pip install -r requirements.txt`
