# Story Generation Web App

This web app allows users to generate long stories based on character details, persona, themes, and description. It uses Google's Gemini generative AI model to create unique and creative stories with specific genres and plot structures.

---

## Features

- **Character Input**: Users can input a character's name and persona to shape the story.
- **Theme Selection**: Users can choose from multiple genres such as Sci-Fi, Mystery, Romance, and more.
- **Story Description**: Users can provide a brief description to influence the story's plot and tone.
- **Story Generation**: The app generates a long-form story with at least 10 chapters based on the provided inputs.
- **Creative and Dynamic Plot**: The story includes twists and dynamic plot points according to the selected genres.

---

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/RajeshAndra/Story-Generation.git
cd Story-Generation
```

### Install Dependencies

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

- Rename the `.env_sample` file to `.env`:

```bash
mv .env_sample .env
```

- Add your **Gemini API Key** to the `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key.

---

## Usage

### Run the Application

Once the environment is set up, run the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will start the application in your browser.

### App Functionality

1. **Character Input**: Enter the name and persona of your character.
2. **Theme Selection**: Choose genres for the story from the available options (Sci-Fi, Romance, etc.).
3. **Description Input**: Provide a brief description (optional) to help guide the story's direction.
4. **Submit Button**: Click "Submit" to generate the story based on the inputs.

The app will then use the Gemini AI model to generate the story, which will be displayed on the page.
