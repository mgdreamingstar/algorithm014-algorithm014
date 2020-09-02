class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		res = []
		
		def dfs(tmp,index):
			if index==len(digits):
				res.append(tmp)
				return
			c = digits[index]
			letters = d[int(c)]
			
			for i in letters:
				dfs(tmp+i,index+1)
		dfs("",0)
		return res
