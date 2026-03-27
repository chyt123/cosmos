class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        while tx > sx or ty > sy:
            old_tx = tx
            old_ty = ty
            if tx > ty:
                tx = (tx - sx) % ty + sx
            else:
                ty = (ty - sy) % tx + sy
            if old_tx == tx and old_ty == ty:
                return False
        if tx == sx and ty == sy:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    sx = 3
    sy = 3
    tx = 12
    ty = 9
    print(sol.reachingPoints(sx, sy, tx, ty))
