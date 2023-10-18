[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✅DESCRIPTION

An ITTTS (Image-to-text-to-speech) python package for integrated conversion of textual images and PDF document to human speech.
This library aims at easing the internal image preprocessing and conversion of extracted text to human speech over multiple languages.
<br />
<br />

## ✅QUICK START

### Dependencies
This pipeline requires the dependencies which can be installed by running:

`pip install -r requirements.txt`

<br />
<br />

## ✅FUNCTIONS

* _**image_to_sound(path_to_image, lang, pre_process="NO")**_

This main function is leveraged to convert the input textual image to human speech in the language present in the text.
The function returns the intermediate text extracted and the speech generated. The speech can then be saved to a .mp3 file.

Parameters:

path_to_image : Defines the path to the "image" as .png or .jpg files. PDF files are also supported along with public image URLs from the internet

lang : Defines the language used in the text. The list of languages supported currently include:

["ENGLISH" , "HINDI", "TELUGU", "KANNADA"]

pre_process(optional) : If the user would like to use our internal pre-processing pipeline for better results.

For example:

`image_to_sound("images/image1.png","ENGLISH",pre_process="YES")`

OR

`image_to_sound("files/text.pdf","HINDI",pre_process="YES")`

OR

`image_to_sound("https://www.techsmith.com/blog/wp-content/uploads/2020/11/TechSmith-Blog-ExtractText.png","ENGLISH",pre_process="YES")`

<p></p>
<br />

* **_preprocess(path_to_image):_**

This function defines the internal pre-processing pipeline used in the package. The user could use this function to retrieve the intermediate preprocessed image before conversion to text and speech.

For example:

`preprocess("images/image1.jpg"):`

<p></p>
<br />

## MODELS USED FOR OCR
After the input image is ensured to be of high quality, we use an efficient OCR
tool called ”EasyOCR” for conversion of textual image to human readable text.
We preferred EasyOCR over other tools like tesseract because EasyOCR provides
us with pre-trained models for various languages. They also perform well on noisy
or low-quality images. It is designed to be fast and can process multiple images
in parallel making it suitable for use.
<br />
<br />

## TEXT TO SPEECH CONVERSION
We leverage ”gTTS (Google Text-to-Speech)”
to accomplish this task. ”gTTS” is a popular TTS (Text-to-Speech) engine
that uses Google’s machine learning and neural network algorithms to synthesize
natural-sounding speech from text input. We chose gTTS engine because GTTS
allows for customization of voice, pitch, speaking rate, and volume to create a more
personalized listening experience
<br />
<br />

## INSTALLATION

Install using pip

For the latest stable release:

`pip install img2speech`
<br />
<br />

## USAGE
```
import img2speech
text,speech = img2speech.image_to_sound("images/image1.png", "ENGLISH", "YES")
print(text) # prints text extracted by OCR model
speech.save("output.mp3") # saves the speech output as mp3 file
```





