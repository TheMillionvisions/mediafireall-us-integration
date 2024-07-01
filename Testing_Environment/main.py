from utils import MediaProcessor
import schedule
import time

folder_path = 'YOUR_INPUT_FOLDER_PATH_HERE'

api_key = 'YOUR_API_KEY_HERE'
user_id = 'YOUR_USERID_HERE'
org_id = 'YOUR_ORGID_HERE'
base_url = 'YOUR_BASE_URL_HERE'

authentication_url = f'https://{base_url}/oauth/token'
moderation_url = f'https://{base_url}/moderation/{org_id}/{user_id}/filters'
moderation_results_url = f'https://{base_url}/mfw/model/config/{{}}/{{}}'

filters = 'YOUR_FILTERS_HERE'
#eg.,filters = 'Disturbing,Nudity(HalfNude),ImageSearch,Violence,MediaLightPerson,ProfilePicture(Single.Visibility.Centered),AIGeneratedImage,ObsceneGesture'

moderation_url_params = {'filters': filters,'apikey': api_key}
moderation_results_url_params = {'apikey': api_key}

processor = MediaProcessor(folder_path, api_key, user_id, authentication_url, moderation_url, moderation_results_url, moderation_url_params, moderation_results_url_params)

processor.run()


