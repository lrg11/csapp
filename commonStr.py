class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        needcnt = len(t)
        #cur = Counter()
        left = 0
        ans = ''
        for i,x in enumerate(s):
            
            if cnt[x] > 0:
                needcnt-= 1
            cnt[x]-= 1
            if needcnt == 0:
                while True:
                    c = s[left]
                    if cnt[c] == 0:
                        break
                    cnt[c] += 1
                    left += 1
                
                if ans == '' or len(ans) > len(s[left: i + 1]):
                    ans = s[left: i + 1]
                cnt[s[left]] += 1
                needcnt += 1
                left += 1
        return ans
        
#

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        needcnt = len(t)
        #cur = Counter()
        left = 0
        ans = ''
        for i,x in enumerate(s):
            
            if cnt[x] > 0:
                needcnt-= 1
            cnt[x]-= 1
            if needcnt == 0:
                while True:
                    c = s[left]
                    if cnt[c] == 0:
                        break
                    cnt[c] += 1
                    left += 1
                
                if ans == '' or len(ans) > len(s[left: i + 1]):
                    ans = s[left: i + 1]
                cnt[s[left]] += 1
                needcnt += 1
                left += 1
        return ans
        