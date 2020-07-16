from boxsdk import DevelopmentClient
client = DevelopmentClient()
filename = input("What file do you wish to upload?")

folder_id = '118025580874'
new_file = client.folder(folder_id).upload(filename)
print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))
