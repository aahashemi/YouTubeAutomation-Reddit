# YouTubeAutomation-Reddit 🎥
Using this project, videos generated from Reddit posts will be automatically uploaded to your YouTube channel

## Sample Video 
https://user-images.githubusercontent.com/69358811/213927870-48c6f2af-f320-4a62-be51-411f6915a283.mp4

## Built With
* [![AWS][AWS.com]][AWS-url]
* [![Python][Python.com]][Python-url]
* [![Reddit][Reddit.com]][Reddit-url]
* [![Youtube][Youtube.com]][Youtube-url]
* [![Json][Json.com]][Json-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python.com]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/

[Youtube.com]: https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[Youtube-url]: https://www.youtube.com/

[AWS.com]: https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white
[AWS-url]: https://aws.amazon.com/
[Reddit.com]: https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white
[Reddit-url]: https://www.reddit.com/

[Json.com]: https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white
[Json-url]: https://www.json.org/json-en.html

## Installation 👨‍💻

1. Clone this repository <br />

2. Run `pip install -r requirements.txt` <br />

3. Run `python -m playwright install and python -m playwright install-deps` <br />

4. Go to [Free Cloud Computing Services - AWS Free Tier](https://aws.amazon.com/)
   * Sing in to the console
   
   ![1](https://user-images.githubusercontent.com/69358811/213929628-3d2ebc7f-f825-4712-8ecb-5b58bcd9dd5d.png)

   * Click on Open account menu
   * Click on Security credentials
   
   ![2](https://user-images.githubusercontent.com/69358811/213930042-23b69401-3aa3-4d03-a18d-68cad0a1918e.png)

    
   * Click on Create access key
   
   ![3](https://user-images.githubusercontent.com/69358811/213930056-56fb00f6-b0ce-4385-a3ee-a8815c893621.png)
   
   * Once you created the access key and obtained the secret key, open the `config.toml` file in the project and update the following parameters accordingly. <br />
   
     ```toml
     [AmazonAWSCredential]
     aws_access_key_id = 'YOUR AWS ACCESS KEY ID'
     aws_secret_access_key = 'YOUR AWS SECRET ACCESS KEY'
     ```
  
5. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps) and click on create another app at the bottom.
   * Fill out the required details, make sure to select **script** and click on create app.
   
   ![4](https://user-images.githubusercontent.com/69358811/213930841-eccce67e-ba81-4c44-b1ff-a5d7ba3a9dc1.png)
   
   * Make a note of the **personal use script** & **secret token** and update the the following credentials in the `config.toml` file. 
   
   ![5](https://user-images.githubusercontent.com/69358811/213931054-5eddc924-ab64-4273-914d-5348838a0846.png)

    ```toml
     [RedditCredential]
     client_id='YOUR PERSONAL USE SCRIPT'
     client_secret='YOUR SECRET TOKEN'
     user_agent='{YOUR REDDIT PROJECT NAME} v4.0 by /u/{YOUR REDDIT USERNAME}'
     username='YOUR REDDIT USERNAME'
     passkey='YOUR REDDIT PASSWORD'
     ```

6. At this point you can run the the program and generate a video however before that you need to updating a few more parameter in the `config.toml` file. 
   
   ```toml
   [Directory]
   # absolute path to where this project is cloned or downloaded e.g: Desktop/YoutubeAutomation-Reddit
   path=''
   # --------------------------------------------
   [Background]
   # absolute path to the background video e.g: Desktop/minecraft.mp4
   path=''
   ```
   
   You can download any YouTube video as a background and add its path to the `config.toml` file. Here are a few options:
    * Minecraft (1:20 h): https://youtu.be/n_Dv4JMiwK8
    * GTA (1:00 h): https://youtu.be/qdvjZ1bUw68
    * Subway Surfer (1:05 h): https://youtu.be/ChBg4aowzX8
   
7. If you want the app to automatically upload the generated video into your Youtube channel, first set `upload_to_youtube = true` and specify how often you want the app to upload a video (in seconds). I don't recommond anything less than every 6 hours because you will reach your qouta limit. 

  ```toml
   [App]
   # whether the result video should be uploaded to your youtube channel
   upload_to_youtube=false
   # how often should the app be run (in seconds) e.g: every 6 hours -> 21600 seconds
   run_every=21600
   ```
8. Finally you need to enable the Youtube api to be able to upload videos from your computer. This process is a bit more involved, so I'll link to a [blog tutorial]('https://youtu.be/aFwZgth790Q'). Just follow the steps until **minute 10:58** and you will be able to get a `client_id` and a `client_secret`. Update the following parameters and HOORAY 🥳🥳🥳!
     
   ```toml
   [YoutubeCredential]
   client_id=''
   client_secret=''
   ```

All we are left do is run
```python3
   python main.py
   ```
And let the app do the the rest!
