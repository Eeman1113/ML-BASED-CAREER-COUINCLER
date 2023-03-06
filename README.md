# ML Based Career Counsellor

The ML Based Career Counsellor is a Streamlit app that uses OpenAI's GPT-3 language model to suggest job positions based on the user's skills. The app asks the user to enter their name, region, date of birth and select the skills they possess from a list of skills. It then generates a prompt using the user's selected skills and asks OpenAI's GPT-3 language model to suggest ten job positions based on the user's skills.

The app uses the PIL library to create a report containing the user's name, selected skills, and the suggested job positions. The report is generated as an image and saved to the local file system.

## Installation
`#Clone the repository to your local machine.
git clone https://github.com/<username>/ml-based-career-counsellor.git`

## Install the required packages listed in the requirements.txt file.

`pip install -r requirements.txt`

Set up an OpenAI API key and Streamlit secrets file to access the GPT-3 API and Streamlit app secrets respectively.
## Usage
Run the Streamlit app locally.<br>
`streamlit run app.py`

* Enter your name, region
* Date of birth 
* Select your skills from the list of skills.
* Click the "Unfuse Me" button to generate job position suggestions based on your skills.
<H3> The app will display the suggested job positions and generate a report image that can be found in the image folder.</H3><br>

# Contributing
*This Project was originally created by:*
* Eeman Majumder
* Aviral Asthana
* Sakshi Sawarkar
* Sannidhya Srivastava
___

Contributions are welcome! If you find any bugs or have any suggestions for improvement, please feel free to open an issue or submit a pull request.


# License
This project is licensed under the terms of the MIT license.
