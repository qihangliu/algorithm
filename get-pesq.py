import os
import sys

clear_filepath = sys.argv[1]
noise_filepath = sys.argv[2]
simple_rate = sys.argv[3]



def signal_pesq(clear_filepath, noise_filepath, simple_rate):
    '''
    P.862 提供的原始 PESQ 得分为 0.5 到 4.5 分。为了获得可以与 MOS 分值相比较的得分，需要将原始得分映射为 MOS-LQO，值越大表示效果越好。
    :param clear_filepath:
    :param noise_filepath:
    :param simple_rate:
    :return:
    '''

    cmd = '.\pesq.exe +{} {} {}'.format(simple_rate,clear_filepath,noise_filepath)
    os.system(cmd)
    pesq_information = os.popen(cmd).readlines()[-1]

    # print(re.split('=',pesq_information.strip()))
    print(pesq_information)

    raw_mos,mos_lqo = re.split('\t',re.split('=',pesq_information.strip())[-1])
    raw_mos = float(raw_mos)
    mos_lqo = float(mos_lqo)

    # os.popen('CMD').readlines()[0]
    # information = os.popen(cmd).read()
    print(raw_mos,mos_lqo)

    return mos_lqo

if __name__ == '__main__':


    signal_pesq(clear_filepath,noise_filepath,simple_rate)

