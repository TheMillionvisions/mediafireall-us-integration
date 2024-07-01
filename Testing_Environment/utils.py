import os
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import xlsxwriter

class MediaProcessor:
    def __init__(self, folder_path, api_key, user_id, authentication_url, moderation_url, moderation_results_url, moderation_url_params, moderation_results_url_params):
        self.folder_path = folder_path
        self.api_key = api_key
        self.user_id = user_id
        self.authentication_url = authentication_url
        self.moderation_url = moderation_url
        self.moderation_results_url = moderation_results_url
        self.moderation_url_params = moderation_url_params
        self.moderation_results_url_params = moderation_results_url_params
        self.token = None
        self.response_dict = {}
        self.video_ids = []
        self.excel_file_path = 'output.xlsx'
        self.lock = threading.Lock()
        self.headers_written = False

    def generate_token(self):
        try:
            response = requests.post(self.authentication_url, json={'userId': self.user_id, 'apikey': self.api_key})
            response.raise_for_status()
            self.token = response.json().get('access_token')
            print("Successfully generated access token")
            self.headers = {'Authorization': f'Bearer {self.token}'}
        except requests.RequestException as e:
            print(f"Error generating token: {e}")
            return None

    def write_dict_to_excel(self, data):
        with self.lock:
            if not hasattr(self, 'workbook'):
                self.workbook = xlsxwriter.Workbook(self.excel_file_path)
                self.worksheet = self.workbook.add_worksheet()

                # Set formats
                self.header_format = self.workbook.add_format({'bold': True, 'font_size': 12})
                self.data_format = self.workbook.add_format({'font_size': 12})
                self.tick_format = self.workbook.add_format({'font_size': 12, 'font_color': 'red'})
                self.cross_format = self.workbook.add_format({'font_size': 12, 'font_color': 'green'})
                self.link_format = self.workbook.add_format({'font_size': 12, 'underline': 1, 'font_color': 'blue'})

                # Write headers
                headers = data.keys()
                for col, header in enumerate(headers):
                    self.worksheet.write(0, col, header, self.header_format)
                self.row = 1

            # Write data
            for col, key in enumerate(data.keys()):
                value = data[key]
                if key == 'Input_Media_URL' and value:
                    self.worksheet.write_url(self.row, col, value, self.link_format, string='Link')
                elif value == '✔':
                    self.worksheet.write(self.row, col, value, self.tick_format)
                elif value == '✘':
                    self.worksheet.write(self.row, col, value, self.cross_format)
                else:
                    self.worksheet.write(self.row, col, value, self.data_format)
            self.row += 1

    def close_workbook(self):
        if hasattr(self, 'workbook'):
            self.workbook.close()

    def process_media(self):
        image_files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        
        with ThreadPoolExecutor(max_workers=1) as executor:
            for idx, image_file in enumerate(image_files, start=1):
                self.send_media(image_file)
                if len(self.video_ids) >= 5:
                    video_ids_batch = self.video_ids.copy()
                    self.video_ids.clear()
                    executor.submit(self.check_status, video_ids_batch)
            
            while self.video_ids:
                # Ensure remaining video IDs are processed
                video_ids_batch = self.video_ids.copy()
                self.video_ids.clear()
                executor.submit(self.check_status, video_ids_batch)

    def send_media(self, image_file):
        file_path = os.path.join(self.folder_path, image_file)
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(self.moderation_url, files=files, params=self.moderation_url_params, headers=self.headers)
        
        if response.status_code == 200:
            response_json = response.json()
            print(response_json)
            video_id = response_json.get('videoId')
            if video_id:
                with self.lock:
                    self.video_ids.append(video_id)
        elif response.status_code == 400 and 'token expired' in response.text.lower():
            self.generate_token()
            self.send_media(image_file)
        else:
            print(f"Failed to submit file {image_file}: {response.text}")
            print(f"Retrying in 10 seconds.....")
            time.sleep(10)
            self.send_media(image_file)

    def check_status(self, video_ids):
        while video_ids:
            video_id = video_ids.pop(0)
            self._check_status_single(video_id)

    def _check_status_single(self, video_id):
        model_status_check_endpoint = self.moderation_results_url.format(self.user_id, video_id)
        max_retries = 5
        retry_count = 0
        csv_data = []

        while retry_count < max_retries:
            status_resp = requests.get(model_status_check_endpoint, params=self.moderation_results_url_params, headers=self.headers)
            if status_resp.status_code == 200:
                status_resp_json = status_resp.json()
                complete_status = status_resp_json['processStatus'].get('complete', False)
                if complete_status:
                    feature_status = status_resp_json['processStatus'].get('featureStatus', {})
                    input_video_url = status_resp_json["video"].get('inputVideoURL', '')
                    csv_data.append({
                        'Video_ID': video_id,
                        'Input_Media_URL': input_video_url,
                        'MediaLightPerson': '✔' if feature_status.get('MediaLightPerson') else '✘',
                        'Nudity': '✔' if feature_status.get('Nudity') else '✘',
                        'Disturbing': '✔' if feature_status.get('Disturbing') else '✘',
                        'Violence': '✔' if feature_status.get('Violence') else '✘',
                        'ProfilePicture': '✔' if feature_status.get('ProfilePicture') else '✘',
                        'AIGeneratedImage': '✔' if feature_status.get('AIGeneratedImage') else '✘',
                        'ObsceneGesture': '✔' if feature_status.get('ObsceneGesture') else '✘',
                        'ImageSearch': '✔' if feature_status.get('ImageSearch') else '✘',
                        'ErrorMessage': '',
                        'Comments': ''
                    })
                    break

            retry_count += 1
            time.sleep(2)

        if retry_count >= max_retries:
            with self.lock:
                self.video_ids.append(video_id)
            print(f"Failed to get status for video ID {video_id} after {max_retries} retries.")

        for data in csv_data:
            self.write_dict_to_excel(data)

    def run(self):
        self.generate_token()
        self.process_media()
        self.close_workbook()
        print(f"All data has been written to {self.excel_file_path}.")


