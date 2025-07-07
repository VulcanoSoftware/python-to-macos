import requests

print("How many ram do you have?")
print("------------------------")
print("1) 8 GB")
print("2) 16 GB")
print("3) 32 GB")

ram = input("Enter your choice (1-3): ")

if ram == "1":
    print("You have 8 GB of RAM.")
    print("Put following launch options in the euro truck simulator 2 properties on steam:")
    print("")
    print("-64bit -nointro -unlimitedlog -rdevice dx11 -mm_pool_size 4096 -mm_max_resource_size 32 mm_max_tmp_buffers_size 1000")
    
elif ram == "2":
    print("You have 16 GB of RAM.")
    print("Put following launch options in the euro truck simulator 2 properties on steam:")
    print("")
    print("-64bit -nointro -unlimitedlog -rdevice dx11 -mm_pool_size 8192 -mm_max_resource_size 32 -mm_max_tmp_buffers_size 1000")
    
elif ram == "3":
    print("You have 32 GB of RAM.")
    print("Put following launch options in the euro truck simulator 2 properties on steam:")
    print("")
    print("-64bit -nointro -unlimitedlog -rdevice dx11 -mm_pool_size 16384 -mm_max_resource_size 32 -mm_max_tmp_buffers_size 1000")

else:
    print("Invalid input. Please enter a number between 1 and 3.")
    
print("===========================")
print("You need to change the buffer page size in the config.cfg file.")
buffer = input("Do you want to download the updated config.cfg file? (Y/N): ").lower()
if buffer == "y":
    print("Downloading config.cfg...")
    
    url = 'https://raw.githubusercontent.com/VulcanoSoftware/ets2-setup-tool/refs/heads/main/config.cfg'
    bestandspad = 'config.cfg'

    response = requests.get(url)

    if response.status_code == 200:
        with open(bestandspad, 'wb') as f:
            f.write(response.content)
        print('Bestand succesvol gedownload als config.cfg')
    else:
        print(f'Fout bij downloaden: {response.status_code}')
    
    print("Download complete! Place the config.cfg file in your Euro Truck Simulator 2 folder which you can find in the documents folder.")
    print("If the file already exists, please replace it.")
elif buffer == "n":
    print("okay, you can change the buffer page size manually.")
    print("find the following line in the config.cfg file:")
    print("")
    print("uset r_buffer_page_size")
    print("")
    print("and change the value to 50")
    
else:
    print("Invalid input. Please enter Y or N.")
    
print("Which version of Euro Truck Simulator 2 do you have?")
print("1) 1.50")
print("2) 1.51")
print("3) 1.52")
print("4) 1.53")
print("5) 1.54")
version = input("Enter your choice (1-5): ")
if version == "1":
    print("You have version 1.50 of Euro Truck Simulator 2.")
    dlc = input("Do you have all the DLCs and mods? (Y/N): ").lower()
    if dlc == "y":
        print("You have all the DLCs and mods for version 1.50.")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    elif dlc == "n":
        print("You do not have all the DLCs and mods for version 1.50.")
        print("You can download the DLCs and mods from the link bellow ... ")
        print("https://archive.org/download/vulcanomods_1.50/vulcanomods_1.50.zip")
        print("The password for the zip file is: MinecraftTijdensDeLesVanBleyen!")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    else:
        print("Invalid input. Please enter Y or N.")
        
elif version == "2":
    print("You have version 1.51 of Euro Truck Simulator 2.")
    dlc = input("Do you have all the DLCs and mods? (Y/N): ").lower()
    if dlc == "y":
        print("You have all the DLCs and mods for version 1.51.")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    elif dlc == "n":
        print("You do not have all the DLCs and mods for version 1.51.")
        print("You can download the DLCs and mods from the link bellow ... ")
        print("https://archive.org/download/vulcanomods_1.51/vulcanomods_1.51.zip")
        print("The password for the zip file is: MinecraftTijdensDeLesVanBleyen!")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    else:
        print("Invalid input. Please enter Y or N.")

elif version == "3":
    print("You have version 1.52 of Euro Truck Simulator 2.")
    dlc = input("Do you have all the DLCs and mods? (Y/N): ").lower()
    if dlc == "y":
        print("You have all the DLCs and mods for version 1.52.")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    elif dlc == "n":
        print("You do not have all the DLCs and mods for version 1.52.")
        print("You can download the DLCs and mods from the link bellow ... ")
        print("https://archive.org/download/archive_vulcanomods_1_52_1749234939/vulcanomods_1.52.zip")
        print("The password for the zip file is: MinecraftTijdensDeLesVanBleyen!")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    else:
        print("Invalid input. Please enter Y or N.")
        
elif version == "4":
    print("You have version 1.53 of Euro Truck Simulator 2.")
    dlc = input("Do you have all the DLCs and mods? (Y/N): ").lower()
    if dlc == "y":
        print("You have all the DLCs and mods for version 1.53.")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    elif dlc == "n":
        print("You do not have all the DLCs and mods for version 1.53.")
        print("You can download the DLCs and mods from the link bellow ... ")
        print("https://archive.org/download/archive_vulcanomods_1_53_1749292145/vulcanomods_1.53.zip")
        print("The password for the zip file is: MinecraftTijdensDeLesVanBleyen!")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    else:
        print("Invalid input. Please enter Y or N.")
        
elif version == "5":
    print("You have version 1.54 of Euro Truck Simulator 2.")
    dlc = input("Do you have all the DLCs and mods? (Y/N): ").lower()
    if dlc == "y":
        print("You have all the DLCs and mods for version 1.54.")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    elif dlc == "n":
        print("You do not have all the DLCs and mods for version 1.54.")
        print("You can download the DLCs and mods from the link bellow ... ")
        print("https://archive.org/download/archive_vulcanomods_1_54_1749376639/vulcanomods_1.54.zip")
        print("The password for the zip file is: MinecraftTijdensDeLesVanBleyen!")
        print("")
        print("For more information about the mods (mod loading order, steam workshop mods, etc) please visit the following link:")
        print("https://vulcanotruck.pages.dev/")
    else:
        print("Invalid input. Please enter Y or N.")
        
else:
    print("Invalid input. Please enter a number between 1 and 5.")
