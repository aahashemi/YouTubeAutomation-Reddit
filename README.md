# YouTubeAutomation-Reddit 🎥



## Sample Video 
https://user-images.githubusercontent.com/69358811/213927870-48c6f2af-f320-4a62-be51-411f6915a283.mp4




## Built With
* [![AWS][AWS.com]][AWS-url]
* [![Python][Python.com]][Python-url]
* [![Reddit][Reddit.com]][Reddit-url]
* [![Youtube][Youtube.com]][Youtube-url]
* [![Json][Json.com]][Json-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

6. At this point you can run the the program and generate a video with updating a few more parameter is the `config.toml` file. 
   
   ```toml
   [Directory]
   # absolute path to where this project is cloned or downloaded e.g: Desktop/YoutubeAutomation-Reddit
   path=''
   # --------------------------------------------
   [Background]
   # absolute path to the background video e.g: Desktop/minecraft.mp4
   path=''
   # --------------------------------------------
   [Reddit]
   # the subredit for which reddit posts are taken
   subreddit='AskReddit'
   # number of top comments
   topn_comments=10
   # --------------------------------------------
   [VideoSetup]
   # the total duration of the final video in seconds
   total_video_duration=60
   # pause between reddit
   pause=0.7
   ```


    
   

