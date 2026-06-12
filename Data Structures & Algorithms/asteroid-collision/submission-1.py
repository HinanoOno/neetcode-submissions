class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for ast in asteroids:
            # 衝突が起こる可能性がある間ループ（スタック末尾が右向き[>0]、現在が左向き[<0]）
            while ans and ast < 0 < ans[-1]:
                if ans[-1] < -ast:  # スタックの石が小さい → 破壊して次と比較
                    ans.pop()
                    continue
                elif ans[-1] == -ast: # 両方同じサイズ → 両方破壊して終了
                    ans.pop()
                break # スタックの石の方が大きい、または両方破壊されたので終了
            else:
                # whileがbreakされなかった（＝衝突しなかった、または自分が生き残った）場合のみ追加
                ans.append(ast)
        return ans