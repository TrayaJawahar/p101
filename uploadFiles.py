import dropbox 
import os 
from dropbox.files import WriteMode
class TransferData :
    def __init__ (self , access_token):
          self.access_token = access_token

    def upload_file(self , file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for roots , dirs , files in os.walk(file_from):
            for file_name in files:
                local_path=os.path.join(roots,file_name)
                relative_path=os.path.relpath(local_path , file_from)
                dropbox_path=os.path.join(file_to , relative_path)

            with open (local_path, 'rb') as f:
                dbx.files_upload(f.read() , dropbox_path , mode=WriteMode('overwrite'))
               
def main():
    access_token = '9dhF2aw4UmsAAAAAAAAAAdt4kWddYuxl6d8Es4vjtswoJqVGtK30ocy5omPSv7w7'
    transferData = TransferData(access_token)

    file_from = input("ENTER THE FILE TO BE TRANSFERED :")

    file_to = input("ENTERR THE FULL PATH : ")


    transferData.upload_file(file_from, file_to)
    print("FILE HAS BEEN MOVED..")


main()
