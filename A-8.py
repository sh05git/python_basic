# A-8: リストを要素に持つリスト
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

for user_info in users_info:
    print(f"Name: {user_info[0]}, Age: " + str(user_info[1]))
