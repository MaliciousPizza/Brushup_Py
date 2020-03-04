import  zipfile, os, shutil,sys

def backup_to_server(folder,backup_location):
    folder = os.path.abspath(folder)

    num = 1
    while True:
        zip_file = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zip_file):
            break
        num += 1
    print(f'Creating {zip_file}...')
    backup_zip = zipfile.ZipFile(zip_file,mode='w')

    for foldername, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backup_zip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('zip'):
                continue

            backup_zip.write(os.path.join(foldername,filename))
        backup_zip.close()
        print('complete!')
        print(zip_file)

        shutil.move(zip_file,backup_location)

backup_to_server(sys.argv,sys.argv)
