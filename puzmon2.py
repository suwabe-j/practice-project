"""
作成日：2026年3月8日（日）
作成目的：Pythonの演習
書籍：すっきりわかるPython入門２
"""

# 記号のディクショナリ
ELEMENT_SYMBOLS = {
        "火":"$",
        "水":"~",
        "風":"@",
        "土":"#",
        "命":"&",
        "無":""
        }

# 色のディクショナリ
ELEMENT_COLORS = {
        "火":1,
        "水":6,
        "風":2,
        "土":3,
        "命":5,
        "無":7
        }

#main関数（ゲーム開始から終了までの責任を持つ）
def main():
    # タイトルの表示
    print("＊＊＊Puzzle & Mosters＊＊＊")
    # ５体のモンスター情報を入れるリストの作成
    enemy_list = list()
    # ４体味方モンスターのリスト作成
    party_list = list()
    # 各モンスターを作成し、リストへ格納
    slime={
            "name":"スライム",
            "hp":100,
            "max_hp":100,
            "element":"水",
            "ap":10,
            "dp":1
            }
    enemy_list.append(slime)

    gobline={
            "name":"ゴブリン",
            "hp":200,
            "max_hp":200,
            "element":"土",
            "ap":20,
            "dp":5
            } 
    enemy_list.append(gobline)

    ookoumori={
            "name":"オオコウモリ",
            "hp":300,
            "max_hp":300,
            "element":"風",
            "ap":30,
            "dp":10
            } 
    enemy_list.append(ookoumori)

    weaurufu={
            "name":"ウェアウルフ",
            "hp":400,
            "max_hp":400,
            "element":"風",
            "ap":40,
            "dp":15
            } 
    enemy_list.append(weaurufu)

    doragon={
            "name":"ドラゴン",
            "hp":600,
            "max_hp":600,
            "element":"火",
            "ap":50,
            "dp":20
            } 
    enemy_list.append(doragon)

    # ４体の味方モンスター作成し、リストへ格納
    seiryuu={
            "name":"青龍",
            "hp":150,
            "max_hp":150,
            "element":"風",
            "ap":15,
            "dp":10
            }
    party_list.append(seiryuu)

    kujaku={
            "name":"朱雀",
            "hp":150,
            "max_hp":150,
            "element":"火",
            "ap":25,
            "dp":10
            } 
    party_list.append(kujaku)

    byakko={
            "name":"白虎",
            "hp":150,
            "max_hp":150,
            "element":"土",
            "ap":20,
            "dp":5
            } 
    party_list.append(byakko)

    genbu ={
            "name":"玄武",
            "hp":150,
            "max_hp":150,
            "element":"水",
            "ap":20,
            "dp":15
            }
    party_list.append(genbu)

    # バトルを開始して、倒したモンスターの個数を表示する
    player_name = input("プレイヤー名を入力してください＞＞")
    # パーティーの様々な情報をリストに入れる
    party_list = organize_party(player_name , party_list)
    # 戦いの勝利数を格納
    monster_endnumber = go_dungeon(party_list , enemy_list)
    
    # 倒したモンスターの体数に応じて、クリアかゲームーバーかを表示する
    if monster_endnumber < 5:
        print("＊＊＊GAME OVER!!!＊＊＊")
    else:      
        print(f"{player_name}はダンジョンを制覇した")
        print("＊＊＊GAME CLEARED！！！＊＊＊")
    print(f"倒したモンスター数＝{monster_endnumber}")

# go_dungeon関数（ダンジョンの開始から終了までの責任を持つ）
def go_dungeon(party_dict,enemy_list):
    
    print(f"{party_dict['プレイヤー名']}のパーティー（HP＝{party_dict['HP']}）はダンジョンに到達した")
    # パーティー情報の表示
    print("＜パーティー編成＞-------------")
    show_party(party_dict)
    print("-------------------------------")

    # 各モンスターとのバトル
    is_win = 0
    for enemy in enemy_list:
        is_win += do_battle(party_dict , enemy)
        if party_dict["HP"] > 0:
            print(f"{party_dict['プレイヤー名']}はさらに奥に進んだ")
            print("=============")
        else:
            print("パーティーのHPは０になった")
            print(f"{party_dict['プレイヤー名']}はダンジョンから逃げ出した")
            print("=============")
            break
    return is_win

# do_battle関数（１回のバトル開始から終了までの責任を持つ）
def do_battle(party_dict , enemy):

    # モンスターの名前を表示
    print_monster_name(enemy)
    print("が現れた！")

    # パーティーや敵の残り体力次第で、攻撃ターンを続ける
    while party_dict['HP'] > 0:
        on_player_turn(party_dict , enemy)
        if enemy['hp'] > 0:
            on_enemy_turn(party_dict , enemy)
            if party_dict['HP'] <= 0:
                break
        else:
            break

    if enemy['hp'] <= 0:
        print_monster_name(enemy)
        print("を倒した！")
        return 1
    else:
        return 0

# モンスターの名前を表示する関数
def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    symbol = ELEMENT_SYMBOLS[ monster["element"] ]
    #色のコードをうけとる
    color = ELEMENT_COLORS[ monster["element"] ]
    # モンスター名を表示
    print(f"\033[{color}m{symbol}{monster['name']}{symbol}\033[0m" , end = '')

# 引数で渡された味方モンスターでパーティーを編成して返す関数
def organize_party(player_name , party_list):
    # 味方モンスターのHP合計値と防御力の平均を求める
    sum_hp = 0
    sum_defence = 0
    for party in party_list:
        sum_hp += party["hp"]
        sum_defence += party["dp"]

    ave_defence = sum_defence / len(party_list)

    # パーティーの情報をまとめる
    party_info = dict()
    party_info["プレイヤー名"] = player_name
    party_info["味方モンスター"] = party_list
    party_info["HP"] = sum_hp
    party_info["最大HP"] = sum_hp
    party_info["防御力"] = ave_defence

    return party_info

# 味方モンスターの情報を表示する関数
def show_party(party_dict):
    party_monster_list = party_dict["味方モンスター"]
    # 味方モンスターの情報をリストから出して、情報表示
    for party_monster in party_monster_list:
        print_monster_name(party_monster)
        print(f"　HP＝{party_monster['hp']}　攻撃＝{party_monster['ap']}　防御＝{party_monster['dp']}")

# プレイヤーの攻撃ターンを実施する関数
def on_player_turn(party_dict , enemy):
    #「【〇〇のターン】（HP＝▲▲））を表示する」
    print(f"【{party_dict['プレイヤー名']}のターン】（HP＝{party_dict['HP']}）")
    #コマンド入力を受け付け、ダメージ値を決定する（固定で５０へ）
    comand = input('コマンドを入力して下さい＞＞')
    #敵モンスターのHPからダメージ分の値を減らす
    do_attack(enemy , comand)

# 敵の攻撃ターンを実施する関数
def on_enemy_turn(party_dict , enemy):
    #「【〇〇のターン】（HP＝▲▲））を表示する」
    print(f"【{enemy['name']}のターン】（HP＝{enemy['hp']}）")
    #敵モンスターのHPからダメージ分の値を減らす
    do_enemy_attack(party_dict)

# プレイヤーによる敵へのダメージを計算する
def do_attack(enemy , comand):
    # ランダム関数をインポート
    import random

    damage = hash(comand)
    if damage >= 0:
        enemy['hp'] -= int((damage / (2**62)) * (random.uniform(1.1,0.9)))
    else:
        enemy['hp'] += int((damage / (2**62)) * (random.uniform(1.1,0.9)))

# 敵によるプレーヤーへのダメージを計算する関数
def do_enemy_attack(party_dict):
    # ランダム関数をインポート
    import random

    party_dict['HP'] -= int(random.uniform(30,100))

# main関数
main()
