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
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.floodx(image, sr, sc, color, image[sr][sc])
        return image