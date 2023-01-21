
from Reddit import reddit
from Graphics.screenshot import get_screenshots_of_reddit_posts
import config
from TextToSpeech.tts import create_tts, get_length
from pathlib import Path
from utils.clean_text import markdown_to_text
from utils.add_mp3_pause import add_pause
from VideoEditor.videomaker import make_final_video
import math
import subprocess
import time



def main():
    my_config = config.load_config()
    my_reddit = reddit.login()
    thread = reddit.get_thread(reddit=my_reddit,
                               subreddit=my_config['Reddit']['subreddit'])

    if thread is None:
        print('No thread found!')
        return

    comments = reddit.get_comments(thread=thread)
    if comments is None:
        print('No comments found!')
        return

    Path(f"./Assets/temp").mkdir(parents=True, exist_ok=True)
    thread_id_path = f"./Assets/temp/{thread.id}"

    # download screenshot of reddit post and its comments
    get_screenshots_of_reddit_posts(reddit_thread=thread, reddit_comments=comments, screenshot_num=1)

    # create a mp3 directory for the tts files
    Path(f"{thread_id_path}/mp3").mkdir(parents=True, exist_ok=True)
    Path(f"{thread_id_path}/mp3_clean").mkdir(parents=True, exist_ok=True)
    print("Getting mp3 files..")

    # download tts files
    thread_title = markdown_to_text(thread.title)
    title_audio_path = f'{thread_id_path}/mp3/title.mp3'
    title_audio_clean_path = f'{thread_id_path}/mp3_clean/title.mp3'
    create_tts(text=thread_title, path=title_audio_path)

    for idx, comment in enumerate(comments):
        path = f"{thread_id_path}/mp3/{idx}.mp3"
        comment_body = markdown_to_text(comment.body)
        create_tts(text=comment_body, path=path)

    # make sure the tts of the title and comments don't exceed the total duration
    total_video_duration = my_config['VideoSetup']['total_video_duration']
    pause = my_config['VideoSetup']['pause']
    current_video_duration = 0

    tts_title_path = f'{thread_id_path}/mp3/title.mp3'
    title_duration = get_length(path=tts_title_path)
    current_video_duration += title_duration + pause

    list_of_number_of_comments = list(range(len(comments)))

    comments_audio_path = []
    comments_audio_clean_path = []
    comments_image_path = []
    for i in list_of_number_of_comments:
        comment_audio_path = f'{thread_id_path}/mp3/{i}.mp3'
        comment_audio_clean_path = f'{thread_id_path}/mp3_clean/{i}.mp3'
        comment_image_path = f'{thread_id_path}/png/{i}.png'
        comment_duration = get_length(comment_audio_path)

        if current_video_duration + comment_duration + pause <= total_video_duration:
            comments_audio_path.append(comment_audio_path)
            comments_audio_clean_path.append(comment_audio_clean_path)
            comments_image_path.append(comment_image_path)
            current_video_duration += comment_duration + pause

    title_image_path = f'{thread_id_path}/png/title.png'

    # convert the pause(in seconds) into milliseconds
    mp3_pause = pause * 1000
    add_pause(title_audio_path, title_audio_clean_path, mp3_pause)

    comments_combined = list(zip(comments_audio_path, comments_audio_clean_path))
    for input_path, output_path in comments_combined:
        add_pause(input_path, output_path, mp3_pause)

    # create final video
    make_final_video(title_audio_path=title_audio_clean_path,
                     comments_audio_path=comments_audio_clean_path,
                     title_image_path=title_image_path,
                     comments_image_path=comments_image_path,
                     length=math.ceil(total_video_duration),
                     reddit_id=thread.id
                     )

    if my_config['App']['upload_to_youtube']:
        upload_file = f'./Results/{thread.id}.mp4'
        directory_path = my_config['Directory']['path']
        cmd = ['python', f'{directory_path}/Youtube/upload.py', '--file', upload_file, '--title',
               f'{thread_title}', '--description', f'{thread_title}']
        subprocess.run(cmd)


if __name__ == '__main__':
    my_config = config.load_config()
    while True:
        print('Starting ..........\n')
        main()
        print('\n-------------------------------------------\n')
        time.sleep(my_config['App']['run_every'])


