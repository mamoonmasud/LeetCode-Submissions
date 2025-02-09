class Solution:
    def floodx(self, image, x, y, color, cur):
        if x >= len(image) or x < 0 or y >= len(image[0]) or y < 0:
            return
        if cur != image[x][y]:
            return
        image[x][y] = color
        self.floodx(image, x-1, y, color, cur)
        self.floodx(image, x+1, y, color, cur)
        self.floodx(image, x, y-1, color, cur)
        self.floodx(image, x, y+1, color, cur)
        return 