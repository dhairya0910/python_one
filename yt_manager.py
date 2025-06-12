#New Sytax (or new thing) Alert!!
import json

cont= "youtube.txt"

def data_saver(videos):
    with open (cont, "w") as f:
        json.dump(videos,f)

def load_data():
    try:
        with open (cont,"r") as f:
            test=  json.load(f)
            print(type(test))
            return (test)
             #Ye kya krega kii file ko kholega and data ko load krke usko json mein bhi convert kr dega!!
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    for index,video in enumerate(videos,start = 1):
        print (f" {"*"*110}  {index}. {video['name']}, Duration: {video['time']} ")
         # enumerate se kya hoga tuple yaa koi bhi data type list mein convert kr deta hai and hrr element mein index bhi daaal deta hai!!
   
def add_video(videos):
    name = input("Enter Video Name: ")
    time=input("Enter Video Time: ")
    videos.append({'name':name,'time':time})
    data_saver(videos)

def update_video(videos):
    list_all_videos(videos)
    ind= int(input("Write the index of video u want to delete"))
    if 1<=ind<=len(videos):
        name= input("Input the new Video Name: ")
        time= input("Input the new duration of video: ")
        videos[ind-1]={'name':name,'time':time}
        data_saver(videos)
    else:
        print("Invalid Index selected")

def delete_video(videos):
    list_all_videos(videos)
    ind= int(input("Write the index of video u want to deleted: "))
    if 1<=ind<= len(videos):
        del videos[ind-1]
        data_saver(videos)
    else:
        print("Invalid Index selected")

def exit_app():
    pass







def main():
    videos = load_data()
    while True :
        print("Youtube Manager App| Choose One among options which are getting printed")
        print("1.List all youtube videos")
        print("2. Add a Youtube Video")
        print("3. Update a youtube video Details")
        print("4.Delete A Youtube Video")
        print("5. Exit this bullshit App")
        choice = input("Enter ur choice: ")
        print(videos)

        # NEW SYNTAX ALERT
        match choice:
            case "1":
                list_all_videos(videos)
            
            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                break
            case _:
                print("Invalid Response")

if __name__== "__main__":
    main()



