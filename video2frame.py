import cv2
import os
import argparse



def video2frame(videos_path,frames_save_path,time_interval):
 
  '''
  :param videos_path: 视频的存放路径
  :param frames_save_path: 视频切分成帧之后图片的保存路径
  :param time_interval: 保存间隔
  :return:
  '''
  vidcap = cv2.VideoCapture(videos_path)
  success, image = vidcap.read()
  count = 0
  while success:
    success, image = vidcap.read()
    if success is not True:
      continue
    count += 1
    if count % time_interval == 0:
      #print(count)
      if count == 24080:
       a = count

      #以  framexxx.jpg名字保存
      #cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "/frame%d.jpg" % count)

      base_name = os.path.split(frames_save_path)[1]
      #cv2.imencode('.jpg', image)[1].tofile(frames_save_path + '/'+base_name + "/frame%d.jpg" % count)
      #cv2.imencode('.jpg', image)[1].tofile('F:\data\customer_complaint\customer_data' + r'\' + base_name + "/frame%d.jpg" % count)
      #cv2.imencode('.jpg', image)[1].tofile(os.path.join('F:\data\customer_complaint\customer_data'  , base_name + "_frame%d.jpg" % count))

      #cv2.imencode('.jpg', image)[1].tofile(frames_save_path + '/' + base_name + "_frame%d.jpg" % count)
      cv2.imencode('.jpg', image)[1].tofile(frames_save_path + '/' +   "%d.jpg" % count)

  print(count)


 
def read_videos():
 
  videos_path = opt.videos_path
  time_interval = opt.time_interval
  frames_save_path = opt.save_path

  if not os.path.exists(frames_save_path):
    os.makedirs(frames_save_path)

  if not os.path.exists(videos_path):
    print('This video path is not exist!')
    return
  else:
    videos_lists = os.listdir(videos_path)
    for video in videos_lists:
      
      
      base_name=os.path.splitext(video)[0]  
      if not os.path.exists(os.path.join(frames_save_path ,base_name)):
        os.makedirs(os.path.join(frames_save_path ,base_name))

      video2frame(os.path.join(videos_path,video),os.path.join(frames_save_path ,base_name),time_interval)

      print('完成:{}'.format(os.path.join(videos_path, video)))
    




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--videos_path', type=str, default=r'F:\data\tiktok', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=2, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\tiktok\tiktok_frame_interval', help='output path')

    # parser.add_argument('--videos_path', type=str, default=r'F:\data\tiktok330', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=5, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\tiktok330\tiktok_frame_interval', help='output path')

    # parser.add_argument('--videos_path', type=str, default=r'F:\data\vjshi', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=5, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\vjshi\tiktok_frame_interval', help='output path')

    # parser.add_argument('--videos_path', type=str, default=r'F:\data\customer_complaint', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=10, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\customer_complaint\customer_data', help='output path')

    # parser.add_argument('--videos_path', type=str, default=r'F:\data\ff003_demo_data\ori_data', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=1, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\ff003_demo_data\frame_data', help='output path')

    # parser.add_argument('--videos_path', type=str, default=r'F:\data\ff003_demo_data\result', help='*.video path')
    # parser.add_argument('--time_interval', type=str, default=1, help='every time catch one frame')
    # parser.add_argument('--save_path', type=str, default=r'F:\data\ff003_demo_data\result', help='output path')
    
    parser.add_argument('--videos_path', type=str, default=r'D:\Users\liuqihang\Desktop\inbox\FF002\0619', help='*.video path')
    parser.add_argument('--time_interval', type=str, default=1, help='every time catch one frame')
    parser.add_argument('--save_path', type=str, default=r'D:\Users\liuqihang\Desktop\inbox\FF002\0619\result', help='output path')

    opt = parser.parse_args()

    read_videos()


#if __name__ == '__main__':
#   videos_path = 'D:\测试\测试视频01.mp4'
#   frames_save_path = 'D:\测试\测试视频01'
#   time_interval = 2#隔一帧保存一次
#   video2frame(videos_path, frames_save_path, time_interval)