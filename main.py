file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

        with open('voice.mp3', 'wb') as f:
            f.write(file.content)