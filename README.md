# OpenAI-API-Interface
OpenAI API Interface written by FreeGPT is an opensource code that allows anyone to use OpenAI's API directly from their Python console. No knowledge of coding necesarry.

## OpenAI Console Access

This project allows users to access the OpenAI API from their console. The project is written in Python and utilizes the openai library. It also uses the transformers library, which is required to be installed in order to run the project.

## Usage

To run the project, first install the required dependencies by running the command pip install -r requirements.txt. Then, in the project's root directory, run the command python main.py. This will start a console where users can input their queries and receive a response generated by the OpenAI API.

## API Key

In order to use the OpenAI API, users must provide their own API key in the main.py file. Replace //OpenAI API KEY HERE with your own API key.

## Additional Features

## The project also includes the Cognify.Cleaner module, which contains functions for cleaning text data. These functions can be utilized for pre-processing text before sending it to the API for generation.

## Note

This project uses the text-davinci-003 API endpoint. This is the highest quality model offered by OpenAI, however it is also the most expensive and slowest processing. If you want to use other API endpoints, you can replace the model_engine variable with desired API endpoint on the OpenAI website, or simply reference the models from this readme.

## Contributions

Feel free to fork this repository and make any necessary changes to fit your needs. Pull requests are also welcome.

# How to Install:

1. Install PyCharm: Go to the PyCharm website (https://www.jetbrains.com/pycharm/download/) and download the community version of PyCharm. Follow the instructions to install it on your computer.

2. Start a new project: Open PyCharm and click on "Create New Project". Name the project and select a location to save it in.

3. Install the OpenAI library: In PyCharm, go to File > Settings > Project: [Your Project Name] > Project Interpreter. Click on the "+" button to add a new library and search for "openai". Select the "openai" library and click "Install Package".

4. Get an API Key from OpenAI: Go to the OpenAI website (https://beta.openai.com/) and sign up for an account. Once you have an account, go to the API section and generate an API key.

5. Add the API key to the code: In PyCharm, open the main.py file. Replace "//OpenAI API KEY HERE" with the API key you obtained from OpenAI.

6. Copy the code: Copy the code from the provided source code and paste it into the main.py file in PyCharm.

7. Run the project: In PyCharm, click on the green arrow button at the top right corner of the window or press Shift + F10 to run the project. You should now be able to input your queries and receive a response generated by the OpenAI API in the console.

If you are not familiar with PyCharm or running a python script, it might be helpful to consult the PyCharm documentation or a tutorial on running Python scripts before starting this project.

# Models
## These models are in top to bottom order, ranging from most capable to least capable.

|Available Models  | Cost  |
| ------------- | ------------- |
| Davinci  |$0.1200 / 1K tokens |
| Curie  |$0.0120 / 1K tokens|
| Babbage  | $0.0024 / 1K tokens  |
| Ada  | $0.0016 / 1K tokens|


**Please read the terms of service for OpenAI's API usages and requirements. Do not sell or share your API key. I am not responsible for anything you do with this code beyond this repository, and I do not assume any liability for damages or financial losses accrued from using this code. You assume full responsibility for your actions by using this code.**

### License

MIT License

Copyright (c) 2023 Devon Chase

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
