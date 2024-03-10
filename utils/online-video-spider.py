import argparse
import os
import requests


def parse_args():
    """
    @description 参数解析器
    @return {argparse} args 参数空间
    """
    # 创建解析器
    parser = argparse.ArgumentParser()

    # 武将编号（网站id）
    parser.add_argument("name", help="武将编号（网站id）")

    # 武将编号（实际id）
    parser.add_argument("id", help="武将编号（实际id）")

    # 技能个数
    parser.add_argument("skill_num", help="技能个数", choices = [1,2,3,4], type = int)

    # 保存地址（可选）
    parser.add_argument("--save_path", help = "保存路径")

    # 解析参数
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    # 获取参数
    args = parse_args()
    # 武将编号（网站id）
    name = args.name
    # 武将编号（实际id）
    id = args.id
    # 技能个数
    skill_num = args.skill_num
    # 保存路径
    save_path = args.save_path
    if save_path == None:
        save_path = "./mp3"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 获取技能个数
    if skill_num == 1:
        # 爬取名
        skills = ["1skill1_1.mp3", "1skill1_2.mp3", "1dead01.mp3"]
        # 存储名
        save_skills = [id+"_1_1.mp3", id+"_1_2.mp3", id+"_dead.mp3"]
    elif skill_num == 2:
        # 爬取名
        skills = ["1skill1_1.mp3","1skill1_2.mp3",
                "1skill2_1.mp3","1skill2_2.mp3",
                "1dead01.mp3"]
        # 存储名
        save_skills = [id+"_1_1.mp3", id+"_1_2.mp3", 
                       id+"_2_1.mp3", id+"_2_2.mp3", 
                       id+"_dead.mp3"]
    elif skill_num == 3:
        # 爬取名
        skills = ["1skill1_1.mp3","1skill1_2.mp3",
                "1skill2_1.mp3","1skill2_2.mp3",
                "1skill3_1.mp3","1skill3_2.mp3",
                "1dead01.mp3"]
        # 存储名
        save_skills = [id+"_1_1.mp3", id+"_1_2.mp3", 
                       id+"_2_1.mp3", id+"_2_2.mp3", 
                       id+"_3_1.mp3", id+"_3_2.mp3", 
                       id+"_dead.mp3"]
    else:
        # 爬取名
        skills = ["1skill1_1.mp3","1skill1_2.mp3",
                "1skill2_1.mp3","1skill2_2.mp3",
                "1skill3_1.mp3","1skill3_2.mp3",
                "1skill4_1.mp3","1skill4_2.mp3",
                "1dead01.mp3"]
        # 存储名
        save_skills = [id+"_1_1.mp3", id+"_1_2.mp3", 
                       id+"_2_1.mp3", id+"_2_2.mp3", 
                       id+"_3_1.mp3", id+"_3_2.mp3", 
                       id+"_4_1.mp3", id+"_4_2.mp3", 
                       id+"_dead.mp3"]
    
    # 获取url
    base = "https://web.sanguosha.com/220/h5_2/res/runtime/pc/voice/spell/"
    urls = [base + name + "/" + skill  for skill in skills]

    # 枚举urls爬取语音数据
    for index,url in enumerate(urls):
        res = requests.get(url)
        music = res.content
        with open(save_path + "/" +save_skills[index], 'ab') as f:
            f.write(res.content)
            f.flush()
