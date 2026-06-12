class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        ans = []
  
        for i in range(n):
            if asteroids[i] < 0: # 左に進む石が来たときだけ衝突判定
                while ans and ans[-1] > 0: # スタックの末尾が右に進む石である限り戦う
                    if ans[-1] < abs(asteroids[i]):
                        ans.pop() # スタック側が小さいので消滅。自分はまだ進む（while継続）
                        continue
                    elif ans[-1] == abs(asteroids[i]):
                        ans.pop() # 相打ち。スタック側を消す
                        asteroids[i] = 0 # 自分も消滅（0にする）
                        break # 戦い終了
                    else:
                        asteroids[i] = 0 # スタック側が大きい。自分だけ消滅
                        break # 戦い終了

                if asteroids[i] != 0: # 衝突を生き残った、または衝突しなかった場合のみ追加
                    ans.append(asteroids[i])
            else:
                ans.append(asteroids[i]) # 右に進む石はそのまま追加
        return ans

