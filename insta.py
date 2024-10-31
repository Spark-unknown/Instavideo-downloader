import instaloader

# Initialize instaloader with options
loader = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_pictures=False,
    download_video_thumbnails=False,
    save_metadata=False
)

# Replace with your Instagram credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Login and save session
try:
    loader.load_session_from_file(USERNAME)
    print("Session loaded successfully.")
except FileNotFoundError:
    # Session file doesn't exist, log in and save session
    try:
        loader.login(USERNAME, PASSWORD)
        loader.save_session_to_file()
        print("Logged in and session saved successfully.")
    except instaloader.exceptions.BadCredentialsException:
        print("Error: Incorrect credentials.")
        exit()
    except Exception as e:
        print(f"Login failed: {e}")
        exit()

# Extract shortcode from URL
url = 'https://www.instagram.com/reel/C4KRx6xMYhh'
shortcode = url.split('/')[-2]

# Try downloading the post
try:
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target=shortcode)
    print(f"Downloaded post with shortcode '{shortcode}'")
except Exception as e:
    print(f"Error occurred: {e}")
